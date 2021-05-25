var object = {};

// which of the following are valid?
// V = valid
// IV = invalid
object._name = "Headwig"; // V

object.age = 6; // V

var prop = "Color";
object[prop] = "red"; // V

// object.123 = true; // IV

var someObject = {
    friends: [
        {name: "Malfoy"},
        {name: "Crabbe"},
        {name: "Goyle"}
    ],
    color: "baby blue",
    isEvil: true
}
// retrieve "Malfoy":
someObject.friends[0].name;
