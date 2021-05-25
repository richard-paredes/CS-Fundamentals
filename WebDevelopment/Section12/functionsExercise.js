var isEven = function (number) {
    if (typeof(number) !== "number") {
        return false;
    }
    return (number % 2 === 0);
}

var factorial = function (number) {
    if (typeof(number) !== "number") {
        return undefined;
    }

    var factorial = 1;
    for (let i = 1; i <= number; i++) {
        factorial *= i;
    }
    return factorial;
};

var kebabToSnake = function(str) {
    if (typeof(str) !== "string") {
        return undefined;
    }
    // var snakeString = "";
    // for (let i = 0; i < str.length; i++) {
    //     if (str[i] === "-") {
    //         snakeString += "_";
    //     } else {
    //         snakeString += str[i];
    //     }
    // }
    // or
    return str.replace('-', '_');
}

console.log("Is 93 even? " + isEven(93));
console.log("Is 100 even? " + isEven(100));

console.log("Factorial of 6: " + factorial(6));
console.log("Factorial of 4: " + factorial(4));
console.log("Factorial of 0: " + factorial(0));

console.log("Snake of 'hello-world': " + kebabToSnake("hello-world"));
