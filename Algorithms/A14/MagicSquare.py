#  File: MagicSquare.py

#  Description: Assignment 14, generate N magic squares of order 4

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 03/26/19

#  Date Last Modified: 03/28/19

import time
start = time.time()
dimension = 4
magicNum = int(dimension * ((dimension * dimension) + 1) / 2)
printCounter = 0

def getNum():
	num = 0
	while (num < 2) or (num > 20):
		num = input("Enter number of magic squares (2 - 20): ")
		while True:
			try:
				num = int(num)
				break
			except ValueError:
				num = input("Enter number of magic squares (2 - 20): ")
	return num

def get1DList():
	nums = [ i for i in range (1, dimension**2 + 1)]
	return nums

def permute(remaining, permutation):
	#base case of permutation
	if (len(remaining) == 0):
		# checking that last row leads to valid permutation
		if validDiag(permutation, remaining) and validRow(permutation):
			global printCounter
			print()
			for i in range(dimension):
				for j in range(dimension):
					print(format(permutation[j + (i * dimension)], "3d"), end = ' ')
				print()


			
			printCounter += 1
			if printCounter == numToPrint:
				end = time.time()
				print("Runtime", end - start)
				exit()
		return

	else:
		for i in range(len(remaining)):
			if not validRow(permutation):
				break
			if not validCol(permutation, remaining):
				break
			if not validDiag(permutation, remaining):
				break
			permutation.append(remaining[i])
			tempRemain = remaining[:]
			tempRemain.pop(i)
			permute(tempRemain, permutation)
			permutation.remove(remaining[i])
		return


def getSubsets(lst, subset, idx, size, allSubsets):
	if (idx == len(lst)):
		if (len(subset) == size):
			allSubsets.append(subset)
		return
	elif len(subset) > size:
		return
	else:
		temp = subset[:]
		subset.append(lst[idx])
		getSubsets(lst, subset, idx + 1, size, allSubsets)
		getSubsets(lst, temp, idx + 1, size, allSubsets)

def validCol(lst, remainingNums):

	if len(lst) % dimension == 0:
		rowIdx = len(lst) // dimension
	else:
		rowIdx = (len(lst) // dimension) + 1


	colTotal = getColTotal(lst)

	allNumSubsets = []
	numSets = []
	getSubsets(remainingNums, numSets, 0, dimension - rowIdx, allNumSubsets)

	for subset in allNumSubsets:
		setSum = sum(subset)
		if colTotal + setSum == magicNum:
			return True
	return False


def validDiag(lst, remainingNums):

	#waits until an entire row is filled
	if len(lst) % dimension != 0:
		return True

	if len(lst) % dimension == 0:
		rowIdx = len(lst) // dimension
	else:
		rowIdx = (len(lst) // dimension) + 1


	diag1Total = getDiagTotal1(lst)
	diag2Total = getDiagTotal2(lst)

	allNumSubsets = []
	numSets = []
	getSubsets(remainingNums, numSets, 0, dimension - rowIdx, allNumSubsets)

	#testing diag1 (upperleft start)
	diag1 = False
	for subset in allNumSubsets:
		setSum = sum(subset)
		if diag1Total + setSum == magicNum:
			diag1 = True
			break

	#testing diag2 (upper right start)
	diag2 = False
	for subset in allNumSubsets:
		setSum = sum(subset)
		if diag2Total + setSum == magicNum:
			diag2 = True
			break

	return diag1 and diag2

def getDiagTotal1(lst):
	total = 0
	numRows = len(lst) // dimension
	for row in range(numRows):
		for col in range(dimension):
			if (col + row * dimension) % dimension == row:
				#means it's at a diagonal
				total += lst[col + row * dimension]

	return total

def getDiagTotal2(lst):

	total = 0
	numRows = len(lst) // dimension
	for row in range(numRows):
		for col in range(dimension):
			if (col + row * dimension) % (dimension) == dimension - row - 1:
				total += lst[col + row * dimension]

	return total

def getColTotal(lst):

	total = 0
	colIdx = (len(lst) % dimension) - 1
	for i in range(len(lst)):
		if (i - colIdx) % dimension == 0:
			total += lst[i]

	return total


def validRow(lst):

	# number of times to loop:
	numRows = len(lst) // dimension
	for i in range(numRows):
		total = 0
		for j in range(dimension):
			total += lst[(i * dimension) + j]
		if total != magicNum:
			return False
	return True


numToPrint = getNum()

def main():

	#getting values set
	numbers = get1DList()

	permutations = []
	perm = []
	permute(numbers, perm)

main()
