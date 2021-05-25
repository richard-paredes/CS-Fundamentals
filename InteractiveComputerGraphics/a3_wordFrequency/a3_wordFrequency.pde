//information from frequency file
String[]lines;
int[]numbers;
int[]numbers2;

//items for converting numbers to angles in degrees
float[]angles;
int total;
float radians;
float degrees;
float onePercent= (PI/50);
float percentage;

void setup(){
  size(1000,1000);
  background(0);
  noStroke();
  noLoop();
  lines = loadStrings("../wordFrequency.txt");
}

//Gets the angles in degrees of each frequency's frequency
public float[] get_angles(String[]lines){
  int[] numbers = new int[lines.length];
  int[] numbers2 = new int[lines.length];
  float[]angles = new float[lines.length];
  
  
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
    
    //Gets total occurances of each frequency
    for (int i=0; i< numbers.length; i++){
      total += numbers2[i];
    }
    
    //gets degrees and appends to a list
    for (int i=0; i< numbers2.length; i++){
      percentage = (float(numbers2[i])/float(total)) * 100;
 
      radians = percentage * onePercent;
      degrees = (radians) * (180/PI);
      angles[i]=degrees;
    }
  return angles;
}

//From Processing's website-- takes the percentage of the total frequency and writes it to a pie chart. Changed from gray to random RGB values for better visualization
void pieChart(float diameter, float[] angles) {
  float lastAngle = 0;
  int R;
  int G;
  int B;
  for (int i = 0; i < angles.length; i++) {
    R = int(random(255));
    G = int(random(255));
    B = int(random(255));
    fill(R, G, B);
    arc(width/2, height/2, diameter, diameter, lastAngle, lastAngle+radians(angles[i]));
    lastAngle += radians(angles[i]);
  }
}


void draw(){
  angles = get_angles(lines);
  pieChart(800,angles); 
  fill(255);
  textSize(30);
  text("Frequency of Word Frequencies", 270, 50);
  
}
