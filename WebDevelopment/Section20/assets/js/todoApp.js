generateBackgroundGradient();

// Check off to-do item by clicking
// add event listener to parent UL
// then only process click event if on li
$('.unfinished').on('click', 'li', function () {
    var completed = $(this).text();
    $('.finished').append('<li class=""><span class="trash"><i class="fas fa-trash"></i></span> ' + completed + '</li>');
    $('.finished').children().last().toggleClass('completed');
    $(this).remove();
});

$('.finished').on('click', 'li', function () {
    var uncompleted = $(this).text();
    $('.unfinished').append('<li class=""><span class="trash"><i class="fas fa-trash"></i></span> ' + uncompleted + '</li>');
    $(this).remove();
});

// Click on trash to delete
$('ul').on('click', 'span', function (event) {
    // prevents event-bubbling up (top layers/nests)
    event.stopPropagation();
    $(this).parent().slideUp(250, function () {
        $(this).remove();
    });

})

$('input[type="text"].addIncomplete').on('keypress', function (event) {
    if (event.which === 13) {
        // add new todo
        // appends adds an HTML element onto the specified element
        $('.unfinished').append('<li class=""><span class="trash"><i class="fas fa-trash"></i></span> ' + $(this).val() + '</li>');
        // clear the input
        $(this).val("");
    }
});

$('input[type="text"].addComplete').on('keypress', function (event) {
    if (event.which === 13) {
        // add new finished item
        // appends adds an HTML element onto the specified element
        $('.finished').append('<li class=""><span class="trash"><i class="fas fa-trash"></i></span> ' + $(this).val() + '</li>');
        $('.finished').children().last().toggleClass('completed');
        // clear the input
        $(this).val("");
    }
});

$('.fa-pencil-alt').on('click', function () {

    $('input[type="text"].addIncomplete').fadeToggle();
})

$('.fa-check').on('click', function () {

    $('input[type="text"].addComplete').fadeToggle();
})

var redL, greenL, blueL; // left half of gradient
var redR, greenR, blueR; // right half of gradient

// gets integer between min and max (inclusive of both)
function generateRandomInteger(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateRandomColor() {
    let red = generateRandomInteger(0, 255);
    let green = generateRandomInteger(0, 255);
    let blue = generateRandomInteger(0, 255);

    var rgbColor = "rgb(" + red + ", " + green + ", " + blue + ")";

    return rgbColor;
}

function generateBackgroundGradient() {
    console.log("-webkit - linear - gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")");
    console.log("linear - gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")");
    // $('body').css({
    //     backgroundColor: "-webkit - linear - gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")",
    //     /* Chrome 10-25, Safari 5.1-6 */
    //     backgroundColor: "linear - gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")"
    //     /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    // })
    $('body').css({
        backgroundImage: "-webkit - linear - gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")",
        backgroundImage: "linear-gradient(to right, "+generateRandomColor()+", "+generateRandomColor()+")"
    });
}