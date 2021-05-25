// to change attributes of elements:
// use .getAttribute() and .setAttribute()
// to read and write attributes such as
// src="" and href=""

var link = document.querySelector('a');

// get attribute
link.getAttribute('href'); // pulls up the attribute (http://www.google.com)

// change attribute:
link.setAttribute('href', "http://www.instagram.com");
var isGoogle = true;

setInterval(function() {
    if (isGoogle) {
        link.setAttribute("href", "http://www.instagram.com");
        link.textContent = "I am a link to Instagram";
    } else {
        link.setAttribute("href", "http://www.google.com");
        link.textContent = "I am a link to Google";
    }
    isGoogle = !isGoogle;
    console.log(link);
}, 5000);

// image sliders are made by changing source of the image

// to change the image src:
var img = document.querySelector('img');
img.getAttribute('src'); // returns '#'
img.setAttribute('src', 'https://images.unsplash.com/photo-1561614457-c7d60237fce2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=900&q=60');
