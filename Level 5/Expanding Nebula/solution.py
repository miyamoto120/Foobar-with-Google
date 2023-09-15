def solution(g):
	rows = len(g)
	cols = len(g[0])
	evolve0 = [[0,3],[1,2,3],[1,2,3],[0,1,2,3]]
	evolve1 = [[1,2],[0],[0],[]]
	temp = [[0, 0] for _ in range(rows + 1)]
	result = [[[] for _ in range(2**(rows + 1))] for _ in range(cols)]
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
			col_value = 0
			next_col_value = 0
			for i in range(rows + 1):
				col_value = col_value * 2 +  temp[i][0]
				next_col_value = next_col_value * 2 + temp[i][1]
			result[col][col_value].append(next_col_value)		
		branch.pop()

	def count_dfs(col,row):
		global count
		for i in result[col][row]:
			if col + 2> cols:
				count += 1
			else:
				count_dfs(col + 1,i)

	for col in range(cols):
		for val in range(4):
			dfs(col,-1,val)

	count = 0
	for start in range(2**(rows+1)):
		count_dfs(0,start)

	return(count)