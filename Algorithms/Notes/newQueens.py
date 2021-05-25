#  File: Queens.py

#  Description: Determining number of queen solutions for a given chess board

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50730 

#  Date Created: 03/31/2019

#  Date Last Modified: 03/31/2019

numSolutions = 0

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q'):
        return False
    for i in range(self.n):
      if (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  def hasEmptyCol(self):
    for i in range(self.n):
      if self.board[i][0] == 'Q':
        return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
      # print()
      # self.print_board()
      global numSolutions
      numSolutions += 1

    else:
      #ensures the board doesn't continue with an empty first column
      if col > 0 and self.hasEmptyCol():
        return
      for row in range (self.n):
        if self.is_valid(row, col):
          self.board[row][col] = 'Q'
          self.recursive_solve(col + 1)
        self.board[row][col] = '*'

          
  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      self.recursive_solve(i)
 
def getBoardSize():
  num = 0
  while (num < 2) or (num > 100):
    num = input("Enter the size of board: ")
    #tries to convert input to integer if possible
    while True: 
      try:
        num = int(num)
        break
      except ValueError:
        num = input("Enter the size of board: ")
  return num


def main():
  #getting size of board
  size = getBoardSize()
  # create a regular chess board
  game = Queens (size)

  # place the queens on the board
  game.solve()
  print("\nNumber of solutions: " + str(numSolutions))

main()


