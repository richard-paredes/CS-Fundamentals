
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
        
            SELECT *
            FROM gam8r0.airports;
        
            SELECT a.*,
                COUNT(distinct s.seat_key) as total_seats
            FROM gam8r0.aircrafts a
            JOIN gam8r0.seats s ON a.aircraft_code = s.aircraft_code
            GROUP BY a.aircraft_code;
        
            SELECT *
            FROM gam8r0.gates;
        
            SELECT *
            FROM gam8r0.baggage_claims;
        
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
        
            SELECT *
            FROM gam8r0.airports;
        
            SELECT a.*,
                COUNT(distinct s.seat_key) as total_seats
            FROM gam8r0.aircrafts a
            JOIN gam8r0.seats s ON a.aircraft_code = s.aircraft_code
            GROUP BY a.aircraft_code;
        
            SELECT *
            FROM gam8r0.gates;
        
            SELECT *
            FROM gam8r0.baggage_claims;
        
                SELECT *
                FROM gam8r0.customers
                WHERE customer_id = "1";
            
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
            WHERE cf.stops + 1 < 1
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
        WHERE departure_airport.city ILIKE "Houston" AND arrival_airport.city ILIKE "New York" AND DATE(cf.scheduled_departure) = "2020-12-23";
    
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
            WHERE f.flight_id IN ( 2 )
            GROUP BY f.flight_id, departure_airport.city, arrival_airport.city;
        