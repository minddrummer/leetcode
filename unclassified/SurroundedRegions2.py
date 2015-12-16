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
	'''this code transfer the O to Y when qualified, in this way to speed up'''
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m,n = self.get_board_size(board)
		if m == 0:
			return 
		#check the 1 and last rows, with 1 and last cols, and save all the O s; and then flip all the other 'X'	

		#make dictionary, checking dict, and make value as 0 if not checking.
		idx_dct = dict(zip([(i,j) for i in range(m) for j in range(n)],[0]*m*n))
		
		total_queue = [(0,i) for i in range(n)] + [(m-1,i) for i in range(n)] + [(j,0) for j in range(1,m-1)]+ [(j,n-1) for j in range(1,m-1)]
		
		while len(total_queue) > 0:
			idx = total_queue[0]
			if board[idx[0]][idx[1]] == 'O':
				self.bfs(idx, board, idx_dct)
			total_queue.pop(0)
						
		for i in range(0,m):
			for j in range(0,n):
				if board[i][j] == 'O':
					board[i][j] = 'X'
				elif board[i][j] == 'Y':	
					board[i][j] = 'O'
				else:
					pass
				
	def get_board_size(self, board):
		#m is the # of rows
		m = len(board)
		if m == 0:
			return m,None
		#n is the # of cols
		n = len(board[0])
		return m,n
	

	def bfs(self, idx, board, idx_dct):
		'''if the idx has O on the bound, then search through it, to find all the Os next to it as a region, change them to Y'''
		queue = [idx]
		while len(queue) >0:
			cur = queue[0]
			board[cur[0]][cur[1]] = 'Y'
			neight_idx = self.get_neight(cur[0],cur[1])
			for ele in neight_idx:
				if ele in idx_dct and board[ele[0]][ele[1]] == 'O':
					queue.append(ele)
					board[ele[0]][ele[1]] = 'Y'
			queue.pop(0)



	def get_neight(self, i,j):
		return [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]



if __name__ == '__main__':
	test = Solution()
	input1 = [['X','X','O'],['X','O','X'],['X','X','X']]
	input2 = [['X','X','O','O'],['X','X','X','X'],['X','X','O','X'],['X','X','X','X']]
	print test.solve(input1)
	print test.solve(input2)


