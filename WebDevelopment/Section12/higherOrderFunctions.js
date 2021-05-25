// Higher order functions are functions that:
/*
    take a function as an argument

    OR

    return a function
*/

function singSong() {
    console.log("Twinkle, twinkle, little star,");
    console.log("How I wonder what you are");
    console.log("Up above the world so high");
    console.log("Like a diamond in the sky");
}

// we dont pass in singSong() because
// what we want to do is pass in the fUNCTIOn
//  not its return value:
// using parenthesis causes the function to execute,
//  which is not what we want-- we want setInterval to do that

// var clearNumber = setInterval(singSong, 5000);


// var clearNumber = setInterval(function() {
//     console.log("I am an anonymous function!");
//     console.log("THIS IS AWESOME!");
// }, 3000);

// clearInterval(clearNumber);