class Queens (object):
	#initialize the chess board (2D list & positions filled with * if empty)
	def __init__(self, n = 8):
		self.board = []
		self.n = n
		for i in range(self.n):
			row = []
			for j in range(self.n):
				row.append('*')
			self.board.append(row)

	#print out the board
	def print_board(self):
		for i in range(self.n):
			for j in range(self.n):
				print(self.board[i][j], end = ' ')
			print()
		print()

	#perform checks along row, col, and diags
	def is_valid(self, row, col):
		for i in range(self.n):
			#check row and col in one loop bc it's a square matrix
			if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
				return False
		#check diags
		for i in range(self.n):
			for j in range(self.n):
				row_diff = abs(row - i)
				col_diff = abs(col - j)
				if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
					return False
		#means no queens in any direction
		return True

	#perform a recursive backtracking solution
	def recursive_solve(self, col):
		#reached end of array
		if (col == self.n):
			return True
		else:
			for i in range(self.n):
				#self.print_board()
				#print()
				if (self.is_valid(i, col)):
					#print("Placing a queen: ")
					self.board[i][col] = 'Q'
					#self.print_board()
					#print()
					#print("Checking future: ")
					if (self.recursive_solve(col + 1)):
						#self.print_board()
						#print()
						return True
					#print("backtracking! ")
					self.board[i][col] = '*'
					#self.print_board()
					#print()
		return False


	def solve(self):
		for i in range(self.n):
			if (self.recursive_solve(i)):
				self.print_board()

#asks user for a number
def getBoardSize():
	num = 0
	while (num < 1) or (num > 16):
		num = input("Enter the size of board: ")
		#tries to convert input to integer if possible
		while True: 
			try:
				num = int(num)
				break
			except ValueError:
				num = input("Enter the size of board: ")
	return num

#asks user for a number of solutions
def getNumSolutions():
	
	num = 0
	while (num < 2) or (num > 16):
		num = input("Number of solutions: ")
		#tries to convert input to integer if possible
		while True: 
			try:
				num = int(num)
				break
			except ValueError:
				num = input("Enter number of magic squares (2 - 20): ")
	return num

def main():

	size = getBoardSize()
	#create a chess board
	game = Queens(size)

	#place the Queens on the board
	game.solve()

main()
