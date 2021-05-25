// there are 8 boolean operators:

// > greater than
// < less than
// >= greater than or equal to
// <= less than or equal to
// == equal to
// != not equal to
// === equal value and type
// !== not equal value or equal type

var x = 5;

var isFalse = (x==="5");
console.log("x == '5' : " + isFalse);
// '==' does not compare data types because it 
//  does something called type coercion
//  which is to switch into the same data types
var isTrue = (x==5);
console.log("x == 5 : " + isTrue);
var isTrue = (true == 1);
console.log("true == 1 : " + isTrue);
var isTrue = (false == 0);
console.log("false == 0 : " + isTrue);
var isTrue = (null == undefined);
console.log("null == undefined : " + isTrue);
var isFalse = (NaN == NaN);
console.log("NaN == NaN : " + isFalse);

console.log();
// there are 3 logical operators:

// && AND
// || OR
// !  NOT
var x = 5;
var y = 9;
console.log("x < 10 && x !== 5 : " + (x < 10 && x !== 5)); //false
console.log("y > 9 || x === 5 : " + (y > 9 || x ===5)); //true
console.log("!(x === y) : " + !(x===y)); //true

console.log();
// true:
var x = 10;
var y = "a";
console.log("y === 'b' || x >= 10 : " + (y === 'b' || x >= 10));

console.log();
// false:
var x = 3;
var y = 8;
console.log("!(x=='3' || x === y) &&  !(y!= 8 && x <= y) : " + (!(x=='3' || x === y) &&  !(y!= 8 && x <= y)));

console.log();
// every value is inherently truthy or falsey even if they arent explicity true or false
//  so they can still be used in boolean contexts
var x = "hello";
console.log("hello truthy value : " + !!x);
console.log("null truthy value : " + !!null);
console.log();
// THE ONLY VALUES THAT ARE FALSEY:
console.log("Values that are inherently false:\n\tfalse, 0, \"\", null, undefined, NaN");

console.log();
// false:
var str = "";
var msg = "haha!";
var isFunny = "false";
console.log("!((str||msg)&&isFunny) : " + !((str||msg)&&isFunny))
