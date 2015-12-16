# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X



class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m,n = self.get_board_size(board)
		if m == 0 or n == 0:
			return 
		#check the 1 and last rows, with 1 and last cols, and save all the O s; and then flip all the other 'X'	

		#make dictionary, checking dict, and make value as 0 if not checking.
		dct = dict(zip([(i,j) for i in range(m) for j in range(n)],[0]*m*n))
		odct = [(i,j) for i in range(m) for j in range(n) if board[i][j] == 'O']
		odct = dict(zip(odct, [0]*len(odct)))
		queue = [] + [(0,i) for i in range(n)] + [(m-1,i) for i in range(n)] + [(j,0) for j in range(1,m-1)]+ [(j,n-1) for j in range(1,m-1)]
		
		while len(queue) > 0:
			idx = queue[0]
			dct[idx] = 1
			queue.pop(0)
			if idx in odct: 
				odct[idx] = 1
				neigh_lst = self.get_neight(idx[0], idx[1])
				for neigh in neigh_lst:
					if neigh in dct:
						if dct[neigh] == 0 and neigh in odct:
							odct[neigh] = 1
							if neigh not in queue: queue.append(neigh)
						dct[neigh] = 1
						
		for item in odct:
			if odct[item] == 0:
				board[item[0]][item[1]] = 'X'

	def get_board_size(self, board):
		#m is the # of rows
		m = len(board)
		if m == 0:
			n = 0
			return m,n
		#n is the # of cols
		n = len(board[0])
		return m,n
	
	def get_neight(self, i,j):
		# res= []
		# if (i-1,j) in dct and dct[(i-1,j)] == 0 and board[i-1][j] == 'O':
		# 	dct[(i-1,j)] = 1
		# 	res.append((i-1,j))
		# if (i+1,j) in dct and dct[(i+1,j)] == 0 and board[i+1][j] == 'O':
		# 	dct[(i+1,j)] = 1
		# 	res.append((i+1,j))
		# if (i,j-1) in dct and dct[(i,j-1)] == 0 and board[i][j-1] == 'O':
		# 	dct[(i,j-1)] = 1
		# 	res.append((i,j-1))
		# if (i,j+1) in dct and dct[(i,j+1)] == 0 and board[i][j+1] == 'O':
		# 	dct[(i,j+1)] = 1
		# 	res.append((i, j+1))
		return [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]



if __name__ == '__main__':
	test = Solution()
	input1 = [['X','X','O'],['X','O','X'],['X','X','X']]
	input2 = [['X','X','O','O'],['X','X','X','X'],['X','X','O','X'],['X','X','X','X']]
	print test.solve(input1)
	print test.solve(input2)


