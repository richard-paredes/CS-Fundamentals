// 5 Primitive Datatypes

typeof "John"                 // Returns "string"
typeof 3.14                   // Returns "number"
typeof NaN                    // Returns "number"
typeof false                  // Returns "boolean"
typeof [1,2,3,4]              // Returns "object"
typeof {name:'John', age:34}  // Returns "object"
typeof new Date()             // Returns "object"
typeof function () {}         // Returns "function"
typeof myCar                  // Returns "undefined" *
typeof null                   // Returns "object" 

// // Numbers:

// division:
1/3 // = 0.33333
1/5 // = 0.2

// modulo:
10 % 3; // = 1
24 % 2; // = 0
15 % 11 // = 4

(3-8) * 24 // = -120

// // Strings: "" and ''

// String concatenation:
"charlie " + "brown" // = "charlie brown"

// string length property:
"hello word".length // = 11

// string indexing:
"hello"[0] // = "h"

// escape sequences with '\'
"What's up \"this is a quote!\"" // = What's up "this is a quote!"

// "Hello World"
// "43"


// // Booleans
// true
// false

// // null and undefined
// null
// undefined

// VARIABLES:
// var yourVariableName = yourValue;

var name = "Rusty";
var secretNubmer= 73;
var isAdorable = true;

var name = "Rusty";
"hello there " + name;

var num = 37;
name = "Bob";

// NULL AND UNDEFINED
// variables that are declared but not initialized are undefiend
var name;
var age;

// null is "explicitly nothing" -- its defined as being nothing
// undeclared is just theres nothing in it (yet)
var currentPlayer = "charlie";
currentPlayer = null;

// alert:
sends out a message to user, cannot get input back, can take in various data types
alert(12);
// prompt
sends out message to user, prompting for input, returned as String
var stringstuff = prompt("enter a string: ");
// console.log()
sends out message to log

