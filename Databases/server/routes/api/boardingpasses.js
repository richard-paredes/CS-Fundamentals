const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index'),
    array_utils = require('../../utils/array-utils');

// used to check in
router.post('/', async (req, res) => {
    try {
        const {ticket_no, flight_id} = req.body;
        
        await pool.query(`BEGIN;`);

        const ticket_flight_data = await pool.query(`
            SELECT tf.*, 
                f.flight_id, 
                f.aircraft_code
            FROM gam8r0.ticket_flights tf
            JOIN gam8r0.flights f ON tf.flight_id = f.flight_id
            WHERE tf.ticket_no = $1
                AND tf.flight_id = $2;
        `, [ticket_no, flight_id]);
        const ticket_flight = ticket_flight_data.rows[0];

        const seat_data = await pool.query(`
            SELECT seat_key, 
                fare_conditions
            FROM gam8r0.seats 
            WHERE fare_conditions = $1
                AND seat_key IN (
                    SELECT seat_key
                    FROM gam8r0.seats s
                    WHERE s.aircraft_code = $2
                    EXCEPT
                    SELECT seat_key
                    FROM gam8r0.boarding_passes b
                    WHERE b.flight_id = $3
                )
            LIMIT 1;
        `, [ticket_flight.fare_conditions, ticket_flight.aircraft_code, ticket_flight.flight_id]);

        if (seat_data.rowCount === 0) {
            throw new Error("No more seats are available on the flight");
        }
        const seat = seat_data.rows[0];
        
        // create boarding pass
        const boarding_pass_data = await pool.query(`
            INSERT INTO
            gam8r0.boarding_passes (flight_id, ticket_no, seat_key)
            VALUES ($1, $2, $3)
            RETURNING *;
        `, [ticket_flight.flight_id, ticket_flight.ticket_no, seat.seat_key]);

        const boarding_pass = boarding_pass_data.rows[0];

        // create baggages 
        const baggages = []
        for (let i = 0; i < ticket_flight.carry_ons; i++) baggages.push([boarding_pass.ticket_no, boarding_pass.flight_id, 'Carry-On']);
        for (let i = 0; i < ticket_flight.checked_bags; i++) baggages.push([boarding_pass.ticket_no, boarding_pass.flight_id, 'Luggage']);
        
        const baggage_data = await pool.query(`
            INSERT INTO
            gam8r0.baggages (ticket_no, flight_id, type)
            VALUES ${array_utils.expand(baggages.length, 3, 1, ['INTEGER', 'INTEGER', 'TEXT'])};
        `, array_utils.flatten(baggages));

        await pool.query(`COMMIT;`);
        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});
    }
});

router.delete('/', async (req, res) => {
    try {
        const { ticket_no, flight_id } = req.body;
        
        await pool.query('BEGIN;');
        const boarding_pass_data = await pool.query(`
            DELETE
            FROM gam8r0.boarding_passes
            WHERE ticket_no = $1
                AND flight_id = $2
            RETURNING *;
        `, [ticket_no, flight_id]);

        const baggages_data = await pool.query(`
            DELETE
            FROM gam8r0.baggages
            WHERE ticket_no = $1
                AND flight_id = $2
            RETURNING *;
        `, [ticket_no, flight_id])
        await pool.query('COMMIT;');
        
        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});
    }
});

module.exports = router;