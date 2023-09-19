def solution(g):
	rows = len(g)
	cols = len(g[0])
	evolve0 = [[0,3],[1,2,3],[1,2,3],[0,1,2,3]]
	evolve1 = [[1,2],[0],[0],[]]
	temp = [[0, 0] for _ in range(rows + 1)]
	result = [[[] for _ in range(2**(rows + 1))] for _ in range(cols)]

	global branch
	branch = []
	global count
	count = 0

	def dfs(col, row, val):
        # Add the current position to the branch
		branch.append(val)
	
		if row + 1 < rows:
			row += 1
			if g[row][col] is False:
				for node in evolve0[val]: dfs(col,row,node)
			else:
				for node in evolve1[val]: dfs(col,row,node)
		else:
			for i in range(rows + 1):
				temp[i][0] = branch[i] // 2
				temp[i][1] = branch[i] % 2
			col_value = temp[0][0]
			next_col_value = temp[0][1]
			for i in range(1,rows + 1):
				col_value = col_value << 1
				col_value += temp[i][0]
				next_col_value = next_col_value << 1
				next_col_value += temp[i][1]
			result[col][col_value].append(next_col_value)		
		branch.pop()
				
	for col in range(cols):
		for val in range(4):
			dfs(col,-1,val)

	left_column = {i: 1 for i in range(2**(rows+1))}
	for col1 in range(cols):
		right_column = {i: 0 for i in range(2**(rows+1))}
		for col2 in range(2**(rows+1)):
			if col2 in left_column:
				for value in result[col1][col2]:
					right_column[value] += left_column[col2]
		left_column = right_column
		
	count = 0
	for value in left_column.values():
		count += value
	return(count)