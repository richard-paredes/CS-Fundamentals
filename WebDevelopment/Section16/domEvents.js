// Events are everywhere!
// - clicking on a button
// - hovering over a link
// - dragging and dropping
// - pressing the enter key
// - arrow keys to change slides, etc

// PROCESS:
// select and element
// add an event listener
// ex:
/*
    var button = document.querySelector('button');
    button.addEventListener('click/hover/keypress')

    element.addEventListener(type, functionToCall(){

    })
    
*/

var button = document.querySelector('button');
var paragraph = document.querySelector('p');

button.addEventListener('click', function() {
    console.log("SOMEONE CLICKED THE BUTTON!");
    paragraph.innerHTML += "<br><strong>You clicked me!</strong><br>"
});

var h1 = document.querySelector('h1');

h1.addEventListener('click', function(){
    h1.classList.toggle('clicked');
})


// works on the entire block (all nested tags)
document.querySelector('ul').addEventListener('click', function() {
    console.log('YOU CLICKED THE UL!');
    this.classList.toggle('changeBG');
});

var lis = document.querySelectorAll('li');

for (let i = 0; i < lis.length; i++) {
    lis[i].addEventListener('click', function(){
        console.log("You clicked: " + this.textContent);
        this.classList.toggle('changeBG');
    })
}

function changeText() {
    paragraph.textContent += 'Someone clicked the button!';
}