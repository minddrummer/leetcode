# 131. Palindrome Partitioning My Submissions Question
# Total Accepted: 58041 Total Submissions: 211765 Difficulty: Medium
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# For example, given s = "aab",
# Return
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

# class Solution(object):
# 	def partition(self, s):
# 		"""
# 		:type s: str
# 		:rtype: List[List[str]]
# 		"""
# 		# dfs, questions: 1)path, count? 2)how to save state
# 		# 3)how to expand state and save results
# 		# 4)remove duplicate? 5)ending condition, 6)converge condition? 7)prunning or cache ..
# 		dct = {}
# 		return self.help(s, dct)		

# 	def help(self, s, dct):
# 		n=len(s)
# 		if n==0: return [[]]
# 		if n==1: return [[s]]
# 		res=[]
# 		for i in range(n):
# 			first = s[:i+1]
# 			if self.pali(first): 
# 				#use space to save time: space efficiency cost for time efficiency
# 				#but for this problem, it does NOT work, and will time limit
# 				#just no saving would be fine
# 				if i+1 in dct: last_res = dct[i+1]
# 				else:
# 					last_res = self.help(s[i+1:],dct)
# 					dct[i+1] = last_res
# 				for item in last_res:
# 					res.append([first]+item)
# 		return res

# 	def pali(self, s):
# 		n=len(s)
# 		if n==1: return True
# 		i=0
# 		j=n-1
# 		while i<=j:
# 			if s[i]==s[j]:
# 				i +=1
# 				j -=1
# 			else:
# 				return False
# 		return True


# class Solution(object):
# 	def partition(self, s):
# 		"""
# 		:type s: str
# 		:rtype: List[List[str]]
# 		"""
# 		n=len(s)
# 		if n==0: return [[]]
# 		if n==1: return [[s]]
# 		res=[]
# 		for i in range(n):
# 			first = s[:i+1]
# 			if self.pali(first): 
# 				last_res = self.partition(s[i+1:])
# 				for item in last_res:
# 					res.append([first]+item)
# 		return res
	
# 	def pali(self, s):
# 		n=len(s)
# 		if n==1: return True
# 		i=0
# 		j=n-1
# 		while i<=j:
# 			if s[i]==s[j]:
# 				i +=1
# 				j -=1
# 			else:
# 				return False
# 		return True

# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.partition('aab')

# 62. Unique Paths My Submissions Question
# Total Accepted: 76364 Total Submissions: 216914 Difficulty: Medium
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Above is a 3 x 7 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

# Subscribe to see which companies asked this question

class Solution(object):
	DCT = {}
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""

		if m<1 or n<1: return 0
		if m==1 and n == 1: 
			self.DCT[(m,n)] = 1
			return 1
		if (m,n) in self.DCT:
			return self.DCT[(m,n)]
		else:
			self.DCT[(m,n)] = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
			return self.DCT[(m,n)]


# 63. Unique Paths II My Submissions Question
# Total Accepted: 57920 Total Submissions: 200431 Difficulty: Medium
# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
				

# 52. N-Queens II My Submissions Question
# Total Accepted: 40139 Total Submissions: 104819 Difficulty: Hard
# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.



# Subscribe to see which companies asked this question

# class Solution(object):
#     def totalNQueens(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
				

# 51. N-Queens My Submissions Question
# Total Accepted: 48429 Total Submissions: 185184 Difficulty: Hard
# The n-queens puzzle is the problem of placing n queens on an n *n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Subscribe to see which companies asked this question

# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
				

# 93. Restore IP Addresses My Submissions Question
# Total Accepted: 50042 Total Submissions: 220989 Difficulty: Medium
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# Subscribe to see which companies asked this question

# class Solution(object):
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """


# 39. Combination Sum My Submissions Question
# Total Accepted: 78729 Total Submissions: 263128 Difficulty: Medium
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2,, ak) must be in non-descending order. (ie a1 <=a2 <= ak)
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3] 


# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
				

# 40. Combination Sum II My Submissions Question
# Total Accepted: 59648 Total Submissions: 222533 Difficulty: Medium
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2,, ak) must be in non-descending order. (ie, a1 <=a2 <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6] 
# Subscribe to see which companies asked this question

# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
				


# 216. Combination Sum III My Submissions Question
# Total Accepted: 24112 Total Submissions: 70931 Difficulty: Medium
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Ensure that numbers within the set are sorted in ascending order.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def combinationSum3(self, k, n):
#         """
#         :type k: int
#         :type n: int
#         :rtype: List[List[int]]
#         """
				

# 22. Generate Parentheses My Submissions Question
# Total Accepted: 76174 Total Submissions: 214866 Difficulty: Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"

# Subscribe to see which companies asked this question

# class Solution(object):
# 	def binaryTree_dfs(self, l,r,item, res):
# 		if l>r:
# 			return None
# 		if l == 0 and r == 0:
# 			res.append(item)
# 		if l > 0:
# 			self.binaryTree_dfs(l-1,r,item+'(',res)
# 		if r > 0:
# 			self.binaryTree_dfs(l,r-1,item+')',res)

# 	def generateParenthesis(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[str]
# 		"""
# 		if n == 0:
# 			return []
# 		res = []
# 		self.binaryTree_dfs(n,n,'',res)
# 		return res  

# 37. Sudoku Solver My Submissions Question
# Total Accepted: 44889 Total Submissions: 187041 Difficulty: Hard
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.


# A sudoku puzzle...


# ...and its solution numbers marked in red.

# Subscribe to see which companies asked this question


# class Solution(object):
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
				


# 79. Word Search My Submissions Question
# Total Accepted: 64858 Total Submissions: 292849 Difficulty: Medium
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# Subscribe to see which companies asked this question




# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
				


# 212. Word Search II My Submissions Question
# Total Accepted: 14961 Total Submissions: 82885 Difficulty: Hard
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# class Solution(object):
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
				




#         		                                                                