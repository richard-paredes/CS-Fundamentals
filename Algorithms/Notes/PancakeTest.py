  # File: Pancake.py

  # Description: Assignment 10, Flips pancakes to have largest at bottom

  # Student's Name: Richard Paredes

  # Student's UT EID: ROP242
 
  # Partner's Name: Diana De La Torre

  # Partner's UT EID: DD32653

  # Course Name: CS 313E 

  # Unique Number: 50730

  # Date Created: 03/06/2019

  # Date Last Modified: 03/07/2019

#performs a single pancake flip, returns the flip index
#as well as the new list
def flip(stack):
  flipIndex = stack.index(max(stack))
  # print("incoming: ", stack)
  if flipIndex == 0:
    #print("left edge case")
    newStack = [num for num in stack]
    newStack.reverse()
    flipIndex = 1

  elif flipIndex == len(stack)-1:
    #print("right edge case")
    newStack = [num for num in stack]
    flipIndex = -1 # no flip was done

  else: #not edge case
    newStack = stack[:flipIndex+1]
    newStack.reverse()
    newStack += stack[flipIndex+1:]
    flipIndex = len(stack) - flipIndex

  # print("output: ",  newStack, "flipped at index: ", flipIndex)

  return newStack, flipIndex


#remember: bottom (last item is index of 1)
#continues to flip pancakes until they are sorted
#will slice off one element at a time
def sortPancakes(pancakes):
  i = len(pancakes)
  sortedPancakes = sorted(pancakes)
    #until it's sorted, flip
  while pancakes != sortedPancakes:
    # print("\ncurrent pancakes: ", pancakes)
    temp = pancakes[i:]
    pancakes, currentFlip = flip(pancakes[:i])
    pancakes += temp
    if currentFlip != -1:
      print(currentFlip + len(pancakes) - i, end = ' ')

    #until it's in the right position, flip current max
    currentMax = max(pancakes[:i])
    while pancakes.index(currentMax) != sortedPancakes.index(currentMax):
      pancakes, currentFlip = (flip(pancakes[:i]))
      pancakes += temp
      if currentFlip != -1:
        print(currentFlip + len(pancakes) - i, end = ' ')
    i -= 1

  print()
  print("Finished sorting:", pancakes)

def main():

  inf = open("pancakes-1.txt", "r")
  pancakes = []

  for line in inf:
    #prints out elements
    pancakes = line.split()
   
    #does flips
    sortPancakes(pancakes)



main()

