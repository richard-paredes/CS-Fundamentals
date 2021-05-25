#include <iostream>
#include "Circle.h"

Circle::Circle()
{
   radius = 1;
}

Circle::Circle(double r)
{
   radius = r;
}

void Circle::setRadius(double r) { radius = r; }

double Circle::getRadius() const { return radius; }
bool Circle::operator==(const Circle &other) const
{
   return (this->radius * pi) == (other.radius * pi);
}
bool Circle::operator<(const Circle &other) const
{
   return (this->radius * pi) < (other.radius * pi);
}