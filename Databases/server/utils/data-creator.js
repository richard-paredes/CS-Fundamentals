const create_flight = (id) => {
    const airports = ['IAH', 'DFW', 'PHX', 'JFK', 'SFO', 'ATL', 'LAX', 'ORD', 'PHL', 'SEA', 'DEN', 'MCO', 'LAS', 'IAD', 'CLT'];
    const aircrafts = ['737-800', '737-700', 'A320', 'A321', '757-200', 'CRJ200', 'E175', 'A319', '737-900ER', 'CRJ900']

    const min_date = new Date('2020-12-10');
    const max_date = new Date('2021-01-31');
    const start_hour = Math.floor(getRandomNumber(0, 23));
    const end_hour = Math.floor(getRandomNumber(start_hour, 24));
    const flight_duration = Math.floor(getRandomNumber(2, 6));

    const boarding_time = getRandomDate(min_date, max_date, start_hour, end_hour);
    boarding_time.setSeconds(0);
    const departure_time = new Date(boarding_time);
    departure_time.setMinutes(getRandomNumber(80, 95));
    const arrival_time = new Date(departure_time);
    arrival_time.setHours(departure_time.getHours() + flight_duration);
    arrival_time.setMinutes(getRandomNumber(30, 60))
    const boarding = boarding_time.toLocaleString();
    const scheduled_departure = departure_time.toLocaleString();
    const scheduled_arrival = arrival_time.toLocaleString();
    const includes_movie = getRandomBoolean();
    const includes_meal = getRandomBoolean();
    const allow_waitlist = getRandomBoolean();
    let dep_idx = Math.floor(getRandomNumber(0, airports.length));
    let arr_idx = Math.floor(getRandomNumber(0, airports.length));

    while (dep_idx === arr_idx)
        arr_idx = Math.floor(getRandomNumber(0, airports.length));

    const departure_airport = airports[dep_idx];
    const arrival_airport = airports[arr_idx];
    const departure_gate_no = Math.floor(getRandomNumber((dep_idx + 1) * 12 - 12, (dep_idx + 1) * 12));
    const arrival_gate_no = Math.floor(getRandomNumber((arr_idx + 1) * 12 - 12, (arr_idx + 1) * 12));
    const baggage_claim_no = Math.floor(getRandomNumber((arr_idx + 1) * 15 - 15, (arr_idx + 1) * 15));
    const aircraft_code = aircrafts[Math.floor(getRandomNumber(0, aircrafts.length))]


    return [
        id, 
        'Scheduled',
        boarding,
        scheduled_departure,
        scheduled_arrival,
        scheduled_departure, 
        scheduled_arrival, 
        baggage_claim_no,
        includes_movie, 
        includes_meal, 
        allow_waitlist, 
        departure_airport,
        departure_gate_no, 
        arrival_airport, 
        arrival_gate_no, 
        aircraft_code
    ];
}

const getRandomDate = (start, end, startHour, endHour) => {
    var date = new Date(+start + Math.random() * (end - start));
    var hour = startHour + Math.random() * (endHour - startHour) | 0;
    date.setHours(hour);
    return date;
};

const getRandomNumber = (min, max) => {
    return Math.random() * (max - min) + min;
};

const getRandomBoolean = () => {
    return Math.random() > 0.5;
};

const create_baggage_price = (id) => {
    const flight_id = id;
    // const flight_cost = getRandomNumber(75, 100);
    const carry_on_cost = getRandomNumber(35, 55);
    const checked_bag_cost = getRandomNumber(carry_on_cost + 20, 90);
    
    return [flight_id, carry_on_cost, checked_bag_cost];
};

const create_fare_prices = (id) => {
    const flight_id = id;
    const business_fare = getRandomNumber(350, 650);
    const first_fare = getRandomNumber(business_fare + 150, business_fare + 350);
    const economy_fare = getRandomNumber(business_fare - 200, business_fare - 100);
    
    return [[flight_id, 'Business', business_fare], [flight_id, 'First', first_fare], [flight_id, 'Economy', economy_fare]];
};


exports.create_flight = create_flight;
exports.create_baggage_price = create_baggage_price;
exports.create_fare_prices = create_fare_prices;