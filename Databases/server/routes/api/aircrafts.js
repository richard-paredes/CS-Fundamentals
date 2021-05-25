const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index'),
    array_utils = require('../../utils/array-utils');

/** GET Aircrafts */
router.get('/', async (req, res) => {
    try {
        const aircrafts = await pool.query(`
            SELECT a.*,
                COUNT(distinct s.seat_key) as total_seats
            FROM gam8r0.aircrafts a
            JOIN gam8r0.seats s ON a.aircraft_code = s.aircraft_code
            GROUP BY a.aircraft_code;
        `);
        return res.json(aircrafts.rows);
    } catch (err) {
        return res.status(500).json({...err, message: err.message});;
    }
});

/** GET Aircraft */
router.get('/:id', async (req, res) => {
    try {
        const { id: aircraft_code } = req.params;
        const aircraft = await pool.query(`
            SELECT *
            FROM gam8r0.aircrafts 
            WHERE aircraft_code = $1;`
            , [aircraft_code]);
        return res.json(aircraft.rows);
    } catch (err) {
        return res.status(500).json({...err, message: err.message});;
    }
});

/** POST Aircraft */
router.post('/', async (req, res) => {
    try {
        const { aircraft_code, model, range,
            business_no_seats,
            first_no_seats,
            economy_no_seats } = req.body;
        const num_business = parseInt(business_no_seats);
        const num_first = parseInt(first_no_seats);
        const num_economy = parseInt(economy_no_seats)
        const num_seats = num_business + num_first + num_economy;
        let seats = [];
        for (let i = 0; i < num_seats; i++) {
            if (i < num_first)
                seats.push([i, aircraft_code, 'First']);
            else if (i < num_business + num_first)
                seats.push([i, aircraft_code, 'Business']);
            else if (i < num_economy + num_business + num_first)
                seats.push([i, aircraft_code, 'Economy']);
        }

        await pool.query(`BEGIN;`);
        const aircraft = await pool.query(`
            INSERT INTO 
            gam8r0.aircrafts (aircraft_code, model, range)
            VALUES ($1, $2, $3)
            RETURNING *;
        `, [aircraft_code, model, range]);
        await pool.query(`
            INSERT INTO
            gam8r0.seats (seat_no, aircraft_code, fare_conditions)
            VALUES ${array_utils.expand(seats.length, 3)};
        `, array_utils.flatten(seats));
        
        await pool.query(`COMMIT;`);
        return res.json(aircraft.rows);
    } catch (err) {
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});
    }
});


/** PUT Aircraft */
router.put('/:id', async (req, res) => {
    try {
        const { id: aircraft_code } = req.params;
        const { model, range } = req.body;
        await pool.query(`BEGIN;`);
        const aircraft = await pool.query(`
            UPDATE gam8r0.aircrafts 
            SET 
                model = $1,
                range = $2
            WHERE aircraft_code = $3
            RETURNING *;
        `, [model, range, aircraft_code]);
        await pool.query(`COMMIT;`);
        return res.json(aircraft.rows);
    } catch (err) {
        // console.log(err);
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});;
    }
});

/** DELETE Aircraft */
router.delete('/:id', async (req, res) => {
    try {
        const { id: aircraft_code } = req.params;
        await pool.query(`BEGIN;`);
        const aircraft = await pool.query(`
            DELETE 
            FROM gam8r0.aircrafts
            WHERE aircraft_code = $1
            RETURNING *;
        `, [aircraft_code]);
        await pool.query(`COMMIT;`);
        return res.json(aircraft.rows);
    } catch (err) {
        // console.log(err);
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});;
    }
});

module.exports = router;