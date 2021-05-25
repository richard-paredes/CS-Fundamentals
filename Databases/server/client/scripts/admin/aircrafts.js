// set global variable todos
let aircrafts = []

// function to set todos
const setAircrafts = (data) => {
    aircrafts = data;
};


// function to display todos
const displayAircrafts = () => {
    const aircraftsTable = document.querySelector('#aircrafts-table');
    
    // display all todos by modifying the HTML in "todo-table"
    let tableHTML = "";
    aircrafts.map(aircraft => {
        tableHTML +=
            `<tr key=${aircraft.aircraft_code}>
                <th>${aircraft.aircraft_code}</th>
                <th>${aircraft.model}</th>
                <th>${aircraft.range}</th>
                <th>${aircraft.total_seats}</th>
            </tr>`;
    });
    aircraftsTable.innerHTML = tableHTML;

    const aircrafts_list = document.querySelector('#aircraft_code');
    let aircraftsHTML = `<option selected disabled value="">Choose...</option>`;
    aircrafts.map(x => {
        aircraftsHTML += `
            <option value="${x.aircraft_code}">
            ${x.aircraft_code} - ${x.model}
            </option>
        `;
    });
    aircrafts_list.innerHTML = aircraftsHTML;
};

// The following are async function to select, insert, update and delete todos
// select all the todos
const selectAircrafts = async () => {
    // use try... catch... to catch error
    try {

        // GET all todos from "/api/todos"
        const response = await fetch("/api/aircrafts")
        const json = await response.json();
        if (response.status === 200) {
            setAircrafts(json);
            displayAircrafts();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

// insert a new todo
const insertAircraft = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const aircraft_details = {};
        formData.forEach((val, key) => {
            aircraft_details[key] = val;
        });

        // insert new todo to "/api/todos", with "POST" method
        const response = await fetch("/api/aircrafts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(aircraft_details)
        });
        const json = await response.json();
        
        // refresh the page when inserted
        if (response.status === 200) {
            location.reload();
        } else {
            console.log(json);
            handleError(json);
        }
    } catch (err) {
        handleError(err);
    }
};

// select all the todos when the codes first run
selectAircrafts();