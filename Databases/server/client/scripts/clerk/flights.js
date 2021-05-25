// set global variable todos
let flights = [];
let seats = [];
let selectedFlight = null;
// function to set todos
const setFlights = (data) => {
    flights = data;
};


// function to display todos
const displayFlights = () => {
    const flightsTable = document.querySelector('#flights-table');

    // display all todos by modifying the HTML in "todo-table"
    let tableHTML = "";
    flights.map(flight => {
        tableHTML +=
            `<tr key=${flight.flight_id}>
                <th>${flight.flight_id}</th>
                <th>${flight.economy_seats_price}</th>
                <th>${flight.status}</th>
                <th>${flight.departure_airport} - ${flight.departure_city} @ ${new Date(flight.scheduled_departure).toLocaleString()}</th>
                <th>${flight.arrival_airport} - ${flight.arrival_city} @ ${new Date(flight.scheduled_arrival).toLocaleString()}</th>
                <th>${flight.aircraft_code}</th>
                <th>${flight.total_seats_available}</th>
                <th>
                    <button class="btn btn-outline-primary" data-toggle="modal" data-target="#flight-details-modal" onclick="selectFlight(${flight.flight_id})">Details</button>
                </th>
                <th>
                    <button class="btn btn-outline-primary" data-toggle="modal" data-target="#flight-passengers-modal" onclick="selectFlight(${flight.flight_id})">Passengers</button>
                </th>
            </tr>`;
    });
    flightsTable.innerHTML = tableHTML;
};

function toLocal(date) {
    var local = new Date(date);
    local.setMinutes(date.getMinutes() - date.getTimezoneOffset());
    return local.toJSON();
}

const populateFlightDetails = () => {
    if (selectedFlight.flight) {
        const flight = selectedFlight.flight;
        const details = document.querySelector('#selected-flight-details');
        // what can be edited?
        // actual departure, actual arrival, status, baggage_claim_no, carry_on_fee, checked_bag_fee, allow_waitlist, includes_movie, includes_meal, price, aircraft_code,
        
        details.innerHTML = `
            <div class="form-row">
                <div class="form-group col-md-4">
                    <label for="departure_airport">Departure Airport</label>
                    <select class="custom-select" id="departure_airport" name="departure_airport" readonly disabled>
                        <option selected disabled value="${flight.departure_airport}">${flight.departure_airport} - ${flight.departure_city}</option>
                    </select>
                </div>
                <div class="form-group col-md-2">
                    <label for="departure_gate">Departure Gate</label>
                    <select class="custom-select" id="departure_gate" name="departure_gate" onblur="onBlur(event)" required>
                        ${airports.find(x => x.airport_code === flight.departure_airport).gates.map(y => `
                            <option value="${y.gate_key}" ${y.gate_key === flight.departure_gate_no && 'selected'}>${y.gate_no}</option>
                        `)}
                    </select>
                </div>
                <div class="form-group col-md-4">
                    <label for="arrival_airport">Arrival Airport</label>
                    <select class="custom-select" id="arrival_airport" name="arrival_airport" readonly disabled>
                        <option selected disabled value="${flight.arrival_airport}">${flight.arrival_airport} - ${flight.arrival_city}</option>
                    </select>
                </div>
                <div class="form-group col-md-2">
                    <label for="arrival_gate">Arrival Gate</label>
                    <select class="custom-select" id="arrival_gate" name="arrival_gate" onblur="onBlur(event)" required>
                        ${airports.find(x => x.airport_code === flight.arrival_airport).gates.map(y => `
                            <option value="${y.gate_key}" ${y.gate_key === flight.arrival_gate_no && 'selected'}>${y.gate_no}</option>
                        `)}
                    </select>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-4">
                    <label for="baggage_claim">Baggage Claim</label>
                    <select class="custom-select" id="baggage_claim" name="baggage_claim" onblur="onBlur(event)" required>
                        ${airports.find(x => x.airport_code === flight.arrival_airport).baggage_claims.map(y => `
                            <option value="${y.baggage_claim_key}" ${y.baggage_claim_key === flight.baggage_claim_no && 'selected'}>${y.baggage_claim_no}</option>
                        `)}
                    </select>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-4">
                    <label for="scheduled_departure">Scheduled Departure</label>
                    <input type="datetime-local" class="form-control" id="scheduled_departure" name="scheduled_departure" value="${toLocal(new Date(flight.scheduled_departure)).slice(0, 16)}" onblur="onBlur(event)" required>
                </div>
                <div class="form-group col-md-4">
                    <label for="scheduled_arrival">Scheduled Arrival</label>
                    <input type="datetime-local" class="form-control" id="scheduled_arrival" name="scheduled_arrival" value="${toLocal(new Date(flight.scheduled_arrival)).slice(0, 16)}" onblur="onBlur(event)" required>
                </div>
                <div class="form-group col-md-4">
                    <label for="boarding_time">Scheduled Boarding</label>
                    <input type="datetime-local" class="form-control" id="boarding_time" name="boarding_time" value="${toLocal(new Date(flight.boarding_time)).slice(0, 16)}" onblur="onBlur(event)" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-4">
                    <label for="scheduled_departure">Actual Departure</label>
                    <input type="datetime-local" class="form-control" id="scheduled_departure" name="actual_departure" value="${flight.actual_departure ? toLocal(new Date(flight.actual_departure)).slice(0, 16) : toLocal(new Date(flight.scheduled_departure)).slice(0, 16)}" onblur="onBlur(event)" required>
                </div>
                <div class="form-group col-md-4">
                    <label for="scheduled_arrival">Actual Arrival</label>
                    <input type="datetime-local" class="form-control" id="scheduled_arrival" name="actual_arrival" value="${flight.actual_arrival ? toLocal(new Date(flight.actual_arrival)).slice(0, 16) : toLocal(new Date(flight.scheduled_arrival)).slice(0, 16)}" onblur="onBlur(event)" required>
                </div>
                <div class="form-group col-md-4">
                    <label for="status">Status</label>
                    <select class="custom-select" id="status" name="status">
                        ${['On Time', 'Scheduled', 'Boarding', 'Departed', 'Arrived', 'Cancelled', 'Delayed'].map(x => `
                            <option value="${x}" ${flight.status === x && 'selected'}>${x}</option>
                        `)}
                    </select>
                </div>
            </div>
            <div>
                <label for="aircraft_code">Aircraft Model</label>
                <select class="custom-select" id="aircraft_code" name="aircraft_code" disabled readonly>
                    <option selected disabled value="${flight.aircraft_code}">${flight.aircraft_code}</option>
                </select>
            </div>
            <div class="form-row mt-3">
                <div class="form-group col-md-4">
                    <label for="economy_seats_price">Economy Fare Price</label>
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text">$</span>
                        </div>
                        <input type="number" class="form-control" name="economy_seats_price"
                            aria-label="Amount (to the nearest dollar)" min="0.00" step="0.01" value="${flight.economy_seats_price.slice(1,)}" onblur="onBlur(event)" required>
                    </div>
                </div>
                <div class="form-group col-md-4">
                    <label for="business_seats_price">Business Fare Price</label>
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text">$</span>
                        </div>
                        <input type="number" class="form-control" name="business_seats_price"
                            aria-label="Amount (to the nearest dollar)" min="0.00" step="0.01" value="${flight.business_seats_price.slice(1,)}" onblur="onBlur(event)" required>
                    </div>
                </div>
                <div class="form-group col-md-4">
                    <label for="first_seats_price">First Fare Price</label>
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text">$</span>
                        </div>
                        <input type="number" class="form-control" name="first_seats_price"
                            aria-label="Amount (to the nearest dollar)" min="0.00" step="0.01" value="${flight.first_seats_price.slice(1,)}" onblur="onBlur(event)" required>
                    </div>
                </div>
            </div>
            <div class="form-row mt-3">
                <div class="form-group col-md-4">
                    <label for="checked_bag_price">Checked Bag Fee</label>
                    <div class="input-group m">
                        <div class="input-group-prepend">
                            <span class="input-group-text">$</span>
                        </div>
                        <input type="number" class="form-control" name="checked_bag_price"
                            aria-label="Amount (to the nearest dollar)" min="0.01" step="0.01" value="${flight.checked_bag_price.slice(1,)}" onblur="onBlur(event)" required>
                    </div>
                </div>
                <div class="form-group col-md-4">
                    <label for="carry_on_price">Carry-On Fee</label>
                    <div class="input-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text">$</span>
                    </div>
                    <input type="number" class="form-control" name="carry_on_price"
                        aria-label="Amount (to the nearest dollar)" min="0.01" step="0.01" value="${flight.carry_on_price.slice(1,)}" onblur="onBlur(event)" required>
                    </div>
                </div>
            </div>
            <div class="form-row text-center">
                <div class="form-group col-md-4">
                    <input type="checkbox" id="includes_meal" name="includes_meal" ${flight.includes_meal && 'checked'}>
                    <label for="includes_meal">Includes Meal</label>
                </div>
                <div class="form-group col-md-4">
                    <input type="checkbox" id="includes_movie" name="includes_movie" ${flight.includes_movie && 'checked'}>
                    <label for="includes_movie">Includes Movie</label>
                </div>
                <div class="form-group col-md-4">
                    <input type="checkbox" id="allow_waitlist" name="allow_waitlist" ${flight.allow_waitlist && 'checked'} disabled readonly>
                    <label for="allow_waitlist">Allow Waitlist</label>
                </div>
            </div>
        `;
    }
};

const populateFlightPassengers = () => {
    if (selectedFlight) {
        const securedPassengers = document.querySelector('#secured-flight-passengers');
        const waitlistedPassengers = document.querySelector('#waitlisted-flight-passengers');
        let securedPassengersHTML = ``;
        let waitlistedPassengersHTML = ``;
        console.log(selectedFlight);
        selectedFlight.passengers.forEach(x => {
            if (!x.is_waitlisted) {
                securedPassengersHTML +=
                `
                <div class="p-2 mb-1 badge alert-primary">
                    <div class="badge text-left d-block">Passenger ID: ${x.passenger_id}</div>
                    <div class="badge text-left d-block">${x.first_name} ${x.last_name}</div>
                    <div class="badge text-left d-block">Fare: ${x.fare_conditions} Class</div>
                    <div class="badge text-left d-block">Seat #: ${x.checked_in ? x.boarding_pass.seat_no : 'Unassigned'} </div>
                    <div class="badge text-left d-block">Checked Bags: ${x.checked_bags}</div>
                    <div class="badge text-left d-block">Carry Ons: ${x.carry_ons}</div>
                    ${x.checked_in ? `<div class="badge d-block badge-pull badge-success mt-1">CHECKED IN</div>` : '<div class="badge d-block badge-pull badge-danger mt-1">NOT CHECKED IN</div>'}
                    ${x.checked_in ? `<div class="badge d-block mt-2 btn btn-sm btn-outline-danger" onclick="deleteBoardingPass('${x.ticket_no}', '${selectedFlight.flight.flight_id}')">REMOVE FROM FLIGHT</div>` 
                        : `<div class="badge d-block mt-2 btn btn-sm btn-outline-primary" onclick="createBoardingPass('${x.ticket_no}', '${selectedFlight.flight.flight_id}')">ADD TO FLIGHT</div>`}
                </div>
                `;
            } else {
                waitlistedPassengersHTML += 
                `
                <div class="p-2 mb-1 badge alert-warning">
                    <div class="badge text-left d-block">Passenger ID: ${x.passenger_id}</div>
                    <div class="badge text-left d-block">${x.first_name} ${x.last_name}</div>
                    <div class="badge text-left d-block">Fare: ${x.fare_conditions} Class</div>
                    <div class="badge text-left d-block">Seat #: ${x.checked_in ? x.boarding_pass.seat_no : 'Unassigned'} </div>
                    <div class="badge text-left d-block">Checked Bags: ${x.checked_bags}</div>
                    <div class="badge text-left d-block">Carry Ons: ${x.carry_ons}</div>
                    ${x.checked_in ? `<div class="badge d-block badge-pull badge-success mt-1">CHECKED IN</div>` : '<div class="badge d-block badge-pull badge-danger mt-1">NOT CHECKED IN</div>'}
                    ${x.checked_in ? `<div class="badge d-block mt-2 btn btn-sm btn-outline-danger" onclick="deleteBoardingPass('${x.ticket_no}', '${selectedFlight.flight.flight_id}')">REMOVE FROM FLIGHT</div>` 
                    : `<div class="badge d-block mt-2 btn btn-sm btn-outline-primary" onclick="createBoardingPass('${x.ticket_no}', '${selectedFlight.flight.flight_id}')">ADD TO FLIGHT</div>`}
                </div>
                `;
            }
        })
        securedPassengers.innerHTML = securedPassengersHTML;
        waitlistedPassengers.innerHTML = waitlistedPassengersHTML;
    }
};

const selectFlight = async (flight_id) => {
    try {
        if (!selectedFlight || selectedFlight.flight_id !== flight_id) {
            const response = await fetch(`/api/flights/${flight_id}`);
            selectedFlight = await response.json();
            
            populateFlightDetails();
            populateFlightPassengers();
        }
    } catch (err) {
        console.log(err.message);
        // handleError(err);
    }
};


const searchFlights = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const flights_details = {}
        formData.forEach((value, key) => {
            flights_details[key] = value;
        });
        // console.log(flights_details);
        const response = await fetch('/api/flights/search/all', {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(flights_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            setFlights(json);
            displayFlights();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err);
        handleError(err);

    }
};

const resetFlights = async () => {
    location.reload();
};

// The following are async function to select, insert, update and delete todos
// select all the todos
const selectFlights = async () => {
    // use try... catch... to catch error
    try {

        // GET all todos from "/api/todos"
        const response = await fetch("/api/flights")
        const json = await response.json();
        if (response.status === 200) {
            setFlights(json);
            displayFlights();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

// insert a new todo
const editFlight = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const flight_details = {}
        formData.forEach((value, key) => {
            flight_details[key] = value;
        });

        const response = await fetch(`/api/flights/${selectedFlight.flight.flight_id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(flight_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }

    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

const createBoardingPass = async (ticket_no, flight_id) => {
    try {
        const boarding_pass_details = { ticket_no, flight_id };
        const response = await fetch(`/api/boardingpasses`, {
            method: "POST",
            headers: { "Content-Type" : "application/json" },
            body: JSON.stringify(boarding_pass_details)
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

const deleteBoardingPass = async (ticket_no, flight_id) => {
    try {
        const boarding_pass_details = { ticket_no, flight_id };
        const response = await fetch(`/api/boardingpasses`, {
            method: "DELETE",
            headers: { "Content-Type" : "application/json" },
            body: JSON.stringify(boarding_pass_details)
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


// select all the todos when the codes first run
selectFlights();