const e = require('express');

const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index.js'),
    array_utils = require('../../utils/array-utils.js');

/** GET Customer from cookie */
router.get('/', async (req, res) => {
    try {
        const customer_id = req.cookies['cid'];
        if (customer_id) {
            const customers_data = await pool.query(`
                SELECT *
                FROM gam8r0.customers
                WHERE customer_id = $1;
            `, [customer_id]);
            if (customers_data.rowCount === 0)
                return res.status(401).json('Invalid customer session');

            const bookings_data = await pool.query(`
                SELECT b.*, 
                    p.payment_ref,
                    p.card_no,
                    p.taxes::money::numeric::float8, 
                    p.discount::money::numeric::float8,
                    p.base_amount::money::numeric::float8,
                    ps.*,
                    t.*,
                    tf.*,
                    f.*,
                    bp.seat_key,
                    s.seat_no,
                    bg.baggage_id,
                    bg.type,
                    da.city as departure_city,
                    aa.city as arrival_city,
                    departure_gate.gate_no as departure_gate,
                    arrival_gate.gate_no as arrival_gate,
                    bc.baggage_claim_no as baggage_claim
                FROM gam8r0.bookings b
                JOIN gam8r0.payments p ON b.payment_ref = p.payment_ref
                JOIN gam8r0.tickets t ON b.book_ref = t.book_ref
                JOIN gam8r0.passengers ps ON t.passenger_id = ps.passenger_id
                JOIN gam8r0.ticket_flights tf ON t.ticket_no = tf.ticket_no
                JOIN gam8r0.flights f ON tf.flight_id = f.flight_id
                JOIN gam8r0.airports da ON f.departure_airport = da.airport_code
                JOIN gam8r0.airports aa ON f.arrival_airport = aa.airport_code
                JOIN gam8r0.gates departure_gate ON f.departure_gate_no = departure_gate.gate_key
                JOIN gam8r0.gates arrival_gate ON f.arrival_gate_no = arrival_gate.gate_key
                JOIN gam8r0.baggage_claims bc ON f.baggage_claim_no = bc.baggage_claim_key
                LEFT JOIN gam8r0.boarding_passes bp ON tf.ticket_no = bp.ticket_no AND tf.flight_id = bp.flight_id
                LEFT JOIN gam8r0.seats s ON bp.seat_key = s.seat_key
                LEFT JOIN gam8r0.baggages bg ON bp.ticket_no = bg.ticket_no AND bp.flight_id = bg.flight_id
                WHERE customer_id = $1 AND p.status != 'Refunded'
                ORDER BY b.book_date;
            `, [customer_id]);
            const bookings = [];
            // console.log(bookings_data.rows);
            // each booking has one ticket per passenger, each ticket has multiple ticket-flights
            bookings_data.rows.map((book) => {
                const booking_obj = bookings.find(x => x.book_ref === book.book_ref);
                if (booking_obj) {
                    const ticket_obj = booking_obj.tickets.find(x => x.ticket_no === book.ticket_no);
                    if (ticket_obj) {
                        if (ticket_obj.flights.some(x => x.flight_id === book.flight_id)) {
                            const boarding_pass_obj = ticket_obj.boarding_passes.find(x => x.ticket_no === book.ticket_no && x.flight_id === book.flight_id && x.seat_key === book.seat_key);
                            if (boarding_pass_obj) {
                                if (book.baggage_id && book.type) {
                                    boarding_pass_obj.baggages.push({
                                        baggage_id: book.baggage_id,
                                        type: book.type
                                    })
                                }
                            } else {
                                if (book.seat_key) {
                                    const boarding_pass = {
                                        ticket_no: book.ticket_no,
                                        flight_id: book.flight_id,
                                        seat_no: book.seat_no,
                                        seat_key: book.seat_key,
                                        baggages: []
                                    };
                                    if (book.baggage_id && book.type) {
                                        boarding_pass.baggages.push({
                                            baggage_id: book.baggage_id,
                                            type: book.type
                                        })
                                    }
                                    ticket_obj.boarding_passes.push(boarding_pass)
                                }
                            }
                        } else {
                            ticket_obj.flights.push({
                                flight_id: book.flight_id,
                                status: book.status,
                                boarding_time: book.boarding_time,
                                scheduled_departure: book.scheduled_departure,
                                scheduled_arrival: book.scheduled_arrival,
                                baggage_claim_no: book.baggage_claim_no,
                                includes_meal: book.includes_meal,
                                includes_movie: book.includes_movie,
                                departure_airport: book.departure_airport,
                                departure_gate_no: book.departure_gate_no,
                                arrival_airport: book.arrival_airport,
                                arrival_gate_no: book.arrival_gate_no,
                                aircraft_code: book.aircraft_code,
                                is_waitlisted: book.is_waitlisted,
                                carry_ons: book.carry_ons,
                                checked_bags: book.checked_bags,
                                departure_city: book.departure_city,
                                arrival_city: book.arrival_city,
                                fare_conditions: book.fare_conditions,
                                departure_gate: book.departure_gate,
                                arrival_gate: book.arrival_gate,
                                baggage_claim: book.baggage_claim
                            });
                            
                            if (book.seat_key) {
                                const boarding_pass = {
                                    ticket_no: book.ticket_no,
                                    flight_id: book.flight_id,
                                    seat_no: book.seat_no,
                                    seat_key: book.seat_key,
                                    baggages: []
                                }
                                if (book.baggage_id && book.type) {
                                    boarding_pass.baggages.push({
                                        baggage_id: book.baggage_id,
                                        type: book.type
                                    });
                                }
                                ticket_obj.boarding_passes.push(boarding_pass);
                            }
                        }
                    } else {
                        // add new ticket
                        const ticket = {
                            ticket_no: book.ticket_no,
                            passenger: {
                                passenger_id: book.passenger_id,
                                first_name: book.first_name,
                                last_name: book.last_name
                            },
                            flights: [{
                                flight_id: book.flight_id,
                                status: book.status,
                                boarding_time: book.boarding_time,
                                scheduled_departure: book.scheduled_departure,
                                scheduled_arrival: book.scheduled_arrival,
                                baggage_claim_no: book.baggage_claim_no,
                                includes_meal: book.includes_meal,
                                includes_movie: book.includes_movie,
                                departure_airport: book.departure_airport,
                                departure_gate_no: book.departure_gate_no,
                                arrival_airport: book.arrival_airport,
                                arrival_gate_no: book.arrival_gate_no,
                                aircraft_code: book.aircraft_code,
                                is_waitlisted: book.is_waitlisted,
                                carry_ons: book.carry_ons,
                                checked_bags: book.checked_bags,
                                departure_city: book.departure_city,
                                arrival_city: book.arrival_city,
                                fare_conditions: book.fare_conditions,
                                departure_gate: book.departure_gate,
                                arrival_gate: book.arrival_gate,
                                baggage_claim: book.baggage_claim
                            }],
                            boarding_passes: []
                        }
    
                        if (book.seat_key) {
                            const boarding_pass = {
                                ticket_no: book.ticket_no,
                                flight_id: book.flight_id,
                                seat_key: book.seat_key,
                                seat_no: book.seat_no,
                                baggages: []
                            }
                            if (book.baggage_id && book.type) {
                                boarding_pass.baggages.push({
                                    baggage_id: book.baggage_id,
                                    type: book.type
                                });
                            }
                            ticket.boarding_passes.push(boarding_pass)
                        }

                        booking_obj.tickets.push(ticket)
                    }
                } else {
                    const booking = {
                        book_ref: book.book_ref,
                        book_date: book.book_date,
                        customer_id: book.customer_id,
                        payment: {
                            payment_ref: book.payment_ref,
                            card_no: book.card_no,
                            taxes: book.taxes,
                            discount: book.discount,
                            base_amount: book.base_amount
                        },
                        tickets: []
                    }
                    const ticket = {
                        ticket_no: book.ticket_no,
                        passenger: {
                            passenger_id: book.passenger_id,
                            first_name: book.first_name,
                            last_name: book.last_name
                        },
                        flights: [{
                            flight_id: book.flight_id,
                            status: book.status,
                            boarding_time: book.boarding_time,
                            scheduled_departure: book.scheduled_departure,
                            scheduled_arrival: book.scheduled_arrival,
                            baggage_claim_no: book.baggage_claim_no,
                            includes_meal: book.includes_meal,
                            includes_movie: book.includes_movie,
                            departure_airport: book.departure_airport,
                            departure_gate_no: book.departure_gate_no,
                            arrival_airport: book.arrival_airport,
                            arrival_gate_no: book.arrival_gate_no,
                            aircraft_code: book.aircraft_code,
                            is_waitlisted: book.is_waitlisted,
                            carry_ons: book.carry_ons,
                            checked_bags: book.checked_bags,
                            departure_city: book.departure_city,
                            arrival_city: book.arrival_city,
                            fare_conditions: book.fare_conditions,
                            departure_gate: book.departure_gate,
                            arrival_gate: book.arrival_gate,
                            baggage_claim: book.baggage_claim
                        }],
                        boarding_passes: []
                    }

                    if (book.seat_key) {
                        const boarding_pass = {
                            ticket_no: book.ticket_no,
                            flight_id: book.flight_id,
                            seat_key: book.seat_key,
                            seat_no: book.seat_no,
                            baggages: []
                        }
                        if (book.baggage_id && book.type) {
                            boarding_pass.baggages.push({
                                baggage_id: book.baggage_id,
                                type: book.type
                            })
                        }
                        ticket.boarding_passes.push(boarding_pass)
                    }
                    booking.tickets.push(ticket);
                    bookings.push(booking);
                }
            });

            return res.json({ customers: customers_data.rows, bookings: bookings });
        } else {
            return res.json([]);
        }
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** GET Customers */
router.get('/:id', async (req, res) => {
    try {
        const { id: customer_id } = req.params;
        const customer = await pool.query(`
            SELECT *
            FROM gam8r0.customers 
            WHERE customer_id = $1;`
            , [customer_id]);
        const bookings = await pool.query(`
            SELECT *
            FROM gam8r0.bookings b
            JOIN gam8r0.payments p ON b.payment_ref = b.payment_ref
            WHERE customer_id = $1;
        `, [customer_id]);
        return res.json(
            {
                customers: customer.rows,
                bookings: bookings.rows
            });
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** POST Customers */
router.post('/', async (req, res) => {
    try {
        const { first_name, last_name, telephone, email } = req.body;

        await pool.query('BEGIN;');
        const customers = await pool.query(`
            INSERT INTO 
            gam8r0.customers (first_name, last_name, telephone, email)
            VALUES ($1, $2, $3, $4)
            RETURNING *;
        `, [first_name, last_name, telephone, email]);
        await pool.query('COMMIT;');
        res.cookie('cid', customers.rows[0].customer_id, { path: "/", maxAge: 86400000, httpOnly: false, sameSite: false })
        return res.status(200).json('OK');
    } catch (err) {
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});;
    }
});

router.post('/login', async (req, res) => {
    try {
        const { email } = req.body;
        const customers = await pool.query(`
            SELECT *
            FROM gam8r0.customers
            WHERE email = $1
        `, [email]);
        if (customers.rowCount == 0) {
            return res.status(401).json('Invalid customer login.');
        } else {
            res.cookie('cid', customers.rows[0].customer_id, { path: "/", maxAge: 86400000, httpOnly: true })
            return res.status(200).json('OK');
        }
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

router.post('/logout', async (req, res) => {
    try {
        res.clearCookie('cid');
        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** PUT Customers */
router.put('/:id', async (req, res) => {
    try {
        const { id: customer_code } = req.params;
        const { customer_name, city, coordinates, timezone } = req.body;
        await pool.query(`BEGIN;`);
        await pool.query(`
            UPDATE gam8r0.customers 
            SET 
                customer_name = $1,
                city = $2,
                coordinates = $3,
                timezone = $4
            WHERE customer_code = $5
            RETURNING *;
        `, [customer_name, city, coordinates, timezone, customer_code]);
        await pool.query(`COMMIT;`);

        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** DELETE Customers */
router.delete('/:id', async (req, res) => {
    try {
        const { id: customer_code } = req.params;
        await pool.query(`BEGIN;`);
        const customer = await pool.query(`
            DELETE 
            FROM gam8r0.customers
            WHERE customer_code = $1
            RETURNING *;
        `, [customer_code]);
        await pool.query(`COMMIT`);
        return res.json(customer.rows);
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});

module.exports = router;