// how to style with DOM


/* 

*****EXAMPLE***** 

// SELECT:
// var tag = document.getElementById("highlight");

// MANIPULATE:
// style comes from CSS -- contains all properties!
// (object).style.(property)
// tag.style.color = "green";
// tag.style.border = "10 px solid red";
// tag.style.fontSize = "70px";
// tag.style.background = "yellow";
// tag.style.marginTop = "200px";

*/

var head = document.querySelector('h2');
head.style.border = "2px solid blue";
head.style.background = "orange";
head.style.color = "blue";

// its not good practice to have multiple styling 
// done here-- that's DRY!

// separation of concern--
// DONT DO STYLING HERE IF YOU CAN DO IT IN CSS
// try to just focus on behavior here
// good example: define all the styling in a class in css
// then switch it on and off here by giving/removing the class
// from the target element

// instead of this:
/** 
var tag = document.getElementById("highlight");
tag.style.color = "blue";
tag.style.border = "10px solid red";

// have this in CSS:

.switchColor {
    color: blue;
    border: 10px solid red;
}


// and then activate it here
tag.classList.add("switchColor")
*/

var images = document.querySelectorAll('img');
var isFirst = false;

// classList:
// returns an object (kind of like BUT NOT an array)
// with the classes applied to the element object
// -- cant add into the array like normal:
// must use:
// .add, .remove, .toggle

setInterval(function(){
    if (isFirst) {
        images[0].classList.toggle("alterImage");
        // images[0].classList.add("alterImage");
        // images[1].classList.remove("alterImage");
    } else {
        images[1].classList.toggle("alterImage");
        // images[1].classList.add("alterImage");
        // images[0].classList.remove("alterImage");
    }
    isFirst = !isFirst;
    console.log(isFirst);
}, 3000);