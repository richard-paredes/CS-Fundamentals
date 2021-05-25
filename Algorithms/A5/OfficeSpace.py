#  File: OfficeSpace.py

#  Description: Assignment 5, Allocating office spaces with rectangle objects

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 02/14/2019

#  Date Last Modified: 02/15/2019

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

class Rectangle (object):
  # constructor
  def __init__ (self, ll_x = 0, ll_y = 1, ur_x = 1, ur_y = 0):
    if ((ll_x < ur_x) and (ur_y > ll_y)):
      self.ur = Point (ur_x, ur_y)
      self.ll = Point (ll_x, ll_y)
    else:
      self.ur = Point (0, 1)
      self.ll = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return (self.ur.x - self.ll.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return (self.ur.y - self.ll.y)


  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return self.length() * self.width()

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    return (self.ll.x <= p.x <= self.ur.x) and (self.ur.y >= p.y >= self.ll.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    return self.point_inside(r.ur) and self.point_inside(r.ll)

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  # TODO: check if two vertices are inside ...
  def rectangle_overlap (self, r):

    if not self.rectangle_inside(r):

      if self.point_inside(r.ur):
        #upper right corner of other overlaps
        #print("UR is in!")
        #check if UL is in as well)
        if self.point_inside(Point(r.ll.x, r.ur.y)):
          if Rectangle(r.ll.x, self.ll.y, r.ur.x, r.ur.y).area() > 0:
            return Rectangle(r.ll.x, self.ll.y, r.ur.x, r.ur.y).area()
          else:
            return 0
        
        elif Rectangle(self.ll.x, self.ll.y, r.ur.x, r.ur.y).area() > 0:
          return Rectangle(self.ll.x, self.ll.y, r.ur.x, r.ur.y).area()
        
        else:
          return 0
      
      elif self.point_inside(Point(r.ll.x, r.ur.y)):
        #upper left corner of other overlaps
        #print("UL is in!")
        if Rectangle(r.ll.x, self.ll.y, self.ur.x, r.ur.y).area() > 0:
          #print("UL and UR are in!")
          return Rectangle(r.ll.x, self.ll.y, self.ur.x, r.ur.y).area()
        else:
          return 0
      
      elif self.point_inside(r.ll):
        #lower left corner of other overlaps
        #check if LR is in as well)
        if self.point_inside(Point(r.ur.x, r.ll.y)):
          #print("LL and LR are in!")
          if Rectangle(r.ll.x, r.ll.y, r.ur.x, self.ur.y).area() > 0:
            return Rectangle(r.ll.x, r.ll.y, r.ur.x, self.ur.y).area()
          else:
            return 0
        
        elif Rectangle(r.ll.x, r.ll.y, self.ur.x, self.ur.y).area() > 0:
          return Rectangle(r.ll.x, r.ll.y, self.ur.x, self.ur.y).area()
        
        else:
          return 0
      
      elif self.point_inside(Point(r.ur.x, r.ll.y)):
        # ONLY lower right corner of other overlaps
        #print("LR is in!")
        if Rectangle(self.ll.x, r.ll.y, r.ur.x, self.ur.y).area() > 0:
          return Rectangle(self.ll.x, r.ll.y, r.ur.x, self.ur.y).area()
        else:
          return 0
      
      elif self.point_inside(Point((r.ur.x + r.ll.x)/2 , (r.ur.y + r.ll.y)/2)):
        #overlaps with vertices outside
        if r.ur.x < self.ur.x:
          return Rectangle(r.ll.x, self.ll.y, r.ur.x, self.ur.y).area()
        else:
          return Rectangle(self.ll.x, r.ll.y, self.ur.x, r.ur.y).area()
        
        #rectangle is outside -- not overlapping
      else:
        return 0
  
    #rectangle is inside 
    else:
      #print("rectangle is inside!")
      return r.area()

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "LL: " + str(self.ll) + ", UR: " + str(self.ur)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.length() - other.length()) < tol) and (abs(self.width - other.width) < tol)

def main():
  # open the file office.txt
  inf = open("office.txt", "r")

  line = inf.readline().split()

  #reading the file line by line
  while line != '':

    #generating total office space available
    officeSpace = Rectangle(0, 0, int(line[0]), int(line[1]))
    print("Total:", officeSpace.area())

    #obtaining number of employees in office
    line = inf.readline().split()
    numEmployees = int(line[0])
    
    #creating lists of employees, their assigned rectangle spaces, their allocated spaces after contested spaces
    #also creating contested area and unallocated area counters
    employees = []
    employeeOffices = []
    employeeOfficeAllocated = []
    contested = 0
    unallocated = officeSpace.area()
 
    for employee in range(numEmployees):
      line = inf.readline().split()
      #appending employee names to list
      employees.append(line[0])
      #appending desired employee rectangle spaces to list
      employeeOffices.append(Rectangle(int(line[1]), int(line[2]), int(line[3]), int(line[4])))
      #appending rectangle allocated spaces to be subtracted from
      employeeOfficeAllocated.append(Rectangle(int(line[1]), int(line[2]), int(line[3]), int(line[4])).area())

    #subtracting all desired rectangle spaces from total office area
    for employeeSpaces in employeeOffices:
      unallocated -= employeeSpaces.area()

    #doing pair-wise comparisons of the employees to determine overlapping
    for number in range(len(employeeOffices) - 1):
      
      index = number + 1
      for employee in range(len(employeeOffices)-1 - number):
        currentContested = 0
        currentContested = employeeOffices[number].rectangle_overlap(employeeOffices[index])
        #any contested areas will be accumulated in contested
        contested += currentContested

        #contested overlapping area must be subtracted from of both employee office areas
        employeeOfficeAllocated[number] -= currentContested
        employeeOfficeAllocated[index] -= currentContested

        #must add back in contested area to make sure the overlapping areas aren't counted for twice
        #when determining unallocated spaces
        unallocated += currentContested
        #print(employees[number], "tested against:", employees[index], "; contested space:", currentContested)
        index += 1

    #if all area is occupied with no contested spaces
    #must make sure unallocated is not a negative value
    if unallocated > 0:    
      print("Unallocated", unallocated)
    else:
      print("Unallocated", 0)
    
    print("Contested", contested)

    #printing employee names and their allocated areas
    for employee in range(len(employeeOffices)):
      print(employees[employee], employeeOfficeAllocated[employee])

    #reading next line to continue file-reading loop
    line = inf.readline().split()

    #will stop reading file if the next line contains nothing after whitespace is removed
    if line == []:
      break
    else:
      print()

  inf.close()
  
  
if __name__ == "__main__":
  main()
