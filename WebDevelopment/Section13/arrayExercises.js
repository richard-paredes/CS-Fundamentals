var numbers = [22, 67, 33, 96, 88];
console.log(numbers[numbers.length]); // error out of bounds

var friendGroups = [
    ["Harry", "Ron", "Hermione"],
    ["Malfoy", "Crabbe", "Goyle"],
    ["Mooney", "Wormtail", "Prongs"]
];

console.log(friendGroups[2][0]); // Mooney

// iteration exercise:
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var colors = ["red", "orange", "yellow", "green"];

numbers.forEach(function (color) {
    if (color % 3 === 0) {
        console.log(color);
    }
});

// for-loop equivalent
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 3 === 0) {
        console.log(numbers[i]);
    }
}

function printReverse(arr) {
    if (!Array.isArray(arr)) {
        console.log("Error: not an array");
        return;
    }
    for (let i = arr.length-1; i > -1; i--) {
        console.log(arr[i]);
    }
}

printReverse(colors);

function isUniform(arr) {
    if (!Array.isArray(arr)) {
        console.log("Error: not an array");
        return false;
    }
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[i-1]) {
            return false;
        }
    }
    return true;
}
var uniform = isUniform([1, 3, 1, 1]);
console.log(uniform);

function sumArray(arr) {
    if (!Array.isArray(arr)) {
        console.log("Error: not an array");
        return 0;
    }
    let sum = 0;
    arr.forEach(function(element) {
        sum += element;
    });
    return sum;
}

console.log(sumArray([1, 1, 1, 1, 1]));

function max(arr) {
    if (!Array.isArray(arr)) {
        console.log("Error: not an array");
        return;
    }
    let max = arr[0];
    arr.forEach(function(element){
        if (max < element) {
            max = element;
        }
    });
    return max;
}
var num = max([9,23,4352,134,3239,9233,30,0]);
console.log(num);


// our local definition of forEach:
// arr.forEach(someFunction(element, index, arr)) {
//     // function code
// }

function myForEach(arr, func) {
    for(let i = 0; i < arr.length; i++) {
        func(arr[i]);
    }
};

var colors = ["red", "orange", "yellow"];
myForEach(colors, alert);

// invoking an anonymous function:
(function() {
    console.log("IN A FUNCTION");
})();


myForEach(colors, function(color) {
    console.log(color);
});

Array.prototype.myForEach = function(func) {
    for (let i = 0; i< this.length; i++) {
        func(this[i]);
    }
}

var friends = ["Charlie", "David", "Mattis", "Kaitlyn"];
friends.myForEach(alert);

friends.myForEach(function(elem){
    console.log("I love " + elem);
})