
// print all numbers between -10 and 19
var num = -10;
while (num <= 19) {
    console.log(num);
    num++;
}
// NOTE: REMEMBER TO USE '===', its better practice than ==
// print all even numbers between 10 and 40
var num = 10;
while (num <= 40) {
    if (num % 2 === 0) {
        console.log(num);
    }
    num++;
}
// more efficient:
var num = 10;
while (num <= 40) {
    console.log(num);
    num += 2;
}

// print all odd numbers between 300 and 333
var num = 300;
while (num <= 333) {
    if (num % 2 === 1){
        console.log(num);
    }
    num++;
}

// print all numbers divisible by 5 and 3 between 5 and 50
var num = 5;
while (num <= 50){
    if (num % 5 === 0 && num % 3 === 0) {
        console.log(num);
    }
    num++;
}

// for (init; condition; increment)

for (var count = 0; count < 6; count++) {
    console.log(count);
}

var str = "hello";

for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}

// print all numbers between -10 and 19
for (let i = -10; i <= 19; i++) {
    console.log(i);
}

// print all even numbers between 10 and 40
for (let i = 10; i <= 40; i+=2) {
    console.log(i);
}

// print all odd numbers between 300 and 333
for (let i = 300; i <= 333; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

// print all numbers divisible by 5 and 3 between 5 and 50
for (let i = 5; i <= 50; i += 1) {
    if (i % 5 === 0 && i % 3 === 0) {
        console.log(i);
    }
}