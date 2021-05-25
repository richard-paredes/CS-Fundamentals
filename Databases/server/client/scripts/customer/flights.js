// set global variable todos
let all_flights = [];
let one_way_flights = [];
let round_trip_departing_flights = [];
let round_trip_returning_flights = [];
let multi_destination_1_flights = [];
let multi_destination_2_flights = [];

let selected_flights = [];
let selected_one_way_flights = [];
let selected_round_departing_flights = [];
let selected_round_returning_flights = [];

// function to set todos
const setFlights = (type, flights) => {
    if (!type) {
        one_way_flights = [];
        round_trip_departing_flights = [];
        round_trip_returning_flights = [];
        multi_destination_1_flights = [];
        multi_destination_2_flights = [];
    } else if (type === 'one') {
        all_flights = flights.data;
        one_way_flights = flights.connections;
    } else if (type === 'round') {
        all_flights = flights.data;
        round_trip_departing_flights = flights.departing_connections;
        round_trip_returning_flights = flights.returning_connections;
    } else if (type === 'multi') {

    }
};

const setLoading = (id, is_loading) => {
    const loading_node = document.querySelector(id);
    if (is_loading) loading_node.removeAttribute('hidden');
    else loading_node.setAttribute('hidden', 'true');
};

const setSelectedOneWayFlights = (selected_flight_ids) => {
    selected_one_way_flights = selected_flight_ids.map(x => all_flights.find(y => y.flight_id === x)); // unnecessary, but whatever
    selected_flights = selected_flights.concat(selected_one_way_flights);
    populateSelectedFlights(selected_one_way_flights);
    resetFlights();
    const button_node = document.querySelector('#selected-flights-btn');
    button_node.removeAttribute('disabled', 'true');
};

const setSelectedDepartingFlights = (selected_flight_ids) => {
    selected_round_departing_flights = selected_flight_ids.map(x => all_flights.find(y => y.flight_id === x));
    selected_flights = selected_flights.concat(selected_round_departing_flights);
    displayReturningRoundTripFlights();
    populateSelectedFlights(selected_round_departing_flights);
    const button_node = document.querySelector('#selected-flights-btn');
    button_node.setAttribute('disabled', 'true');
};

const setSelectedReturningFlights = (selected_flight_ids) => {
    selected_round_returning_flights = selected_flight_ids.map(x => all_flights.find(y => y.flight_id === x));
    selected_flights = selected_flights.concat(selected_round_returning_flights);
    populateSelectedFlights(selected_round_returning_flights);
    resetFlights();
    const button_node = document.querySelector('#selected-flights-btn');
    button_node.removeAttribute('disabled');
};

const clearAndResetFlights = () => {
    clearSelectedFlights();
    resetFlights();
}

const clearSelectedFlights = () => {
    selected_one_way_flights = [];
    selected_round_departing_flights = [];
    selected_round_returning_flights = [];
    selected_flights = [];
    const alert_node = document.querySelector('#selected-flights-alert');
    const details_node = document.querySelector('#selected-flights-details');
    const button_node = document.querySelector('#selected-flights-btn');
    details_node.innerHTML = ``;
    alert_node.setAttribute('hidden', 'true');
    button_node.setAttribute('disabled', 'true');
};

const resetFlights = () => {
    resetForm('#search-one-flights-form');
    resetForm('#search-round-flights-form');
    resetForm('#search-multi-flights-form');
    setFlights();
    displayFlights();
};


const num_tickets_input = document.querySelector('#num_tickets');
const passenger_infos = document.querySelector('#passengers');
const increment_ticket_button = document.querySelector('#increment_ticket');
increment_ticket_button.addEventListener('click', () => {
    num_tickets_input.classList.remove('is-invalid');
    if (num_tickets_input.value < 5) {
        num_tickets_input.value = num_tickets_input.valueAsNumber + 1;
        let innerHTML = `
            <div id="passenger-${num_tickets_input.value}" class="bg-light p-3 my-2 border">
                <h6>Passenger ${num_tickets_input.value}</h6>
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="first_name">First Name</label>
                        <input type="text" class="form-control" name="passenger_${num_tickets_input.value}_first_name" required onblur="onBlur(event)">
                    </div>
                    <div class="col-md-6">
                        <label for="last_name">Last Name</label>
                        <input type="text" class="form-control" name="passenger_${num_tickets_input.value}_last_name" required onblur="onBlur(event)">
                    </div>
                </div>
        `;
        selected_flights.forEach(x => {
            innerHTML += `
                <h6 class="mt-3">Flight: ${x.departure_airport} to ${x.arrival_airport}</h6>
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="checked-bags">Checked bags</label>
                        <div class="input-group mb-3">
                            <div class="input-group-prepend">
                                <span class="input-group-btn btn btn-outline-primary"
                                    onclick="baggageInputHandler('decrement', '#passenger_${num_tickets_input.value}_flight_${x.flight_id}_checked_bags', 0)">&minus;</span>
                            </div>
                            <input type="number" id="passenger_${num_tickets_input.value}_flight_${x.flight_id}_checked_bags" name="passenger_${num_tickets_input.value}_flight_${x.flight_id}_checked_bags"
                            readonly min="1" max="5" step="1" class="form-control text-center" value="0">
                            <div class="input-group-append">
                                <span class="input-group-btn btn btn-outline-primary"
                                    onclick="baggageInputHandler('increment', '#passenger_${num_tickets_input.value}_flight_${x.flight_id}_checked_bags', 3)">&plus;</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label for="carry-ons">Carry Ons</label>
                        <div class="input-group mb-3">
                            <div class="input-group-prepend">
                                <span class="input-group-btn btn btn-outline-primary"
                                    onclick="baggageInputHandler('decrement', '#passenger_${num_tickets_input.value}_flight_${x.flight_id}_carry_ons', 0)">&minus;</span>
                            </div>
                            <input type="number" id="passenger_${num_tickets_input.value}_flight_${x.flight_id}_carry_ons" name="passenger_${num_tickets_input.value}_flight_${x.flight_id}_carry_ons" 
                                readonly min="1" max="5" step="1" class="form-control text-center" value="0">
                            <div class="input-group-append">
                                <span class="input-group-btn btn btn-outline-primary"
                                    onclick="baggageInputHandler('increment', '#passenger_${num_tickets_input.value}_flight_${x.flight_id}_carry_ons', 2)">&plus;</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="fare_conditions">Seat Fare</label>
                        <select class="custom-select" id="passenger_${num_tickets_input.value}_flight_${x.flight_id}_fare_conditions" name="passenger_${num_tickets_input.value}_flight_${x.flight_id}_fare_conditions" required>
                            <option selected value="Economy">Economy</option>
                            <option value="Business">Business</option>
                            <option value="First">First</option>
                        </select>
                    </div>
                </div>`;
        });
        innerHTML += `</div>`;
        passenger_infos.innerHTML += innerHTML;
    }
});

const decrement_ticket_button = document.querySelector('#decrement_ticket');
decrement_ticket_button.addEventListener('click', () => {
    if (num_tickets_input.value > 0) {
        const child = document.querySelector(`#passenger-${num_tickets_input.value}`);
        passenger_infos.removeChild(child);
        num_tickets_input.value = num_tickets_input.valueAsNumber - 1;
    }
});

const baggageInputHandler = (change, id, max) => {
    const input = document.querySelector(id);
    if (change === 'increment' && input.value < max) {
        input.value = input.valueAsNumber + 1;
    } else if (change === 'decrement' && input.value > 0) {
        input.value = input.valueAsNumber - 1;
    }
};

const populateSelectedFlights = (flights) => {
    const alert_node = document.querySelector('#selected-flights-alert');
    const details_node = document.querySelector('#selected-flights-details');

    let innerHTML = ``;
    flights.forEach((x) => {
        innerHTML += `
            <div class="px-3 py-1 rounded">
                <div class="badge d-block text-left">Departure: <span class="font-weight-bold">${x.departure_city} - ${x.departure_airport} </span><span class="">@ ${new Date(x.scheduled_departure).toLocaleString()}</span></div>
                <div class="badge d-block text-left">Arrival: <span class="font-weight-bold">${x.arrival_city} - ${x.arrival_airport} </span><span class="">@ ${new Date(x.scheduled_arrival).toLocaleString()}</span></div>
                <div class="badge d-block text-left">Price: ${x.economy_seats_price}</div>
                <div class="badge d-block text-left">Price per carry-on: ${x.carry_on_price}</div>
                <div class="badge d-block text-left">Price per checked bag: ${x.checked_bag_price}</div>
                ${x.allow_waitlist ? `<div class="badge d-block text-left text">Seat Waitlisting Enabled (performed automatically)</div>` : ''}
                <div class="badge d-block text-left">Status: <div class="badge ${x.status === 'Cancelled' ? 'badge-danger' : 'badge-info'}">${x.status.toUpperCase()}</div></div>
            </div>
        `;
    });
    alert_node.removeAttribute('hidden');
    details_node.innerHTML += innerHTML;
};

// function to display todos
const displayFlights = (type) => {
    if (!type) {
        const oneFlightsTable = document.querySelector('#one-flights-list');
        const roundFlightsTable = document.querySelector('#round-flights-list');
        const multiFlightsTable = document.querySelector('#multi-flights-list');
        const oneNoFlightsMessage = document.querySelector(`#one-no-flights`);
        const roundNoFlightsMessage = document.querySelector(`#round-no-flights`);
        // const multiNoFlightsMessage = document.querySelector(`#multi-no-flights`);
        oneFlightsTable.setAttribute('hidden', 'true');
        roundFlightsTable.setAttribute('hidden', 'true');
        multiFlightsTable.setAttribute('hidden', 'true');
        oneNoFlightsMessage.setAttribute('hidden', 'true');
        roundNoFlightsMessage.setAttribute('hidden', 'true');
        // multiNoFlightsMessage.setAttribute('hidden', 'true');
        return
    } else if (type === 'one') {
        displayOneWayFlights();
    } else if (type === 'round') {
        displayDepartingRoundTripFlights();
    } else if (type === 'multi') {
        displayMutliDestinationFlights();
    }
};

const clearTickets = (form_id) => {
    passenger_infos.innerHTML = ``;
    resetForm(form_id);
};

const searchFlights = async (event, type) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        clearSelectedFlights();

        var flights_details = {};
        formData.forEach((value, key) => {
            flights_details[key] = value;
        });

        setLoading(`#${type}-loading-bar`, true);
        const response = await fetch('/api/flights/search', {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(flights_details)
        });
        const json = await response.json();

        if (response.status === 200) {
            // console.log(json);
            setFlights(type, json);
            setLoading(`#${type}-loading-bar`, false);
            displayFlights(type);
        } else {
            handleError(json);
            setLoading(`#${type}-loading-bar`, false);
        }
    } catch (err) {
        handleError(err);
        // console.log(err);
        setLoading(`#${type}-loading-bar`, false);
    }
};

const displayOneWayFlights = () => {
    const unselected_flights = one_way_flights.filter(x => !selected_one_way_flights.includes(x));
    const flightsTable = document.querySelector(`#one-flights-list`);
    const flightsTableRows = document.querySelector(`#one-flights-table`);
    const noFlightsMessage = document.querySelector(`#one-no-flights`);

    let tableHTML = "";

    // display all todos by modifying the HTML in "todo-table"
    unselected_flights.map(flight => {
        let current_selected_flight_ids = selected_one_way_flights.map(x => x.flight_id).concat(flight.prev_flight_id === -1 ? [flight.flight_id] : [flight.prev_flight_id, flight.flight_id]);
        console.log(current_selected_flight_ids);
        // console.log(current_selected_flight_ids);
        tableHTML +=
            `<tr key="${flight.flight_id}">
                <td>${flight.departure_airport} - ${new Date(flight.scheduled_departure).toLocaleTimeString()}</td>
                <td>${flight.arrival_airport} - ${new Date(flight.scheduled_arrival).toLocaleTimeString()}</td>
                <td>${flight.stops === 0 ? 'Nonstop' : `${flight.stops} stops`}</td>
                <td>${flight.base_price}</td>
                <td>
                    <button class="btn btn-outline-primary" onclick="setSelectedOneWayFlights([${current_selected_flight_ids.join(',')}])" ${(flight.total_seats_available === 0 && !flight.allow_waitlist) && 'disabled'}>Reserve One-Way</button>
                </td>
            </tr>`;
    });

    if (unselected_flights.length > 0) {
        flightsTableRows.innerHTML = tableHTML;
        noFlightsMessage.setAttribute('hidden', 'true');
        flightsTable.removeAttribute('hidden');
    } else {
        flightsTableRows.innerHTML = '';
        noFlightsMessage.removeAttribute('hidden');
        flightsTable.setAttribute('hidden', 'true');
    }
};

const displayDepartingRoundTripFlights = () => {
    const unselected_flights = round_trip_departing_flights.filter(x => !selected_round_departing_flights.includes(x));
    const flightsTable = document.querySelector(`#round-flights-list`);
    const flightsTableRows = document.querySelector(`#round-flights-table`);
    const noFlightsMessage = document.querySelector(`#round-no-flights`);

    let tableHTML = "";

    // display all todos by modifying the HTML in "todo-table"
    unselected_flights.map(flight => {
        let current_selected_flight_ids = selected_round_departing_flights.map(x => x.flight_id).concat(flight.prev_flight_id === -1 ? [flight.flight_id] : [flight.prev_flight_id, flight.flight_id]);
        console.log(current_selected_flight_ids);
        tableHTML +=
            `<tr key="${flight.flight_id}">
                <td>${flight.departure_airport} - ${new Date(flight.scheduled_departure).toLocaleTimeString()}</td>
                <td>${flight.arrival_airport} - ${new Date(flight.scheduled_arrival).toLocaleTimeString()}</td>
                <td>${flight.stops === 0 ? 'Nonstop' : `${flight.stops} stops`}</td>
                <td>${flight.base_price}</td>
                <td>
                    <button class="btn btn-outline-primary" onclick="setSelectedDepartingFlights([${current_selected_flight_ids.join(',')}])" ${(flight.total_seats_available === 0 && !flight.allow_waitlist) && 'disabled'}>Reserve Departure</button>
                </td>
            </tr>`;
    });

    if (unselected_flights.length > 0) {
        flightsTableRows.innerHTML = tableHTML;
        noFlightsMessage.setAttribute('hidden', 'true');
        flightsTable.removeAttribute('hidden');
    } else {
        flightsTableRows.innerHTML = '';
        noFlightsMessage.removeAttribute('hidden');
        flightsTable.setAttribute('hidden', 'true');
    }
};

const displayReturningRoundTripFlights = () => {
    const unselected_flights = round_trip_returning_flights.filter(x => !selected_round_departing_flights.includes(x));
    const flightsTable = document.querySelector(`#round-flights-list`);
    const flightsTableRows = document.querySelector(`#round-flights-table`);
    const noFlightsMessage = document.querySelector(`#round-no-flights`);

    let tableHTML = "";

    // display all todos by modifying the HTML in "todo-table"
    unselected_flights.map(flight => {
        let current_selected_flight_ids = selected_round_returning_flights.map(x => x.flight_id).concat(flight.prev_flight_id === -1 ? [flight.flight_id] : [flight.prev_flight_id, flight.flight_id]);
        console.log(current_selected_flight_ids);
        // console.log(current_selected_flight_ids);
        tableHTML +=
            `<tr key="${flight.flight_id}">
                <td>${flight.departure_airport} - ${new Date(flight.scheduled_departure).toLocaleTimeString()}</td>
                <td>${flight.arrival_airport} - ${new Date(flight.scheduled_arrival).toLocaleTimeString()}</td>
                <td>${flight.stops === 0 ? 'Nonstop' : `${flight.stops} stops`}</td>
                <td>${flight.base_price}</td>
                <td>
                    <button class="btn btn-outline-primary" onclick="setSelectedReturningFlights([${current_selected_flight_ids.join(',')}])" ${(flight.total_seats_available === 0 && !flight.allow_waitlist) && 'disabled'}>Reserve Return</button>
                </td>
            </tr>`;
    });

    if (unselected_flights.length > 0) {
        flightsTableRows.innerHTML = tableHTML;
        noFlightsMessage.setAttribute('hidden', 'true');
        flightsTable.removeAttribute('hidden');
    } else {
        flightsTableRows.innerHTML = '';
        noFlightsMessage.removeAttribute('hidden');
        flightsTable.setAttribute('hidden', 'true');
    }
};

const bookFlights = () => {
    let innerHTML = `
        <div>
            <h6>Flight Details</h6>
    `;
    selected_flights.forEach((x) => {
        innerHTML += `
            <div class="px-3 py-1 rounded bg-warning my-1">
                <div class="badge d-block text-left">Departure: <span class="font-weight-bold">${x.departure_airport} </span><span class="">@ ${new Date(x.scheduled_departure).toLocaleString()}</span></div>
                <div class="badge d-block text-left">Arrival: <span class="font-weight-bold">${x.arrival_airport} </span><span class="">@ ${new Date(x.scheduled_arrival).toLocaleString()}</span></div>
                <div class="badge d-block text-left">Economy Fare Seats (${x.economy_seats_price}): ${x.economy_seats_available}</div>
                <div class="badge d-block text-left">Business Fare Seats (${x.business_seats_price}): ${x.business_seats_available}</div>
                <div class="badge d-block text-left">First Fare Seats (${x.first_seats_price}): ${x.first_seats_available}</div>
                <div class="badge d-block text-left">Price per carry-on: ${x.carry_on_price}</div>
                <div class="badge d-block text-left">Price per checked bag: ${x.checked_bag_price}</div>
                ${x.allow_waitlist ? `<div class="badge d-block text-left text">Seat Waitlisting Enabled (performed automatically)</div>` : ''}
                <div class="badge d-block text-left">Status: <div class="badge ${x.status === 'Cancelled' ? 'badge-danger' : 'badge-info'}">${x.status.toUpperCase()}</div></div>
            </div>
        `;
    });
    innerHTML += `
        </div>
    `;
    document.querySelector('#selected-flight-details').innerHTML = innerHTML;
    document.querySelector(`#flight_ids`).value = selected_flights.map(x => x.flight_id).join(',');

    if (!customer) {
        const saveBtn = document.querySelector('#book-flight-btn');
        saveBtn.setAttribute('disabled', 'true');
        saveBtn.innerHTML = "Login to reserve!";
    } else if (selected_flights.some(x => x.total_seats_available === 0 && !x.allow_waitlist)) {
        const saveBtn = document.querySelector('#book-flight-btn');
        saveBtn.setAttribute('disabled', 'true');
        saveBtn.innerHTML = "No Seats Available";
    } else {
        const saveBtn = document.querySelector('#book-flight-btn');
        saveBtn.removeAttribute('disabled');
        saveBtn.innerHTML = "Book Flight";
    }
};

const bookMultiDestination = async () => {

};

const insertBooking = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const passengers = [];
        let flight_ids = [];
        const booking_details = {};
        formData.forEach((value, key) => {
            if (key.startsWith('flight_ids')) {
                flight_ids = value.split(',');
            } else if (key.startsWith('passenger')) {
                let split_idx = key.slice(10).indexOf('_');
                let passenger_id = key.slice(10, 10 + split_idx);
                let passenger = passengers.find(x => x.key === passenger_id);
                if (!passenger) {
                    passenger = {
                        key: passenger_id,
                    };
                    passengers.push(passenger);
                }
                passenger[key.slice(10 + split_idx + 1)] = value;
            } else {
                booking_details[key] = value;
            }
        });

        if (passengers.length === 0) {
            document.querySelector('#num_tickets').classList.add('is-invalid');
            throw new Error("Invalid tickets for the flight.");
        }

        booking_details['passengers'] = passengers;
        booking_details['flight_ids'] = flight_ids;

        const response = await fetch("/api/bookings", {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(booking_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }

    } catch (err) {
        handleError(err);
    }

};

// The following are async function to select, insert, update and delete todos
// select all the todos
const selectFlights = async () => {
    // use try... catch... to catch error
    try {

        // GET all todos from "/api/todos"
        const response = await fetch("/api/flights")
        const jsonData = await response.json();

        // console.log(jsonData);
        // console.log(jsonData);
        // setLoading();
        // setFlights(jsonData);
        // displayFlights();
        // finishLoading();
    } catch (err) {
        handleError(err, 'Could not fetch flights from database.');
        // console.log(err.message);
    }
};

const getTypeAttributes = (type) => {
    if (type === 'one') {
        return 'data-toggle="modal" data-target="#book-flight-modal"';
    } else {
        return '';
    }
};


$(document).ready(() => {
    $('#book-flight-modal').on('hidden.bs.modal', function () {
        // do something…
        // clear the forms!!
        clearTickets('#flight-booking-form');
    });
});

// select all the todos when the codes first run
// selectFlights();