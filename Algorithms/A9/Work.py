
#  Description: Assignment 9, Finds minimum number of lines needed to write

#  Student's Name: Richard Paredes

#  Student's UT EID: ROP242

#  Course Name: CS 313E 

#  Unique Number: 50730

#  Date Created: 03/03/2019

#  Date Last Modified: 03/03/2019

#returns a series, given a value, v, to use as numerator
def find_series(v, k):
  series = []
  value = 1 #random number to start the while loop
  p = 0 #exponent for K
  while value > 0:
    value = v//(k**p)
    series.append(value);
    p += 1

  return series

#returns mid (the value V) for which a series will sum to N.
def binary_search(n, k):
  lo = 1
  hi = n+1

  while hi >= lo:

    mid = (hi + lo)//2
    lst = find_series(mid, k)

    #if series sum is lower than N, must search with higher numbers
    if sum(lst) < n:
      lo = mid + 1
    
    #if series sum is higher than N, must search with lower numbers
    elif sum(lst) > n:
      hi = mid - 1
    
    #found a value V that sums to N in a series  
    else:
      return mid

  #could not found an exact value of V that sums to N
  #but the closest is this value
  return mid


def main():
  #open file
  inf = open("work.txt", "r")
  numLines = int(inf.readline())

  #runs through all test cases
  for i in range(numLines):
    lst = inf.readline().split()
    n = int(lst[0])
    k = int(lst[1])

    #returns smallest number, V, that sums to N
    v = binary_search(n, k)
    print(v)

main()