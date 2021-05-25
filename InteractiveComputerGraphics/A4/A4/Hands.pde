class Hands {
  PShape hand;
  float x, y, l, w, angle;
  color c;

  
  Hands(Clock clockface, float l, float w,color c){
    //get center of clock in x,y and create shape
    this.x = clockface.x + clockface.w/2;
    this.y = clockface.y + clockface.l/2;
    this.l = l;
    this.w = w;
    this.c = c;
    hand = createShape(RECT,x-w/2,y,w,l,50);
  }

  
  void display(Clock clock, float angle){
    //rotate the hands to correct time and display on screen
    pushMatrix();
    translate(clock.x+100,clock.y+100);
    rotate(angle);
    translate(-clock.x - 100,-clock.y - 100);
    fill(c);
    strokeWeight(0);
    hand = createShape(RECT,x-w/2,y,w,l,50);
    shape(hand, clock.x, clock.y);
    popMatrix();
  }
}
