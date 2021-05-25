# LISTS
'''
    - Create a list using:
        [] or list()
    
    - Lists can hold all data types 
        They are non-homogeneous
    
    - Length of list with len()

    - Lists can be concatentated, just like strings
        ls + ls2 = [ls ... ls2]

    - Lists are mutable!
    
'''
ls = [1, 2, 3, 4, 5]

# List operators:
# ITERATION
for item in ls:
    print(item)

# COMPARISON:
first = [1,2,3]
second = [1,2,3]
first == second # evaluates to True

# MANIPULATION:
test = [1,2,'A',3.1]
print(test[2]) # prints 'A'

# MUTABILITY
a = [1, 2, 3]
a[1] = 7 # a now is [1, 7, 3]
b = a
b[2] = 'A' # a and b are now [1, 7, 'A'] 

# SLICING
ls = [1, 2, 3, 4, 5]
print(ls[1:4]) # prints '2, 3, 4'

# REVERSAL
rev = ls[-1::-1]

# APPENDING AND REMOVING:
rev.append('hello') # adds item to end
rev.insert(2, 'goodbye') # adds item to the second index
rev.insert(9999,'outOfBounds') # adds item to end!
rev.insert(-1, 'atEnd?') # adds to PENULTIMATE position
rev.pop() # removes last item
rev.pop(0) # removes first item