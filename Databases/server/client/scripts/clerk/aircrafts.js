// set global variable todos
let aircrafts = []

// function to set todos
const setAircrafts = (data) => {
    aircrafts = data;
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
        } else {
            handleError(json);
        }
        // displayAircrafts();
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};



// select all the todos when the codes first run
selectAircrafts();