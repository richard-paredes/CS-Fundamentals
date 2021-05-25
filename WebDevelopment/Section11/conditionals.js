if (age < 18) {
    console.log("Sorry, you are not old enough to enter the venue.");
}
// if age is b/w 18 and 21
else if (age < 21) {
    console.log("You can enter, but cannot drink.");
}

else {
    console.log("You can enter and you can drink.")
}

// practice:

if (age < 0) {
    console.log("Error: NEGATIVE AGE");
}

else if (age == 21) {
    console.log("Happy 21st birthday!");
}

if (age % 2 == 1) {
    console.log("Your age is odd!");
}

if (age % (age ** 1/2) == 0) {
    console.log("Perfect square!");
}