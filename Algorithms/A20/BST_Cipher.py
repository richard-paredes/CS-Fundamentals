
#  File: BST_Cipher.py

#  Description: A20, uses a binary search tree to decrypt and encrypt phrases

#  Student Name: Richard Paredes

#  Student UT EID: ROP242

#  Partner Name: Diana De La Torre

#  Partner UT EID: DD32653

#  Course Name: CS 313E

#  Unique Number: 50730

#  Date Created: 04/19/19

#  Date Last Modified: 04/19/19

# nodes for the binary search tree
class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lChild = None
		self.rChild = None
# binary search tree that encrypts and decrypts with a given key
class Tree (object):
	# the init() function creates the binary search tree with the
	# encryption string. If the encryption string contains any
	# character other than the characters 'a' through 'z' or the
	# space character drop that character.
	def __init__ (self, encrypt_str):
		self.root = None

		for char in encrypt_str.lower():
			#only inserts alphabetic chars and spaces into the key
			if (char.isalpha() or char == ' '):
				self.insert(char)

	# the insert() function adds a node containing a character in
	# the binary search tree. If the character already exists, it
	# does not add that character. There are no duplicate characters
	# in the binary search tree.
	def insert (self, ch):
		charNode = Node (ch)
		#empty tree fill
		if (self.root == None):
			self.root = charNode

		#must iterate through tree
		else:
			current = self.root
			parent = self.root
			#iterating through tree
			while (current != None):
				parent = current
				#instantly quitting if element already present
				if (ch == current.data):
					return
				#choosing which subtree to pursue in search
				elif (ch < current.data):
					current = current.lChild
				else:
					current = current.rChild

			#checking where to put the node appropriately
			if (ch < parent.data):
				parent.lChild = charNode
			else:
				parent.rChild = charNode

	# the search() function will search for a character in the binary
	# search tree and return a string containing a series of lefts
	# (<) and rights (>) needed to reach that character. It will
	# return a blank string if the character does not exist in the tree.
	# It will return * if the character is the root of the tree.
	def search (self, ch):
		path = ''
		#checking simple case
		if (ch == self.root.data):
			return '*'

		else:
			current = self.root
			while (current != None):
				#found the character's node
				if (ch == current.data):
					break
				#choosing which subtree to pursue
				elif (ch < current.data):
					current = current.lChild
					path += '<'
				else:
					current = current.rChild
					path += '>'
		#if the search was unsuccessful
		if (current == None) or (current.data != ch):
			path = ''

		return path

	# the traverse() function will take string composed of a series of
	# lefts (<) and rights (>) and return the corresponding 
	# character in the binary search tree. It will return an empty string
	# if the input parameter does not lead to a valid character in the tree.
	def traverse (self, st):
		current = self.root
		#check if it's root:
		if (st == '*'):
			#means there's a root value
			if (current != None):
				return current.data
			#means the key is empty
			else:
				return ''
		#running through characters in the path
		for ch in st:
			#means path was invalid
			if (current == None):
				return ''
			if (ch == '<'):
				current = current.lChild
			elif (ch == '>'):
				current = current.rChild
		# in case current is still None after being selected as a child as the last character in the string
		if (current == None):
			return ''
		return current.data


	# the encrypt() function will take a string as input parameter, convert
	# it to lower case, and return the encrypted string. It will ignore
	# all digits, punctuation marks, and special characters.
	def encrypt (self, st):
		stCopy = st.lower()
		encrypted = ''
		for char in stCopy:
			#only encrypt characters that are spaces or alphabetic
			if (char == ' ' or char.isalpha()):
				encrypted += self.search(char) + '!'
			else:
				encrypted += char + '!'

 		#need to remove the last exclamation mark
		encrypted = encrypted[:-1]
		return encrypted
		


	# the decrypt() function will take a string as input parameter, and
	# return the decrypted string.
	def decrypt (self, st):
		decrypted = ''
		pathChars = ['*', '>', '<']
		paths = st.split('!')
		for path in paths:
			#special characters that arent encrypted
			if not ((pathChars[0] in path) or (pathChars[1] in path) or (pathChars[2] in path)):
				decrypted += path
			else:
				decrypted += self.traverse(path)

		return decrypted

def main():
	encrypt_key = input('Enter the encryption key: ')
	encryptTree = Tree(encrypt_key)

	encrypt_str = input('Enter string to be encrypted: ')
	print('Encrypted string: ' + encryptTree.encrypt(encrypt_str))

	decrypt_str = input('Enter string to be decrypted: ')
	print('Decrypted string: ' + encryptTree.decrypt(decrypt_str))

main()