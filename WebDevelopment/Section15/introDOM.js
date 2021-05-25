var head = document.querySelector("h2");
var body = document.querySelector("body");

var isBlue = false;

setInterval(function(){
    if(!isBlue){
        body.style.background = "white";
        head.style.color = "orange";
    } else {
        body.style.background = "blue";
        head.style.color = "gold"
    }
    isBlue = !isBlue;
}, 1000);

// five main document methods:
/*

document.getElementById()
document.getElementsByClassName()
document.getElementsByTagName()
document.querySelector()
document.querySelectorAll()

*/

// finds element with the id of 'highlight' (should only be one!)
var tag = document.getElementById('highlight');
console.log(tag);

// heres how to see the object representation
// of the element (since it IS an OBJECT)
console.dir(tag);


// returns an HTMLCollection of all elements
// containing the specified class name
var tags = document.getElementsByClassName("bolded");
console.log(tags);
console.dir(tags);
console.log(tags[0]);
console.log(tags.length);
// cannot do forEach on HTMLCollection
// tags.forEach(alert)

// returns a list (HTMLCollection) of all elements of a given element tag
// even if its 1 element, returns a list
var elems = document.getElementsByTagName("li");
var header = document.getElementsByTagName("head");
var title = document.getElementsByTagName("title");
// . . . all tag names!

// gets all elements that are of tag 'li'!
console.log(elems);
console.dir(elems);
console.log(elems[0]); //the li with an ID of highlight

// so to JUST get a single element object:
var elem = document.getElementsByTagName("li")[0] // will get first list element
// equivalent to var elem = elems[0]

// QUERY SELECTOR: Newer method
// returns first element OBJECT that matches a given
// CSS-style selector (tag, id, class)

// same thing as document.getElementById("highlight")
var tag = document.querySelector("#highlight");

// (almost) like document.getElementsByTagName("bolded");
// HOWEVER: 
// since its a querySelector, it returns only
// THE FIRST MATCH -- not all!
var li = document.querySelector(".bolded");

// returns the first corresponding tag
var firstH1 = document.querySelector("h1");
console.log(firstH1);

// querySelector can be very specific!
// note: difference between li.bolded and li . bolded
// is that li.bolded is a single element that is both li and class bolded
// while li .bolded is an element with a class of bolded
// that is a descendant of an li
var li = document.querySelector("ul li.bolded");
console.log(li);


// querySelectorAll 
// returns a list (NodeList) of elements that matches a given
// CSS-style selector
var all = document.querySelectorAll(".bolded");
console.log(all);
console.dir(all);
console.log(all[1]);
