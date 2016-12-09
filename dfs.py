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
# 		# dfs, questions: 1)path, count? 2.1)how to save state
# 		# 2.2)how to expand state and save results
# 		# 3.1)ending condition, 3.2)converge condition? 4.1)remove duplicate?  4.2)prunning or cache ..
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

# 				#more importantly, the indexing dictionary will change over time, make it
# 				#untrackable!!!!---so this code is wrong, you have to figure out some stable tracking 
# 				# method if you want to use space dict
# 				if i+1 in dct: last_res = dct[i+1]
# 				else:
# 					last_res = self.help(s[i+1:],dct)
# 					dct[i+1] = last_res

# 				print first,':',i, ':',dct
# 				for item in last_res:
# 					res.append([first]+item)
# 		return res

# 	def pali(self, s):
# 		n=len(s)
# 		if n<=1: return True
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
# 	sk = Solution()
# 	print sk.partition("fff")
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


#the second method: maybe wrong for '' string:
# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         n=len(s)
#         if n<=1: return [[s]]
#         res = []
#         for i in range(1,n):
#             if self.isPan(s[0:i]):
#                 for item in self.partition(s[i:]):
#                     res.append([s[0:i]]+item)
#         if self.isPan(s): res.append([s])            
#         return res
	
#     def isPan(self, s):
#         n= len(s)
#         if n<=1: return True
#         i=0
#         j=n-1
#         while i<=j:
#             if s[i]==s[j]:
#                 i+=1
#                 j-=1
#             else:
#                 return False
#         return True
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

# class Solution(object):
# 	DCT = {}
# 	def uniquePaths(self, m, n):
# 		"""
# 		:type m: int
# 		:type n: int
# 		:rtype: int
# 		"""
# 		#memorization method: TO(n^2), SO(n^2)
# 		#if not using dict, then it would be TO(n^4), SO(n)
# 		#it can be a math problem by choosing m-1 from m+n-2
# 		#last method, use DP's loop-forward method, rather than DP's dict method, like the code following
# 		#only count, need to count duplicate, ending in two ways: the trick is using the end point as the beginning point
# 		#save to dict to speed up; need prunning?
# 		#if you count from the beginning, it is hard, and more computation; if you start from the ending, it is easier and quick
# 		if m<1 or n<1: return 0
# 		if m==1 and n == 1: 
# 			self.DCT[(m,n)] = 1
# 			return 1
# 		if (m,n) in self.DCT:
# 			return self.DCT[(m,n)]
# 		else:
# 			self.DCT[(m,n)] = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
# 			return self.DCT[(m,n)]

# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         dct={}
#         for i in range(m): dct[(0,i)] = 1
#         for j in range(n): dct[(j,0)] = 1
#         #here, self.dfs will search one instance's method uniquePaths' namespace first,
#		  #to find the local variable dct, since dct is mutable, it would be a reference, and change it within all the recursive self.dfs methods    
#         return self.dfs(n-1, m-1, dct)
		
#     def dfs(self, x,y, dct):
		
#         if (x,y) in dct: return dct[(x,y)]
#         else:
#             dct[(x,y)] = self.dfs(x-1,y, dct) + self.dfs(x,y-1, dct)
#             return dct[(x,y)]

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
# 	def uniquePathsWithObstacles(self, obstacleGrid):
# 		"""
# 		:type obstacleGrid: List[List[int]]
# 		:rtype: int
# 		"""
# 		matrix = obstacleGrid
# 		dct={}
# 		m=len(matrix)				
# 		n=len(matrix[0])
# 		return self.help(matrix, dct, m,n)		


# 	def help(self, matrix, dct, m, n):
# 		'''matrix is not-inversed, dct is inversed'''
# 		if m<1 or n<1: return 0
# 		if matrix[-m][-n] == 1: 
# 			dct[(m,n)] = 0
# 			return 0
# 		if m==1 and n==1:
# 			dct[(m,n)] = 1
# 			return 1
			
# 		if (m,n) in dct:
# 			return dct[(m,n)]
# 		else:
# 			dct[(m,n)] = self.help(matrix, dct, m-1, n) + self.help(matrix, dct, m, n-1)
# 			return dct[(m,n)]


# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         m = len(obstacleGrid)
#         if m==0: return 0
#         n = len(obstacleGrid[0])
#         if n==0: return 0
#         if obstacleGrid[0][0]==1: return 0
		
#         dct={}
#         #initialize
#         dct[(0,0)]=1
#         for i in range(1,m): 
#             if obstacleGrid[i][0] == 1: dct[(0,i)] = 0
#             else: dct[(0,i)] = dct[(0,i-1)]
#         for j in range(1,n): 
#             if obstacleGrid[0][j] == 1: dct[(j,0)] = 0
#             else: dct[(j,0)] = dct[(j-1,0)]
		
#         return self.dfs(n-1,m-1, dct, obstacleGrid)
		
#     def dfs(self, x, y, dct, matrix):
#         if matrix[y][x]==1:
#             dct[(x,y)] = 0
#             return 0
#         else:
#             if (x,y) in dct: return dct[(x,y)]
#             else:
#                 dct[(x,y)] = self.dfs(x-1,y, dct, matrix) + self.dfs(x,y-1,dct,matrix)
#                 return dct[(x,y)]
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.uniquePathsWithObstacles([
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ])

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
# 	def solveNQueens(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[List[str]]
# 		"""
# 		def dfs(depth, lst):
# 			print board
# 			if depth == n: 
# 				print lst
# 				res.append(lst)
# 				return 
# 			for i in range(n):
# 				if check(depth, i):
# 					board[depth]=i
# 					#has to keep lst at the same level constant!
# 					#not changing over time!! : not lst.append
# 					dfs(depth+1, lst + [string[:i]+'Q'+string[i+1:]])

# 		def check(depth, col):
# 			for i in range(depth):
# 				if board[i]==col or abs(depth-i)==abs(board[i]-col):
# 					return False
# 			return True

# 		#n, board and res now is frame-environement within solveNQueens
# 		board = [-1]*n
# 		string = '.'*n
# 		res=[]
# 		dfs(0,[])
# 		return res

#coding version 2: with explanation
# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         def dfs(depth, lst, n):
#             if depth == n:
#                 Res.append(lst)
#                 return
#             for col in range(n):
#                 #if at Row depth, we can put Q in Col, we change Board[depth] to col, and append the corresponding String
#                 if check(depth, col):
#                     #the following doesnot influence later Board' check, because the check only check before depth Row of Board, and the for col in range(n) will check every 0:n-1 for each upper layer
#                     Board[depth] = col
#                     dfs(depth+1, lst+[String[0:col]+'Q'+String[col+1:]],n)
		
#         def check(depth, col):
#             for row in range(depth):
#                 if Board[row] ==col or abs(depth-row) == abs(Board[row]-col):
#                     return False
#             return True
	
#         Board = [-1]*n
#         String = '.'*n
#         Res = []
#         #depth is from 0 to n-1, when =n, stop
#         depth = 0
#         lst = []
#         dfs(depth, lst,n)
#         return Res

# if __name__ == '__main__':
# 	sk  = Solution()
# 	sk.solveNQueens(5)
# 52. N-Queens II My Submissions Question
# Total Accepted: 40139 Total Submissions: 104819 Difficulty: Hard
# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total number of distinct solutions.
# Subscribe to see which companies asked this question

# class Solution(object):
# 	count=None
# 	def totalNQueens(self, n):
# 		"""
# 		:type n: int
# 		:rtype: int
# 		"""
# 		def check(depth, col):
# 			for i in range(depth):
# 				if board[i]==col or abs(depth-i)==abs(board[i]-col):
# 					return False
# 			return True
		
# 		def dfs(depth):
# 			if depth==n: Solution.count += 1; return
# 			#no matter what, for each depth, we search 0-(n-i) col for each depth
# 			for i in range(n):
# 				if check(depth, i):
# 					board[depth]=i
# 					dfs(depth+1)

# 		Solution.count=0
# 		board=[-1]*n
# 		dfs(0)
# 		return Solution.count
# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.totalNQueens(9)


# 93. Restore IP Addresses My Submissions Question
# Total Accepted: 50042 Total Submissions: 220989 Difficulty: Medium
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example:
# Given "25525511135",
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def restoreIpAddresses(self, s):
# 		"""
# 		:type s: str
# 		:rtype: List[str]
# 		"""
# 		#dfs has to reach the ending or prunning at the half if there is 0 beginning
# 		return self.help(s, 1)

# 	def help(self, s, level):
# 		res=[]
# 		#lots of prunning here
# 		if level<=3:
# 			if len(s)>=2:
# 				res=res+[s[0:1]+'.'+item for item in self.help(s[1:], level+1)]
# 			if len(s)>=3 and int(s[0])!=0:
# 				res=res+[s[0:2]+'.'+item for item in self.help(s[2:], level+1)]
# 			if len(s)>=4 and int(s[0:3])<=255 and int(s[0])!=0:
# 				res=res+[s[0:3]+'.'+item for item in self.help(s[3:], level+1)]
# 		else: #level=4, the last level
# 			if len(s)==0: return []
# 			elif len(s)==1: return [s]
# 			elif len(s)==2 and int(s[0])!=0: return [s]
# 			elif len(s) ==3:
# 				if int(s)<=255 and int(s[0])!=0: return [s]
# 				else: return []
# 			else:
# 				return []
# 		return res

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.restoreIpAddresses("010010")
# 	print sk.restoreIpAddresses("00")

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
# 	def combinationSum(self, candidates, target):
# 		"""
# 		:type candidates: List[int]
# 		:type target: int
# 		:rtype: List[List[int]]
# 		"""
# 		#what is the state recording, how to expand, how to pruning and saving memory
# 		#how to sort and no duplicates?
# 		setc = sorted(set(candidates))
# 		res=[]
# 		self.dfs(setc, target, [], res)
# 		return res

# 	def dfs(self, setc, target, lst, res):
# 		#setc is a set, with increase order
# 		n= len(setc)
# 		for i in range(n):
# 			if setc[i] == target:		
# 				res.append(lst + [setc[i]])
# 			elif setc[i]<target:
# 				self.dfs(setc[i:], target-setc[i], lst+[setc[i]], res)
# 			else:
# 				continue

##this problem is actually very hard here for the position part for debugging!!!
#generally two ways to add results: return and use for loop and then return, 
# or keep a list, and whenever reach the end, change the list/dict accordingly
# class Solution(object):
# 	def combinationSum(self, candidates, target):
# 		"""
# 		:type candidates: List[int]
# 		:type target: int
# 		:rtype: List[List[int]]
# 		"""
# 		#sort and remove duplicate numbers first
# 		lst = sorted(list(set(candidates)))
# 		res = []
# 		self.dfs(lst, target, [], res)
# 		return res
		
# 	def dfs(self, lst, target, seq, res):
# 		# print lst, target
# 		# print 'seq is', seq
# 		n = len(lst)
# 		if n==0 or target<=0:
# 			return
# 		#the for loop position here is so important!
# 		for i in range(n):
# 			if lst[i] == target:
# 				res.append(seq+[lst[i]])
# 				break
# 			elif lst[i]> target:
# 				break
# 			elif lst[i]< target:
# 				self.dfs(lst[i:], target-lst[i], seq+[lst[i]], res)
# 		return 
# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.combinationSum([2,3,6,7],7)
# 	# print sk.combinationSum([1,1,1],2)

	
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
# 	def combinationSum2(self, candidates, target):
# 		"""
# 		:type candidates: List[int]
# 		:type target: int
# 		:rtype: List[List[int]]
# 		"""
# 		cand = sorted(candidates)		
# 		res=[]
# 		self.dfs(cand, target, [], res)
# 		return res

# 	def dfs(self, cand, target, lst, res):	
# 		n= len(cand)
# 		#for the duplicate number, like [1,1,1...] 
# 		#set up a pre variable, and skip it when the current number match the pre value should be good in dfs search
# 		#because dfs search would go deep first, and wouldNOT skip any duplicate-number answer for the final answer
# 		pre = None #pre variable
# 		for i in range(n):
# 			#check pre varialble match or NOT
# 			if cand[i] == pre: continue
# 			else: pre=cand[i]

# 			if cand[i]==target:
# 				res.append(lst+[cand[i]])
# 			elif cand[i]<target:
# 				#because of cand[i+1:]---this would retain the duplicate-number answer for the final answer
# 				self.dfs(cand[i+1:], target-cand[i], lst+[cand[i]], res)
# 			else:
# 				continue

# if __name__ == '__main__':
# 	sk =Solution()
# 	print sk.combinationSum2([10,1,2,7,6,1,5], 8)

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
# 	def combinationSum3(self, k, n):
# 		"""
# 		:type k: int
# 		:type n: int
# 		:rtype: List[List[int]]
# 		"""
# 		'''there should be no duplicate number in the results'''
# 		res=[]
# 		self.dfs(k,n,[], res, range(1,10))
# 		return res

# 	def dfs(self, k, n, lst, res, setc):
# 		#you cannot go down searching, so we need START variable
# 		#setc in increaing order for easy computation
# 		if k<=0: return
# 		elif k==1:
# 			for i in setc:
# 				#only single value would be added to the result
# 				if i<n: continue
# 				elif i==n: res.append(lst+[i])
# 				else: break
# 		else:
# 			#k>=2 continue dfs
# 			#for dfs, we cannot search from big number to smalled number, so the setc should be shrinked for final results
# 			for i in range(len(setc)):
# 				#shrink the setc, just from i+1, all the previous have been counted!!!
# 				if n>setc[i]: 
# 					#order matters for these type of problems
# 					#we donot go back and count the prevoius less number, so setc has to be ordered
# 					#and it will be shrinked whenever you use some value
# 					#you have to maintain a list for using purpose, rather than a range(1,10)
# 					#in this way, it will shrinked via dfs and you would get the right answer
# 					#setc[i:](would produce duplicate number in the set) VS setc[i+1](would produce non-duoplicate-number answer in the result)
# 					self.dfs(k-1, n-setc[i], lst+[setc[i]], res, setc[i+1:])
# 					# self.dfs(k-1, n-setc[i], lst+[setc[i]], res, setc[i:])
# 				#if n== or <, then there would be no answer for the following
# 				else: break

# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.combinationSum3(3,9)

# class Solution(object):
# 	def combinationSum3(self, k, n):
# 		"""
# 		:type k: int
# 		:type n: int
# 		:rtype: List[List[int]]
# 		"""
# 		#dfs, using starting number from 1 to 9 or not
# 		#not using binary tree/exponential search
# 		def dfs(can, target, k, seq):
# 			n = len(can)
# 			if n==0 or k<=0 or target<=0: return
			
# 			for i in range(n):
# 				if can[i]==target:
# 					if k==1: res.append(seq+[target])
# 					else: break
# 				elif can[i]>target:
# 					break
# 				else: #can[i]<target
# 					dfs(can[i+1:], target-can[i], k-1, seq+[can[i]])
# 		can = range(1,10)
# 		res =[]
# 		dfs(can, n, k, [])
# 		return res


# 22. Generate Parentheses My Submissions Question
# Total Accepted: 76174 Total Submissions: 214866 Difficulty: Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"

# Subscribe to see which companies asked this question
# class Solution(object):
# 	def binaryTree_dfs(self, l,r,item, res):
# 		'''why binaryTree_dfs, because it is like binaryTree,
# 		you can go left or right or not, given situations, and 
# 		if you reach the bottom-both 0, you return the values'''
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

# class Solution(object):
# 	def generateParenthesis(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[str]
# 		"""
# 		def dfs(seq, lnum, rnum):
# 			if lnum>rnum: return
# 			if rnum==0:
# 				res.append(seq)
# 				return
# 			if lnum>=1:    
# 				dfs(seq+'(', lnum-1, rnum)
# 			if rnum>=1:    	
# 				dfs(seq+')', lnum, rnum-1)
# 			#you can coding like following, but the above is preffered!
# 			# # if rnum>=1:    	
# 			# dfs(seq+')', lnum, rnum-1)
		
# 		res =[]
# 		dfs('', n, n)
# 		return res
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.generateParenthesis(3)

# 37. Sudoku Solver My Submissions Question
# Total Accepted: 44889 Total Submissions: 187041 Difficulty: Hard
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.
# A sudoku puzzle...
# ...and its solution numbers marked in red.
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def solveSudoku(self, board):
# 		"""
# 		:type board: List[List[str]]
# 		:rtype: void Do not return anything, modify board in-place instead.
# 		"""
# 		self.dfs(board)
		
# 	def valid(self, board,x,y):
# 		tmp=board[x][y]
# 		board[x][y]='X'
# 		for i in range(9):
# 			if board[i][y]==tmp: return False
# 		for i in range(9):
# 			if board[x][i]==tmp: return False	

# 		for i in range(3):
# 			for j in range(3):
# 				if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
# 		#if it is true, we need to change back to original value tmp
# 		board[x][y]=tmp
# 		return True

# 	def dfs(self,board):
# 		for i in range(9):
# 			for j in range(9):
# 				if board[i][j] == '.':
# 					for x in '123456789':
# 						board[i][j] = x
# 						if self.valid(board,i,j) and self.dfs(board):
# 							return True
# 						board[i][j]='.'
# 					#if for one 1-9, there is no True, it means there will be False
# 					#so return False just after the for x '1-9' loop
# 					return False
# 		#to the end, if all are not '.', it is True; and should return True			
# 		return True


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
# 	def exist(self, board, word):
# 		"""
# 		:type board: List[List[str]]
# 		:type word: str
# 		:rtype: bool
# 		"""
		
# 		def dfs(board, x, y, word,m,n):
# 			if len(word)==0: return True
# 			if board[x][y] == word[0]:
# 				tmp=board[x][y]
# 				board[x][y]='@'
# 			else: return False
# 			if len(word)==1: return True
# 			#basically the same logic, but pruning via directly judgment board[x-1][y] == word[1], rather than
# 			#board[x-1][y] != '@' will speed up the code
# 			if x-1>=0 and board[x-1][y] == word[1] and dfs(board,x-1,y, word[1:],m,n):
# 				return True
# 			if x+1<=m-1 and board[x+1][y] == word[1] and dfs(board,x+1,y, word[1:],m,n):
# 				return True	
# 			if y+1<=n-1 and board[x][y+1]==word[1] and dfs(board,x,y+1, word[1:],m,n):
# 				return True	
# 			if y-1>=0 and board[x][y-1]==word[1] and dfs(board,x,y-1, word[1:],m,n):
# 				return True		
# 			#whenever dfs not working at this level, set it up to the orignal value
# 			board[x][y]=tmp
# 			return False
		
# 		m = len(board)
# 		n= len(board[0])
# 		for i in range(m):
# 			for j in range(n):
# 				if dfs(board,i,j,word,m,n):
# 					return True
# 		return False
		

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCCED")


# class Solution(object):
# 	def exist(self, board, word):
# 		"""
# 		:type board: List[List[str]]
# 		:type word: str
# 		:rtype: bool
# 		"""
# 		def dfs(board, visit,i,j,m,n, lst):
# 			#lst is new-cutted lst, visit is a reference, board is refernce
# 			if len(lst)==0: return True
# 			ix,iy=i,j
# 			# print visit
# 			if ix-1>=0 and board[ix-1][iy] == lst[0] and visit[ix-1][iy]!=1:
# 				visit[ix-1][iy] = 1
# 				if dfs(board, visit, ix-1, iy,m,n, lst[1:]): return True
# 				else: visit[ix-1][iy]=0 
# 			if ix+1<=m-1 and board[ix+1][iy] == lst[0] and visit[ix+1][iy]!=1:
# 				visit[ix+1][iy] = 1
# 				if dfs(board, visit, ix+1, iy,m,n, lst[1:]): return True
# 				else: visit[ix+1][iy]=0 
# 			if iy-1>=0 and board[ix][iy-1] == lst[0] and visit[ix][iy-1]!=1:
# 				visit[ix][iy-1] = 1
# 				if dfs(board, visit, ix, iy-1,m,n, lst[1:]): return True
# 				else: visit[ix][iy-1]=0 
# 			if iy+1<=n-1 and board[ix][iy+1] == lst[0] and visit[ix][iy+1]!=1:
# 				visit[ix][iy+1] = 1
# 				if dfs(board, visit, ix, iy+1,m,n, lst[1:]): return True
# 				else: visit[ix][iy+1]=0       
# 			# visit[ix-1][iy]=0 
# 			return False
				   
					
			
# 		lst = list(word)
# 		if len(lst)==0: return True
# 		#lst limit here?
# 		m = len(board)
# 		if m==0: return False
# 		n = len(board[0])
# 		if n==0: return False
# 		visit = [[0 for j in range(n)] for i in range(m)]
		
# 		for i in range(m):
# 			for j in range(n):
# 				if board[i][j] == lst[0]:
# 					visit[i][j]=1
# 					res = dfs(board, visit, i,j,m,n,lst[1:])
# 					if res: return True
# 					else:
# 						visit[i][j]=0
# 						continue
# 		# print 'visit board finally is', visit
# 		return False

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCCED")
		
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
# 	def findWords(self, board, words):
# 		"""
# 		:type board: List[List[str]]
# 		:type words: List[str]
# 		:rtype: List[str]
# 		"""
# 		def dfs(board, i, j, word,m,n):
# 			if len(word)<=1: return True
# 			#you can go in, then board[i][j]= word[0]
# 			tmp=board[i][j]
# 			board[i][j]='*'
# 			if i-1>=0 and board[i-1][j] == word[1] and dfs(board,i-1,j,word[1:],m,n):
# 				board[i][j] = tmp
# 				return True
# 			if i+1<=m-1 and board[i+1][j] == word[1] and dfs(board,i+1,j,word[1:],m,n):
# 				board[i][j] = tmp
# 				return True	
# 			if j+1<=n-1 and board[i][j+1] == word[1] and dfs(board,i,j+1,word[1:],m,n):
# 				board[i][j] = tmp
# 				return True		
# 			if j-1>=0 and board[i][j-1] == word[1] and dfs(board,i,j-1,word[1:],m,n):
# 				board[i][j] = tmp
# 				return True			
# 			board[i][j] = tmp
# 			return False


# 		m=len(board)
# 		n=len(board[0])
# 		res=[]
# 		#cannot pass timelimit for longer words list,
# 		#need better pruning for this
# 		for word in words:
# 			# board_new=copy.deepcopy(board)
# 			for i in range(m):
# 				for j in range(n):
# 					if board_new[i][j] == word[0]:
# 						if dfs(board_new,i,j,word,m,n):
# 							res.append(word)
# 		return list(set(res))





# #         		                                                                