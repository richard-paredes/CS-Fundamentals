

void setup(){
String[] lines;

lines = loadStrings("wordFrequency.txt");
int[] numbers = new int[lines.length];
int[] numbers2 = new int[lines.length];


for (int numLines = 0; numLines < lines.length; numLines++){
  String number1 = "";
  String number2 = "";
  //gets character by character of each line and adds it to a string-version of a number
  for (int singleint = 0; singleint < lines[numLines].length(); singleint ++){
    if (lines[numLines].charAt(singleint) != ':') {
      number1 += Character.toString(lines[numLines].charAt(singleint));
    }
    //skips the colon (:) and the space, getting the second number
     else {
        for (int secondSingleInt = singleint+2; secondSingleInt < lines[numLines].length(); secondSingleInt++){
          number2 += Character.toString(lines[numLines].charAt(secondSingleInt));
        }
        break;
     }
  }
  //converts the two number strings into integers and appends them to different arrays
  // the numbers on each line have corresponding indexes
  int firstNum = Integer.parseInt(number1);
  int secondNum = Integer.parseInt(number2);
  //println(firstNum + " : " + secondNum);
  numbers[numLines] = firstNum;
  numbers2[numLines] = secondNum;
  }
}
