#  File: Josephus.py

#  Description: Develops circular linked list and solves Josephus problem

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 04/14/2019

#  Date Last Modified: 04/14/2019

class Link (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList (object):
    def __init__(self):
        self.first = None
        self.last = None
        self.numLinks = 0

    # add an item at the end of a list
    def insert (self, data):
        new_link = Link (data)

        #linked list is empty
        if (self.first == None):
            self.first = new_link
            self.last = new_link
            self.last.next = new_link
            self.numLinks += 1
        else: #inserting at end and connecting link
            self.last.next = new_link
            self.last = new_link
            self.last.next = self.first
            self.numLinks += 1

    # search in an list via sequential search, return None if not found
    def find (self, data):
        current = self.first
        #special case of empty list
        if (current == None):
            return None
        #searches until end of list
        while (current.data != data):
            if (current.next == self.last.next):
                return None
            current = current.next

        return current

    # Delete and return Link from an unordered list or None if not found
    def delete (self, data):
        previous = self.first
        current = self.first

        if (self.numLinks == 0):
            return None
        #iterates through nodes until data is found
        while (current.data != data):
            if (current.next == self.last.next):
                return None
            previous = current
            current = current.next

        #deleting the node and re-establishing links
        #special case if data is first item
        if (current == self.first):
            self.first = current.next
            self.last.next = self.first
            self.numLinks -= 1
        #special case if data is last item
        elif (current == self.last):
            previous.next = self.first
            self.last = previous
            self.numLinks -= 1
        else:
            previous.next = current.next
            self.numLinks -= 1

    def delete_after (self, start, n):
        startingLink = self.find(start.data)
        for i in range(n-1):
            startingLink = startingLink.next
        print(startingLink.data)
        nextLink = startingLink.next
        self.delete(startingLink.data)
        return nextLink

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first
        count = 0
        #makes and returns a string of the node data
        ll = ''
        #iterates through the linked list
        while (count < 10):
            ll += str(current.data) + "  "
            count += 1
            current = current.next
            #ensures only ten data per line

            #will stop if it has gone around the circle once
            if (current == self.last.next):
                break
            if (count >= 10):
                count = 0
                ll += "\n"
        return ll.rstrip()

def main():

    inf = open("josephus1.txt", "r")
    numSoldiers = int(inf.readline().strip())

    soldiers = CircularList()
    for i in range(1, numSoldiers+1):
        soldiers.insert(i)

    start = int(inf.readline().strip())
    startingSoldier = soldiers.find(start)
    countRate = int(inf.readline().strip())


    while (soldiers.numLinks != 1):
        startingSoldier = soldiers.delete_after(startingSoldier, countRate)
    print(soldiers)



if __name__ == "__main__":
    main()
