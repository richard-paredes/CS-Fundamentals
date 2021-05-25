// set global variable todos
let airports = [];
// let gates = [];

// function to set todos
const setAirports = (data) => {
    let airports_data = data.airports;
    airports_data.forEach(x => {
        x['gates'] = data.gates.filter(y => y.airport_code === x.airport_code);
        x['baggage_claims'] = data.baggage_claims.filter(y => y.airport_code === x.airport_code);
    });
    airports = airports_data;
};


// The following are async function to select, insert, update and delete todos
// select all the todos
const selectAirports = async () => {
    // use try... catch... to catch error
    try {
        // GET all todos from "/api/todos"
        const response = await fetch("/api/airports")
        const json = await response.json();
        if (response.status === 200) {
            setAirports(json);
        } else {
            handleError(json);
        }
        // console.log(jsonData);
        // displayAirports();
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};


// select all the todos when the codes first run
selectAirports();