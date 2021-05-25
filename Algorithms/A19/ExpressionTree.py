#  File: ExpressionTree.py

#  Description: A19, Generates a binary expression tree

#  Student's Name: Richard Paredes

#  Student's UT EID: ROP242

#  Partner's Name: Diana De La Torre

#  Partner's UT EID: DD32653

#  Course Name: CS 313E 

#  Unique Number: 50730

#  Date Created: 04/17/19

#  Date Last Modified: 04/18/19

class Stack (object):
	def __init__ (self):
		self.stack = []

  	# add an item to the top of the stack
	def push (self, item):
 		self.stack.append (item)

  	# remove an item from the top of the stack
	def pop (self):
	  	return self.stack.pop()

  	# check the item on top of the stack
	def peek (self):
		return self.stack[-1]

  	# check if the stack is empty
	def is_empty (self):
	 	return (len (self.stack) == 0)

  	# return the number of elements in the stack
	def size (self):
	  	return (len (self.stack))

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lChild = None
		self.rChild = None

class Tree (object):
  	def __init__ (self):
  		self.root = None
  		self.operators = ['+', '-', '*', '/', '//', '%', '**']

  	#creates the expression tree using the expression given
  	def create_tree (self, expr):
  		tokens = expr.split()
  		self.root = Node(None)
  		currentNode = self.root
  		expressionStack = Stack()

  		#iterates through all the tokens
  		#and places the nodes accordingly
  		for i in range(len(tokens)):

  			if (tokens[i] == "("):
  				newNode = Node(None)
  				currentNode.lChild = newNode
  				expressionStack.push(currentNode)
  				currentNode = currentNode.lChild

  			#operators need to be root/parent nodes in subtrees
  			elif (tokens[i] in self.operators):
  				currentNode.data = tokens[i]
  				expressionStack.push(currentNode)
  				newNode = Node(None)
  				currentNode.rChild = newNode
  				currentNode = currentNode.rChild

  			#ending an expresison
  			elif (tokens[i] == ")"):
  				if (not expressionStack.is_empty()):
  					currentNode = expressionStack.pop()

  			#means the token is a number, readjusts the value of a given node
  			else:
  				currentNode.data = tokens[i]
  				currentNode = expressionStack.pop()

  	#evaluates the binary expression tree in a pre-fix/DFS manner
  	def evaluate(self, aNode):
  		
  		#currentNode is root node, which is an operator
  		currentNode = aNode
  		
  		#special case of no expression
  		if (self.root.data == None):
  			return '0'

  		#reached the left or right most child
  		elif (currentNode.lChild == None and currentNode.rChild == None):
  			return currentNode.data

  		#branching out recursively
  		lExpression = self.evaluate(currentNode.lChild)
  		rExpression = self.evaluate(currentNode.rChild)

  		return str(eval(lExpression + currentNode.data + rExpression))

  	#reads binary expression tree in a prefix order
  	def pre_order(self, aNode):
  		# no matter what, self.root will always have at least 
  		# one node if create_tree() is called
  		if (self.root.data == None):
  			return 
  		#recursive loop
  		if (aNode != None):
  			print(aNode.data, end = ' ')
  			self.pre_order(aNode.lChild)
  			self.pre_order(aNode.rChild)

  	#reads the binary expression tree in a postfix order
  	def post_order(self, aNode):
  		#special case
  		if (self.root.data == None):
  			return 
  		#recursive loop
  		if (aNode != None):
  			self.post_order(aNode.lChild)
  			self.post_order(aNode.rChild)
  			print(aNode.data, end = ' ')


def main():
	#opening file
	inf = open("expression.txt", "r")
	for line in inf:
		expressionTree = Tree()
		expressionTree.create_tree(line)

		#printing expression and its value
		print(line.strip() + " = " + expressionTree.evaluate(expressionTree.root))
		print()

		#printing out the different orders
		print('Prefix Expression:', end = ' ')
		expressionTree.pre_order(expressionTree.root)
		print('\n')
		print('Postfix Expression:', end = ' ')
		expressionTree.post_order(expressionTree.root)
		print('\n')

	inf.close()

main()