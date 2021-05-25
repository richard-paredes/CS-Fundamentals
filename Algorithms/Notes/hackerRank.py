#return the max difference of an unsorted list, given that the higher number's index
# is greater than the lower number's index

def getMax(remaining, currentMax):
    if (len(remaining) == 1):
        return -1
    else:
        upperHalf = remaining[len(remaining)//2:]
        lowerHalf = remaining[:len(remaining)//2]

        upperMax = max(upperHalf)
        lowerMin = min(lowerHalf)

        newMax = upperMax - lowerMin
        max1 = getMax(upperHalf, newMax)
        max2 = getMax(lowerHalf, newMax)

        return max(newMax, max1, max2)



def main():
	lst = [9, 8, 7, 6, 4, 1, 5]
	maxDiff = getMax(lst, -1)
	print(maxDiff)

main()
