/* assignment 3
novelvisualization: Processing version of word cloud
*/

PFont font1;
PFont font2;
PFont font3;
//UT colors
color[] c = {color(191, 87, 0), color(51, 63, 72), color(255)};
// can change font Size here
int fontSize = 30;
int w = 700;
int h = 600;
   
void setup(){
 size(700, 600);
 background(200);
 
 //String[] fontlist = PFont.list();
 //printArray(fontlist);
 
 //getting font data
 font1 = createFont("HARNGTON.TTF", fontSize);
 font2 = createFont("BROADW.TTF", fontSize);
 font3 = createFont("HTOWERT.TTF", fontSize);
 PFont[] fonts = {font1, font2, font3};
 
 //loading words and removing newlines chars
 String[] lines = loadStrings("../uniqueWords.txt");
 for (int i = 0; i < lines.length; i++) {
   lines[i] = lines[i].replace("\n", "");
 }
 
 wordCloud(fonts, lines);
}

void wordCloud(PFont[] font, String[] words ) {
   //indexing through x,y of canvas
 for (int y = fontSize; y < h; y += fontSize) {
   for (int x = 10; x < w; x ++) {
     
     int randWord = (int)(random(words.length));
     int randColor = (int)(random(c.length));
     int randFont = (int)(random(font.length));
            
     fill(c[randColor]);
     textFont(font[randFont]);
     
     // checking if word will leave edge of canvas
     if ((x + textWidth(words[randWord])) > w-10) {
       continue;
     }
     
     else {
       text(words[randWord], x, y);
       x += 20 + textWidth(words[randWord]);
     }
   }
 }
}
  
