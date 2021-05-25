Clock c1;
Hands hrH, minH, secH;
color b, r;
float secondD, minuteD, hourD;


void setup() {
  size(500, 500);
  b = color(50,50,50);
  r = color(255,0,0);
  c1 = new Clock(100, 100, 200, 200);
  hrH = new Hands(c1,45,5,b);
  minH = new Hands(c1,65,3,b);
  secH = new Hands(c1,65,3,r);
  hourD = hour()*2*PI/12 + PI + minute()*2*PI/60/12;
  minuteD = minute()*2*PI/60 + PI + second()*2*PI/60/60;
  secondD = second()*2*PI/60 + PI;
}

void draw() {
  background(34,139,34);
  hourD += 3*PI/60/60/60/12;
  minuteD += 2*PI/60/60/60;
  secondD += 2*PI/60/60;
  c1.display();
  hrH.display(c1,hourD);
  minH.display(c1,minuteD);
  secH.display(c1,secondD);
  c1.move();
}
