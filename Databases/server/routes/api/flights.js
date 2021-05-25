const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index.js');

/** GET Flights */
router.get('/', async (req, res) => {
    try {
        const flights = await pool.query(`
            SELECT f.*,
                arrival_airport.city as arrival_city,
                departure_airport.city as departure_city,
                count(distinct s.seat_key) - count(distinct tf_total.ticket_no) as total_seats_available,
                count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as business_seats_available,
                count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as first_seats_available,
                count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as economy_seats_available,
                count(distinct tf_business.ticket_no) as business_seats_taken, 
                count(distinct tf_first.ticket_no) as first_seats_taken,
                count(distinct tf_economy.ticket_no) as economy_seats_taken,
                count(distinct tf_business_wl.ticket_no) as business_seats_waitlisted,
                count(distinct tf_first_wl.ticket_no) as first_seats_waitlisted,
                count(distinct tf_economy_wl.ticket_no) as economy_seats_waitlisted,
                max(distinct business_fare.fare_price) as business_seats_price,
                max(distinct first_fare.fare_price) as first_seats_price,
                max(distinct economy_fare.fare_price) as economy_seats_price,
                max(distinct bag_price.carry_on_price) as carry_on_price,
                max(distinct bag_price.checked_bag_price) as checked_bag_price,
                max(distinct departure_gate.gate_no) as departure_gate,
                max(distinct arrival_gate.gate_no) as arrival_gate,
                max(distinct bc.baggage_claim_key) as baggage_claim
            FROM gam8r0.flights f
            JOIN gam8r0.airports arrival_airport ON f.arrival_airport = arrival_airport.airport_code
            JOIN gam8r0.airports departure_airport ON f.departure_airport = departure_airport.airport_code
            JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
            JOIN gam8r0.gates departure_gate ON f.departure_gate_no = departure_gate.gate_key
            JOIN gam8r0.gates arrival_gate ON f.arrival_gate_no = arrival_gate.gate_key
            JOIN gam8r0.baggage_claims bc ON f.baggage_claim_no = bc.baggage_claim_key
            LEFT JOIN gam8r0.ticket_flights tf_total ON f.flight_id = tf_total.flight_id AND tf_total.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_total_wl ON f.flight_id = tf_total_wl.flight_id AND tf_total_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_business_wl ON f.flight_id = tf_business_wl.flight_id AND tf_business_wl.fare_conditions = 'Business' AND tf_business_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_first_wl ON f.flight_id = tf_first_wl.flight_id AND tf_first_wl.fare_conditions = 'First' AND tf_first_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_economy_wl ON f.flight_id = tf_economy_wl.flight_id AND tf_economy_wl.fare_conditions = 'Economy' AND tf_economy_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
            LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
            LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
            LEFT JOIN gam8r0.baggage_prices bag_price ON f.flight_id = bag_price.flight_id
            LEFT JOIN gam8r0.fare_prices business_fare ON f.flight_id = business_fare.flight_id AND business_fare.fare_conditions = 'Business'
            LEFT JOIN gam8r0.fare_prices first_fare ON f.flight_id = first_fare.flight_id AND first_fare.fare_conditions = 'First'
            LEFT JOIN gam8r0.fare_prices economy_fare ON f.flight_id = economy_fare.flight_id AND economy_fare.fare_conditions = 'Economy'
            GROUP BY f.flight_id, departure_airport.city, arrival_airport.city;
        `);

        return res.json(flights.rows);
    } catch (err) {
        // console.log(err.message);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** GET Flight */
router.get('/:id', async (req, res) => {
    try {
        const { id: flight_id } = req.params;
        // get flight details, seat details, 
        const flights_data = await pool.query(`
            SELECT f.*, 
                arrival_airport.city as arrival_city,
                departure_airport.city as departure_city,
                count(distinct s.seat_key) - count(distinct tf_total.ticket_no) as total_seats_available,
                count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as business_seats_available,
                count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as first_seats_available,
                count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as economy_seats_available,
                count(distinct tf_business.ticket_no) as business_seats_taken, 
                count(distinct tf_first.ticket_no) as first_seats_taken,
                count(distinct tf_economy.ticket_no) as economy_seats_taken,
                count(distinct tf_business_wl.ticket_no) as business_seats_waitlisted,
                count(distinct tf_first_wl.ticket_no) as first_seats_waitlisted,
                count(distinct tf_economy_wl.ticket_no) as economy_seats_waitlisted,
                max(distinct business_fare.fare_price) as business_seats_price,
                max(distinct first_fare.fare_price) as first_seats_price,
                max(distinct economy_fare.fare_price) as economy_seats_price,
                max(distinct bag_price.carry_on_price) as carry_on_price,
                max(distinct bag_price.checked_bag_price) as checked_bag_price,
                max(distinct departure_gate.gate_no) as departure_gate,
                max(distinct arrival_gate.gate_no) as arrival_gate,
                max(distinct bc.baggage_claim_key) as baggage_claim
            FROM gam8r0.flights f
            JOIN gam8r0.airports arrival_airport ON f.arrival_airport = arrival_airport.airport_code
            JOIN gam8r0.airports departure_airport ON f.departure_airport = departure_airport.airport_code
            JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
            JOIN gam8r0.gates departure_gate ON f.departure_gate_no = departure_gate.gate_key
            JOIN gam8r0.gates arrival_gate ON f.arrival_gate_no = arrival_gate.gate_key
            JOIN gam8r0.baggage_claims bc ON f.baggage_claim_no = bc.baggage_claim_key
            LEFT JOIN gam8r0.ticket_flights tf_total ON f.flight_id = tf_total.flight_id AND tf_total.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_total_wl ON f.flight_id = tf_total_wl.flight_id AND tf_total_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_business_wl ON f.flight_id = tf_business_wl.flight_id AND tf_business_wl.fare_conditions = 'Business' AND tf_business_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_first_wl ON f.flight_id = tf_first_wl.flight_id AND tf_first_wl.fare_conditions = 'First' AND tf_first_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_economy_wl ON f.flight_id = tf_economy_wl.flight_id AND tf_economy_wl.fare_conditions = 'Economy' AND tf_economy_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
            LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
            LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
            LEFT JOIN gam8r0.baggage_prices bag_price ON f.flight_id = bag_price.flight_id
            LEFT JOIN gam8r0.fare_prices business_fare ON f.flight_id = business_fare.flight_id AND business_fare.fare_conditions = 'Business'
            LEFT JOIN gam8r0.fare_prices first_fare ON f.flight_id = first_fare.flight_id AND first_fare.fare_conditions = 'First'
            LEFT JOIN gam8r0.fare_prices economy_fare ON f.flight_id = economy_fare.flight_id AND economy_fare.fare_conditions = 'Economy'
            WHERE f.flight_id = $1
            GROUP BY f.flight_id, departure_airport.city, arrival_airport.city;
        `, [flight_id])
        const passengers_data = await pool.query(`
            SELECT tf.*,
                p.*,
                bp.seat_key,
                s.seat_no,
                s.fare_conditions as seat_fare_conditions,
                bg.baggage_id,
                bg.type
            FROM gam8r0.ticket_flights tf
            LEFT JOIN gam8r0.tickets t ON tf.ticket_no = t.ticket_no
            LEFT JOIN gam8r0.passengers p ON t.passenger_id = p.passenger_id
            LEFT JOIN gam8r0.boarding_passes bp ON tf.ticket_no = bp.ticket_no AND tf.flight_id = bp.flight_id  
            LEFT JOIN gam8r0.seats s ON bp.seat_key = s.seat_key
            LEFT JOIN gam8r0.baggages bg ON bp.ticket_no = bg.ticket_no AND bp.flight_id = bg.flight_id
            WHERE tf.flight_id = $1;
        `, [flight_id]);
        const passengers = []; 
        passengers_data.rows.map(passenger => {
            const passenger_obj = passengers.find(x => x.passenger_id === passenger.passenger_id);
            if (passenger_obj) {
                if (passenger.seat_key) {
                    passenger_obj.boarding_pass.seat_key = passenger.seat_key;
                    passenger_obj.boarding_pass.seat_no = passenger.seat_no;
                    passenger_obj.boarding_pass.fare_conditions = passenger.seat_fare_conditions;
                    passenger_obj.checked_in = true;
                }
                if (passenger.baggage_id && passenger.type && passenger_obj.boarding_pass.baggage) {
                    passenger_obj.boarding_pass.baggage.push({
                        baggage_id: passenger.baggage_id,
                        type: passenger.type
                    });
                }
            } else {
                const obj = {
                    book_ref: passenger.book_ref,
                    passenger_id: passenger.passenger_id,
                    ticket_no: passenger.ticket_no,
                    carry_ons: passenger.carry_ons,
                    checked_bags: passenger.checked_bags,
                    fare_conditions: passenger.fare_conditions,
                    is_waitlisted: passenger.is_waitlisted,
                    first_name: passenger.first_name,
                    last_name: passenger.last_name,
                    boarding_pass: {},
                    checked_in: false
                };
                if (passenger.seat_key) {
                    obj.checked_in = true;
                    obj.boarding_pass.seat_key = passenger.seat_key;
                    obj.boarding_pass.seat_no = passenger.seat_no;
                    obj.boarding_pass.fare_conditions = passenger.seat_fare_conditions;
                }
                if (passenger.baggage_id && passenger.type) {
                    obj.boarding_pass.baggage = [{
                        baggage_id: passenger.baggage_id,
                        type: passenger.type
                    }];
                }
                passengers.push(obj);
            }
        })
        const flight = {
            flight: flights_data.rows[0],
            passengers: passengers
        };

        return res.json(flight);
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** POST Flight */
router.post('/', async (req, res) => {
    try {
        const {
            boarding_time, departure_gate, arrival_gate, baggage_claim,
            scheduled_departure, scheduled_arrival, includes_movie,
            includes_meal, allow_waitlist, economy_seats_price, business_seats_price,
            first_seats_price, carry_on_price, checked_bag_price, departure_airport, 
            arrival_airport, aircraft_code
        } = req.body;
        await pool.query('BEGIN;');

        const flight_data = await pool.query(`
            INSERT INTO 
            gam8r0.flights (
                boarding_time,
                departure_airport,
                arrival_airport,
                departure_gate_no,
                arrival_gate_no,
                baggage_claim_no,
                scheduled_departure,
                scheduled_arrival,
                actual_departure,
                actual_arrival,
                aircraft_code,
                includes_movie,
                includes_meal,
                allow_waitlist
            )
            VALUES ($1,$2,$3,$4,$5,$6,$7,
                    $8,$9,$10,$11,$12,$13,$14)
            RETURNING *;
        `, [boarding_time, departure_airport, arrival_airport, departure_gate, arrival_gate, baggage_claim, scheduled_departure,
            scheduled_arrival, scheduled_departure, scheduled_arrival, aircraft_code, !!includes_movie, !!includes_meal, !!allow_waitlist]);
        const flight_id = flight_data.rows[0].flight_id;
        
        await create_flight_fare_prices(flight_id, economy_seats_price, business_seats_price, first_seats_price);
        await create_flight_baggage_prices(flight_id, carry_on_price, checked_bag_price);
        // throw new Error("It worked");
        await pool.query('COMMIT;');
        return res.json(flight_data.rows);
    } catch (err) {
        await pool.query('ROLLBACK;');
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});


/** PUT Flight */
router.put('/:id', async (req, res) => {
    try {
        const { id: flight_id } = req.params;
        const {
            departure_gate, arrival_gate, baggage_claim, scheduled_departure, scheduled_arrival,
            boarding_time, actual_departure, actual_arrival, status,
            economy_seats_price, business_seats_price, first_seats_price,
            checked_bag_price, carry_on_price, includes_meal, includes_movie
        } = req.body;
        await pool.query('BEGIN;');
        
        await update_flight_fare_prices(flight_id, economy_seats_price, business_seats_price, first_seats_price);
        await update_flight_baggage_prices(flight_id, carry_on_price, checked_bag_price);
        const flight_data = await pool.query(`
            UPDATE gam8r0.flights 
            SET 
                status = $1, 
                boarding_time = $2,
                departure_gate_no = $3, 
                arrival_gate_no = $4, 
                scheduled_departure = $5, 
                scheduled_arrival = $6, 
                actual_departure = $7, 
                actual_arrival = $8,
                includes_movie = $9, 
                includes_meal = $10,
                baggage_claim_no = $11
            WHERE flight_id = $12
            RETURNING *;
        `, [status, boarding_time, departure_gate, arrival_gate, 
            scheduled_departure, scheduled_arrival, actual_departure, 
            actual_arrival, !!includes_movie, !!includes_meal, baggage_claim, flight_id]);

        if (status === 'Cancelled') {
            await cancel_boarding_passes(flight_id, status);
        }
        
        await pool.query('COMMIT;');
        return res.status(200).json('OK');
    } catch (err) {
        await pool.query('ROLLBACK;');
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** DELETE Flight */
router.delete('/:id', async (req, res) => {
    try {
        const { id: flight_id } = req.params;
        await pool.query(`BEGIN;`)

        const flight = await pool.query(`
            SELECT * 
            FROM gam8r0.flights
            WHERE flight_id = $1;
        `, [flight_id]);
        await pool.query(`COMMIT;`);
        return res.json(flight.rows);
    } catch (err) {
        await pool.query('ROLLBACK;');
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

router.post('/search', async (req, res) => {
    try {
        const { type } = req.body;
        if (type === 'one') {
            const { departure_airport, arrival_airport, departure_date, allow_connected_flights } = req.body;
            const flights = await get_one_way_flights(departure_airport, arrival_airport, departure_date, allow_connected_flights);
            return res.json(flights);
        } else if (type === 'round') {
            const { departure_airport, arrival_airport, departure_date, returning_date, allow_connected_flights } = req.body;
            const flights = await get_round_trip_flights(departure_airport, arrival_airport, departure_date, returning_date, allow_connected_flights);
            return res.json(flights);
        } else if (type === 'multi') {
            // flights = get_multi_city_flights(departure_airport, arrival_airport,
            throw new Error("Not implemented yet.");
        }

        return res.json(flights);

    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

router.post('/search/all', async (req, res) => {
    try {
        const { departure_airport, arrival_airport, departure_date } = req.body;
        const flights = await pool.query(`
            SELECT f.*, 
                arrival_airport.city as arrival_city,
                departure_airport.city as departure_city,
                count(distinct s.seat_key) - count(distinct tf_total.ticket_no) as total_seats_available,
                count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as business_seats_available,
                count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as first_seats_available,
                count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as economy_seats_available,
                count(distinct tf_business.ticket_no) as business_seats_taken, 
                count(distinct tf_first.ticket_no) as first_seats_taken,
                count(distinct tf_economy.ticket_no) as economy_seats_taken,
                count(distinct tf_business_wl.ticket_no) as business_seats_waitlisted,
                count(distinct tf_first_wl.ticket_no) as first_seats_waitlisted,
                count(distinct tf_economy_wl.ticket_no) as economy_seats_waitlisted,
                max(distinct business_fare.fare_price) as business_seats_price,
                max(distinct first_fare.fare_price) as first_seats_price,
                max(distinct economy_fare.fare_price) as economy_seats_price,
                max(distinct bag_price.carry_on_price) as carry_on_price,
                max(distinct bag_price.checked_bag_price) as checked_bag_price,
                max(distinct departure_gate.gate_no) as departure_gate,
                max(distinct arrival_gate.gate_no) as arrival_gate,
                max(distinct bc.baggage_claim_key) as baggage_claim
            FROM gam8r0.flights f
            JOIN gam8r0.airports arrival_airport ON f.arrival_airport = arrival_airport.airport_code
            JOIN gam8r0.airports departure_airport ON f.departure_airport = departure_airport.airport_code
            JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
            JOIN gam8r0.gates departure_gate ON f.departure_gate_no = departure_gate.gate_key
            JOIN gam8r0.gates arrival_gate ON f.arrival_gate_no = arrival_gate.gate_key
            JOIN gam8r0.baggage_claims bc ON f.baggage_claim_no = bc.baggage_claim_key
            LEFT JOIN gam8r0.ticket_flights tf_total ON f.flight_id = tf_total.flight_id AND tf_total.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_total_wl ON f.flight_id = tf_total_wl.flight_id AND tf_total_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_business_wl ON f.flight_id = tf_business_wl.flight_id AND tf_business_wl.fare_conditions = 'Business' AND tf_business_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_first_wl ON f.flight_id = tf_first_wl.flight_id AND tf_first_wl.fare_conditions = 'First' AND tf_first_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_economy_wl ON f.flight_id = tf_economy_wl.flight_id AND tf_economy_wl.fare_conditions = 'Economy' AND tf_economy_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
            LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
            LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
            LEFT JOIN gam8r0.baggage_prices bag_price ON f.flight_id = bag_price.flight_id
            LEFT JOIN gam8r0.fare_prices business_fare ON f.flight_id = business_fare.flight_id AND business_fare.fare_conditions = 'Business'
            LEFT JOIN gam8r0.fare_prices first_fare ON f.flight_id = first_fare.flight_id AND first_fare.fare_conditions = 'First'
            LEFT JOIN gam8r0.fare_prices economy_fare ON f.flight_id = economy_fare.flight_id AND economy_fare.fare_conditions = 'Economy'
            WHERE departure_airport.city ILIKE $1 
                AND arrival_airport.city ILIKE $2 
                AND DATE(scheduled_departure ) = $3
            GROUP BY f.flight_id, departure_airport.city, arrival_airport.city;
        `, [departure_airport, arrival_airport, departure_date]);

        return res.json(flights.rows);
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});
    }
});

const get_one_way_flights = async (departure_city, arrival_city, departure_date, allow_connected_flights) => {
   
    const depth_limit = allow_connected_flights ? 2 : 1
    const connected_flights_data = await pool.query(`
        WITH RECURSIVE connecting_flights AS (
            SELECT 
                -1 AS prev_flight_id,
                f.flight_id,
                f.departure_airport, 
                f.arrival_airport,
                f.scheduled_departure,
                f.scheduled_arrival,
                f.status,
                fp.fare_price as base_price,
                0 AS stops
            FROM gam8r0.flights f
            JOIN gam8r0.fare_prices fp ON fp.flight_id = f.flight_id AND fp.fare_conditions = 'Economy'
            WHERE f.status != 'Cancelled' 
                AND f.status != 'Departed' 
                AND f.status != 'Arrived'
                AND f.status != 'Boarding'
            UNION ALL
            
            SELECT 
                cf.flight_id AS prev_flight_id,
                f.flight_id,
                cf.departure_airport, 
                f.arrival_airport,
                cf.scheduled_departure,
                f.scheduled_arrival,
                f.status,
                fp.fare_price + cf.base_price as base_price,
                cf.stops + 1 AS stops
            FROM gam8r0.flights f
            INNER JOIN connecting_flights cf ON cf.arrival_airport = f.departure_airport
            JOIN gam8r0.fare_prices fp ON fp.flight_id = f.flight_id AND fp.fare_conditions = 'Economy'
            WHERE cf.stops + 1 < ${depth_limit}
                AND cf.departure_airport != f.arrival_airport 
                AND cf.scheduled_arrival < f.scheduled_departure
                AND f.status != 'Cancelled' 
                AND f.status != 'Departed' 
                AND f.status != 'Arrived'
                AND f.status != 'Boarding'
        )

        SELECT cf.prev_flight_id,
            cf.flight_id,
            cf.departure_airport,
            cf.arrival_airport,
            cf.scheduled_departure,
            cf.scheduled_arrival,
            cf.base_price,
            cf.stops
        FROM connecting_flights cf
        JOIN gam8r0.airports departure_airport ON cf.departure_airport = departure_airport.airport_code
        JOIN gam8r0.airports arrival_airport ON cf.arrival_airport = arrival_airport.airport_code
        WHERE departure_airport.city ILIKE $1 AND arrival_airport.city ILIKE $2 AND DATE(cf.scheduled_departure) = $3;
    `, [departure_city, arrival_city, departure_date]);

    const relevant_flight_ids = {};
    connected_flights_data.rows.forEach(x => {
        if (!relevant_flight_ids[x.flight_id])
            relevant_flight_ids[x.flight_id] = true;
        if (x.prev_flight_id !== -1 && !relevant_flight_ids[x.prev_flight_id])
            relevant_flight_ids[x.prev_flight_id] = true;
    });
    let relevant_flights = [];
    const flight_ids = Object.keys(relevant_flight_ids);
    if (flight_ids.length > 0) {
        const relevant_flights_data = await pool.query(`
            SELECT f.*, 
                arrival_airport.city as arrival_city,
                departure_airport.city as departure_city,
                count(distinct s.seat_key) - count(distinct tf_total.ticket_no) as total_seats_available,
                count(distinct seats_business.seat_key) - count(distinct tf_business.ticket_no) as business_seats_available,
                count(distinct seats_first.seat_key) - count(distinct tf_first.ticket_no) as first_seats_available,
                count(distinct seats_economy.seat_key) - count(distinct tf_economy.ticket_no) as economy_seats_available,
                count(distinct tf_business.ticket_no) as business_seats_taken, 
                count(distinct tf_first.ticket_no) as first_seats_taken,
                count(distinct tf_economy.ticket_no) as economy_seats_taken,
                count(distinct tf_business_wl.ticket_no) as business_seats_waitlisted,
                count(distinct tf_first_wl.ticket_no) as first_seats_waitlisted,
                count(distinct tf_economy_wl.ticket_no) as economy_seats_waitlisted,
                max(distinct business_fare.fare_price) as business_seats_price,
                max(distinct first_fare.fare_price) as first_seats_price,
                max(distinct economy_fare.fare_price) as economy_seats_price,
                max(distinct bag_price.carry_on_price) as carry_on_price,
                max(distinct bag_price.checked_bag_price) as checked_bag_price,
                max(distinct departure_gate.gate_no) as departure_gate,
                max(distinct arrival_gate.gate_no) as arrival_gate,
                max(distinct bc.baggage_claim_no) as baggage_claim
            FROM gam8r0.flights f
            JOIN gam8r0.airports arrival_airport ON f.arrival_airport = arrival_airport.airport_code
            JOIN gam8r0.airports departure_airport ON f.departure_airport = departure_airport.airport_code
            JOIN gam8r0.seats s ON f.aircraft_code = s.aircraft_code
            JOIN gam8r0.gates departure_gate ON f.departure_gate_no = departure_gate.gate_key
            JOIN gam8r0.gates arrival_gate ON f.arrival_gate_no = arrival_gate.gate_key
            JOIN gam8r0.baggage_claims bc ON f.baggage_claim_no = bc.baggage_claim_key
            LEFT JOIN gam8r0.ticket_flights tf_total ON f.flight_id = tf_total.flight_id AND tf_total.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_total_wl ON f.flight_id = tf_total_wl.flight_id AND tf_total_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_business ON f.flight_id = tf_business.flight_id AND tf_business.fare_conditions = 'Business' AND tf_business.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_business_wl ON f.flight_id = tf_business_wl.flight_id AND tf_business_wl.fare_conditions = 'Business' AND tf_business_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_first ON f.flight_id = tf_first.flight_id AND tf_first.fare_conditions = 'First' AND tf_first.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_first_wl ON f.flight_id = tf_first_wl.flight_id AND tf_first_wl.fare_conditions = 'First' AND tf_first_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.ticket_flights tf_economy ON f.flight_id = tf_economy.flight_id AND tf_economy.fare_conditions = 'Economy' AND tf_economy.is_waitlisted = FALSE
            LEFT JOIN gam8r0.ticket_flights tf_economy_wl ON f.flight_id = tf_economy_wl.flight_id AND tf_economy_wl.fare_conditions = 'Economy' AND tf_economy_wl.is_waitlisted = TRUE
            LEFT JOIN gam8r0.seats seats_business ON s.seat_key = seats_business.seat_key AND seats_business.fare_conditions = 'Business'
            LEFT JOIN gam8r0.seats seats_first ON s.seat_key = seats_first.seat_key AND seats_first.fare_conditions = 'First'
            LEFT JOIN gam8r0.seats seats_economy ON s.seat_key = seats_economy.seat_key AND seats_economy.fare_conditions = 'Economy'
            LEFT JOIN gam8r0.baggage_prices bag_price ON f.flight_id = bag_price.flight_id
            LEFT JOIN gam8r0.fare_prices business_fare ON f.flight_id = business_fare.flight_id AND business_fare.fare_conditions = 'Business'
            LEFT JOIN gam8r0.fare_prices first_fare ON f.flight_id = first_fare.flight_id AND first_fare.fare_conditions = 'First'
            LEFT JOIN gam8r0.fare_prices economy_fare ON f.flight_id = economy_fare.flight_id AND economy_fare.fare_conditions = 'Economy'
            WHERE f.flight_id IN ( ${flight_ids.join(',')} )
            GROUP BY f.flight_id, departure_airport.city, arrival_airport.city;
        `);
        relevant_flights = relevant_flights_data.rows;
    }
    return {
        connections: connected_flights_data.rows,
        data: relevant_flights,
    };
};

const get_round_trip_flights = async (departure_airport, arrival_airport, departure_date, returning_date, allow_connected_flights) => {
    const departing_flights = await get_one_way_flights(departure_airport, arrival_airport, departure_date, allow_connected_flights);
    const returning_flights = await get_one_way_flights(arrival_airport, departure_airport, returning_date, allow_connected_flights);
    const relevant_flights = departing_flights.data.concat(returning_flights.data);
    // return departure_flights and returning_flights
    return {
        departing_connections: departing_flights.connections,
        returning_connections: returning_flights.connections,
        data: relevant_flights
    };
};

const create_flight_fare_prices = async (flight_id, economy_seats_price, business_seats_price, first_seats_price) => {
    const economy_fare_prices_data = await pool.query(`
        INSERT INTO
        gam8r0.fare_prices (flight_id, fare_conditions, fare_price)
        VALUES ($1, $2, $3)
        RETURNING *;
    `, [flight_id, 'Economy', economy_seats_price]);
    const business_fare_prices_data = await pool.query(`
        INSERT INTO
        gam8r0.fare_prices (flight_id, fare_conditions, fare_price)
        VALUES ($1, $2, $3)
        RETURNING *;
    `, [flight_id, 'Business', business_seats_price]);
    const first_fare_prices_data = await pool.query(`
        INSERT INTO
        gam8r0.fare_prices (flight_id, fare_conditions, fare_price)
        VALUES ($1, $2, $3)
        RETURNING *;
    `, [flight_id, 'First', first_seats_price]);
};

const create_flight_baggage_prices = async (flight_id, carry_on_price, checked_bag_price) => {
    const baggage_price_data = await pool.query(`
        INSERT INTO
        gam8r0.baggage_prices (flight_id, carry_on_price, checked_bag_price)
        VALUES ($1, $2, $3)
        RETURNING *;
    `, [flight_id, carry_on_price, checked_bag_price]);
};

const update_flight_fare_prices = async (flight_id, economy_seats_price, business_seats_price, first_seats_price) => {
    const economy_fare_prices_data = await pool.query(`
        UPDATE gam8r0.fare_prices
        SET fare_price = $1
        WHERE flight_id = $2 
            AND fare_conditions = 'Economy'
        RETURNING *;
    `, [economy_seats_price, flight_id]);
    const business_fare_prices_data = await pool.query(`
        UPDATE gam8r0.fare_prices
        SET fare_price = $1
        WHERE flight_id = $2 
            AND fare_conditions = 'Business'
        RETURNING *;
    `, [business_seats_price, flight_id]);
    const first_fare_prices_data = await pool.query(`
        UPDATE gam8r0.fare_prices
        SET fare_price = $1
        WHERE flight_id = $2 
            AND fare_conditions = 'First'
        RETURNING *;
    `, [first_seats_price, flight_id]);
};

const update_flight_baggage_prices = async (flight_id, carry_on_price, checked_bag_price) => {
    const baggage_price_data = await pool.query(`
        UPDATE gam8r0.baggage_prices
        SET carry_on_price = $1,
            checked_bag_price = $2
        WHERE flight_id = $3
        RETURNING *;
    `, [carry_on_price, checked_bag_price, flight_id]);
};

const cancel_boarding_passes = async (flight_id, status) => {
    await pool.query(`
        DELETE 
        FROM gam8r0.boarding_passes
        WHERE flight_id = $1
        RETURNING *;
    `, [flight_id]);
    await pool.query(`
        DELETE
        FROM gam8r0.baggages
        WHERE flight_id = $1
        RETURNING *;
    `, [flight_id]);
};

module.exports = router;