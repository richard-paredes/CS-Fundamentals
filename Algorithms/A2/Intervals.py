#  File: Intervals.py

#  Description: Merges intersecting intervals and sorts them by size

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 02/03/2019

#  Date Last Modified: 02/04/2019


#takes a list and combines intersecting intervals
def intervalMerger(givenList):

    lst3 = []
    lst3.append(givenList[0])

    #taking each interval from givenList one at a time and comparing
    for currentInterval in givenList:
        lowerIntervalUpperBound = lst3[-1][1]
        currentIntervalLowerBound = currentInterval[0]

        #determining if the intervals intersect
        if lowerIntervalUpperBound >= currentIntervalLowerBound:
            
            #generating new interval
            lowerIntervalLowerBound = lst3[-1][0]
            currentIntervalUpperBound = currentInterval[1]
            
            #print("Making new interval from:", min(lowerIntervalLowerBound, currentIntervalLowerBound), max(lowerIntervalUpperBound, currentIntervalUpperBound))
            newLowerBound = min(lowerIntervalLowerBound, currentIntervalLowerBound)
            newUpperBound = max(lowerIntervalUpperBound, currentIntervalUpperBound)
            
            newInterval = (newLowerBound, newUpperBound)

            #replacing the lowerInterval with the newInterval and passing up the currentInterval
            lst3[-1] = (newInterval)

        #currentInterval does not intersect, will be inserted into lst3    
        else:
            lst3.append(currentInterval)

    return lst3

#orders the intervals by size using selection sort
def sizeOrder(lst):

        #obtaining size difference of intervals
        #the size differences index corresponds to interval index
        lst4 = []
        for tpl in lst:
            diff = tpl[1]-tpl[0]
            lst4.append(diff)

        #performing selection sort based on size differences
        #then using corresponding indexes in lst4 to list passed into function
        for num in range(len(lst4)):
            minIndex = num
            #finding smallest number's index and retaining it
            for remaining in range(minIndex+1, len(lst4)):
                if lst4[minIndex] > lst4[remaining]:
                    minIndex = remaining
                #if size is the same, will compare the lower bounds of the tuple interval
                elif lst4[minIndex] == lst4[remaining]:
                    if lst[minIndex][0] > lst[minIndex][0]:
                        minIndex = remaining

            #performs the switch of smallest number's index to current index
            lst4[num], lst4[minIndex] = lst4[minIndex], lst4[num]
            lst[num], lst[minIndex] = lst[minIndex], lst[num]


def main():

    #opening file
    inFile = open("intervals5.txt", "r")
    line = inFile.readline()
    lst = []
    
    #obtaining intervals from file & placing into list
    while line != "":
            lst.append(line.split())
            line = inFile.readline()

    lst2 = []
    #converting str items in list to integers only
    #and then placing them into list of tuples
    for row in range(len(lst)):
        for col in range(len(lst[row])):
                lst[row][col] = int(lst[row][col])
        lst2.append(tuple(lst[row]))

    #checking list of tuples to remove any empty tuples
    for item in lst2: 
        if item == ():
            lst2.remove(item)
    
    #sorting the list of tuples
    lst = sorted(lst2)

    #converging intersecting intervals
    mergedList = intervalMerger(lst)

    #ordering intervals by size
    sizeOrder(mergedList)

    #printing intervals
    for item in mergedList:
        print(item)
        
    inFile.close()
    
main()
