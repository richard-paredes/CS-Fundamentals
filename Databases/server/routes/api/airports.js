const express = require('express'),
    router = express.Router({ mergeParams: true }),
    pool = require('../../database/index.js'),
    array_utils = require('../../utils/array-utils.js');

/** GET Airports */
router.get('/', async (req, res) => {
    try {
        const airports = await pool.query(`
            SELECT *
            FROM gam8r0.airports;
        `);
        const gates = await pool.query(`
            SELECT *
            FROM gam8r0.gates;
        `);
        const baggage_claims = await pool.query(`
            SELECT *
            FROM gam8r0.baggage_claims;
        `);
        return res.json({
            airports: airports.rows,
            gates: gates.rows,
            baggage_claims: baggage_claims.rows
        });
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** GET Airport */
router.get('/:id', async (req, res) => {
    try {
        const { id: airport_code } = req.params;
        const airport = await pool.query(`
            SELECT *
            FROM gam8r0.airports 
            WHERE airport_code = $1;`
            , [airport_code]);
        const gates = await pool.query(`
            SELECT *
            FROM gam8r0.gates
            WHERE airport_code = $1;
        `, [airport_code]);
        return res.json(
            {
                airports: airport.rows,
                gates: gates.rows
            });
    } catch (err) {
        // console.log(err);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** POST Airport */
router.post('/', async (req, res) => {
    try {
        const { airport_code, airport_name, city, coordinates, timezone, gates, baggage_claims } = req.body;

        await pool.query('BEGIN;');
        await pool.query(`
            INSERT INTO 
            gam8r0.airports (airport_code, airport_name, city, coordinates, timezone)
            VALUES ($1, $2, $3, $4, $5);
        `, [airport_code, airport_name, city, coordinates, timezone]);

        await pool.query(`
            INSERT INTO
            gam8r0.gates (gate_no, airport_code)
            VALUES ${array_utils.expand(gates.length, 2)};
        `, array_utils.flatten(gates));

        await pool.query(`
            INSERT INTO
            gam8r0.baggage_claims (baggage_claim_no, airport_code)
            VALUES ${array_utils.expand(baggage_claims.length, 2)}
        `, array_utils.flatten(baggage_claims));
    
        await pool.query('COMMIT;');

        return res.status(200).json('OK');
    } catch (err) {
        await pool.query('ROLLBACK;');
        return res.status(500).json({...err, message: err.message});;
    }
});


/** PUT Airport */
router.put('/:id', async (req, res) => {
    try {
        const { id: airport_code } = req.params;
        const { airport_name, city, coordinates, timezone } = req.body;
        await pool.query(`BEGIN;`);
        await pool.query(`
            UPDATE gam8r0.airports 
            SET 
                airport_name = $1,
                city = $2,
                coordinates = $3,
                timezone = $4
            WHERE airport_code = $5
            RETURNING *;
        `, [airport_name, city, coordinates, timezone, airport_code]);
        await pool.query(`COMMIT;`);

        return res.status(200).json('OK');
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});

/** DELETE Airport */
router.delete('/:id', async (req, res) => {
    try {
        const { id: airport_code } = req.params;
        await pool.query(`BEGIN;`);
        const airport = await pool.query(`
            DELETE 
            FROM gam8r0.airports
            WHERE airport_code = $1
            RETURNING *;
        `, [airport_code]);
        await pool.query(`COMMIT`);
        return res.json(airport.rows);
    } catch (err) {
        // console.log(err);
        await pool.query(`ROLLBACK;`);
        return res.status(500).json({...err, message: err.message});;
    }
});

module.exports = router;