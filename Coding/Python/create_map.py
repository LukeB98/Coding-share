def create_cells(rows, columns):
	cells = []
	m = 0
	n = 0
	#(m,n)
	while n < columns:
		
		while m < rows:
			
			cells.append((n,m))
			m += 1
			
		m = 0	
		n += 1	
		
	return cells
CELLS_2 = create_cells(3,3)	
print(CELLS_2)
