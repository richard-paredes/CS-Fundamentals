// come up with 4 different ways to select the first <p> tag
var p1 = document.querySelector('p');
var p2 = document.querySelector('#first.special');
var p3 = document.getElementById('first');
var p4 = document.getElementsByTagName('p')[0];
var p5 = document.querySelector('#first');
var p6 = document.querySelector('.special');
var p7 = document.querySelectorAll('.special')[0];
var p8 = document.querySelectorAll('p')[0];
var p8 = document.querySelectorAll('h1+p');

console.log(p1);
console.log(p2);
console.log(p3);
console.log(p4);
console.log(p5);
console.log(p6);
console.log(p7);
console.log(p8);

