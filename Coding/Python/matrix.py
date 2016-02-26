import random

def create_matrix(rows, columns): #creates a mxn matrix

	matrix = [[0 for x in range(columns)] for x in range(rows)]
	matrix[0][0] = 1
	n = 0
	m = 0

	for item in matrix:
		while m < columns:
			matrix[n][m] = random.randint(0,3)
			m += 1
		m = 0
		n += 1
	matrix[0][0] = 1 #--------------------------------------------------------------------------------#
	return matrix 
	
def print_matrix(matrix): #prints the matrix in a viewable way
	n = 0
	
	for item in matrix:
		print(matrix[n])
		n += 1

def row_replacement_matrix(matrix,x,z): #finds the rows you would use to do a replacement
	n = 0
	m = 0
	z = z
	x = x
	replacement_matrix = []
	if matrix[x][z] == 0:
			return 'null'
	for row in matrix:
		if n > rows - 2:
			break
		new_row = list()
		for entry in matrix[z]:
								
			if matrix[n+1][z] == 0:
				new_row.append(0)
			else:
				new_row.append(round(entry * (-matrix[n+1][z] / matrix [x][z]),2)) 
		m += 1
		n += 1
		replacement_matrix.append(new_row)
	return replacement_matrix
		
def perform_replacement(matrix,replacement_matrix,n): #takes the replacement rows and adds it to the original matrix
	if replacement_matrix == 'null':
		return 'null'
	n = n
	m = 0
	while n < rows - 1:
		while m < columns:
			matrix[n+1][m] = round((matrix[n+1][m] + replacement_matrix[n][m]),2)
			m += 1
		n += 1
		m = 0
	return matrix

def check_matrix_rows(matrix): #if a row has more entries than the one above it, it will swap them
	
	n = 0
	m = 0
	for row in matrix: #make a way to find the leading entry position
		while n < rows - 1:
			if matrix[m][n] != 1:
				leading_position = matrix.index([m][n-1])
				print(leading_position)
			n += 1
		n = 0
		m = 0
	
		
def solve_matrix(matrix): #calls the functions for each row
	z = 0
	for item in matrix:
		print('---')
		replacement_matrix = row_replacement_matrix(matrix,z,z)
		matrix_n = perform_replacement(matrix,replacement_matrix,z)
		print_matrix(matrix)
		z += 1
	print('---')
	check_matrix_rows(matrix)	
	print_matrix(matrix)
#-----------------add a function that swaps row position if it has more non-zero rows that the one above------------------------#
#calling functions:
rows = 4
columns = 4
matrix = create_matrix(rows,columns)
print_matrix(matrix)
solve_matrix(matrix)







