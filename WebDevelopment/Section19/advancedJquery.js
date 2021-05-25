// event handling
// the most important:
/*

    click()
    keypress()
    on()

*/
/* EXAMPLES:

$('#submit').click(function(){
    console.log('Another click');
})

$('button').click(function(){
    alert('Someone clicked a button!');
})

*/

// click
$('h1').click(function(){

    alert("h1 clicked!");

});

$('button').click(function(){

    alert('button clicked!');

});

$('button').click(function(){
    $(this).css('background','pink');
    console.log("You clicked:", $(this).text());
})

// keypress
// keydown: triggered as soon as key is pushed down
// keyup: trigged as soon as key released
// keypress: triggered in between keydown/keyup
// NOTE:
// keydown&keyup provide code indicating key pressed
// keypress indicates which character was entered
// ex:
// keydown/keyup will trigger for shift and a (both times)
// keypress will trigger once for 'A' (shift+a)

// on test, doesnt trigger on 'backspace', 'tab','capslock'
$('input').keypress(function (event) { 
    console.log('you pressed a key!');
    // returns n.event object
    // has a 'which' and 'keycode' 
    // of what key was pressed
    // console.log(event);

    // .which 13 is 'ENTER' key
    if (event.which === 13) {
        console.log('you pressed: ENTER');
    }
});

// on
// behaves the same as addEventListener
// lets you specify the type of event 
// to listen for

// key difference: 
// ***********
// 'on' specifies to add listeners for
// all existing and future elements
// **************
// while specific ones like .click() specify
// only for existing

$('h2').on('click', function(){
    // will affect the SPECIFIC h2 that was clicked
    $(this).toggleClass('clicked');
    // will affect ALL h2s, even if not clicked
    // $('h2').toggleClass('clicked');
})

$('input').on('keypress', function(){
    console.log('key pressed!');
});

// only triggers once when entering
$('button').on('mouseenter', function(){
    $(this).toggleClass('hovered');
})

$('button').on('mouseleave', function () {
    $(this).toggleClass('hovered');
});