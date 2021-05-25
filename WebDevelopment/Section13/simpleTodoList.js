var todos = [];
// wrap around this function so page loads before executing
// this JS
window.setTimeout(function () {
    var userAnswer;
    do {
        userAnswer = (prompt("What would you like to do?")).toLowerCase();
        if (userAnswer.indexOf("new") !== -1) {
            // add a new item
            addItem();

        } else if (userAnswer.indexOf("delete") !== -1) {
            // remove an item
            removeItem();

        } else if (userAnswer.indexOf("list") !== -1) {
            // show list
            alert(showTodos());
        } else if (userAnswer.indexOf("clear") !== -1) {
            todos = [];
        } else {
            alert("Sorry, I couldn't understand that.")
        }
    } while (userAnswer.indexOf("quit") === -1);


}, 500);

function showTodos() {
    if (todos.length === 0) {
        return " Nothing in your list! ";
    }
    var array = "****************\n";
    todos.forEach(function (element, index) {
        array += (index + 1) + ". " + element + "\n"
    })
    array += "****************";
    return array;
}

function addItem() {
    var element = prompt("Enter a new todo:");
    todos.push(element);
}

function removeItem() {
    if (todos.length === 0) {
        alert("Your list is already empty!");
        continue
    }

    var todo = prompt("Enter which todo you'd like to remove: " + "\n" + showTodos());
    todo = Number(todo);
    if (Number.isNaN(todo)) {
        alert("Sorry, couldn't do that!");
    } else {
        if (todo > 0 && todo < todos.length + 1) {
            todos.splice(todo - 1, 1);
        }
    }
}