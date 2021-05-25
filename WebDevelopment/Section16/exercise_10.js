const playerOne = document.querySelector('#playerOne');
const playerOneButton = document.querySelector('#playerOneButton');
const playerTwo = document.querySelector('#playerTwo');
const playerTwoButton = document.querySelector('#playerTwoButton');

const resetButton = document.querySelector('#resetButton');

const maxSelector = document.querySelector('#maxSelector');
const currentMax = document.querySelector('#currentMax');

var gameOver = false;

playerOneButton.addEventListener('click', function() {
    incrementPlayerScore(playerOne, playerTwo);
});
playerTwoButton.addEventListener('click', function(){
    incrementPlayerScore(playerTwo, playerOne);
});

resetButton.addEventListener('click', resetScores);

// dont use a click event listener because
// this wont update if user uses keyboard
maxSelector.addEventListener('change', updateMaxScore)

function incrementPlayerScore(player, opponent) {
    if (!gameOver) {
        checkScore(player, opponent);
    }
}

function updateMaxScore() {
    // .value returns the value of the input
    // in a STRING data type
    currentMax.textContent = maxSelector.value;
    resetScores();
}

function resetScores() {
    // resetting score
    playerOne.textContent = '0';
    playerTwo.textContent = '0';
    // clearing classes
    playerOne.classList = ""; 
    playerTwo.classList = "";
    // resetting game state
    gameOver = false;
}

function checkScore(player, opponent) {

    var maxScore = Number(currentMax.textContent);
    var score = Number(player.textContent);

    console.log(player);

    score++;
    player.textContent = score;

    gameOver = (score >= maxScore);

    if (gameOver) {
        player.classList.toggle('winner');
        opponent.classList.toggle('loser');
    }
}
