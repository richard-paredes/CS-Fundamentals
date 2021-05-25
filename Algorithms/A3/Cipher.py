#  File: Cipher.py

#  Description: Assignment3, encrypts and decrypts messages

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 02/05/2019

#  Date Last Modified: 02/07/2019

# takes a string and returns the encrypted string
def encrypt ( strng ):
    
    #extracting dimensions from nearest square
    dimensions = int(findNearestSquare(len(strng)) ** (1/2))

    #generating padded list
    lst = [["*" for i in range(dimensions)] for j in range(dimensions)]

    #replacing padded * with characters of strng
    rowIndex = 0
    colIndex = 0
    strIndex = 0
    for i in range(len(strng)):
        lst[rowIndex][colIndex] = strng[i]
        colIndex += 1
        if colIndex == dimensions:
            colIndex -= dimensions
            rowIndex += 1
        if rowIndex == dimensions:
            rowIndex -= dimensions

    #generating empty list for transposition of elements
    transposedList = [["" for i in range(dimensions)] for j in range(dimensions)]
    #transposing original list    
    for row in range(len(lst)):
        for col in range(len(lst)):
            transposedList[col][-1*row - 1] = lst[row][col]

    #converting 2D list to 1D
    encryptList = []
    for item in transposedList:
        for subItem in item:
            encryptList.append(subItem)

    #removing asterisks and convering list to string
    encrypt = [char for char in encryptList if char != "*"]
    encryptString = "".join(encrypt)

    return encryptString

# takes an encrypted string and returns the plain text version
def decrypt ( strng ):
    #extracting nearest square and dimensions
    nearSquare = findNearestSquare(len(strng))
    dimensions = int(nearSquare ** (1/2))

    #generating empty list
    lst = [["" for i in range(dimensions)] for j in range(dimensions)]

    #padding the empty list in a backwards-transposed fashion
    rowIndex = dimensions - 1
    colIndex = 0
    for i in range(nearSquare - len(strng)):
        lst[rowIndex][colIndex] = "*"
        rowIndex -= 1
        if rowIndex == -1:
            rowIndex += dimensions
            colIndex += 1

    #entering characters of encrypted strng into list
    rowIndex = 0
    colIndex = 0
    strIndex = 0
    for row in range(dimensions):
        for col in range(dimensions):
            if lst[row][col] == "*":
                continue
            else:
                lst[row][col] = strng[strIndex]
                strIndex += 1

    #reversing the 90 degree transposition of encryption
    untransposedList = [["" for i in range(dimensions)] for j in range(dimensions)]
    for row in range(len(lst)):
        for col in range(len(lst)):
            untransposedList[-1*col - 1][row] = lst[row][col]

    #converting 2D matrix to 1D
    decryptList = []
    for item in untransposedList:
        for subitem in item:
            decryptList.append(subitem)

    #removing asterisks and concatenating elements into a string
    decrypt = [char for char in decryptList if char != "*"]
    decryptString = "".join(decrypt)

    return decryptString

#finds the nearest square using recursion and returns that number
def findNearestSquare( lenMessage ):

    #tests if the square root of a given number
    #and its int form are equivalent, if not increment
    if lenMessage ** (1/2) != int(lenMessage ** (1/2)):
        lenMessage += 1
        lenMessage = findNearestSquare(lenMessage)
    return lenMessage

def main():
    # open file encrypt.txt
    inFile = open("encrypt.txt", "r")
    numMessages = inFile.readline().strip()

    # printing out characters from encrypted list
    print("Encryption:")
    for i in range(int(numMessages)):
        line = inFile.readline()
        print(encrypt(line.strip()))

    inFile.close()
    print()
    
    # open file decrypt.txt
    secondFile = open("decrypt.txt", "r")
    numMessages = secondFile.readline().strip()
    
    #printing out characters from decrypted list
    print("Decryption:")
    for i in range(int(numMessages)):
        line = secondFile.readline()
        print(decrypt(line.strip()))

    secondFile.close()
    print()
    
main()
