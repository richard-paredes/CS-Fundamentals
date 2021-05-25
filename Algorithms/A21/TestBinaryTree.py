#  File: TestBinaryTree.py

#  Description: Creates and adds functionality to a binary search tree

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 04/20/19

#  Date Last Modified: 04/25/19

# queue object to print breadth first
class Queue (object):
	# construct the queue
	def __init__ (self):
		self.queue = []

	# adds item to end of queue
	def enqueue (self, item):
		self.queue.append (item)

	# eliminates item from begining of queue
	def dequeue (self):
		return (self.queue.pop (0))

	# checks if queue is empty
	def isEmpty (self):
		return (len (self.queue) == 0)

	# returns how long the queue is
	def size (self):
		return (len (self.queue))

# node object for the BST
class Node (object):
	# constructor
	def __init__ (self, data, parent = None):
		self.data = data
		self.lChild = None
		self.rChild = None
		self.parent = parent

# binary search tree object
class Tree (object):
	# constructs the BST
	def __init__ (self):
		self.root = None
		self.numNodes = 0

	# inserts an element into the binary search
	# tree in a normal fashion (not balanced)
	def insert (self, data):
		# newNode = Node (data, self.numNodes)
		# case of an empty tree
		if (self.root == None):
			self.root = Node (data)
			self.numNodes += 1
		else:
			# finding where to place item
			current = self.root
			parent = self.root
			# traversing tree to place node
			while (current != None):
				parent = current
				if (data < current.data):
					current = current.lChild
				else:
					current = current.rChild
			# deciding if node should be left or right child
			if (data < parent.data):
				parent.lChild = Node (data, parent)
				self.numNodes += 1
			else:
				parent.rChild = Node (data, parent)
				self.numNodes += 1

	# searches for a node in the binary search tree containing
	# a key of the data
	def search (self, data):
		if (data == None):
			return None

		current = self.root
		# continuing search until either data isn't found or it is
		while (current != None) and (current.data != data):
			if (data < current.data):
				current = current.lChild
			else:
				current = current.rChild
		return current

	# finds the lowest-level node
	def get_deepest(self, aNode, edgeCounter):
		# return if it's a leaf node (no children)
		if (aNode.lChild == None) and (aNode.rChild == None):
			return edgeCounter

		left_subtree_height = edgeCounter
		right_subtree_height = edgeCounter
		# if it only has one child or both:
		if (aNode.lChild != None):
			left_subtree_height = self.get_deepest(aNode.lChild, edgeCounter + 1)
		if (aNode.rChild != None):
			right_subtree_height = self.get_deepest(aNode.rChild, edgeCounter + 1)
		# only returns whichever is deeper
		return max(left_subtree_height, right_subtree_height)

	# returns the height of the tree
	def get_height (self, aNode):
		# we're given an empty node/subtree
		if (aNode == None):
			return -1

		# need to get to the deepest node
		return self.get_deepest(aNode, 0)

	# returns the number of nodes in the left subtree and
	# the number of nodes in the right subtree and the root
	def num_nodes (self, aNode):
		numNodes = 0
		if (aNode == None):
			return 0
		# create a queue holding the nodes
		queue = Queue()
		queue.enqueue(aNode)
		while (not queue.isEmpty()):
			# add one for every node present in the subtree
			numNodes += 1
			node = queue.dequeue()
			# add children to the queue if presenet
			if (node.lChild != None):
				queue.enqueue(node.lChild)
			if (node.rChild != None):
				queue.enqueue(node.rChild)
		# no nodes left in queue
		return numNodes

	# returns the difference between the height of the left
	# sub tree and the height of the right sub tree
	def balance_factor (self, aNode):
		#potentially check if aNode is None?
		if (aNode == None):
			return 0
		#empty subtrees start with height -1
		left_subtree_height = self.get_height(aNode.lChild)

		right_subtree_height = self.get_height(aNode.rChild)

		return left_subtree_height - right_subtree_height

	# returns True if the tree is balanced and False otherwise
	# in a balanced tree, every node has a balance factor of -1, 0, 1
	def is_balanced (self, aNode):
		# an empty subtree is always balanced
		if (aNode == None):
			return True

		tree_balance_factor = self.balance_factor(aNode)
		subtree_balance = (tree_balance_factor <= 1) and (tree_balance_factor >= -1)

		# no need to continue recursion if this fails: node is unbalanced
		if (not subtree_balance):
			return False

		return self.is_balanced(aNode.lChild) and self.is_balanced(aNode.rChild)

	# performs a rotation, switching parents, children, and applicable grandchildren
	def swap_parents(self, child, parent):
		# special case of where
		# the root is the pivot point
		if (self.root == parent):
			# since root's parent is none, must be handled differently
			grandChild = child.lChild
			self.root = child
			parent.rChild = child.lChild
			# only change grandchildren's parents if applicable
			if (grandChild != None):
				grandChild.parent = parent
			child.lChild = parent
			# root's parent must be None
			child.parent = None
			parent.parent = child
		# need to just swap as normal, given a SORTED LIST
		else:
			# swap all the attributes and readjust the tree
			grandChild = child.lChild
			grandParent = parent.parent
			grandParent.rChild = child
			parent.rChild = child.lChild
			if (grandChild != None):
				grandChild.parent = parent

			child.lChild = parent
			child.parent = grandParent
			parent.parent = child

	# create a balanced binary search tree from a sorted list
	# basically, an AVL tree..
	def create_tree (self, a_list):
		# insert item and then check, starting from the bottom
		# if all the parent nodes are balanced...
		balanced_tree = Tree()

		for item in a_list:
			balanced_tree.insert(item)
			child = balanced_tree.search(item)
			parent = child.parent

			while (child.parent != None):
				# need to rotate
				if (not balanced_tree.is_balanced(parent)):
					balanced_tree.swap_parents(child, parent)

				child = parent
				parent = child.parent

		return balanced_tree

	# prints the nodes breadth first
	def print_level (self, aNode):
		if (aNode == None):
			print()
			return
		# create a queue
		queue = Queue()
		queue.enqueue(aNode)
		queue.enqueue(-1) # -1 used to separate nodes

		while (not queue.isEmpty()):
			node = queue.dequeue()
			# means a new level was reached, need to
			# print a new line to separate levels
			if (node == -1):
				print()
				# to prevent infinite while loop, only add this if no
				# more children left in queue
				if (not queue.isEmpty()):
					queue.enqueue(-1)
			else:
				# print the data at the given level
				print(node.data, end = ' ')
				if (node.lChild != None):
					queue.enqueue(node.lChild)
				if (node.rChild != None):
					queue.enqueue(node.rChild)
		return

	# prints the tree in order (left, center, right)
	def inOrder (self, aNode):
		if (aNode != None):
			self.inOrder (aNode.lChild)
			print(aNode.data, end = ' ')
			self.inOrder(aNode.rChild)

	# prints the tree in a pre order (center, left, right)
	def preOrder (self, aNode):
		if (aNode != None):
			print(aNode.data)
			preOrder(aNode.lChild)
			preOrder(aNode.rChild)

	# prints the tree in a post order (left, right, center)
	def postOrder (self, aNode):
		if (aNode != None):
			postOrder(aNode.lChild)
			postOrder(aNode.rChild)
			print(aNode.data)

	# Find the node with the smallest value
	def minimum (self):
		current = self.root
		parent = current
		while (current != None):
			parent = current
			current = current.lChild
		return parent

	# Find the node with the largest value
	def maximum (self):
		current = self.root
		parent = current
		while (current != None):
			parent = current
			current = current.rChild
		return parent

	# Delete a node with a given key
	def delete (self, key):
		deleteNode = self.root
		parent = self.root
		isLeft = False

		# If empty tree
		if (deleteNode == None):
			return False

		# Find the delete node
		while ((deleteNode != None ) and (deleteNode.data != key)):
			parent = deleteNode
			if (key < deleteNode.data):
				deleteNode = deleteNode.lChild
				isLeft = True
			else:
				deleteNode = deleteNode.rChild
				isLeft = False

		# If node not found
		if (deleteNode == None):
		  return False

		# Delete node is a leaf node
		if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
			if (deleteNode == self.root):
				self.root = None
			elif (isLeft):
				parent.lChild = None
			else:
				parent.rChild = None

		# Delete node is a node with only left child
		elif (deleteNode.rChild == None):
			if (deleteNode == self.root):
				self.root = deleteNode.lChild
			elif (isLeft):
				parent.lChild = deleteNode.lChild
			else:
				parent.rChild = deleteNode.lChild

		# Delete node is a node with only right child
		elif (deleteNode.lChild == None):
			if (deleteNode == self.root):
				self.root = deleteNode.rChild
			elif (isLeft):
				parent.lChild = deleteNode.rChild
			else:
				parent.rChild = deleteNode.rChild

		# Delete node is a node with both left and right child
		else:
		  # Find delete node's successor and successor's parent nodes
			successor = deleteNode.rChild
			successorParent = deleteNode

			while (successor.lChild != None):
				successorParent = successor
				successor = successor.lChild

		  # Successor node right child of delete node
			if (deleteNode == self.root):
				self.root = successor
			elif (isLeft):
				parent.lChild = successor
			else:
				parent.rChild = successor

		  # Connect delete node's left child to be successor's left child
			successor.lChild = deleteNode.lChild

		  # Successor node left descendant of delete node
			if (successor != deleteNode.rChild):
				successorParent.lChild = successor.rChild
				successor.rChild = deleteNode.rChild

		return True

def main():
	# Create at least two binary search trees - one balanced and the other not

	# TA kaitlin test code:
	# tree1 = Tree()
	# tree1.insert(33)
	# new_tree = tree1.create_tree([1, 9, 11, 17])
	# tree1.print_level(tree1.root) #should print 33
	# new_tree.print_level(new_tree.root) #should print 9 on first line, 1 11 on second, 17 on third

   # Create at least two binary search trees - one balanced and
   # the other not

   # Test your function get_height() for those trees

   # Test your function num_nodes() for those trees

   # Find the balance factors of the roots of those trees

   # Find if the trees are balanced or not

   # Create a balanced binary search tree from a sorted list
   # check that it is balanced

   # Print all the trees that you have breadth first
	binaryList = [500, 400, 600, 300, 700, 200, 800]
	print("List to be made into trees:", binaryList)

	tree = Tree()
	for num in binaryList:
		tree.insert(num)

	print()
	print("Testing height of unbalanced tree:", tree.get_height(tree.root))
	print("Testing number of nodes of unbalanced tree:", tree.num_nodes(tree.root))
	print("Finding balance factor of unbalanced tree's root:", tree.balance_factor(tree.root))
	print("Testing if unbalanced tree is balanced:", tree.is_balanced(tree.root))
	print("Unbalanced tree breadth first traversal:")
	tree.print_level(tree.root)
	print()

	binaryList.sort()
	bal_tree = tree.create_tree(binaryList)
	print("Testing height of balanced tree:", bal_tree.get_height(bal_tree.root))
	print("Testing number of nodes of balanced tree:", bal_tree.num_nodes(bal_tree.root))
	print("Finding balance factor of balanced tree's root:", bal_tree.balance_factor(bal_tree.root))
	print("Testing if balanced tree is balanced:", bal_tree.is_balanced(bal_tree.root))
	print("Balanced tree breadth first traversal:")
	bal_tree.print_level(bal_tree.root)


	print()
	binaryList = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
	print("List to be made into a tree:", binaryList)
	normal_tree = Tree()
	for num in binaryList:
		normal_tree.insert(num)

	print()
	print("Testing height of normal tree:", normal_tree.get_height(normal_tree.root))
	print("Testig number of nodes of normal tree:", normal_tree.num_nodes(normal_tree.root))
	print("Finding balance factor of normal tree's root:", normal_tree.balance_factor(normal_tree.root))
	print("Testing if normal tree is balanced:", normal_tree.is_balanced(normal_tree.root))
	print("A Binary tree without balancing: ")
	normal_tree.print_level(normal_tree.root)
	print()

	binaryList.sort()
	balanced_tree = normal_tree.create_tree(binaryList)
	print("Testing height of balanced tree:", balanced_tree.get_height(balanced_tree.root))
	print("Testing number of nodes of balanced tree:", balanced_tree.num_nodes(balanced_tree.root))
	print("Finding balance factor of balanced tree's root:", balanced_tree.balance_factor(balanced_tree.root))
	print("Testing if balanced tree is balanced:", balanced_tree.is_balanced(balanced_tree.root))
	print("Balanced tree breadth first traversal:")
	balanced_tree.print_level(balanced_tree.root)
	print()

	binaryList = [50, 17, 76, 9, 23, 54, 14, 19, 72, 12, 67]
	print("List to be made into a tree:", binaryList)
	normal_tree = Tree()
	for num in binaryList:
		normal_tree.insert(num)

	print()
	print("Testing height of normal tree:", normal_tree.get_height(normal_tree.root))
	print("Testig number of nodes of normal tree:", normal_tree.num_nodes(normal_tree.root))
	print("Finding balance factor of normal tree's root:", normal_tree.balance_factor(normal_tree.root))
	print("Testing if normal tree is balanced:", normal_tree.is_balanced(normal_tree.root))
	print("A Binary tree without balancing: ")
	normal_tree.print_level(normal_tree.root)
	print()

	binaryList.sort()
	balanced_tree = normal_tree.create_tree(binaryList)
	print("Testing height of balanced tree:", balanced_tree.get_height(balanced_tree.root))
	print("Testing number of nodes of balanced tree:", balanced_tree.num_nodes(balanced_tree.root))
	print("Finding balance factor of balanced tree's root:", balanced_tree.balance_factor(balanced_tree.root))
	print("Testing if balanced tree is balanced:", balanced_tree.is_balanced(balanced_tree.root))
	print("Balanced tree breadth first traversal:")
	balanced_tree.print_level(balanced_tree.root)
	print()

	binaryList = [4, 7, 16, 20, 37, 38, 43, 56, 62, 77, 89]
	print("List to be made into a tree:", binaryList)
	normal_tree = Tree()
	for num in binaryList:
		normal_tree.insert(num)

	print()
	print("Testing height of normal tree:", normal_tree.get_height(normal_tree.root))
	print("Testig number of nodes of normal tree:", normal_tree.num_nodes(normal_tree.root))
	print("Finding balance factor of normal tree's root:", normal_tree.balance_factor(normal_tree.root))
	print("Testing if normal tree is balanced:", normal_tree.is_balanced(normal_tree.root))
	print("A Binary tree without balancing: ")
	normal_tree.print_level(normal_tree.root)
	print()

	binaryList.sort()
	balanced_tree = normal_tree.create_tree(binaryList)
	print("Testing height of balanced tree:", balanced_tree.get_height(balanced_tree.root))
	print("Testing number of nodes of balanced tree:", balanced_tree.num_nodes(balanced_tree.root))
	print("Finding balance factor of balanced tree's root:", balanced_tree.balance_factor(balanced_tree.root))
	print("Testing if balanced tree is balanced:", balanced_tree.is_balanced(balanced_tree.root))
	print("Balanced tree breadth first traversal:")
	balanced_tree.print_level(balanced_tree.root)

main()
