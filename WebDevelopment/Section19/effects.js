// https://api.jquery.com/category/effects/

var isFaded = false;
$('#fade').on('click', function () {
    // $('div').fadeOut(2000, function(){
    //     console.log("Fade completed!");
    //     // completely removes divs from HTML
    //     // $(this).remove();
    //     $(this).fadeIn(2000);
    // });

    $('.faders').fadeToggle(2000);

    // java script is asyncronous, so it can
    // move onto the next code even if it hasn't finished
    // the previous one
});
$('#slide').on('click', function(){
    // $('.sliders').slideUp(1000, function(){
    //     $(this).slideDown(1000);
    // })
    $('.sliders').slideToggle(1000, function(){
        console.log('slided!');
    });
})

