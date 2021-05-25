// Selecting with jQuery:
// similar to querySelectorAll()
// $("selectorGoesHere")
// https://api.jquery.com/

// when an element with id trigger is clicked,
// will perform the anon function:
$('#trigger').click(function(){
    // body element will change background to yellow
    $('body').css('background', 'yellow');
    $(this).css('background', 'green');

    // (all) images will fade out for 3000ms and then
    // at the end, will be removed
    $('img').fadeout(3000, function(){

        $(this).remove();
    });
});

$('h1').css('color',"red");

var stylize = {
    backgroundColor: "pink",
    fontWeight: "bold"
}

// can pass in objects to the .css() function!
$('ul').css(stylize);
$('h1').css({
    backgroundColor: "blue",
    border: "3px solid black"
})
$('li').css({
    fontSize:"10px",
    border:"3px dashed orange",
    background: "white"
})