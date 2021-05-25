def bottles_dp (v):
    s_v = []
    b_v = []
    ls = []
    total, prev = 0, 0
    i = 0
    for volume in v:
        total2 = total
        volume = int(volume)
        prev, total = total, max(total, prev + volume)
        s_v.append(total)

        if total2 != total :
            b_v.append(i)
        else:
            b_v.append("-1")
        i+=1

    temp = 0
    for i in range(len(b_v)-1,-1,-1):
        if b_v[i] != "-1":
            if temp - i != 1:
              ls.append(v[i])
              temp = i
    ls.reverse()
    print("ls:",ls)
    print("List s_v =", s_v)
    print("List b_v =",b_v)
    #print("Bottles contributing to the largest sum:",ls)
    print()
    return total



def main():
    # create empty list of bottles
    v = []

    # open file bottles.txt for reading
    in_file = open ("./bottles1.txt", "r")

    # read the number of bottles
    bottle_num = in_file.readline()
    #test bottle numbers
    #print(bottle_num)

    # populate the list v with bottles
    with open('bottles1.txt') as temp_file:
        v = [line.rstrip('\n') for line in temp_file]
    del v[0]

    #test bottles list
    #print(v)


    # close the file
    in_file.close()

    # find the greatest sum
    #s_v, b_v = bottles_dp (v)

    # print the list s_v

    # print the list b_v


    # print the greatest sum

    print("Greatest sum =",(bottles_dp(v)))

    # print the bottles contributing to the largest sum

main()
