// functions are reusable bits of code
/*

wadu
*/

function doSomething() {
    console.log("HELLO WORLD");
}

function sayHi() {
    console.log("HELLO!");
    console.log("GOODBYE!");
}

function sing() {
    console.log("Twinkle, twinkle, little star,");
    console.log("How I wonder what you are");
    console.log("Up above the world so high");
    console.log("Like a diamond in the sky");
}

doSomething();
sayHi();
sing();

// functions can take arguments!
// you don't need to specify the value it seems
function square(num) {
    // means the argument was left blank
    if (num === undefined) {
        console.log("Error.");
        return;
    }
    var square = num * num;
    console.log("The square of " + num + " is: " + square);
}
square();
square(4);

function sayHello(name) {
    console.log("Hello there, " + name + "!");
}

sayHello('Richard');
sayHello(); // argument is left undefined!

function area(length, width) {
    var area = (length*width);
    console.log("Area is: " + area);
    return area;
}

area(5, 3);

// using return value:
function squareNumber(num){
    return num*num;
}

console.log("5 squared is: " + squareNumber(5));

function capitalize(str) {
    // OR + str.slice(1);
    if (typeof(str) === 'number') {
        // console.log("Error.");
        return "Error: not a string"
    }
    return str.charAt(0).toUpperCase() + str.slice(1);
}

console.log("'hello' capitalized is: " + capitalize('hello'));
console.log("'37' capitalized is: " + capitalize(37));
function reverseString(str) {
    if (typeof(str) !== "string") {
        return "Error: Not a string!";
    }
    var reversed = "";
    for (x = str.length - 1; x >= 0; x--) {
        reversed += str[x];
    }
    return reversed;
}

console.log("Reverse of 'string' is: " + reverseString('string'));
console.log("Reverse of '935314' is: " + reverseString(935134));

function capitalizeFunction(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
// function expression
var capitalizeVariable = function(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

// the downside of function expression is that the variable
// can be reassigned to something else, and the function
//  will then be lost
// 
// however, the function can also be changed by declaring another
// function with the same name!

// they are called in the same way, as well!
console.log(capitalizeFunction("amazing"));
console.log(capitalizeVariable('awesome'));

function test(x, y) {
    return y - x;
}

console.log(test(10, 40));

function test(x) {
    return x*2;
    // this gives a warning: unreachable code
    console.log(x);
    return x/2;
}
console.log(test(40));