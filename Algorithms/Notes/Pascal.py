def pascal(n):
	triangle = []
	for i in range(n):
		row = [x+1 for x in range(i+1)]
		triangle.append(row)
		for j in range(i):
			if j == 0:
				triangle[i][j] = 1
			elif j == i:
				triangle[i][j] = 1
			else:
				triangle[i][j] = (triangle[i-1][j-1] + triangle[i-1][j])
		
	return triangle

def main():
	pascList = pascal(5)
	for i in pascList:
		print(i)
main()
