// create an array of movie objects:
// each movie has:

// title
// rating
// hasWatched

// task: iterate through array and print out:
// "You have watched 'In Bruges' - 5 stars":

var movieDB = [
    {
        title: "Detective Pikachu",
        rating: 3.0,
        hasWatched: true
    },
    {
        title: "Iron Man",
        rating: 3.0,
        hasWatched: false
    },
    {
        title: "John Wick 3",
        rating: 4.5,
        hasWatched: false
    },
    {
        title: "Coco",
        rating: 4.5,
        hasWatched: false
    },
    {
        title: "Life of Pets 2",
        rating: 4.5,
        hasWatched: false
    },
    {
        title: "Dark Phoenix",
        rating: 4.0,
        hasWatched: true
    },
    {
        title: "Avenger's Endgame",
        rating: 4.8,
        hasWatched: true
    },
    {
        title: "Frozen",
        rating: 3.4,
        hasWatched: true
    },
    {
        title: "Interstellar",
        rating: 5.0,
        hasWatched: true
    },
    {
        title: "X-Men First Class",
        rating: 4.0,
        hasWatched: true
    },
    {
        title: "X-Men Days of Future Past",
        rating: 3.5,
        hasWatched: true
    },
    {
        title: "X-Men Apocalypse",
        rating: 4.0,
        hasWatched: true
    },
    {
        title: "Logan",
        rating: 4.3,
        hasWatched: true
    }
];

function printLine(object) {
    var str = "You ";
    if (object.hasWatched) {
        str += "have watched ";
    } else {
        str += "have not seen ";
    }
    str += "\"" + object.title + "\" -- ";
    str += object.rating + " stars";
    console.log(str);
}


movieDB.forEach(printLine);

