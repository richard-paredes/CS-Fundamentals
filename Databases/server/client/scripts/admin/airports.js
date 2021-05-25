// set global variable todos
let airports = [];
// let gates = [];

// function to set todos
const setAirports = (data) => {
    let airports_data = data.airports;
    airports_data.forEach(x => {
        x['gates'] = data.gates.filter(y => y.airport_code === x.airport_code);
        x['baggage_claims'] = data.baggage_claims.filter(y => y.airport_code === x.airport_code);
    })
    airports = airports_data;
};


// function to display todos
const displayAirports = () => {
    const airportsTable = document.querySelector('#airports-table');

    // display all todos by modifying the HTML in "todo-table"
    let tableHTML = "";
    airports.map(airport => {
        tableHTML +=
            `<tr key=${airport.airport_code}>
                <th>${airport.airport_code}</th>
                <th>${airport.airport_name}</th>
                <th>${airport.city}</th>
                <th>${airport.coordinates}</th>
                <th>${airport.timezone}</th>
            </tr>`;
    });
    airportsTable.innerHTML = tableHTML;

    const departure_airport_list = document.querySelector('#departure_airport');
    const arrival_airport_list = document.querySelector('#arrival_airport');
    let listHTML = `<option selected disabled readonly value="">Choose...</option>`;
    airports.map(airport => {
        listHTML +=
            `
            <option value="${airport.airport_code}">
                ${airport.airport_code} - ${airport.city}
            </option>
            `;
    });
    departure_airport_list.innerHTML = listHTML;
    arrival_airport_list.innerHTML = listHTML;
};

// The following are async function to select, insert, update and delete todos
// select all the todos
const selectAirports = async () => {
    // use try... catch... to catch error
    try {
        // GET all todos from "/api/todos"
        const response = await fetch("/api/airports")
        const json = await response.json();
        // console.log(jsonData);
        
        if (response.status === 200) {
            setAirports(json);
            displayAirports();
        } else {
            handleError(json);
        }
    } catch (err) {
        handleError(err);
    }
};

// insert a new todo
const insertAirport = async (event) => {

    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const airport_details = {};
        formData.forEach((val, key) => {
            airport_details[key] = val;
        });
    
        let gates = [];
        let baggage_claims = [];
        document.querySelectorAll('.gate-no').forEach(x => gates.push([x.getAttribute('value'), airport_details['airport_code']]));
        document.querySelectorAll('.baggage-claim-no').forEach(x => baggage_claims.push([x.getAttribute('value'), airport_details['airport_code']]));


        if (gates.length < 1) {
            document.querySelector(`input[name='gate-no']`).classList.add('is-invalid');
            throw new Error("Invalid gate");
        } else {
            document.querySelector(`input[name='gate-no']`).classList.remove('is-invalid');
        }
        airport_details['gates'] = gates;
        if (baggage_claims.length < 1) {
            document.querySelector(`input[name='baggage-claim-no']`).classList.add('is-invalid');
            throw new Error("Invalid baggage claim");
        } else {
            document.querySelector(`input[name='baggage-claim-no']`).classList.remove('is-invalid');
        }
        airport_details['gates'] = gates;
        airport_details['baggage_claims'] = baggage_claims;

        if (!airport_details['timezone']) {
            document.querySelector(`select[name='timezone']`).classList.add('is-invalid');
            throw new Error("Invalid timezone");
        } else {
            document.querySelector(`select[name='timezone']`).classList.remove('is-invalid');
        }

        const response = await fetch("/api/airports", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(airport_details)
        });
        const json = await response.json();
        // refresh the page when inserted
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        handleError(err);
    }
};

const insertGate = () => {
    const gate_node = document.querySelector('#gate-no');
    const gate_no = gate_node.value;
    const gates_list = document.querySelector("#create-gates-list");
    if (gate_no && !gates_list.querySelector(`#gate-${gate_no}`)) {
        const new_gate = document.createElement('div');
        new_gate.id = `gate-${gate_no}`;
        new_gate.setAttribute('class', "badge badge-warning d-flex justify-content-center mx-1 mb-1 align-items-center");
        new_gate.innerHTML += `<span class="px-1 gate-no" value="${gate_no}">${gate_no}</span> <button class="border-0 rounded-circle bg-transparent px-0 mx-1 py-0" type="button" onclick="removeGate('${gate_no}')">&times;</button>`;
        gates_list.appendChild(new_gate);
        gate_node.value = "";
    }
};

const insertBaggageClaim = () => {
    const baggage_node = document.querySelector('#baggage-claim-no');
    const baggage_claim_no = baggage_node.value;
    const baggage_claims_list = document.querySelector("#create-baggage-claim-list");
    if (baggage_claim_no && !baggage_claims_list.querySelector(`#baggage-claim-${baggage_claim_no}`)) {
        const new_baggage_claim = document.createElement('div');
        new_baggage_claim.id = `baggage-claim-${baggage_claim_no}`;
        new_baggage_claim.setAttribute('class', "badge badge-warning d-flex justify-content-center mx-1 mb-1 align-items-center");
        new_baggage_claim.innerHTML += `<span class="px-1 baggage-claim-no" value="${baggage_claim_no}">${baggage_claim_no}</span> <button class="border-0 rounded-circle bg-transparent px-0 mx-1 py-0" type="button" onclick="removeBaggageClaim('${baggage_claim_no}')">&times;</button>`;
        baggage_claims_list.appendChild(new_baggage_claim);
        baggage_node.value = "";
    }
};

const removeGate = async (gate_no) => {
    const gates_list = document.querySelector('#create-gates-list');
    const gate = gates_list.querySelector(`#gate-${gate_no}`);
    if (gate) {
        gates_list.removeChild(gate);
    }
};


const removeBaggageClaim = async (baggage_no) => {
    const baggages_list = document.querySelector('#create-baggage-claim-list');
    const baggage_claim = baggages_list.querySelector(`#baggage-claim-${baggage_no}`);
    if (baggage_claim) {
        baggages_list.removeChild(baggage_claim);
    }
};


// select all the todos when the codes first run
selectAirports();