#  File: TestLinkedList.py

#  Description: Develops linked list class and useful functions

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 04/11/2019

#  Date Last Modified: 04/12/2019

class Link (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList (object):
    def __init__(self):
        self.first = None
        self.last = None
        self.numLinks = 0

    # # get number of links 
    # def get_num_links (self):
    #     return self.numLinks
  
    # # add an item at the beginning of the list
    # def insert_first (self, data):
    #     new_link = Link (data)

    #     #check if linked list is empty
    #     if (self.first == None):
    #         self.first = new_link
    #         self.last = new_link
    #         self.numLinks += 1
    #     else: #re-establish links 
    #         new_link.next = self.first
    #         self.first = new_link
    #         self.numLinks += 1

    # add an item at the end of a list
    def insert (self, data): 
        new_link = Link (data)

        #linked list is empty
        if (self.first == None):
            self.first = new_link
            self.last = new_link
            self.numLinks += 1
        else: #inserting at end and connecting link
            self.last.next = new_link
            self.last = new_link
            self.numLinks += 1

    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
        new_link = Link (data)
        # check if linked list is empty
        if (self.first == None):
            self.insert_last(data)
            return

        #if not empty, insert in order
        current = self.first
        #special case: should go in the first node
        if (current.data > data):
            self.insert_first(data)
            return
        #iterates through linked list
        while ((current.data < data) and (current.next != None)):
            current = current.next

        new_link.next = current.next
        current.next = new_link
        self.numLinks += 1

    # search in an unordered list, return None if not found
    def find_unordered (self, data):
        current = self.first
        #special case of empty list
        if (current == None):
            return None
        #searches until end of list
        while (current.data != data):
            if (current.next == None):
                return None
            current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        current = self.first
        #special case of empty list
        if (current == None):
            return None
        #searches until finds data
        while (current.data != data):
            if (current.next == None):
                return None
            if (current.next.data != data and data < current.next.data):
                return None
            current = current.next

        return current
        #not sure, probs a binary search? but how with links...

    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        previous = self.first
        current = self.first

        if (self.numLinks == 0):
            return None
        #iterates through nodes until data is found
        while (current.data != data):
            if (current.next == None):
                return None
            previous = current
            current = current.next

        #deleting the node and re-establishing links
        if (current == self.first):
            self.first = self.first.next
            self.numLinks -= 1
        else:
            previous.next = current.next
            self.numLinks -= 1

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first
        count = 0
        #makes and returns a string of the node data
        ll = ''
        #iterates through the linked list
        while (count < 10 and current != None):
            ll += str(current.data) + "  "
            count += 1
            current = current.next
            #ensures only ten data per line
            if (count >= 10):
                count = 0
                ll += "\n"
        return ll

    # Copy the contents of a list and return new list
    def copy_list (self):
        newLinkedList = LinkedList()
        #just makes a new linked list and appends nodes to the end
        current = self.first
        while (current != None):
            newLinkedList.insert_last(current.data)
            current = current.next

        return newLinkedList

    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        newLinkedList = LinkedList()
        #inserts elements to the beginning 
        current = self.first
        while (current != None):
            newLinkedList.insert_first(current.data)
            current = current.next

        return newLinkedList

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        sortedLinks = []
        current = self.first

        #makes a list of the nodes' data
        while (current != None):
            sortedLinks.append(current.data)
            current = current.next

        #sorts the node data
        sortedLinks.sort()
        #appends the data into a linked list
        sortedLinkedList = LinkedList()
        for data in sortedLinks:
            sortedLinkedList.insert_last(data)

        return sortedLinkedList


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current = self.first
        ahead = self.first

        if (self.numLinks == 0):
            return True

        #check that the data is greater than the preceding data
        while (ahead.next != None):
            current = ahead
            ahead = ahead.next
            if (current.data > ahead.data):
                return False

        return True



    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return (self.numLinks == 0)

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        if ((not self.is_sorted()) or (not other.is_sorted())):
            return None

        selfCurrent = self.first
        otherCurrent = other.first

        mergedLinkedList = LinkedList()
        #adds items into the list, putting the lesser node first
        #until one of the linked list is emptied
        while (selfCurrent != None and otherCurrent != None):
            if (selfCurrent.data <= otherCurrent.data):
                mergedLinkedList.insert_last(selfCurrent.data)
                selfCurrent = selfCurrent.next
            else: #otherCurrent is less than selfCurrent
                mergedLinkedList.insert_last(otherCurrent.data)
                otherCurrent = otherCurrent.next

        #fill in what's left from either linkedList (only one of these should apply)
        while (selfCurrent != None):
            mergedLinkedList.insert_last(selfCurrent.data)
            selfCurrent = selfCurrent.next
        while (otherCurrent != None):
            mergedLinkedList.insert_last(otherCurrent.data)
            otherCurrent = otherCurrent.next

        return mergedLinkedList


    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        selfCurrent = self.first
        otherCurrent = other.first
        isEqual = True

        #special case of if one is empty and the other isnt
        #or one linked list has more elements than the other
        if (self.get_num_links() != other.get_num_links()):
            isEqual = False
        #check each item one at a time, if any differ then its not equal
        while ((selfCurrent != None and otherCurrent != None) and (isEqual)):
            if (selfCurrent.data != otherCurrent.data):
                isEqual = False
                break
            selfCurrent = selfCurrent.next
            otherCurrent = otherCurrent.next

        return isEqual

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        current = self.first
        noDuplicateLinkedList = LinkedList()

        while (current != None):
            # iterate through the new list to see if data already present
            if (noDuplicateLinkedList.find_unordered(current.data) == None):
                noDuplicateLinkedList.insert_last(current.data)

            current = current.next


        return noDuplicateLinkedList

def main():
     # Test methods insert_first() and __str__() by adding more than
     # 10 items to a list and printing it.
    print("inserted 1-10 backwards:")
    ll = LinkedList()
    for i in range(11):
        ll.insert_first(i)

    print(ll)
    print()

     # Test method insert_last()
    print("inserted 11-20:")
    for i in range(11, 21):
        ll.insert_last(i)
    print(ll)
    print()

     # Test method insert_in_order()
    print("inserts 15 in order")
    ll.insert_in_order(15)
    print(ll)
    print()

     # Test method get_num_links()
    print("number of links:")
    print(ll.get_num_links())
    print()

     # Test method find_unordered()
     # Consider two cases - data is there, data is not there
    print("searching for 5:")
    print(ll.find_unordered(5))
    print("searching for 100:")
    print(ll.find_unordered(100))
    print()

     # Test method find_ordered()
     # Consider two cases - data is there, data is not there
    sortedll = ll.sort_list()
    print(sortedll)
    print("searching ordered list for 20:")
    print("searching ordered list for 1:")
    print(sortedll.find_ordered(20))
    print(sortedll.find_ordered(1))
    print()

     # Test method delete_link()
     # Consider two cases - data is there, data is not there
    print("deleting 15 and 100 from linkedlist")
    ll.delete_link(15)
    print(ll)
    print()
    ll.delete_link(100)
    print(ll.delete_link(100))
    print(ll)
    print()

     # Test method copy_list()
    copiedll = ll.copy_list()
    print("copy:")
    print(copiedll)
    print()

     # Test method reverse_list()
    reversedll = ll.reverse_list()
    print("reversed:")
    print(reversedll)
    print()


     # Test method sort_list()
    print("sorted:")
    newll = ll.sort_list()
    print(newll)
    print()

     # Test method is_sorted()
     # Consider two cases - list is sorted, list is not sorted
    linkd = LinkedList()
    linkd.insert_last(0)
    linkd.insert_in_order(100)
    print(linkd)
    print("checking if ll is sorted:", ll.is_sorted())
    print()
    print("checking if sortedll is sorted:", linkd.is_sorted())
    print()
    print('checking if newll is sorted:', newll.is_sorted())
    print()

     # Test method is_empty()
    newl = LinkedList()
    print("Empty list is:", newl)
    print(newl.is_empty())
    print()

     # Test method merge_list()
    print('merging two lists:')
    print('merged list:')
    mergedll = sortedll.merge_list(sortedll)
    print(mergedll)
    print()

     # Test method is_equal()
     # Consider two cases - lists are equal, lists are not equal
    newml = mergedll.copy_list()
    print('checking if list1:')
    print(newml)
    print()
    print('and lst2:')
    print(mergedll)
    print()
    print('sizes:', newml.get_num_links(), mergedll.get_num_links())
    print('are equal:', mergedll.is_equal(newml))
    print()

     # Test remove_duplicates()
    nodupll = mergedll.remove_duplicates()
    print("duplicating the merged list:", "\nduplicate:\n",nodupll)
    print()
    print('checking if merged list is sorted:', mergedll.is_sorted())
    mergedll.insert_first(0)
    print(mergedll)
    print('checking if modified merged list is sorted:', mergedll.is_sorted())
    print()
    print("duplicating an empty list:")
    print("duplicate:\n", newl)
    l = newl.sort_list()
    print('checking if duplicate is sorted:', newl.is_sorted())
    print()

if __name__ == "__main__":
    main()
