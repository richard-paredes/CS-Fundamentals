// suppose wanted to model a person:
var person = ["Cindy", 32, "Missoula"];

// fetching hometown
person[2] // not meaniningful code

// what if i accidentally reversed the order
var person2 = ["Travis", "Los Angeles", 21]; // !!

// person OBJECT!
// this stores data in key-value pairs
// NOTE: stores it all bunched up in memory block
// but not in order like an array
var person3 = {
    name: "Cindy",
    age: 32,
    city: "Missoula"
};

// methods of retrieving data:
console.log(person3.age); // dot notation
console.log(person3["name"]); // bracket notation

var dog = {
    name: "Rusty",
    breed: "Mutt",
    age: 3
}

console.log(dog.age);

// differences between data-retrieval notations:
// someObject.1blah; // cannot access properties that start with numbers
var someObject = {};
someObject["1blah"]; // valid

// you can loopup using a variable with bracket notation
var str = "name";
someObject.str // doesn't look for "name"
someObject[str] // will evaluate and look for name

// you cannot use dot notation for property names with space
// someObject.fav color; // invalid
someObject["fav color"]; // valid

// UPDATING OBJECT DATA:
var person4 = {
    name: "Travis",
    age: 21,
    city: "LA"
};

// to update age:
person4["age"] += 1;
// to update city:
person4.city = "London";

// Empty Objects
var person = {};
person.name = "Travis";
person.age = 21;
person.city = "LA";

// all at once
var person = {
    name: "Travis",
    age: 21,
    city: "LA"
}

// another way
var person = new Object();
person.name = "Travis";
person.age = 21;
person.city = "LA";

// objects can hold any sort of data!!
var junkObject = {
    age: 57,
    color: "purple",
    isHungry: true,
    friends: ["Horatio", "Hamlet"],
    pet: {
        name: "Rusty",
        species: "Dog",
        age: 2
    }
};

// Arrays Vs Objects:

// arrays:
// - index-bound itemization
var dogs = ["Rusty", "Lucky", "Bubba"];
dogs[1] // = Lucky
dogs.push("Wyatt") // adds a new dog, must specify where (end of arr)
dogs[1] = "Lucy";

// objects:
// - un-ordered (not index-bound)
// - dictionary
// - key/value pairs
var dog = {
    name: "Bubba",
    breed: "Lab"
};
dog.name // Bubba
dog["name"] // Bubba
dog.age = 6; // adds a new property to the object
dog["age"] = 6; // adds a new property to the object, no need to specify where
dog.breed = "Black Lab";


// EXAMPLE:
var posts = [
    {
        title: "Cats are mediocre",
        author: "Colt",
        comments: ["Awesome post!", "Terrible post. . "]
    },
    {
        title: "Cats are actually awesome",
        author: "Cat Luvr",
        comments: ["<3", "Stop being dumb"]
    }
]

// to access title of first post:
posts[0].title;

// to access second comment of second post
posts[1].comments[1];


// here is how you declare classes!
// class declarations are NOT hoisted
// meaning we have to define it first before we can use it
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this.isHappy = true;
    }
    get getName() {
        return this.name;
    }

    get getAge() {
        return this.age;
    }

    birthday() {
        this.age += 1;
    }

    changeMood() {
        this.isHappy = !this.isHappy;
    }
}

let pers = new Person("Richard", 21);
console.log();
pers.birthday();
console.log(pers.getAge);