var path = new Path();
var circles = [];
var currentSounds = 0;
var sounds = [
    keyData_A, keyData_B, keyData_C, 
    keyData_D, keyData_E, keyData_F,
    keyData_G
];
var keyData = sounds[currentSounds];


function generateRandomInteger(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function generateRandomColor() {
    var red = generateRandomInteger(0, 255);
    var green = generateRandomInteger(0, 255);
    var blue = generateRandomInteger(0, 255);

    var rgbColor = "rgb(" + red + ", " + green + ", " + blue + ")";

    return rgbColor;
}

function generateCircle(color) {
    var x = generateRandomInteger(0, view.size.width);
    var y = generateRandomInteger(0, view.size.height);
    var r = generateRandomInteger(1, 100);
    var circle = new Path.Circle(new Point(x, y), r);
    if (color) { // if color provided
        circle.fillColor = color;
    } else {
        circle.fillColor = generateRandomColor();
    }
    circles.push(circle);
}

function onKeyDown(event) {

    // if the event is truthy (not undefined):
    // keyData[event.key]
    if (event.key in keyData) {
        keyData[event.key].sound.play();
        generateCircle(keyData[event.key].color);
    } else if (event.key === "enter") {
        currentSounds++;
        keyData = sounds[currentSounds % sounds.length];
        
    }

}

var path = new Path.Circle({
    center: view.center,
    radius: 70,
    fillColor: 'red'
});

function onFrame(event) {
    // Each frame, change the fill color of the path slightly by
    // adding 1 to its hue:
    for (var i = 0; i < circles.length; i++) {
        circles[i].fillColor.hue += 2;
        circles[i].scale(0.9);
        if (circles[i].area < 0.1) {
            circles[i].remove();
            circles.splice(i, 1);
        }
    }

}