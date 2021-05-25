def permuteQ1(remaining, permutation, allPerms):
	if (len(remaining) == 0) and isValid(permutation):
		allPerms.append(permutation[:])
	else:
		if not isValid(permutation):
			return
		for i in range(len(remaining)):
			temp = remaining[:]
			temp.pop(i)
			permutation.append(remaining[i])
			permuteQ1(temp, permutation, allPerms)
			permutation.remove(remaining[i])

def isValid(permutation):
	lst = ['A', 'B', 'C', 'D']
	for i in range(len(permutation)):
		if permutation[i] == lst[i]:
			return False

	return True
def q1(lst):
	temp = []
	wrongEnvelopes = []
	permuteQ1(lst, temp, wrongEnvelopes)
	print(len(wrongEnvelopes), "number of ways to put the letters in the wrong envelopes:\n")
	for envelopes in wrongEnvelopes:
		print(envelopes)


def permuteQ2(remaining, permutation, allPerms):
	if (len(remaining) == 0):
		if permutation not in allPerms:
			allPerms.append(permutation[:])
	else:
		for i in remaining:
			temp = remaining[:]
			temp.remove(i)
			permutation.append(i)
			permuteQ2(temp, permutation, allPerms)
			permutation.remove(i)

def isValidShelf(subset, lst):
	if len(subset) != len(lst):
		return False
	# copy = subset[:]
	for i in range(len(subset)-1):
		for bookPairs in subset[i+1:]:
			#need to check individual books to see
			if subset[i][0] in bookPairs:
					# print(subset[i][0], "in", subset[i+1:])
				return False
	return True


def subsetQ2(lst, subset, idx, allSubsets, compare):
	if idx == len(lst):
		if isValidShelf(subset, compare):
			allSubsets.append(subset[:])
	else:
		temp = subset[:]
		temp.append(lst[idx])
		subsetQ2(lst, temp, idx + 1, allSubsets, compare) or subsetQ2(lst, subset, idx + 1, allSubsets, compare)


def q2(lst):
	books = []
	for i in lst:
		book = i.split()
		books.append(book)

	shelf = []
	temp = books[:]
	temp.pop(0)
	book = 0

	while book < len(books):
		sameAuthors = [books[book]]
		idx = book
		for j in temp:
			if books[idx][-1] == j[-1]:
				sameAuthors.append(j)
				temp.remove(j)
				book +=1
		if (len(temp) > 0):
			temp.pop(0)
		book += 1
		shelf.append(sameAuthors)

	for i in shelf:
		print(i)

	print()

	newShelf = []
	for bookPair in shelf:
		newBook = []
		for book in bookPair:
			string = ' '.join(book)
			newBook.append(string)
		newShelf.append(newBook)

	print(newShelf)
	print()

	orderedShelf = []
	for book in newShelf:
		permuteQ2(book, [], orderedShelf)

	# orderedShelf = newShelf[:]
	# permuteQ2(book, [], orderedShelf)


	allSubsets = []
	subsetQ2(orderedShelf, [], 0, allSubsets, newShelf)

	for i in allSubsets:
		print(i)
	
	allPossibleShelves = []
	for books in allSubsets:
		permuteQ2(books, [], allPossibleShelves)

	allPossibleShelves.sort()
	print(len(allPossibleShelves), "different ways to arrange the shelf", "\n")
	for shelf in allPossibleShelves:
		for order in shelf:
			for book in order:
				print("-", book)
		print()
		# print(shelf ,"\n")


	# allPairs = []
	# # temp = []
	# for bookPair in shelf:
	# 	permuteQ2(bookPair, [], allPairs)

	# for bookPair in allPairs:


def permuteq3(remaining, lst, allPerms):
	if (len(remaining) == 0):
		if goodSitting(lst):
			allPerms.append(lst[:])
	else:
		for i in remaining:
			temp = remaining[:]
			temp.remove(i)
			lst.append(i)
			permuteq3(temp, lst, allPerms)
			lst.remove(i)

def goodSitting(permutation):
	check1 = False
	# print(permutation.index('A'), permutation.index('B'), end = ' ')
	if (permutation.index('A') == permutation.index('B') + 1) or (permutation.index('A') == permutation.index('B') - 1):
		# print(permutation, 'has A and B sitting next to each other')
		check1 = True

	check2 = False
	if (permutation.index('C') != permutation.index('D') + 1) and (permutation.index('C') != permutation.index('D') - 1):
		# print(permutation, 'has C and D sitting next to each other')
		check2= True

	return check1 and check2


def q3(lst):
	allSittings = []
	temp = []
	permuteq3(lst, temp, allSittings)

	print(len(allSittings), "number of ways to arrange seatings:\n")
	for i in allSittings:
		print(i)

def meetsHomeOwner(subset):
	if len(subset) > 3 or len(subset) < 3:
		return False
	# check2 = False
	if 'A' in subset:
		if 'B' not in subset:
			return False
	if 'C' in subset:
		if 'D' in subset:
			return False
	return True


def subsetq4(lst, subset, idx, allSubs):
	if idx == len(lst):
		if meetsHomeOwner(subset):
			allSubs.append(subset[:])
		return
	elif len(subset) > 3:
		# print(subset)
		return
	else:
		a = subset[:]
		a.append(lst[idx])
		subsetq4(lst, subset, idx + 1, allSubs) or subsetq4(lst, a, idx + 1, allSubs)

def q4(lst):
	homeOwners = []
	temp = []
	subsetq4(lst, temp, 0, homeOwners)
	print(len(homeOwners), "different combinations of home owner groups:\n")
	for i in homeOwners:
		print(i)

def addsUp(subset):
	return (sum(subset) == 17)

def subsetq5(lst, subset, idx, allSubs):
	if idx == len(lst):
		if addsUp(subset):
			allSubs.append(subset[:])
		# print(subset, ' = ', sum(subset))
		return
	else:
		a = subset[:]
		a.append(lst[idx])
		subsetq5(lst, subset, idx + 1, allSubs) or subsetq5(lst, a, idx + 1, allSubs)


def q5(lst):
	sums = []
	temp = []
	subsetq5(lst, temp, 0, sums)
	print(len(sums), 'number of sums that add to 50:\n')
	for i in sums:
		print(i)

def getNum():
  num = -1
  while num < 0:
    num = input("Enter the number of stairs: ")
    #tries to convert input to integer if possible
    while True: 
      try:
        num = int(num)
        break
      except ValueError:
        num = input("Enter the number of stairs: ")
  return num

def getSteps():
  num = -1
  while num < 0:
    num = input("Enter the number of steps in this staircase: ")
    #tries to convert input to integer if possible
    while True: 
      try:
        num = int(num)
        break
      except ValueError:
        num = input("Enter the number of steps in this staircase: ")
  return num

def stepPerm(n):
	if n <= 0:
		return n
	elif n == 1:
		return n
	elif n == 2:
		return n
	elif n == 3:
		return n + 1
	return stepPerm(n-1) + stepPerm(n-2) + stepPerm(n-3)

def q6():

	x = getNum()
	for i in range(x):
		n = getSteps()
		ans = stepPerm(n)
		print(ans)

def sort(a):
	for i in range(len(a) - 1):
		minNum = a[i]
		minIdx = i
		for j in range(i+1, len(a)):
			if (a[j][0] < minNum[0]):
				minNum = a[j]
				minIdx = j
		a[minIdx] = a[i]
		a[i] = minNum

#merge times that collapse
def merge(a):
	length = len(a)
	j = 0

	new = []

	while j < len(a) - 1:
		time = []
		#ending time of current item goes int start time
		#of next item
		if a[j][1] >= a[j+1][0]:
			#append start time
			time.append(a[j][0])
			if a[j][1] > a[j+1][1]:
				time.append(a[j][1])
			else:
				time.append(a[j+1][1])
			a.pop(j+1)
		if len(time) > 0:
			new.append(time)
		else:
			new.append(a[j])
		j += 1

	return new


	

def q7(intervals):

	length = len(intervals)
	mergedIntervals = intervals[:]
	print(mergedIntervals)
	sort(mergedIntervals)
	print(mergedIntervals)
	merged = merge(mergedIntervals)

	print(merged)



# def validDiag(lst):
# 	lst = get2DList(lst)
# 	diag1Total = 0
# 	diag2Total = 0

# 	for row in range(len(lst)):
# 		for col in range(len(lst)):
# 			if row == col:
# 				diag1Total += lst[row][col]
# 			elif row == (len(lst) - col):
# 				diag2Total += lst[row][col]
	
# 	return (diag1Total == magicNum) and (diag2Total == magicNum)


# def subsets2(lst, subset, idx, allSubsets):

# 	if (idx == len(lst)):
# 		if (len(subset) == dimension) and checSubset(subset) and checkCol(subset) and checkDiag(subset):
# 			print(subset)
# 			allSubsets.append(subset)
# 		return
# 	else:
# 		# if numbers of lst[idx] are in subset, want to not append it.
# 		if (len(subset) < dimension):
# 			if checkSubset(subset):
# 				temp = subset[:]
# 				subset.append(lst[idx])
# 				subsets2(lst, subset, idx + 1, allSubsets)
# 				subsets2(lst, temp, idx + 1, allSubsets)
# 			else:
# 				return
# 		elif (len(subset) > dimension):
# 			return
# 		else:
# 			temp = subset[:]
# 			subset.append(lst[idx])
# 			subsets2(lst, subset, idx + 1, allSubsets)
# 			subsets2(lst, temp, idx + 1, allSubsets)

# def subsets(lst, subset, idx, size, allSubsets):
# 	if (idx == len(lst) and len(subset) == size):
# 		allSubsets.append(subset)
# 		print(subset)
# 		return
# 	# elif (len(subset) > dimension - size):
# 	# 	return
# 	else:
# 		temp = subset[:]
# 		subset.append(lst[idx])
# 		subsets(lst, subset, idx + 1, size, allSubsets)
# 		subsets(lst, temp, idx + 1, size, allSubsets)

# def checkSubset(currentSubset):
# 	# print("Checking subset of: ", currentSubset)

# 	for subsetIdx in range(len(currentSubset)):
# 		# print("Looking at current subset of: ", currentSubset[subsetIdx])
# 		#should also equal dimensions
# 		for num in currentSubset[subsetIdx]:
# 			for setComparedIdx in range(subsetIdx):
# 				# print("Checking if:", num, "is within", currentSubset[setComparedIdx])
# 				if num in currentSubset[setComparedIdx]:
# 					# print("failed check")
# 					return False
# 	return True


# def backtrackPermute2(lst, currentLength, permutation, square):
# 	if (currentLength == len(lst)):
# 		square += permutation
# 		# if checkDiagonal(permutation):
# 		print(square)
# 		return
# 	else:
# 		for i in lst:
# 			if i not in permutation:
# 				if validCol(permutation + [i], (len(permutation + [i]) % dimension)):
# 					permutation.append(i)
# 					print("partial solution to add to square: ", square, " + ", permutation)
# 					backtrackPermute2(lst, currentLength + 1, permutation)
# 					permutation.remove(i)
# 		return


# def finishPermutation(lst, permutation):
# 	nums = []
# 	for num in lst:
# 		if num not in permutation:
# 			nums.append(num)
# 	print(nums, permutation)
# 	perm = []
# 	backtrackPermute2(nums, 0, perm, permutation)
# 	# permute(nums, temp, permofNums)
# 	# for perm in permofNums:
# 	# 	permutation += perm
# 	# 	if checkCol(permutation):
# 	# 		print(permutation)
# 	# 	else:
# 	# 		permutation = [i for i in permutation if i not in perm]

# def validCol(lst, colIdx):
# 	total = 0
# 	for idx in range(len(lst)):
# 		if (idx - colIdx) % 4 == 0:
# 			total += lst[idx]
# 	return total == magicNum

# def validSingleCol(lst, colIdx):
# 	total = 0
# 	# print()
# 	# print(len(lst), lst)
# 	# print("checking column of", colIdx)
# 	for idx in range(len(lst)):
# 		if (idx - colIdx) % 4 == 0:
# 			# print(lst[idx], end = ' ')
# 			total += lst[idx]
# 	# print(", total is: ", total)
# 	# print()
	# return total == magicNum

# def validSingleCols(lst, colIdx):
# 	total = 0
# 	print()
# 	print(len(lst), lst)
# 	print("checking column of", colIdx)
# 	for idx in range(len(lst)):
# 		if (idx - colIdx) % 4 == 0:
# 			print(lst[idx], end = ' ')
# 			total += lst[idx]
# 	print(", total is: ", total)
# 	print()
# 	return total == magicNum



# def permute(a, currentIdx, maxIdx, allPermutations):
# 	if (currentIdx == maxIdx):
# 		#print(a)
# 		allPermutations += [[i for i in a]]
# 		return
# 	else:
# 		for i in range(currentIdx, maxIdx):
# 			a[i], a[currentIdx] = a[currentIdx], a[i]
# 			permute(a, currentIdx + 1, maxIdx, allPermutations)
# 			a[i], a[currentIdx] = a[currentIdx], a[i]

# def getMagicSquares(numbers):

# 	numSubsets = [] #all subsets
# 	tempsubset = []
# 	getSubsets(numbers, tempsubset, 0, numSubsets)
# 	# for i in numSubsets:
# 	# 	print("\n", i, "sum is:", sum(i), "\n")

# 	# print(len(numSubsets))

# 	setOfSubsets = []
# 	tempsubset = []
# 	subsets(numSubsets, tempsubset, 0, setOfSubsets)

# 	print(len(setOfSubsets))
# 	# square, needs to be rearranged
# 	singleSquareSubsets = []
# 	for subset in setOfSubsets:
# 		rowPermutations = []
# 		for subSubset in subset:
# 			permute(subSubset, 0, len(subSubset), rowPermutations)

# 		tempsubset = []
# 		subsets2(rowPermutations, tempsubset, 0, singleSquareSubsets)

def main():
	# lst1 = ['A', 'B', 'C', 'D']
	# q1(lst1)
	# print()

	# lst2 = ['War and Peace by Leo Tolstoy', 'Anna Karenina by Leo Tolstoy', 'Magic Mountain by Thomas Mann', 'Death in Venice by Thomas Mann', 'Arms and the Man by Bernard Shaw', 'Candida by Bernard Shaw']
	# q2(lst2)
	# print()

	# lst3 = ['A', 'B', 'C', 'D', 'E']
	# q3(lst3)
	# print()

	# lst4 = ['A', 'B', 'C', 'D', 'E', 'F']
	# q4(lst4)
	# print()

	lst5 = [3, 3, 9, 8, 4, 5, 7, 10]
	# lst5 = [15, 9, 30, 21, 19, 3, 12, 6, 25, 27]
	q5(lst5)
	print()

	# q6()

	# lst7 = [ [4,5], [1, 4]]
	# q7(lst7)

main()