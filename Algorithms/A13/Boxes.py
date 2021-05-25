#  File: Boxes.py

#  Description: Assignment 12, determining largest nesting boxes subset

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: Dd32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 03/21/2019

#  Date Last Modified: 03/22/2019


#determins if a single box will fit (nest) inside another
def does_fit(box1, box2):
	return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

#get all possible nesting subsets of boxes
def getSubsets(boxList, subsets, idx, allSubsets):
	if (idx == len(boxList)):
		if len(subsets) > 1:
			subsets.sort()
			allSubsets.append(subsets)
		return
	else:
		tempSubset = subsets[:]
		subsets.append(boxList[idx])
		if len(subsets) > 1:
			#compare last and second to last boxes before continuing a subset
			if does_fit(subsets[-2], subsets[-1]):
				#continue with that subset, and diverge to make other subsets
				getSubsets(boxList, subsets, idx + 1, allSubsets)
				getSubsets(boxList, tempSubset, idx + 1, allSubsets)
			else: #don't continue with that subset
				getSubsets(boxList, tempSubset, idx + 1, allSubsets)
		else: #only to get subset length up to 2
			getSubsets(boxList, subsets, idx + 1, allSubsets)
			getSubsets(boxList, tempSubset, idx + 1, allSubsets)

# #determines which subsets are all nesting
# def getNestedBoxes(subsets):
# 	nestedBoxes = [] #stores nesting subsets
# 	for subset in subsets:
# 		temp = [] #list of bools used to check if all comparisons are true 
# 		for i in range(len(subset) - 1): #pairwise comparison
# 			if does_fit(subset[i], subset[i + 1]):
# 				temp.append(True)
# 			else:
# 				temp.append(False)
# 				break #automatically quit the pairwise comparisons
# 		if False not in temp:
# 			nestedBoxes.append(subset)
# 	return nestedBoxes

#just prints out the largest subset of nesting boxes
#if applicable
def printNestedBoxes(nestedBoxes):
	#means no nested boxes were there
	if (len(nestedBoxes) == 0):
		print("No Nesting Boxes")
	#check what the greatest subset length is & print
	else:
		print("Largest Subset of Nesting Boxes")
		hi = len(nestedBoxes[0])
		for nest in nestedBoxes:
			if len(nest) == hi:
				for box in nest:
					print(box)
				print()
			else:
				break

def main():
	#open file for reading
	inFile = open("boxes1.txt", "r")
	
	#read the number of boxes
	line = inFile.readline().strip()
	numBoxes = int(line)

	#create an empty list of boxes
	boxList = []

	#read the list of boxes from the file
	for i in range(numBoxes):
		line = inFile.readline().strip()
		box = line.split()
		for j in range(len(box)):
			box[j] = int(box[j])
		box.sort()
		boxList.append(box)

	inFile.close()

	boxList.sort()

	#get applicable subsets
	allSubsets = []
	idx = 0
	getSubsets(boxList, [], idx, allSubsets)

	#sort list to prepare for nest-checking
	#allSubsets.sort() #sorting based on first element
	allSubsets.sort(key = len, reverse = True) #sorting based on length

	printNestedBoxes(allSubsets)

	# for subsets in allSubsets:
	# 	for subset in subsets:
	# 		print(subset)
	# 	print()

	# #get nesting subsets
	# nestedBoxes = getNestedBoxes(allSubsets)

	# #output result
	# printNestedBoxes(nestedBoxes)

main()
