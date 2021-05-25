#code
# want contigous subarray
def subarrayWithGivenSum(arr, size, target):
    # time complexity = O(N^2)
    for i in range(size):
        expectedSum = target - arr[i]
        # special case check
        if (expectedSum == 0):
            print(i+1, i+1)
            return
        # quick stop if sum is too big
        elif (expectedSum < 0):
            continue

        # check through
        for j in range(i + 1, size):
            expectedSum -= arr[j]

            if (expectedSum == 0):
                print(i+1, j+1)
                return
            elif (expectedSum < 0):
                break
    #couldnt find a solution
    print(-1)
    return


def checkTriplet(nums):

    if (nums[0] + nums[1] == nums[2]):
        return True
    elif (nums[1] + nums[2] == nums[0]):
        return True
    elif (nums[2] + nums[0] == nums[1]):
        return True
    else:
        return False

# finds the triplets in each
# does not need to be contigous
def findTriplets(arr, size):

    numTriplets = 0

    # anchor the first number until we iterate through the rest of the loop
    for i in range(size - 2):
        triplet = [arr[i]]

        # anchor the second number until we iterate tthrough all third number possibilities left
        for j in range(i + 1, size - 1):
            triplet.append(arr[j])

            # go through third number possibilities
            for k in range(j + 1, size):
                triplet.append(arr[k])

                if (checkTriplet(triplet) == True):
                    numTriplets += 1

                triplet.pop()

            triplet.pop()

    if (numTriplets == 0):
        print(-1)
    else:
        print(numTriplets)

#[1 , 5, 3 , 2] ==> [1, 2, 3, 5]
#triplets: 1 + 2 = 3, no 4, so move onto next, add +1 to index check
#instead, start from very end and work backwards:
# [ 1, 2, 3, 5 ]
#   ^     ^  ~
#   j     k  i
# i remains anchored until j and k meet
# 2 + 3 = 5 (skipped one bc indexCheck = 3 // 2 -> 1 3 -> 2 5 -> )
def findTripletsSorted(arr, size):

    arr.sort() # sorting takes O(N logN)
    numTriplets = 0

    # we need to start from the end, otherwise it skips potential answers
    # [1, 2, 3, 5]
    # []
    for i in range(size - 1, -1, -1):
        # start from the beginning
        j = 0
        # start from one before last (max) element which is where i is
        k = i - 1

        # i = size - 1 - j

        while (j < k):
            # found a match, need to close the two pointers
            if (arr[j] + arr[k] == arr[i]):
                numTriplets += 1
                j += 1
                k -= 1
            # sum is too small right now, need to increase left side (smaller number)
            elif (arr[j] + arr[k] < arr[i]) :
                j += 1
            # sum is too large, need to decrease right side (larger number)
            else:
                k -= 1

    if (numTriplets == 0):
        print(-1)
    else:
        print(numTriplets)

    return

# try to find how to return the array
def kadanesAlgorithm(arr, size):

    maxSum = arr[0]
    currentSum = arr[0]

    # no need to start from beginning
    for i in range(1, size):
        # add into current sum
        currentSum += arr[i]

        # check if having added into current sum made it a bigger
        # or smaller number ( don't do anything if bigger )
        if (currentSum < arr[i]):
            currentSum = arr[i]

        # update maxSum if needed
        if (maxSum < currentSum):
            maxSum = currentSum

    print (maxSum)

    return

# sorts arrays containing only 0, 1, and 2
def sortArray(arr, size):

    zero = 0 # index of where 0s will be stored (which will be at the beginning!)
    one = 0 # this will be kind of like a partition (pivot) point, also where 1s are; needs to start with 0's index incase there arent any 0s
    two = size - 1  # index of where 2s will be stored

    for i in range(size):
        # we want to place this at the zero index
        if (arr[one] == 0):
            # want to swap these elements; don't discard
            arr[one], arr[zero] = arr[zero], arr[one]
            one += 1
            zero += 1
        # we don't need to switch this, we just need to increment our pivot point (switching would waste memory)
        elif (arr[one] == 1):
            one += 1
        # we need to switch the 2 to the two index
        else:
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1

    for i in arr:
        print(i, end = ' ')
    print()

    return

# find an element where all elements to its left are smaller
# and all elements to its right are larger
def equilibriumPoint(arr, size):

    arraySum = 0
    # get sum of the array first
    # this will be converted to the right-half sum of the array
    for i in range(size): # O(N)
        arraySum = arraySum + arr[i]

    # this will be accumulating the left-side of the equilibrium point
    leftSum = 0

    # check if the current index splits the sums evenly or not
    for i in range(size): # O(N)
        # check if left half equals to the right half
        # need to subtract arr[i] because arraySum contains its value added
        # so we need to adjust for that (equilibrium point isn't involved in the additions)
        if (leftSum == arraySum - leftSum - arr[i]):
            # answer calls for 1-indexing
            print(i + 1)
            return
        # keep going to end, can update the leftSum
        leftSum += arr[i]

    # did not find solution
    print(-1)
    return

# find increasing subsequences within an array that provides
# the largest sum between all the increasing subsequences
def maximumSumIncreasingSubsequence(arr, size):
    # will contain all the sums for every possible subsequence
    maxSums = [arr[i] for i in range(size)]

    # since maxSums contains arr[i:size], no need to start at 0
    for i in range(1, size):

        # need to examine the previous elements up to i
        # check if these elements are increasing, and if they are, then they are part of the
        # increasing subsequence
        for j in range(i):
            # if the element is increasing in value, let's add it into the subsequences' sum list
            # however, we will only decide to add into it if:
            # there is a previous
            if (arr[i] > arr[j]) and (maxSums[i] < maxSums[j] + arr[i]):
                maxSums[i] = maxSums[j] + arr[i]

    maxSum = maxSums[0]
    for i in range(size):
        if (maxSum < maxSums[i]):
            maxSum = maxSums[i]

    print(maxSum)
    return

def arrayLeaders():

    return

def mergeSortedArrays(arr1, arr2, size1, size2):

    mergedArray = []

    arr1Pointer = 0
    arr2Pointer = 0

    while (arr1Pointer < size1) and (arr2Pointer < size2):

        if (arr1[arr1Pointer] < arr2[arr2Pointer]):
            mergedArray.append(arr1[arr1Pointer])
            arr1Pointer += 1
        else:
            mergedArray.append(arr2[arr2Pointer])
            arr2Pointer += 1

    while (arr1Pointer < size1):
        mergedArray.append(arr1[arr1Pointer])
        arr1Pointer += 1
    while (arr2Pointer < size2):
        mergedArray.append(arr2[arr2Pointer])
        arr2Pointer += 1

    for i in mergedArray:
        print(i, end = ' ')
    print()

    return


def main():

    testcases = int(input())

    # driver code for subarray with given sum
    # for i in range(testcases):

    #     nums = input().split()

    #     size = int(nums[0])
    #     target = int(nums[1])

    #     arr = input().split()

    #     for i in range(size):
    #         arr[i] = int(arr[i])

    #     subarrayWithGivenSum(arr, size, target)

    # driver code for find triplets


    for i in range(testcases):
        size = int(input())

        arr = input().split()

        for i in range(size):
            arr[i] = int(arr[i])

        findTriplets(arr, size)


