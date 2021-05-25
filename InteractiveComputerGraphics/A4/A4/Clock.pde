class Clock {
  PShape clockFace;
  float l, w, x, y, xSpeed, ySpeed;

  Clock(){
    this.l = 100;
    this.w = 100;
    this.x = -(this.l/2);
    this.y = -(this.w/2);
    this.xSpeed = 1;
    this.ySpeed = 1;
    clockFace = loadShape("clock.svg");
  }
  
  Clock(float x, float y, float l, float w){
    //vector origin is top-left of vector graphic
    this.l = l; //length of vector
    this.w = w; //width of vector
    this.x = x-(l/2); //x-center position of vector
    this.y = x-(w/2); //y-center position of vector
    this.xSpeed = 1; 
    this.ySpeed = 2;
    clockFace = loadShape("clock.svg");
  }
  
  void display(){
    pushMatrix();
    translate(x,y);
    ellipseMode(CENTER);
    fill(255);
    ellipse(this.l/2, this.w/2, this.l, this.w);
    shape(clockFace, 0, 0, this.l, this.w);
    popMatrix(); 
  }
   
  //makes it bounce around the screen
  void move(){
    this.x += this.xSpeed;
    this.y += this.ySpeed;
    
    if (this.x > width - l){
      this.xSpeed = -this.xSpeed;
    }
    if (this.y > height - w){
      this.ySpeed = -this.ySpeed;
    }
    
    if (this.x < 0){
      this.xSpeed = -this.xSpeed;
    }
    if (this.y < 0){
      this.ySpeed = -this.ySpeed;
    }
  }
}
  
  
