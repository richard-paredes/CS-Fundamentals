const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index.js'),
    array_utils = require('../../utils/array-utils.js');

/** GET Bookings */
router.get('/', async (req, res) => {
    try {
        const bookings = await pool.query(`
            SELECT *
            FROM gam8r0.bookings;
        `);
        return res.json(bookings.rows);
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** GET Booking */
router.get('/:id', async (req, res) => {
    try {
        const { id: booking_code } = req.params;
        const booking = await pool.query(`
            SELECT *
            FROM gam8r0.bookings 
            WHERE booking_code = $1;`
            , [booking_code]);
        return res.json(booking.rows);
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** POST Booking */
router.post('/', async (req, res) => {
    try {
        const { card_no, flight_ids, passengers: passenger_details } = req.body;

        const booking_date = new Date();
        const customer_id = req.cookies['cid'];

        await pool.query('BEGIN;');

        const total_payment_estimate = { base_amount: 0, taxes: 0, discount: 0 };
        for (let flight_id of flight_ids) {
            await confirm_flight_availability(flight_id, passenger_details);
            await accumulate_payment_estimate(flight_id, total_payment_estimate, passenger_details);
        }
        
        const payment = await create_payment(card_no, total_payment_estimate);
        const booking = await create_booking(customer_id, booking_date, payment);
        const passengers = await create_passengers(passenger_details);
        const ticket = await create_ticket(booking, passengers);
        const ticket_flights = await create_ticket_flights(ticket, flight_ids, passenger_details);

        await pool.query(`COMMIT;`);
        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});;
    }
});

/** PUT Booking */
router.put('/:id', async (req, res) => {
    try {
        const { id: book_ref } = req.params;
        const { payment_ref, flight_ids, passengers: passenger_details } = req.body;

        const book_date = new Date();
        await pool.query(`BEGIN;`);
        
        const total_payment_estimate = { base_amount: 0, taxes: 0, discount: 0 };
        for (let flight_id of flight_ids) {
            await confirm_flight_availability(flight_id, passenger_details);
            await accumulate_payment_estimate(flight_id, total_payment_estimate, passenger_details);
        }

        const payment = await update_payment(payment_ref,total_payment_estimate);
        const passengers = await update_passengers(passenger_details);
        const ticket_flights = await update_ticket_flights(flight_ids, passenger_details);
        const booking = await update_booking(book_ref, book_date);
        await pool.query(`COMMIT;`);

        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** DELETE Booking */
router.delete('/:id', async (req, res) => {
    try {
        const { id: book_ref } = req.params;
        await pool.query(`BEGIN;`);

        const ticket_flights = await pool.query(`
            DELETE
            FROM gam8r0.ticket_flights
            WHERE ticket_no IN (
                SELECT ticket_no
                FROM gam8r0.tickets
                WHERE book_ref = $1
            )
            RETURNING *;
            `, [book_ref]);
        const tickets = await pool.query(`
            DELETE
            FROM gam8r0.tickets 
            WHERE book_ref = $1
            RETURNING *;
            `, [book_ref]);

        const ticket_nos = tickets.rows.map(x => x.ticket_no);

        const passengers = await pool.query(`
                DELETE
                FROM gam8r0.passengers
                WHERE passenger_id IN ${array_utils.expand(1, ticket_nos.length)}
                RETURNING *;
            `, ticket_nos);
        const payments = await pool.query(`
            UPDATE gam8r0.payments
            SET status = 'Refunded'
            WHERE payment_ref IN (
                SELECT payment_ref
                FROM gam8r0.bookings
                WHERE book_ref = $1
            )
            RETURNING *;
        `, [book_ref]);

        // const booking = await pool.query(`
        //     DELETE 
        //     FROM bookings
        //     WHERE book_ref = $1
        //     RETURNING *;
        // `, [book_ref]);
        await pool.query(`COMMIT`);
        return res.json(booking.rows);
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});



const confirm_flight_availability = async (flight_id, passenger_details) => {
    const seat_availability_data = await pool.query(`
        SELECT f.flight_id,
            f.allow_waitlist,
            count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as first_seats_available,
            count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as business_seats_available,
            count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as economy_seats_available
        FROM gam8r0.flights f
        JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
        LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
        LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
        LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
        LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
        LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
        LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
        WHERE f.flight_id = $1 AND f.status != 'Arrived' AND f.status != 'Departed' AND f.status != 'Cancelled'
        GROUP BY f.flight_id;
    `, [flight_id]);

    if (seat_availability_data.rowCount === 0)
        throw new Error(`Flight ${flight_id} is unavailable.`)

    const seat_availability = seat_availability_data.rows[0];
    const first_seats_requested = passenger_details.filter(x => x[`${flight_id}_fare_conditions`] === 'First' && x[`${flight_id}_old_fare_conditions`] !== 'First').length;
    const business_seats_requested = passenger_details.filter(x => x[`${flight_id}_fare_conditions`] === 'Business' && x[`${flight_id}_old_fare_conditions`] !== 'Business').length;
    const economy_seats_requested = passenger_details.filter(x => x[`${flight_id}_fare_conditions`] === 'Economy' && x[`${flight_id}_old_fare_conditions`] !== 'Economy').length;

    const is_available = seat_availability.allow_waitlist ||
        (seat_availability.first_seats_available >= first_seats_requested &&
            seat_availability.business_seats_available >= business_seats_requested &&
            seat_availability.economy_seats_available >= economy_seats_requested);

    if (!is_available)
        throw new Error(`Flight ${flight_id} has reached maximum capacity.`)
};

const get_prices = async (flight_id) => {
    const baggage_prices_data = await pool.query(`
        SELECT carry_on_price::money::numeric::float8,
            checked_bag_price::money::numeric::float8
        FROM gam8r0.baggage_prices
        WHERE flight_id = $1;
    `, [flight_id]);
    const fare_prices_data = await pool.query(`
        SELECT fare_conditions,
            fare_price::money::numeric::float8
        FROM gam8r0.fare_prices
        WHERE flight_id = $1;
    `, [flight_id]);
    
    return {
        first_fare_price: fare_prices_data.rows.find(x => x.fare_conditions === 'First').fare_price,
        business_fare_price: fare_prices_data.rows.find(x => x.fare_conditions === 'Business').fare_price,
        economy_fare_price: fare_prices_data.rows.find(x => x.fare_conditions === 'Economy').fare_price,
        carry_on_price: baggage_prices_data.rows[0].carry_on_price,
        checked_bag_price: baggage_prices_data.rows[0].checked_bag_price
    };
};

const accumulate_payment_estimate = async (flight_id, payment_estimate, passenger_details) => {
    const prices = await get_prices(flight_id);

    const tax_rate = 0.0825;
    let discount = 0;
    let base_amount = 0;
    let taxes = 0;
    
    passenger_details.forEach(x => {
        base_amount += parseInt(x[`flight_${flight_id}_checked_bags`]) * prices.checked_bag_price;
        base_amount += parseInt(x[`flight_${flight_id}_carry_ons`]) * prices.carry_on_price;
        if (x[`flight_${flight_id}_fare_conditions`] === 'First') {
            base_amount += prices.first_fare_price;
            discount += parseInt(x[`flight_${flight_id}_checked_bags`]) * prices.checked_bag_price;
            discount += parseInt(x[`flight_${flight_id}_carry_ons`]) * prices.carry_on_price;
        } else if (x[`flight_${flight_id}_fare_conditions`] === 'Business') {
            base_amount += prices.business_fare_price;
        } else if (x[`flight_${flight_id}_fare_conditions`] === 'Economy') {
            base_amount += prices.economy_fare_price;
        } else {
            throw new Error("Invalid fare selected.")
        }
    });

    taxes = base_amount * tax_rate;

    // discount based on number of passengers
    if (passenger_details.length > 1) {
        discount += base_amount * (0.05 * passenger_details.length);
    }

    payment_estimate.base_amount += base_amount;
    payment_estimate.taxes += taxes;
    payment_estimate.discount += discount;
};

const create_payment = async (card_no, payment) => {
    const payment_data = await pool.query(`
        INSERT INTO
        gam8r0.payments (card_no, taxes, discount, base_amount, status)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING *;
    `, [card_no, payment.taxes, payment.discount, payment.base_amount, 'Paid']);

    return payment_data.rows[0];
};

const create_booking = async (customer_id, date, payment) => {
    const booking_data = await pool.query(`
        INSERT INTO
        gam8r0.bookings (customer_id, book_date, payment_ref)
        VALUES ($1, $2, $3)
        RETURNING *;
    `, [customer_id, date, payment.payment_ref]);

    return booking_data.rows[0];
};

const create_passengers = async (passenger_details) => {
    const passenger_names = passenger_details.map(x => [x.first_name, x.last_name]);
    const passenger_data = await pool.query(`
        INSERT INTO
        gam8r0.passengers (first_name, last_name)
        VALUES ${array_utils.expand(passenger_names.length, 2)}
        RETURNING *;
    `, array_utils.flatten(passenger_names));

    return passenger_data.rows;
};

const create_ticket = async (booking, passengers) => {
    
    const ticket_details = passengers.map(x => [booking.book_ref, x.passenger_id]);
    const ticket_data = await pool.query(`
        INSERT INTO
        gam8r0.tickets (book_ref, passenger_id)
        VALUES ${array_utils.expand(ticket_details.length, 2)}
        RETURNING *;
    `, array_utils.flatten(ticket_details));

    return ticket_data.rows;
};

const get_seat_status = async (flight_ids) => {
    // need to do this so i can determine to waitlist a ticket_flight or not
    const params = flight_ids.map((_, idx) => `$${idx+1}`);
    const flight_seats_data = await pool.query(`
        SELECT f.flight_id,
            f.allow_waitlist,
            count(distinct s.seat_key) - count(distinct tf_total.ticket_no) as total_seats_available,
            count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as Business,
            count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as First,
            count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as Economy,
            count(distinct tf_business.ticket_no) as business_seats_taken, 
            count(distinct tf_first.ticket_no) as first_seats_taken,
            count(distinct tf_economy.ticket_no) as economy_seats_taken
        FROM gam8r0.flights f
        JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
        LEFT JOIN gam8r0.ticket_flights tf_total ON f.flight_id = tf_total.flight_id AND tf_total.is_waitlisted = FALSE
        LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
        LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
        LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
        LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
        LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
        LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
        WHERE f.status != 'Cancelled' AND f.status != 'Departed' AND f.status != 'Arrived'
            AND f.flight_id IN ( ${params.join(',')} )
        GROUP BY f.flight_id;
    `, flight_ids);
    
    return flight_seats_data.rows.map(x => ({
        flight_id: x.flight_id,
        allow_waitlist: x.allow_waitlist,
        Total: parseInt(x.total_seats_available),
        Business: parseInt(x.business),
        First: parseInt(x.first),
        Economy: parseInt(x.economy)
    }));
};

const create_ticket_flights = async (tickets, flight_ids, passenger_details) => {
    const flight_seat_status = await get_seat_status(flight_ids);
    let ticket_flight_details = [];
    tickets.forEach((ticket, idx) => {
        const ticket_no = ticket.ticket_no;
        const passenger = passenger_details[idx];
        const ticket_flights = flight_ids.map((flight_id) => {
            const flight_seats = flight_seat_status.find(x => x.flight_id == flight_id);
            
            const requested_seat = passenger[`flight_${flight_id}_fare_conditions`];
            const carry_ons = passenger[`flight_${flight_id}_carry_ons`];
            const checked_bags = passenger[`flight_${flight_id}_checked_bags`];
            const is_waitlisted = flight_seats[requested_seat] < 1;

            if (!is_waitlisted)
                flight_seats[requested_seat]--;
            return [ticket_no, flight_id, requested_seat, carry_ons, checked_bags, is_waitlisted];
        });
        ticket_flight_details = ticket_flight_details.concat(ticket_flights);
    });
    
    await pool.query(`
        INSERT INTO
        gam8r0.ticket_flights (ticket_no, flight_id, fare_conditions, carry_ons, checked_bags, is_waitlisted)
        VALUES ${array_utils.expand(ticket_flight_details.length, 6)}
        RETURNING *;
    `, array_utils.flatten(ticket_flight_details));
};

const update_payment = async (payment_ref, payment) => {
    const payment_data = await pool.query(`
        UPDATE gam8r0.payments 
        SET taxes = $1,
            discount = $2,
            base_amount = $3
        WHERE payment_ref = $4
        RETURNING *;
    `, [payment.taxes, payment.discount, payment.base_amount, payment_ref]);
    return payment_data.rows[0];
};

const update_passengers = async (passenger_details) => {
    const passenger_updates = passenger_details.map(x => [parseInt(x.passenger_id), x.first_name, x.last_name]);
    const passengers_data = await pool.query(`
        UPDATE gam8r0.passengers AS ps
        SET first_name = p.first_name,
            last_name = p.last_name
        FROM 
            (
                VALUES ${array_utils.expand(passenger_updates.length, 3, 1, ['INTEGER'])}
            ) AS p(passenger_id, first_name, last_name)
        WHERE ps.passenger_id = p.passenger_id
        RETURNING *;
    `, array_utils.flatten(passenger_updates));
    
    return passengers_data.rows;
};

const update_ticket_flights = async (flight_ids, passenger_details) => {
    const flight_seat_status = await get_seat_status(flight_ids);
    let ticket_flight_updates = [];
    passenger_details.forEach((passenger) => {
        const ticket_no = passenger.ticket_no;
        const ticket_flights = flight_ids.map((flight_id) => {
            const flight_seats = flight_seat_status.find(x => x.flight_id == flight_id);
            const current_seat = passenger[`flight_${flight_id}_old_fare_conditions`];
            const requested_seat = passenger[`flight_${flight_id}_fare_conditions`];
            const seat_changed = current_seat !== requested_seat;
            const carry_ons = passenger[`flight_${flight_id}_carry_ons`];
            const checked_bags = passenger[`flight_${flight_id}_checked_bags`];
            const is_waitlisted = seat_changed && flight_seats[requested_seat] < 1;

            if (seat_changed) {
                if (!is_waitlisted) {
                    flight_seats[requested_seat]--;
                }
                flight_seats[current_seat]++;
            }
            return [ticket_no, flight_id, requested_seat, carry_ons, checked_bags, is_waitlisted];
        });
        ticket_flight_updates = ticket_flight_updates.concat(ticket_flights);
    });
    const ticket_flights_data = await pool.query(`
        UPDATE gam8r0.ticket_flights AS tf
        SET 
            fare_conditions = u.fare_conditions,
            carry_ons = u.carry_ons,
            checked_bags = u.checked_bags,
            is_waitlisted = u.is_waitlisted
        FROM 
            (
                VALUES ${array_utils.expand(ticket_flight_updates.length, 6, 1, ['INTEGER', 'INTEGER', 'TEXT', 'INTEGER', 'INTEGER', 'BOOLEAN'])}
            ) AS u(ticket_no, flight_id, fare_conditions, carry_ons, checked_bags, is_waitlisted)
        WHERE tf.ticket_no = u.ticket_no AND tf.flight_id = u.flight_id;
    `, array_utils.flatten(ticket_flight_updates));

    return ticket_flights_data.rows;
};

const update_booking = async (book_ref, book_date) => {
    const booking_data = await pool.query(`
        UPDATE gam8r0.bookings
        SET book_date = $1
        WHERE book_ref = $2
        RETURNING *;
    `, [book_date, book_ref]);

    return booking_data.rows[0];
};

module.exports = router;