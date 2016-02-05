# 130. Surrounded Regions My Submissions Question
# Total Accepted: 46767 Total Submissions: 298769 Difficulty: Medium
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

# # Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

# # A region is captured by flipping all 'O's into 'X's in that surrounded region.

# # For example,
# # X X X X
# # X O O X
# # X X O X
# # X O X X
# # After running your function, the board should be:

# # X X X X
# # X X X X
# # X X X X
# # X O X X



# class Solution(object):
# 	'''this code transfer the O to Y when qualified, in this way to speed up'''
'''use a big queue, not each row queue, and put index first, with different method to get neighours, should be faster'''
# 	def solve(self, board):
# 		"""
# 		:type board: List[List[str]]
# 		:rtype: void Do not return anything, modify board in-place instead.
# 		"""
# 		m,n = self.get_board_size(board)
# 		if m == 0 or n == 0:
# 			return 
# 		#check the 1 and last rows, with 1 and last cols, and save all the O s; and then flip all the other 'X'	

# 		#make dictionary, checking dict, and make value as 0 if not checking.
# 		idx_dct = dict(zip([(i,j) for i in range(m) for j in range(n)],[0]*m*n))
		
# 		total_queue = [] + [(0,i) for i in range(n)] + [(m-1,i) for i in range(n)] + [(j,0) for j in range(1,m-1)]+ [(j,n-1) for j in range(1,m-1)]
		
# 		while len(total_queue) > 0:
# 			idx = total_queue[0]
# 			if board[idx[0]][idx[1]] == 'O':
# 				self.bfs(idx, board, idx_dct,total_queue)
# 			total_queue.pop(0)
						
# 		for i in range(0,m):
# 			for j in range(0,n):
# 				if board[i][j] == 'O':
# 					board[i][j] = 'X'
# 				elif board[i][j] == 'Y':	
# 					board[i][j] = 'O'
# 				else:
# 					pass
				
# 	def get_board_size(self, board):
# 		#m is the # of rows
# 		m = len(board)
# 		if m == 0:
# 			n = 0
# 			return m,n
# 		#n is the # of cols
# 		n = len(board[0])
# 		return m,n
	

# 	def bfs(self, idx, board, idx_dct,total_queue):
# 		'''if the idx has O on the bound, then search through it, to find all the Os next to it as a region, change them to Y'''
# 		queue = [idx]
# 		while len(queue) >0:
# 			cur = queue[0]
# 			board[cur[0]][cur[1]] = 'Y'
# 			neight_idx = self.get_neight(cur[0],cur[1])
# 			for ele in neight_idx:
# 				if ele in idx_dct and board[ele[0]][ele[1]] == 'O':
# 					queue.append(ele)
# 					board[ele[0]][ele[1]] = 'Y'
# 					# if ele in total_queue:
# 					# 	total_queue.remove(ele)
# 			queue.pop(0)



# 	def get_neight(self, i,j):
# 		return [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]



# 127. Word Ladder My Submissions Question
# Total Accepted: 65673 Total Submissions: 335577 Difficulty: Medium
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.


class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: Set[str]
		:rtype: int
		"""
		#bfs:queue, dict and tree
		#to record the level/path, just add the step after the word state, that is it
		wordList.add(endWord)
		dct = dict(zip(wordlist, [1]*len(wordList)))        
		queue = [(beginWord,1)]
		n=len(endWord)
		letters = 'abcdefghijklmnopqrstuvwxyz'
		while queue:
			cur = queue.pop(0)
			curword, curlevel = cur[0], cur[1]
			if curword == endWord: return curlevel 

			for i in range(n):
				for letter in letters:
					new = curword[:i] + letter + curword[i+1:]
					if new in dct:
						queue.append((new, curlevel+1))
						dct.remove(new)
		return 0
# 126. Word Ladder II My Submissions Question
# Total Accepted: 38549 Total Submissions: 285578 Difficulty: Hard
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordlist):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordlist: Set[str]
#         :rtype: List[List[int]]
#         """






