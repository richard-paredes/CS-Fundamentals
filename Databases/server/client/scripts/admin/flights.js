// set global variable todos
let flights = []

// function to set todos
const setFlights = (data) => {
    flights = data;
};

const departure_airport = document.querySelector('#departure_airport');
departure_airport.addEventListener('change', () => {
    const gates_list = document.querySelector('#departure_gate');

    if (departure_airport.value === "Choose...") {
        gates_list.innerHTML = "";
    } else {
        const airport_gates = airports.find(x => x.airport_code === departure_airport.value).gates;
        let gatesHTML = `<option selected disabled readonly value="">Choose...</option>`;
        airport_gates.map(x => {
            gatesHTML += `
            <option value="${x.gate_key}">
                ${x.gate_no}
            </option>
        `;
        });
        gates_list.innerHTML = gatesHTML;
    }
});
const arrival_airport = document.querySelector('#arrival_airport');
arrival_airport.addEventListener('change', () => {
    const gates_list = document.querySelector('#arrival_gate');
    const baggage_claims_list = document.querySelector('#baggage_claim');
    if (arrival_airport.value === "Choose...") {
        gates_list.innerHTML = "";
        baggage_claims_list.innerHTML = "";
    } else {
        const airport = airports.find(x => x.airport_code === arrival_airport.value);
        let gatesHTML = `<option selected disabled readonly value="">Choose...</option>`;
        airport.gates.map(x => {
            gatesHTML += `
            <option value="${x.gate_key}">
                ${x.gate_no}
            </option>
        `;
        });
        let baggageClaimsHTML = `<option selected disabled readonly value="">Choose...</option>`;
        airport.baggage_claims.map(x => {
            baggageClaimsHTML += `
            <option value="${x.baggage_claim_key}">
                ${x.baggage_claim_no}
            </option>
            `;
        })
        gates_list.innerHTML = gatesHTML;
        baggage_claims_list.innerHTML = baggageClaimsHTML;
    }
});

// function to display todos
const displayFlights = () => {
    const flightsTable = document.querySelector('#flights-table');
    console.log(flights);
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
            </tr>`;
    });
    flightsTable.innerHTML = tableHTML;
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
const insertFlight = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const flight_details = {};
        formData.forEach((val, key) => {
            flight_details[key] = val;
        });

        // insert new todo to "/api/todos", with "POST" method
        const response = await fetch("/api/flights", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(flight_details)
        });
        const json = await response.json();
        // refresh the page when inserted
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

// select all the todos when the codes first run
selectFlights();