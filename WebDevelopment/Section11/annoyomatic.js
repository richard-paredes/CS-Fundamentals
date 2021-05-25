var userAnswer;

do {
    userAnswer = prompt("Are we there yet?");
    
} while ((userAnswer.indexOf("yes") === -1 && userAnswer.indexOf("yea") === -1));

alert("Yay, we're here!");