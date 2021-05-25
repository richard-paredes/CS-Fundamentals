var friend1 = "Charlie";
var friend2 = "Liz";
var friend3 = "David";
var friend4 = "Mattias";

// different ways to declare and initialize arrays:
var arr = []; //empty array
var arr = new Array(); // uncommon, empty array
var arr = [49, true, "hermione", null]; // array with different values
var arr = [45, 37, 89, 24]; // array will all numbers
arr.length // length property

// instead: DRY ! (dont repeat yourself)
var friends = ["Charlie", "Liz", "David", "Mattias"];

// arrays are 0-indexed
console.log(friends);
console.log(friends[0]);

// re-assigned Charlie to Chuck
friends[0]="Chuck";

// we can also add in new data by putting data in the lastIndex + 1:
friends[4] = "Amelia";
console.log("Amelia has joined the friend group!");
console.log(friends);

console.log();


var colors = ["red", "blue", "yellow"];
console.log(colors);
console.log("Length: " + colors.length);
console.log(colors[2]);

colors[3]="green";
console.log(colors);
console.log("Length: " + colors.length);

colors[3] = "dark green";
console.log(colors);

// going far out of bounds and assigning values
// will generate empty array slots (undefined) with no values
// so the array length changes a lot
colors[7] = "violet";
console.log(colors);
console.log("Length: " + colors.length);


// array methods:
var colors = ["red", "orange", "yellow"];
colors[3] = "green";
colors[4] = "blue";

console.log(colors);

// push appends to end of the array (enqueue)
// push returns the number of elements in the array
var numElements = colors.push("indigo");
console.log("Number of elemetns from push: ", numElements);
console.log(colors);

// pop removes and returns the element at the end of the array
var element = colors.pop();
console.log(element);
console.log(colors);

// unshift APPENDS to the front of the array (push)
colors.unshift("orange");
console.log(colors);

// shift REMOVES element from front of array (dequeue)
var element = colors.shift();
console.log(element);
console.log(colors);

// indexOf: returns index of first instance of item in an array
// returns -1 if not there
var friends = ["Charlie", "Liz", "David", "Mattias", "Liz"];
console.log(friends.indexOf("David")); // returns 2
console.log(friends.indexOf("Liz")); // returns 1
console.log(friends.indexOf("Hagrid"));

// slice: returns a sub-array from (start, end) (non-inclusive end)
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(1, 3); // will only have 2 elements (3 - 1)

console.log(fruits); // B, O, L, A, M
console.log(citrus); // O, L


// iterating through an array:

// for loop:
arr = new Array(7);
for (let i=0; i < arr.length; i++) {
    arr[i] = i;
    console.log(arr[i]);
}
console.log();
// forEach: (with anonymous function)
counter = 1;
arr.forEach(function(element) {
    element = counter;
    counter++;
    console.log(element);
})

var colors = ["red", "orange", "yellow", "green", "blue", "violet"]
function printColor(color) {
    console.log("************");
    console.log(color);
    console.log("************");
}
// using forEach with defined function:
// NOTE: don't use parenthesis when calling the function!
// use only the function name!!
colors.forEach(printColor);

