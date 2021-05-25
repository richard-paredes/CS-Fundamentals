class Hands {
  PShape hand;
  
  
  float x, y, l, w;
  
  Hands(Clock clockface){
    //get center of clock in x,y
    this.x = clockface.x;
    this.y = clockface.y;
    this.l = 100;
    this.w = 100;

  }
  
  Hands(Clock clockface, float l, float w){
    //get center of clock in x,y
    this.x = clockface.x;
    this.y = clockface.y;
    this.l = l;
    this.w = w;
  }

  
  void display(Clock clock){
    hand = loadShape("hourHand.svg");
    shape(hand, clock.x, clock.y, this.l, this.w);
  }
  
  void rotate(){
    
  }
  
}
