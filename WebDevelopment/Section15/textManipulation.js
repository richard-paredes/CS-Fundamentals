var para = document.querySelector('p'); // select first tag instance

// .textContent
// returns a string of ALL the text
// contained in a given element
// (excluding the tags, but including
// text from nested tags)
console.log(para.textContent); // prints the current contents ('This is an awesome paragraph')

// this will add onto the text 
// (but also override nested tags)
// para.textContent += "blah blah. Added from DOM!"

// this will completely remove ALL nested tags,
// overriding them with just text
// para.textContent = "text added from JS!"

// heres the correct structure maintained:
console.log(para.innerHTML);
para.innerHTML;

var ul = document.querySelector('ul');
console.log(ul.textContent);
console.log(ul.innerHTML);

// however, setting innerHTML = to something also
// overrides the current contents!
ul.innerHTML = "<li>Vines</li>";

// here it appends it to the inner html:
ul.innerHTML += "<li>Oak</li>";

// most people use textContent if 
// theres no nested elements!
document.querySelector("h1").textContent = "End Of This Lesson";

// more differences between inner HTML and text content
console.log(document.body.innerHTML); // shows html tags and stuff!
console.log(document.body.textContent);

// this doesn't work as expected:
// it will put out the LITERAL '<h1>Goodbye!</h1>'
// which won't be a header and will be the ONLY
// thing the document :(
// document.body.textContent = "<h1>Goodbye!</h1>"

// this WILL behave as expected!!
document.body.innerHTML += "<h2>Thanks for Learning!</h2>"