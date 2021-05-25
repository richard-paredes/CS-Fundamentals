const squares = document.querySelectorAll('.square');
const colorDisplay = document.querySelector('#colorDisplay');
const messageDisplay = document.querySelector('#messageDisplay');
const title = document.querySelector('#title');
const resetButton = document.querySelector('#reset');
const easyButton = document.querySelector('#easy');
const mediumButton = document.querySelector('#medium');
const hardButton = document.querySelector('#hard');

const backgroundColor = "#272822";
const titleBackground = "#ae81ff";

var goalColor;
var currentMode = mediumButton;
var numberOfSquares = 6; // start on hard mode

var redChannel;
var greenChannel;
var blueChannel;

function randomizeSquareColors(numberOfSquares) {
    let winningSquare = generateRandomInteger(0, numberOfSquares - 1);

    for (let i = 0; i < numberOfSquares; i++) {
        // add initial colors to squares
        squares[i].style.backgroundColor = generateRandomColor(i === winningSquare);
        // add event handlers to squares
        squares[i].addEventListener('click', function () {
            checkClickedSquare(this);
        })
    }
    setColorDisplay();
}

function generateRandomInteger(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateRandomColor(isWinningColor) {
    var red = generateRandomInteger(0, 255);
    var green = generateRandomInteger(0, 255);
    var blue = generateRandomInteger(0, 255);

    var rgbColor = "rgb(" + red + ", " + green + ", " + blue + ")";

    // winning color selected
    if (isWinningColor) {
        goalColor = rgbColor;
        redChannel = red;
        greenChannel = green;
        blueChannel = blue;
    }
    return rgbColor;
}

function getColorChannel(colorString) {
    // remove parenthesis
    colorString = colorString.replace("(", "");
    colorString = colorString.replace(")", "");
    colorString = colorString.replace(",", "");
    colorString = colorString.replace(",", "");
    console.log(colorString);
    var channel = "";

    return channel;
}

function setColorDisplay() {
    colorDisplay.innerHTML = "<span class='parentheses'>(</span><span class='red'>" + redChannel + ", </span><span class='green'>" + greenChannel + ", </span><span class='blue'>" + blueChannel + "</span><span class='parentheses'>)</span>";
}

function displayCorrectMessage() {
    messageDisplay.textContent = "NICE JOB!";
}

function displayIncorrectMessage() {
    messageDisplay.textContent = "TRY AGAIN!";
}

function clearMessageDisplay() {
    messageDisplay.textContent = "";
}

function checkClickedSquare(square) {
    if (square.style.backgroundColor === goalColor) {
        displayCorrectMessage();
        makeSquaresGoalColor();
        finishedResetDisplay();
    } else {
        displayIncorrectMessage();
        // square.classList.toggle("wrongSquare");
        resetSquareColor(square);
    }
}

function unfinishedResetDisplay() {
    resetButton.textContent = "NEW COLORS"
}

function finishedResetDisplay() {
    resetButton.textContent = "PLAY AGAIN?";
}

function makeSquaresGoalColor() {
    for (let i = 0; i < numberOfSquares; i++) {
        squares[i].style.backgroundColor = goalColor;
    }
    title.style.background = goalColor;
}

function resetTitleBackground() {
    title.style.backgroundColor = titleBackground;
}

function resetSquareColor(square) {
    square.style.backgroundColor = backgroundColor;
}

function resetButtons() {
    easyButton.classList = "";
    mediumButton.classList = "";
    hardButton.classList = "";
}

function removeSquare(square, remove) {

    // ternary operator: 
    // 3 parts:
    // condition ? (what we want to happen if true) : (what we want if false)

    remove === true ? square.style.display = "none" : square.style.display = "block";
    // if (remove) {
    //     square.style.display = "none";
    // } else {
    //     square.style.display = "block";
    // }
}

function resetSquareDisplay() {
    for (let i = 0; i < squares.length; i++) {
        resetSquareColor(squares[i]);
        if (i >= numberOfSquares) {
            removeSquare(squares[i], true);
        } else {
            removeSquare(squares[i], false);
        }
    }
}

function selectMode() {
    resetButtons();
    if (currentMode === easyButton) {
        easyButton.classList.toggle("selected");
    } else if (currentMode === mediumButton) {
        mediumButton.classList.toggle("selected");
    } else {
        hardButton.classList.toggle("selected");
    }
}

function resetGame() {
    resetSquareDisplay();
    // resetTitleBackground();
    resetButtons();
    randomizeSquareColors(numberOfSquares);
    clearMessageDisplay();
    unfinishedResetDisplay();
    selectMode();
}

resetGame();

resetButton.addEventListener('click', resetGame);

easyButton.addEventListener('click', function () {
    // prevent easy from acting as a reset
    numberOfSquares = 3;
    currentMode = easyButton;
    resetGame();
});

mediumButton.addEventListener('click', function () {
    // prevent medium from acting as a reset
    numberOfSquares = 6;
    currentMode = mediumButton;
    resetGame();
});

hardButton.addEventListener('click', function () {
    // prevent hard from acting as a reset
    numberOfSquares = 9;
    currentMode = hardButton;
    resetGame();
});