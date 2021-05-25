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

class Triangle(object):
	def __init__(self, p1x, p1y, p2x, p2y, p3x, p3y):
		self.p1 = Point(p1x, p1y)
		self.p2 = Point(p2x, p2y)
		self.p3 = Point(p3x, p3y)

	def isTriangle(self):
		if (self.p1.dist(self.p2) + self.p2.dist(self.p3)) > self.p1.dist(self.p3):
			return True

	def isRight(self):
		side1 = self.p1.dist(self.p2)
		side2 = self.p2.dist(self.p3)
		side3 = self.p3.dist(self.p1)

		#print("sides lengths:", side1, side2, side3)
		#print("side lengths squared:", side1**2, side2**2, side3**2)
		#print(side1**2 + side2**2 - side3**2)
		#print(side2**2 + side3**2)
		#print(side3**2 + side1**2)
		tol = 1.0e-10

		if (abs((side1**2 + side2**2) - side3**2) < tol):
			return True
		elif (abs((side2**2 + side3**2) - side1**2) < tol):
			return True
		elif (abs((side3**2 + side1**2) - side2**2) < tol):
			return True
		else:
			return False

	def area(self):
		side1 = self.p1.dist(self.p2)
		side2 = self.p2.dist(self.p3)
		side3 = self.p1.dist(self.p3)

		s = (side1 + side2 + side3)/2

		return (s*(s-side1)*(s-side2)*(s-side3))**1/2

def main():
	tri1 = Triangle(0, 0, 2, 0, 2, 2)
	print("Is tri1 a triangle?", tri1.isTriangle())
	print("Is tri1 a right triangle?", tri1.isRight())
	print("Area of tri1:", tri1.area())
main()



