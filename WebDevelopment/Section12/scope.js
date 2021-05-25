function sayHello(name) {
    var str = "Hello, " + name;
    console.log(str);
}

let x = 5;
var y = 10;

function doLet() {
    console.log(x);
    // this will change x!
    x = 8;
}

function doVar() {
    console.log(y);
    // this will change y!
    y = 20;
}

sayHello("Richard");
// console.log(str); // not within the scope
console.log();
doLet();
doVar();
console.log("Changing values inside a function will change them globally");
console.log(x);
console.log(y);

console.log();

function changeLet() {
    let x = 3;
    console.log(x);
}
function changeVar() {
    let y = 22;
    console.log(y);
}

changeLet();
changeVar();
console.log("Re-initializing and chaning values will not affect global variables");
console.log(x);
console.log(y);

// scope examples:

// global scope
function foo1() {

    // local foo1 scope
    function foo2() {

        // local foo2 scope
        let x = 0;
    }
}

function foo() {
    // function scope
    if (true) {
        
        var fruit1 = 'apple'; // exists in function scope
        const fruit2 = 'banana'; // exists in block scope
        let fruit3 = 'strawberry'; // exists in block scope
    }

    console.log(fruit1);
    console.log(fruit2); // error
    console.log(fruit3); // error
}

// examples of block scope:
// means any let's or const's initialized here
// will not be avaiable outside of these scopes

// however, var's will be!
if (true) {

}

switch (x) {

}

for (i=0;i>1;) {

}


