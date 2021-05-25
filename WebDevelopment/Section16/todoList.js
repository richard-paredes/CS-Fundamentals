// const firstLi = document.querySelectorAll('li');

// runs ONCE for the first time the mouse hovers over the
// specified element
// even if hovering around the element--
// you have to move OFF the element before it runs again
// firstLi.addEventListener('mouseover', function(){
//     firstLi.style.color = "red";
// });
// firstLi.addEventListener('mouseout', function(){
//     firstLi.style.color = "black";
// });

const listItems = document.querySelectorAll('li');

for (let i = 0; i < listItems.length; i++) {
    listItems[i].addEventListener('mouseover', function(){
        this.classList.add("selected");
    });
    listItems[i].addEventListener('mouseout', function(){
        this.classList.remove('selected');
    });
    listItems[i].addEventListener('click', function(){
        this.classList.toggle("completed");
    })
}