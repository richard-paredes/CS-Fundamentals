var obj = {
    name: "Chuck",
    age: 45,
    isCool: false,
    friends: ["Bob", "Tina"],
    add: function (x, y) {
        return x + y;
    }
}

// you can add functions to properties!
obj.add(10, 20); // returns 30


// cats and dogs
// NAMESPACE COLLISION: lose access to first function
function speak() {
    return "woof";
}

function speak() {
    return "meow";
}
speak(); // returns meow

var dog = {};
dog.speak = function () {
    return "WOOF";
}

var cat = {};
cat.speak = function () {
    return "MEOW";
}

dog.speak();
cat.speak();

// keyword: THIS:
// basically a pointer to the object itself
var comments = {};
comments.data = ["Good job!", "Awesome", "Crappy"];
comments.data;

comments.print = function () {
    this.data.forEach(function (comment) {
        console.log(comment);
    });
}

comments.print();
