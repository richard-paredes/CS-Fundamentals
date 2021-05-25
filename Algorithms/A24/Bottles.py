#  File: Bottles.py

#  Description: Uses dynamic programming to find greatest sum of bottle volume

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 05/04/2019

#  Date Last Modified: 05/04/2019

# determine the bottles that contribute to the greatest sum
def get_contributing(v, b_v, target):
    contributing = []
    previous = 0

    for i in b_v[::-1]:
        if (i != -1) and (i != previous - 1):
            previous = i
            contributing.append(v[i])
            # print(v[i])

    return contributing[::-1]

# this function takes as input a list v of positive integers
# it returns two lists s_v and b_v, containing the contents of
# the columns S(v) and B(v) as shown
def bottles_dp (v):
    # quick special case check
    if (len(v) == 1):
        return [v[0]], [0]


    consumed = []
    indices = []
    idx = 0
    # start from the bottom and build up
    while (idx < len(v)):
        # perform first two bottle checks
        if (len(consumed) == 0):
            # bottle one always greatest
            consumed.append(v[idx])
            indices.append(idx)
            idx += 1
            # check whether to consume from bottle 2 or not
            if (v[idx] > consumed[-1]):
                consumed.append(v[idx])
                indices.append(idx)
            else:
                consumed.append(consumed[-1])
                indices.append(-1)
            idx += 1
        else:
            # continue down remaining bottles
            # consume the bottle at current index
            if ((v[idx] + consumed[-2]) > consumed[-1]):
                consumed.append(v[idx] + consumed[-2])
                indices.append(idx)
            else: # dont consume bottle at current index
                consumed.append(consumed[-1])
                indices.append(-1)
            idx += 1

    return consumed, indices


def main():
    #create empty list of bottles
    v = []

    # open file bottles.txt for reading
    in_file = open("./bottles.txt", "r")

    # read the number of bottles
    n = int(in_file.readline().strip())
    for bottle in range(n):
        # populate the list v with bottles
        v.append(int(in_file.readline().strip()))

    # close the file
    in_file.close()

    # find the greatest sum
    s_v, b_v = bottles_dp (v)

    # print the list s_v
    print(str(s_v)[1:-1].replace(",", ""))

    # print the list b_v
    print(str(b_v)[1:-1].replace(",", ""))

    # print the greatest sum
    greatest_sum = max(s_v)
    print(greatest_sum)

    # print the bottles contributing to the largest sum
    contributing = get_contributing(v, b_v, greatest_sum)
    print((str(contributing)[1:-1]).replace(",", ""))

main()
