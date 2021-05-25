var secretNumber = 9;

var userNumber = Number(prompt("HEY!\nGuess what number I'm thinking of?"));

if (userNumber === secretNumber) {
    alert("Awesome guess!");
}
else if (userNumber < secretNumber) {
    alert("Aww, too low of a guess!")
}
else {
    alert("Sorry, buddy. Too high!");
}