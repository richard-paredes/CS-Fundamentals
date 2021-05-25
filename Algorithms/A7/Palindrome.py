#  Description: Assignment 7, Returns shortest palindrome

#  Student's Name: Richard Paredes

#  Student's UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E 

#  Unique Number: 50730

#  Date Created: 02/20/2019

#  Date Last Modified: 02/22/2019

def is_palindrome(word):

	#iterates through each letter, 
	#checks if it matches the opposite
	#half in its corresponding position
	#for i in range(len(word)):
	#	if word[i] != word[-(i+1)]:
	#		return False

	#means all letters reflected
	#return True

	#just checks if the word's 
	#reflection matches original
	return word == word[::-1]


def make_palindrome(newWord):


	stringLength = len(newWord)

	halfIndex = stringLength // 2

	#looks for any symmetry in word:
	#examines word if palindome is possible
	#from current letters in word	
	symmetryIndex = halfIndex
	for i in range(stringLength//2):

		#index from which reflection will occur, if any available
		#is excluded from first and second partitions of the word
		newSymmetryPoint = newWord[symmetryIndex]

		newFirst = newWord[:symmetryIndex]

		newSecond = newWord[(symmetryIndex+1):]

		#reverses the first partition of string
		newFirstReversed = newFirst[::-1]

		#if there aren't any letters within the second partition
		#that reflect in second half to extend into a palindrome
		#then decrease first partition of word and increase second
		#partition of word
		if newFirstReversed not in newSecond:
			symmetryIndex -= 1

		#if there is a reflection, continues
		#extending the word until it is the shortest
		#palindrome
		else:
			missingChars = ''
			for char in newSecond:
				if char not in newFirstReversed:
					missingChars = char + missingChars
			return missingChars + newFirst + newSymmetryPoint + newSecond

	#symmetryIndex is 0, meaning no reflections available:
	#therefore, will just reflect everything from second letter & forward
	#to before the first letter
	reflectionPoint = newWord[0]
	secondHalf = newWord[1:]
	return (secondHalf[::-1] + newWord[0] + secondHalf)


def main():
	
	inFile = open("palindrome.txt", "r")

	for line in inFile:
		if is_palindrome(line.strip()) == False:
			print(make_palindrome(line.strip()))
		else:
			print(line.strip())
		
main()
