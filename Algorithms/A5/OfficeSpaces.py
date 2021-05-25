#  File: OfficeSpace.py 

#  Description: Assignment 5, Generates office spaces and overlapping offices for employees

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 02/13/2019

#  Date Last Modified: 02/15/2019



#define details of company, size of areas, number of employees, and specified areas of office
def company(office_size, employeeNum, measurements):

   #index, first 2 digits are width and height
   w = office_size[0]
   h = office_size[1]

   #creating office space with 0s in a list
   area = [[0 for i in range(h)] for j in range(w)]

   # set employee's room areas to 0 initially for the number of employees
   employeeRoomSize = [0 for i in range(employeeNum)]

   for index in range(employeeNum):
       #1st number per line is employee name
       name = measurements[index][0]
       
       #setting points/spaces for each employee in the office space
       x1 = measurements[index][1]
       y1 = measurements[index][2]
       x2 = measurements[index][3]
       y2 = measurements[index][4]
       
       #for the distance between x and distance between y, add 1 to
       #the given x,y position in the office space
       for x in range(x1, x2):
           for y in range(y1, y2):
               area[x][y] += 1
               
   #to find total area of the building, set unallocated and contested to 0 as accumulators
   totalArea = w*h
   Unallocated = 0
   Contested = 0
   
   #creating ranges depending on height and width, for each space in matrix replace 0s dependent on
   #how long width and height are
   for x in range(w):
       for y in range(h):

           #if no employee in that area, will be unallocated
           if area[x][y] == 0:
               Unallocated += 1

           #if multiple employees in an area, points at the given list index will be greater than 1
           #thus its contested
           elif area[x][y] > 1:
               Contested += 1
           else:

               #checking allocated area for each employee
               for employee in range(employeeNum):
                   x1 = measurements[employee][1]
                   y1 = measurements[employee][2]
                   x2 = measurements[employee][3]
                   y2 = measurements[employee][4]
                   if x1 <= x and x < x2 and y1 <= y and y < y2 :
                       #if in the range of the employee there is a place which is is occupied by only one employee then it's to that employee
                       employeeRoomSize[employee] += 1
                       
   #printing employee names and their allocated areas 
   print("Total", totalArea)
   print("Unallocated", Unallocated)
   print("Contested", Contested)
   for index in range(employeeNum):
       print(measurements[index][0], employeeRoomSize[index])
   print()


def main():
   
   #open file
   office = []
   file =  open("office.txt", "r")
   for line in file:
       #print(line.split())
       if line.split() == []:
           break
       else:
           for word in line.split():
               office.append(word)
               
   #setting a indexing counter
   i = 0
   n = len(office)

   #while i less than length of office, simulate all office spaces
   while i < n:

      #getting total dimensions of office
      buildingSize = [int(office[i]), int(office[i+1])]
      i += 2

      #getting total employees per office
      employeeNum = int(office[i])
      i += 1

      #each employee and according office space dimensions will be a list element within a list
      measurements = []
      for x in range(employeeNum):
          measurements.append([(office[i]), int(office[i+1]), int(office[i+2]), int(office[i+3]), int(office[i+4])])
          i += 5
      # call company function
      company(buildingSize, employeeNum, measurements)

   file.close()

main()


