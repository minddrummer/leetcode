# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution:
	# @param {character[][]} board
	# @return {boolean}
	def isValidSudoku(self, board):
		res = True
		for i in range(9):
			tmp = []
			for j in range(9):
				if board[i][j] != '.': #and board[i][j]>=1 and board[i][j]<=9:
					if board[i][j] not in tmp:
						tmp.append(board[i][j])
					else:
						res = False
						return res
		for i in range(9):
			tmp = []
			for j in range(9):
				if board[j][i] != '.':# and board[j][i]>=1 and board[j][i]<=9:
					if board[j][i] not in tmp:
						tmp.append(board[j][i])
					else:
						res = False
						return res
		
		#ssquare = []
		for i in range(3):
			for j in range(3):
				s0 = board[(3*i):(3*i+3)]
				ss = []
				for item in s0:
					ss= ss + item[(3*j):(3*j+3)]
				tmp = []
				for item in ss:
					if item != '.':# and item>=1 and item<=9:
						if item not in tmp:
							tmp.append(item)
						else:
							res = False
							return res
		return res			

if __name__ == '__main__':
	test = Solution()
	print test.isValidSudoku()










