// tasks:
// correctly include jquery
if (jQuery) {
    // alert("jQuery loaded successfully");
    console.log('Successful loading');
} else {
    alert("failed to load jQuery");
}
// 
// select all divs and give them a purple bg
$('div').css('background', 'purple');

// select highlight divs and make 200 px wide
$('.highlight').css('width', '200px');

// select div #third and give orange border
$('#third').css({
    border: "3px solid orange"
})

// select first div only and change font color to pink
$('div').first().css({
    color:'pink'
})
// CSS-standard
$('div:first-of-type').css({
    border:'1px dashed yellow'
})

// important methods:
// https://api.jquery.com/
/*
.val()
.text()
.attr()
.html()
.addClass()
.removeClass()
.toggleClass()

*/

// text is same as .textContent in DOM:
// however, it returns all text in ALL ul's
// this is HTML-safe!
var textContent = $('ul').text();

$('h1').text('New Text!')

$('li').text('Changed all li in one statement');

// html is same as .innerHTML in DOM:
// retrieves inner HTML

$('ul').html("<li>Li 1</li><li>Li 2</li>");


// attr
// retrieves or changes the attribute
$('img').css('width', '300px');
$('img:first').attr('src', 'https://tinypng.com/images/social/page-analyzer.jpg')
$('img').eq(1).attr('src','https://scottiestech.info/wp-content/uploads/2016/02/tinypng.jpg')
$('img').last().attr('src','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNMg3w59Vbj7ORFLY-gQF9mCShP63KYPbF6U_xTYqA2SfRuyt3')

$("input").attr('type') // "color"
// $('input').attr('type','color');

// .val() 
// returns the value
$('input').val(); // empty until something is inputted
$('input').val('Miiko!');

$('option').val(); // returns what the selected dropdown is

// manipulation of classes:
// same things as classList.add/remove/toggle
$('h1').addClass('correct');
$('h1').removeClass('correct');

// dont need to iterate through objects:
// will affect all of them
$('li').addClass('done');

$('div').last().toggleClass('correct');


