#pragma once

class Circle
{
private:
   double radius;
   double pi = 3.14; // tell students to use using pi = 3.14

public:
   Circle();
   Circle(double r);
   void setRadius(double r);
   double getRadius() const;
   //Add necessary operators
   bool operator==(const Circle &other) const;
   bool operator<(const Circle &other) const;
};