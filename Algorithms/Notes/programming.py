#working on interview questions

#find missing number in an int array of 1 to 100
def missingInt(a):
	if a[0] != 100:
		return 100
	if a[1] != a[0] + 1:
		return a[0] + 1
	else:
		return missingInt(a[1:])
def main():
	lst = [i for i in range(101)]
	lst.remove(100)
	print(missingInt(lst))
main()