DROP TABLE IF EXISTS customers CASCADE;

DROP TABLE IF EXISTS tickets CASCADE;

DROP TABLE IF EXISTS bookings CASCADE;

DROP TABLE IF EXISTS ticket_flights CASCADE;

DROP TABLE IF EXISTS flights CASCADE;

DROP TABLE IF EXISTS passengers CASCADE;

DROP TABLE IF EXISTS payments CASCADE;

DROP TABLE IF EXISTS airports CASCADE;

DROP TABLE IF EXISTS aircrafts CASCADE;

DROP TABLE IF EXISTS gates CASCADE;

DROP TABLE IF EXISTS boarding_passes CASCADE;

DROP TABLE IF EXISTS seats CASCADE;

DROP TABLE IF EXISTS baggage_claims CASCADE;

DROP TABLE IF EXISTS baggages CASCADE;

DROP TABLE IF EXISTS baggage_prices CASCADE;

DROP TABLE IF EXISTS fare_prices CASCADE;

CREATE TABLE customers(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telephone VARCHAR(50) NOT NULL
);

CREATE TABLE passengers(
    passenger_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL
);

CREATE TABLE payments(
    payment_ref SERIAL PRIMARY KEY,
    card_no VARCHAR(250) NOT NULL,
    taxes MONEY NOT NULL,
    discount MONEY NOT NULL,
    base_amount MONEY NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE bookings(
    book_ref SERIAL PRIMARY KEY,
    book_date TIMESTAMP,
    customer_id SERIAL NOT NULL REFERENCES customers(customer_id),
    payment_ref SERIAL NOT NULL REFERENCES payments(payment_ref) ON DELETE CASCADE
);

CREATE TABLE tickets(
    ticket_no SERIAL PRIMARY KEY,
    book_ref SERIAL NOT NULL REFERENCES bookings(book_ref) ON DELETE CASCADE,
    passenger_id SERIAL NOT NULL REFERENCES passengers(passenger_id) ON DELETE CASCADE
);

CREATE TABLE airports(
    airport_code VARCHAR(10) NOT NULL PRIMARY KEY,
    airport_name VARCHAR(50) NOT NULL,
    city VARCHAR(25) NOT NULL,
    coordinates VARCHAR(50) NOT NULL,
    timezone VARCHAR(25) NOT NULL
);

CREATE TABLE aircrafts(
    aircraft_code VARCHAR(10) PRIMARY KEY,
    model VARCHAR(25) NOT NULL,
    range INT NOT NULL
);

CREATE TABLE gates(
    gate_key SERIAL PRIMARY KEY,
    gate_no VARCHAR(10) NOT NULL,
    airport_code VARCHAR(10) NOT NULL REFERENCES airports(airport_code),
    UNIQUE (gate_no, airport_code)
);

CREATE TABLE baggage_claims(
    baggage_claim_key SERIAL PRIMARY KEY,
    baggage_claim_no VARCHAR(10) NOT NULL,
    airport_code VARCHAR(10) NOT NULL REFERENCES airports(airport_code),
    UNIQUE (baggage_claim_no, airport_code)
);

CREATE TABLE seats(
    seat_key SERIAL PRIMARY KEY,
    seat_no SERIAL NOT NULL,
    aircraft_code VARCHAR(10) NOT NULL REFERENCES aircrafts(aircraft_code),
    fare_conditions VARCHAR(25),
    UNIQUE (seat_no, aircraft_code)
);

CREATE TABLE flights(
    flight_id SERIAL PRIMARY KEY,
    status VARCHAR(25) DEFAULT 'Scheduled',
    boarding_time TIMESTAMP NOT NULL,
    scheduled_departure TIMESTAMP NOT NULL,
    scheduled_arrival TIMESTAMP NOT NULL,
    actual_departure TIMESTAMP NOT NULL,
    actual_arrival TIMESTAMP NOT NULL,
    includes_movie BOOLEAN NOT NULL,
    includes_meal BOOLEAN NOT NULL,
    allow_waitlist BOOLEAN NOT NULL,
    baggage_claim_no SERIAL NOT NULL REFERENCES baggage_claims(baggage_claim_key),
    departure_airport VARCHAR(10) NOT NULL REFERENCES airports(airport_code),
    departure_gate_no SERIAL NOT NULL REFERENCES gates(gate_key),
    arrival_airport VARCHAR(10) NOT NULL REFERENCES airports(airport_code),
    arrival_gate_no SERIAL NOT NULL REFERENCES gates(gate_key),
    aircraft_code VARCHAR(10) NOT NULL REFERENCES aircrafts(aircraft_code)
);

CREATE TABLE baggage_prices(
    flight_pricing_id SERIAL PRIMARY KEY,
    flight_id SERIAL NOT NULL REFERENCES flights(flight_id),
    carry_on_price MONEY NOT NULL,
    checked_bag_price MONEY NOT NULL
);

CREATE TABLE fare_prices(
    fare_pricing_id SERIAL PRIMARY KEY,
    flight_id SERIAL NOT NULL REFERENCES flights(flight_id),
    fare_conditions VARCHAR(25) NOT NULL,
    fare_price MONEY NOT NULL
);

CREATE TABLE ticket_flights(
    flight_id SERIAL NOT NULL REFERENCES flights(flight_id),
    ticket_no SERIAL NOT NULL REFERENCES tickets(ticket_no) ON DELETE CASCADE,
    carry_ons SMALLINT NOT NULL,
    checked_bags SMALLINT NOT NULL,
    fare_conditions VARCHAR(25) NOT NULL,
    is_waitlisted BOOLEAN NOT NULL,
    PRIMARY KEY (flight_id, ticket_no)
);

CREATE TABLE boarding_passes(
    flight_id SERIAL NOT NULL REFERENCES flights(flight_id),
    ticket_no SERIAL NOT NULL REFERENCES tickets(ticket_no) ON DELETE CASCADE,
    seat_key SERIAL REFERENCES seats(seat_key),
    PRIMARY KEY (flight_id, ticket_no)
);

CREATE TABLE baggages(
    baggage_id SERIAL PRIMARY KEY,
    ticket_no SERIAL NOT NULL REFERENCES tickets(ticket_no),
    flight_id SERIAL NOT NULL REFERENCES flights(flight_id),
    type VARCHAR(25) NOT NULL
);