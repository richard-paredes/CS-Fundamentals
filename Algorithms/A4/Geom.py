#  File: Geom.py

#  Description: Assignment 3, Geometrical constructors and comparisons 

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 02/10/2019

#  Date Last Modified: 02/10/2019

import math

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  def circle_outside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) >= (self.radius + c.radius)

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
    if not self.circle_inside(c) and not self.circle_outside(c):
        return True
    else:
        return False
    
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribe (self, r):
    return Circle((r.ul.dist(r.lr)/2), ((r.lr.x + r.ul.x)/2), ((r.ul.y+r.lr.y)/2))

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(round(self.radius, 2)) + ", Center: " + str(self.center)
    
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.radius - other.radius) < tol)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return (self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return (self.ul.y - self.lr.y)

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    return 2*self.width() + 2*self.length()

  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return self.length() * self.width()

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    return (self.ul.x <= p.x <= self.lr.x) and (self.ul.y >= p.y >= self.lr.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    return self.point_inside(r.ul) and self.point_inside(r.lr)

  # determine if another Rectangle is strictly outside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  def rectangle_outside (self, r):
    # checking if X bounds are outside of each other (other rect is left or right side of our Rectangle)
    if r.ul.x >= self.lr.x or self.ul.x >= r.lr.x:
        return True
    # checking if other rect is above or below our Rectangle when X bounds equal
    elif (self.ul.x == r.ul.x or self.lr.x == r.lr.x) and (r.lr.y >= self.ul.y or self.lr.y >= r.ul.y):
        return True
    # checking i other rect is above or below when other X bounds are in between  our Rectangle UL.x and LR.x
    elif (self.ul.x < r.lr.x < self.lr.x or self.ul.x < r.ul.x < self.lr.x) and (self.lr.y >= r.ul.y or r.lr.y >= self.ul.y):
        return True
    else:
        return False

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
    if not self.rectangle_inside(r) and not self.rectangle_outside(r):
        return True
    else:
        return False

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rectangle_circumscribe (self, c):
    return Rectangle(c.center.x - c.radius, c.center.y + c.radius, c.center.x + c.radius, c.center.y - c.radius)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.length() - other.length()) < tol) and (abs(self.width - other.width) < tol)

def main():
  # open the file geom.txt
  inFile = open("geom.txt", "r")

  # create Point objects P and Q
  line = inFile.readline().split()
  P = Point(float(line[0]), float(line[1]))
  line = inFile.readline().split()
  Q = Point(float(line[0]), float(line[1]))
  
  # print the coordinates of the points P and Q
  print("Coordinates of P:", P)
  print("Coordinates of Q:", Q)

  # find the distance between the points P and Q
  print("Distance between P and Q:", round(P.dist(Q), 2))
 
  # create two Circle objects C and D
  line = inFile.readline().split()
  C = Circle(float(line[0]), float(line[1]), float(line[2]))
  line = inFile.readline().split()
  D = Circle(float(line[0]), float(line[1]), float(line[2]))
  
  # print C and D
  print("Circle C:", C)
  print("Circle D:", D)

  # compute the circumference of C
  print("Circumference of C:", round(C.circumference(), 2))

  # compute the area of D
  print("Area of D:", round(D.area(), 2))

  # determine if P is strictly inside C
  print("P", "is" if C.point_inside(P) else "is not", "inside C")

  # determine if C is strictly inside D
  print("C", "is" if D.circle_inside(C) else "is not", "inside D")

  # determine if C and D intersect (non zero area of intersection)
  print("C", "does" if C.circle_overlap(D) else "does not", "intersect D")

  # determine if C and D are equal (have the same radius)
  print("C", "is" if C == D else "is not", "equal to D")

  # create two rectangle objects G and H
  line = inFile.readline().split()
  G = Rectangle(float(line[0]), float(line[1]), float(line[2]), float(line[3]))
  line = inFile.readline().split()
  H = Rectangle(float(line[0]), float(line[1]), float(line[2]), float(line[3]))

  # print the two rectangles G and H
  print("Rectangle G:", G)
  print("Rectangle H:", H)    

  # determine the length of G (distance along x axis)
  print("Length of G:", G.length())

  # determine the width of H (distance along y axis)
  print("Length of H:", H.width())

  # determine the perimeter of G
  print("Perimeter of G:", G.perimeter())

  # determine the area of H
  print("Area of H", H.area())

  # determine if point P is strictly inside rectangle G
  print("P", "is" if G.point_inside(P) else "is not", "inside G")

  # determine if rectangle G is strictly inside rectangle H
  print("G", "is" if H.rectangle_inside(G) else "is not", "inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  print("G", "does" if H.rectangle_overlap(G) else "does not", "overlap H")

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print("Circle that circumscribes G:", C.circle_circumscribe(G))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print("Rectangle that circumscribes D:", G.rectangle_circumscribe(D))
  # determine if the two rectangles have the same length and width
  print("Rectangle G", "is" if G == H else "is not", "equal to H")
  
  # close the file geom.txt
  inFile.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
