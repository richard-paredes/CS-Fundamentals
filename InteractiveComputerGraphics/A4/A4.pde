
Clock c1;
Hands hrH;


void setup() {
  
  size(1000, 1000);
  background(255);
  c1 = new Clock(100, 100, 100, 100);
  hrH = new Hands(c1);
  
}

void draw() {
  
  background(111);
  c1.display();
  hrH.display(c1);
  c1.move();
}
