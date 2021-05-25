#  File: Triangle.py

#  Description: Assignment 16, testing algorithms for max path sum of a triangle

#  Student's Name: Richard Paredes

#  Student's UT EID: ROP242

#  Course Name: CS 313E 

#  Unique Number: 50730

#  Date Created: 04/06/2019

#  Date Last Modified: 04/06/2019

from timeit import timeit

# finds subsets of all the possible routes for a given triangle
def getRoutes(grid, allRoutes, route = 0, startCol = 0, rowIdx = 0):
  if (rowIdx >= len(grid)):
    # found a route sum, so it appends the value
    allRoutes.append(route)

  else:
    # just selects the first element at the top, since there's no choice
    if (len(grid[rowIdx]) == 1):
      route = grid[rowIdx][0]
      getRoutes(grid, allRoutes, route, 0, rowIdx + 1)

    else:
      # chooses between potential paths and diverges
      for i in range(startCol, startCol + 1):

        # colIdx used to prevent from testing numbers outside of adjacent values
        route1 = route + grid[rowIdx][i]
        getRoutes(grid, allRoutes, route1, startCol, rowIdx + 1)

        route2 = route + grid[rowIdx][i + 1]
        getRoutes(grid, allRoutes, route2, startCol + 1, rowIdx + 1)


# returns the greatest path sum using exhaustive search
def brute_force (grid):

  # get all routes
  allRoutes = []
  getRoutes(grid, allRoutes)
    
  return max(allRoutes)

# returns the greatest path sum using greedy approach
def greedy (grid):

  colIdx = 0
  # just starts with the first element, since that's the only choice
  greedyRoute = grid[0][colIdx]

  # traversing through the grid, finding only the max adjacent values
  for i in range(1, len(grid)):
    route = grid[i][colIdx]
    # selecting greedy route
    if (grid[i][colIdx + 1] > grid[i][colIdx]):
      route = grid[i][colIdx + 1]
      colIdx += 1

    greedyRoute += route

  return greedyRoute

# divides the problem into sub-triangles
def getTriangles(grid, rowIdx = 0, colIdx = 0):
  # sub triangle is reached, returns whichever sum is better 
  # for that sub triangle
  if (rowIdx == len(grid) - 1):

    route1 = grid[rowIdx][colIdx]
    route2 = grid[rowIdx][colIdx + 1]

    maxRoute = max(route1, route2)

    return maxRoute

  else:
    # answer base case
    if (len(grid[rowIdx]) == 1):
      return grid[rowIdx][0] + getTriangles(grid, rowIdx + 1, 0)

    else:

      # going through possible sub-triangle paths until reaches the base sub-triangle case
      for i in range(colIdx, colIdx + 1):

        tri1 = grid[rowIdx][colIdx] + getTriangles(grid, rowIdx + 1, colIdx)
        tri2 = grid[rowIdx][colIdx + 1] + getTriangles(grid, rowIdx + 1, colIdx + 1)

        maxTri = max(tri1, tri2)

        return maxTri


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  # just calls it's recursive helper function
  return getTriangles(grid)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  # starting with values at the last row
  routes = [grid[len(grid)-1][i] for i in range(len(grid[len(grid)-1]))]

  # traversing the grid bottom-up
  for row in range(len(grid) - 1, 0, -1):

    # dummy list for the current routes
    current = []
    # traversing the columns in each row
    for j in range(len(grid[row]) - 1):

      route1 = grid[row - 1][j] + routes[j]
      route2 = grid[row - 1][j] + routes[j + 1]

      betterRoute = max(route1, route2)

      # choosing to append only the better path
      current.append(betterRoute)

    # resetting the values 
    routes = current[:]

  # list of routes only contains the best route now
  return routes[0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  inf = open("triangle.txt")
  grid = []
  numRows = int(inf.readline())
  
  # going through file lines
  for i in range(numRows):
    row = inf.readline().strip().split()

    # converting string numbers to ints
    for j in range(len(row)):
      row[j] = int(row[j])
    
    grid.append(row)

  inf.close()

  return grid

def main ():
  # read triangular grid from file
  grid = read_file()

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is " + str(brute_force(grid)) + ".")
  print("The time taken for exhaustive search is " + str(times) + " seconds.\n")

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is " + str(greedy(grid)) + ".")
  print("The time taken for greedy approach is " + str(times) + " seconds.\n")

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is " + str(divide_conquer(grid)) + ".")
  print("The time taken for recursive search is " + str(times) + " seconds.\n")

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through dynamic programming is " + str(dynamic_prog(grid)) + ".")
  print("The time taken for dynamic programming is " + str(times) + " seconds.\n")

if __name__ == "__main__":
  main()