# 120. Triangle My Submissions Question
# Total Accepted: 62417 Total Submissions: 212709 Difficulty: Medium
# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# class Solution(object):
# 	def minimumTotal(self, triangle):
# 		"""
# 		:type triangle: List[List[int]]
# 		:rtype: int
# 		"""
# 		#n is the # of rows of the triangle, shoot for TO(n^2), and SO(n)
# 		n=len(triangle)
# 		if n==0: return 0
# 		array=[triangle[0][0]]
# 		#for rows from second to the last
# 		for i in range(1,n):
# 			m = len(triangle[i])
# 			#j is the index for each row, from 0 to m-1
# 			new_array=[]
# 			for j in range(m):
# 				if j==0: new_array.append(array[0]+triangle[i][j]) 
# 				elif j<m-1:
# 					new_array.append(min(array[j-1], array[j])+triangle[i][j])
# 				else: #j=m-1
# 					new_array.append(array[j-1]+triangle[i][j])
# 			array = new_array
# 		return min(array)

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.minimumTotal([
# 	 [2],
# 	[3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# )

# 53. Maximum Subarray My Submissions Question
# Total Accepted: 97791 Total Submissions: 271579 Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example given the array [-2, 1,-3,4,-1,2,1,-5,4]
# the contiguous subarray [4,-1,2,1]has the largest sum = 6
# click to show more practice.
# Subscribe to see which companies asked this question
# class Solution(object):
# 	def maxSubArray(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		'''first research on different conditions and make it clear and logic, and then
# 		refine the code for brief and beautifulness
# 		1)for different conditions os sucSum+xi >0 or <=0; 2)and then for sucSum<=0 and >0'''
# 		n = len(nums)
# 		if n==0: return None
		
# 		total = nums[0]
# 		sucSum = nums[0]
# 		for i in range(1,n):
# 			if sucSum+nums[i]>0:
# 				sucSum = sucSum + nums[i] if sucSum>0 else nums[i]
# 			else:
# 				sucSum = nums[i]				
# 			total = max(total, sucSum)
# 		return total

# class Solution(object):
# 	def maxSubArray(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		greedy method
# 		add all positive from the beginning, if at some point, the total is <0, that means until this part
# 		there is no contribution to the final result, so reset total = 0
# 		total = 0
# 		cur_max = max(nums)
# 		for i in nums:
# 			total += i
# 			if total > cur_max: cur_max = total
# 			if total >0: continue
# 			else: total = 0
# 		return cur_max
		
# 		dp method:
# 		we set--restrict set the array[j] -- as the max arrary that ends with array[j]
# 		and we know that at least one of the array would be the final result--because you have to end with one element of the array
# 		n=len(nums)
# 		if n==0: return 0
# 		f = nums[0]
# 		res = f
# 		for i in range(1, n):
# 			f = max(f+nums[i], nums[i])
# 			res= max(res, f)
# 		return res

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


# 132. Palindrome Partitioning II My Submissions Question
# Total Accepted: 46174 Total Submissions: 217410 Difficulty: Hard
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Subscribe to see which companies asked this question
# Show Tags
# # Show Similar Problems

# class Solution(object):
# 	def minCut(self, s):
# 		"""
# 		:type s: str
# 		:rtype: int
# 		"""
# 		# self set index for myself, now has length of n for dp, not n+1
# 		#dp problem
# 		n=len(s)
# 		#set all ele of is_pan to False first
# 		is_pan = [[False for i in range(n)] for j in range(n)] #save two dimension isPan or not
# 		#update is_pan
# 		# for i in range(n): is_pan[i][i] = True
# 		#set dp's all element to the max of each first
# 		#if you have n letters, the maximum cut is n-1
# 		#why one cell more, and  add 1 to all?
# 		dp = [i-1 for i in range(n,0,-1)] #save one dimension, about the min cut

# 		for i in range(n-1, -1, -1):
# 			#each outside loop check one i
# 			for j in range(i, n):
# 				# print i
# 				#the string between i and  j is panlindrome or not
# 				if s[i]==s[j] and (i+1>j-1 or is_pan[i+1][j-1]):
# 					is_pan[i][j]=True
# 					#each outside loop check one i, and update only the i based on all the information we have done/computed
# 					# print i,j+1
# 					if j==n-1:
# 						dp[i] = min(dp[j+1]+1, dp[i])
# 					else:
# 						dp[i] = min(0, dp[i])
# 		# print dp
# 		return dp[0]

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.minCut("aab")
# 	print sk.minCut("aabb")


# 85. Maximal Rectangle My Submissions Question
# Total Accepted: 38061 Total Submissions: 165316 Difficulty: Hard
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def maximalRectangle(self, matrix):
# 		"""
# 		:type matrix: List[List[str]]
# 		:rtype: int
# 		"""
# 		m=len(matrix)
# 		if m==0: return 0
# 		n=len(matrix[0])
# 		if n==0: return 0
# 		array = [0 for j  in range(n+1)] #add n+1 not n here to add 0 to each row, to make computing the area right
# 		area = 0
# 		for i in range(m):
# 			for j in range(n):
# 				array[j] = array[j] + 1 if matrix[i][j]	==1 else 0
# 				area=max(area, self.help(array))
# 		return area
	
# 	def help(self, array):
# 		# newarray=array[:]
# 		# newarray.append(0)
# 		# stack =[array[0]]
# 		index_stack=[0]   	
# 		area = 0
# 		for i in range(1,len(array)):
# 			if array[i]>array[index_stack[-1]]:
# 				index_stack.append(i)
# 				# stack.append(array[i])
# 			else:# array[i]<array[index_stack[-1]]:
# 				while len(index_stack) != 0 and array[i] < array[index_stack[-1]]:
# 					tmp_height=array[index_stack[-1]]
# 					tmp_index=index_stack.pop(-1)
# 					area = max(area, tmp_height*(i-tmp_index))
# 				# stack.append(array[i])
# 				index_stack.append(i)
# 		return area

# if __name__ == '__main__':
# 	sk = Solution()
# 	# print sk.maximalRectangle([[0,1,0],[0,1,1],[0,1,0]])
# 	print sk.maximalRectangle([1])

# class Solution(object):
# 	def maximalRectangle(self, matrix):
# 		"""
# 		:type matrix: List[List[str]]
# 		:rtype: int
# 		"""
# 		n = len(matrix)
# 		if n==0: return 0
# 		m = len(matrix[0])
# 		if m==0: return 0
# 		adjArray = [0 for k in range(m)]
# 		area = 0 
# 		for i in range(n):
# 			array = matrix[i]
# 			adjArray = [adjArray[j]+1 if int(array[j])==1 else 0 for j in range(m)]
# 			area = max(area, self.curArea(adjArray) )
# 		return area
		
# 	def curArea(self, array):
# 		'''compute the current area for the array using the filtering trick'''
# 		val = array+[0]
# 		# n = len(val)
# 		indStack = []
# 		heStack = []
# 		area = 0
# 		# print 'the array is', val
# 		for i in range(len(val)):
# 			if len(heStack)==0 or val[i]>= heStack[-1]:
# 				indStack.append(i)
# 				heStack.append(val[i])
# 			else: 
# 				while len(heStack)>0 and val[i]<heStack[-1]:
# 					tmpHe = heStack.pop(-1)
# 					tmpIdx = indStack.pop(-1) 
# 					area = max(area, tmpHe*(i-tmpIdx))
# 				#add i
# 				heStack.append(val[i])
# 				indStack.append(tmpIdx)
# 		return area
		
# if __name__ == '__main__':
# 	sk = Solution()
# 	# print sk.maximalRectangle([[0,1,0],[0,1,1],[0,1,0]])
# 	# print sk.maximalRectangle([[1]])
# 	# print sk.maximalRectangle([[int(j) for j in i] for i in ["10100","10111","11111","10010"]]),'right:6'
# 	# print sk.maximalRectangle([[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,1,1,1,1]]),'right:6'
# 	print sk.maximalRectangle(["10100","10111","11111","10010"])

# 123. Best Time to Buy and Sell Stock III My Submissions Question
# Total Accepted: 51305 Total Submissions: 200248 Difficulty: Hard
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again)
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         #because if transaction twice, then for an index, one happens before, and one happens after
#         #forward and backward to reduce the computational cost
#         #forward once and backward once, and get the value for each point
#         #and count the sum of the backward and forward value in total, get the maximum
#         n = len(prices)
#         if n <=1: return 0
#         forward = [0]
#         #forward count each index(including), and forward[0]=0
#         valley = prices[0]
#         for i in range(1,n):
#         	#update valley value
#         	valley=min(valley, prices[i])
#         	#at each index, either it is the last gain value, or the current price value - valley, so take minimum
#         	forward.append(max(prices[i]-valley, forward[-1]))
#         peak = prices[-1]
#         backward=[0]
#         for i in range(n-2,-1,-1):
#         	#when backward, updated peak
#         	peak = max(peak, prices[i])
#         	#at each index, either peak-current price, or last backward value, return max of them
#         	backward.insert(0, max(peak-prices[i], backward[0]))
#         print forward
#         print backward	
#         res = 0
#         for i in range(n):
#         	res= max(res, forward[i] + backward[i])

#         return res
# if __name__ == '__main__':
# 	sk  = Solution()
# 	print sk.maxProfit([2,1,2,0,1])

		

# 97. Interleaving String My Submissions Question
# Total Accepted: 45241 Total Submissions: 205565 Difficulty: Hard
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Subscribe to see which companies asked this question

# Show Tags

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         '''
#         hard quesions are all 2-dimension dp Problems;
#         sometimes  use space to exchange for time
#         '''
#         n1=len(s1)
#         n2=len(s2)
#         n3=len(s3)
#         if n1+n2 != n3: return False
#         #we record n1+1 cols and n2+1 rows
#         array=[[False for i in range(n1+1)] for j in range(n2+1)]
#         array[0][0] = True
#         #initialize
#         for i in range(1,n1+1):
#         	if array[0][i-1] and s3[i-1] == s1[i-1]: array[0][i]=True        	
#         for j in range(1,n2+1):
#         	if array[j-1][0] and s3[j-1] == s2[j-1]: array[j][0] = True

#         #dp process to fill in all the values
#         for i in range(1, n1+1):
#         	for j in range(1,n2+1):
#         		if (array[j-1][i] and s3[i+j-1]==s2[j-1]) or (array[j][i-1] and s3[i+j-1] == s1[i-1]):
#         			array[j][i] = True
#        	return array[-1][-1]

# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.isInterleave("aabcc","dbbca","aadbbcbcac")
# 	print sk.isInterleave("aabcc","dbbca","aadbbbaccc")







# 87. Scramble String My Submissions Question
# Total Accepted: 42305 Total Submissions: 162870 Difficulty: Hard
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
# # Subscribe to see which companies asked this question

# class Solution(object):
# 	def isScramble(self, s1, s2):
# 		"""
# 		:type s1: str
# 		:type s2: str
# 		:rtype: bool
# 		"""
# 		#we use dfs here
# 		#the problem here is that as long as it is divided substring, it will work
# 		#not necessary to be around half
# 		n1=len(s1)
# 		n2=len(s2)
# 		if n1 != n2: return False
# 		if s1==s2: return True
# 		#prunning by count letters
# 		dct={}
# 		for i in range(n1):
# 			if s1[i] not in dct:
# 				dct[s1[i]] = 1
# 			else: dct[s1[i]] += 1
# 			if s2[i] not in dct:
# 				dct[s2[i]] = -1
# 			else:
# 				dct[s2[i]] -= 1
# 		for key in dct:
# 			if dct[key] != 0: return False
# 		# l1=list(s1)
# 		# l2=list(s2)
# 		# l1.sort()
# 		# l2.sort()
# 		# if l1 != l2: return False

# 		#because any no-empty substring divide
# 		for i in range(1,n1):
# 			if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:],s2[i:])):
# 				return True
# 			if (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
# 				return True
# 		return False

# if __name__ == '__main__':
# 	sk = Solution()
# 	# print sk.isScramble('great','rgeat')		 
# 	# print sk.isScramble('great','great')		 
# 	# print sk.isScramble('great','abcde')		 
# 	# print sk.isScramble('great','rgtea')
# 	# print sk.isScramble('great','eatgr')		 
# 	# print sk.isScramble('great','eatrg')
# 	print sk.isScramble("abcdefghijklmn","efghijklmncadb")		 
# 	print sk.isScramble("ab","ba")		 

# class Solution(object):
# 	def isScramble(self, s1, s2):
# 		"""
# 		:type s1: str
# 		:type s2: str
# 		:rtype: bool
# 		"""
# 		#we use dfs here
# 		#the problem here is that as long as it is divided substring, it will work
# 		#not necessary to be around half
# 		n1 = len(s1)
# 		n2 = len(s2)
# 		if n1 != n2: return False
# 		if n1==0: return True
# 		if n1==1 and s1!=s2: return False
# 		if s1==s2: return True
		
# 		###prunning
# 		dct={}
# 		for i in range(n1):
# 			if s1[i] in dct: dct[s1[i]] +=1
# 			else: dct[s1[i]] = 1
# 		for j in range(n2):
# 			if s2[j] in dct: dct[s2[j]] -=1
# 			else: return False
# 		for key in dct:
# 			if dct[key] != 0: return False
			
# 		#recursion
# 		for i in range(1,n1):
# 			if (self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[0:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
# 				return True
			
	   
# 		#overall and afterall, return False     
# 		return False     
			

# 64. Minimum Path Sum My Submissions Question
# Total Accepted: 62940 Total Submissions: 184697 Difficulty: Medium
# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         #dp problem
#         m = len(grid)
#         n = len(grid[0])
#         if m==0 or n==0: return 0
#         dp= [[0 for i in range(n)] for j in range(m)]
#         dp[0][0] = grid[0][0]
#         for i in range(1,n):
#         	dp[0][i] = dp[0][i-1] + grid[0][i]
#         for j in range(1,m):
#         	dp[j][0] = dp[j-1][0] + grid[j][0]
#         for j in range(1,m):
#         	for i in range(1,n):
#         		dp[j][i] = min(dp[j-1][i], dp[j][i-1])+grid[j][i]
#        	return dp[-1][-1]

# class Solution(object):
# 	def minPathSum(self, grid):
# 		"""
# 		:type grid: List[List[int]]
# 		:rtype: int
# 		"""
# 		m = len(grid)
# 		if m==0: return 0
# 		n = len(grid[0])
# 		if n==0: return 0
# 		dp = [[0 for j in range(n)] for i in range(m)]
# 		dp[0][0] = grid[0][0]
# 		for j in range(1,n): dp[0][j] = dp[0][j-1] + grid[0][j]
# 		for i in range(1,m): dp[i][0] = dp[i-1][0] + grid[i][0]
		
# 		for j in range(1,m):
# 		    for i in range(1,n):
# 		        dp[j][i] = min(dp[j-1][i], dp[j][i-1]) + grid[j][i]
# 		return dp[m-1][n-1]
		    		

# 72. Edit Distance My Submissions Question
# Total Accepted: 52314 Total Submissions: 187031 Difficulty: Hard
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character

# class Solution(object):
# 	def minDistance(self, word1, word2):
# 		"""
# 		:type word1: str
# 		:type word2: str
# 		:rtype: int
# 		"""
# 		#dp problem 
# 		#min([i-1][j-1],[i][j-1],[i-1][j])
# 		n=len(word1)
# 		m=len(word2)
# 		#initialize
# 		dp= [[0 for i in range(n+1)] for j in range(m+1)]
# 		for i in range(1,n+1):
# 			dp[0][i] = i
# 		for j in range(1,m+1):
# 			dp[j][0] = j

# 		#main dp loop
# 		for j in range(1,m+1):
# 			for i in range(1,n+1):
# 				if word1[i-1] == word2[j-1]:
# 					dp[j][i] = dp[j-1][i-1]
# 				else:
# 					dp[j][i] = min(dp[j-1][i-1],dp[j-1][i],dp[j][i-1])+1

# 		return dp[-1][-1]


# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.minDistance('ed','e')        
		
# 91. Decode Ways My Submissions Question
# Total Accepted: 61299 Total Submissions: 357609 Difficulty: Medium
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         #because of 0 to become illegal, there are more logic judgment in the code
#         n= len(s)
#         if n==0: return 0
#         if int(s[0]) == 0 : return 0
#         if n==1: return 1
		
#         dp = [0 for i in range(n+1)]
#         dp[0], dp[1]= 1, 1
#         #following i is index for s
#         for i in range(1,n):
#         	if int(s[i])==0 and (int(s[i-1])<1 or int(s[i-1])>2):
#         		return 0
#         	elif int(s[i])==0 and (int(s[i-1])>=1 and int(s[i-1])<=2):
#         		dp[i+1]=dp[i-1]
#         	elif int(s[i-1:i+1])>26 or int(s[i-1])==0:
#         		dp[i+1]=dp[i]        		
#         	else:
#         		dp[i+1] = dp[i-1]+dp[i]
#         return dp[-1]

# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.numDecodings('123')
# 	print sk.numDecodings('30')
# 	print sk.numDecodings('0123')

# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         #because of 0 to become illegal, there are more logic judgment in the code
#         #the following is a much  better way, with clear logic
#         n= len(s)
#         if n==0: return 0
#         if s[0]=='0': return 0 
#         dp = [0  for i in range(n+1)]
#         dp[0]=1 #index as 0, empty string here
#         dp[1]=1
        
#         for i in range(2,n+1):
#         	#if only count the current number
#             part1=0
#             if int(s[i-1]) ==0: part1 = 0
#             else: part1 = dp[i-1]
            
#             #if count the current + the previous numbers
#             part2=0
#             if int(s[i-2])==1: part2 = dp[i-2]
#             if int(s[i-2])==2 and int(s[i-1])<=6: part2 = dp[i-2]
#             dp[i]= part1 + part2
        
#         return dp[-1]		

# 115. Distinct Subsequences My Submissions Question
# Total Accepted: 46914 Total Submissions: 166243 Difficulty: Hard
# Given a string S and a string T, count the number of distinct subsequences of T in S.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Here is an example:
# S = "rabbbit", T = "rabbit"
# Return 3.

# Subscribe to see which companies asked this question

# class Solution(object):
# 	def numDistinct(self, s, t):
# 		"""
# 		:type s: str
# 		:type t: str
# 		:rtype: int
# 		"""
# 		#n*m time
# 		ns = len(s)
# 		nt = len(t)
# 		dp = [[0 for i in range(ns+1)] for j in range(nt+1)]
# 		#initialize
# 		for i in range(ns+1): dp[0][i] = 1
# 		#main loop
# 		for j in range(1,nt+1):
# 			for i in range(1,ns+1):
# 				if t[j-1] == s[i-1]:
# 					#index's problem: it represents that how to change from one end to the other end
# 					#in this problem it is from s to t
# 					#the tips are: typically three ways to draw arrows, you draw them,and try to explain how each one means;
# 					#you pick the one that stands right; in this problem, it is changing from the row string and ends with the column string point
# 					dp[j][i] = dp[j][i-1]+dp[j-1][i-1]
# 				else:
# 					dp[j][i] = dp[j][i-1]
# 		return dp[nt][ns]


# 		# the following would be n^3 time, which is expensive in some way
# 		# ns = len(s)
# 		# nt = len(t)
# 		# if nt==0: return 1
# 		# dp = []
# 		# for letter in t:
# 		# 	array = []
# 		# 	for i in range(ns):
# 		# 		if letter == s[i]:
# 		# 			array.append(i)
# 		# 	if not array: return 0
# 		# 	dp.append(array)
# 		# # print dp
# 		# a0 = dp[0]
# 		# # print nt	
# 		# for i in range(1, nt):
# 		# 	# print i
# 		# 	array = dp[i]
# 		# 	new_array=[]
# 		# 	for ele in array:
# 		# 		for item in a0:
# 		# 			if ele>item: new_array.append(ele)
# 		# 			else: break
# 		# 	a0=new_array
# 		# return len(a0)
# if __name__ == '__main__':
# 	sk  =Solution()
# 	print sk.numDistinct('ac','')		
# 	print sk.numDistinct('acac','ac')
# 	print sk.numDistinct('rabbbit','rabit')		
# 	print sk.numDistinct('ddd','dd')		

# 139. Word Break My Submissions Question
# Total Accepted: 77794 Total Submissions: 317862 Difficulty: Medium
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def wordBreak(self, s, wordDict):
# 		"""
# 		:type s: str
# 		:type wordDict: Set[str]
# 		:rtype: bool
# 		"""
# 		n = len(s)
# 		dp = [False for i in range(n+1)]
# 		dp[0] = True

# 		for i in range(1, n+1):
# 			for j in range(i):
# 				if dp[j] and s[j:i] in wordDict:
# 					dp[i] = True
# 					break
# 		# print dp
# 		return dp[-1]
# if __name__ == '__main__':
# 	sk= Solution()
# 	print sk.wordBreak('lll',set(['l']))
# 	print sk.wordBreak('leetcode', set(['leet','code']))

#more complicated way
# class Solution(object):
# 	def wordBreak(self, s, wordDict):
# 		"""
# 		:type s: str
# 		:type wordDict: Set[str]
# 		:rtype: bool
# 		"""
# 		n=len(s)
# 		if n<=1: 
# 		    if s in wordDict: return True
# 		    else: return False
# 		dp =[False for i in range(n)]
# 		dp[0] = True if s[0] in wordDict else False
		
# 		for i in range(n):
# 		    if s[:i+1] in wordDict: 
# 		        dp[i] = True
# 		        continue
# 		    for j in range(i):
# 		        if dp[j] and s[j+1:i+1] in wordDict:
# 		            dp[i] = True
# 		            break
# 		return  dp[-1]
#dfs can NOT pass time limit
#dfs is computing backwarding
#and dp is computing forwarding along the string
# def wordBreak(self, s, wordDict):
# 	    n = len(s)
# 	    if n<=1: 
# 	        if s in wordDict: return True
# 	        else: return False
# 	    #if length is n      
# 	    if s in wordDict: return True
# 	    for i in range(1,n):
# 	        if s[:i] in wordDict:
# 	            if self.wordBreak(s[i:], wordDict):
# 	                return True
# 	            else:
# 	                continue
# 	    return False   

# 140. Word Break II My Submissions Question
# Total Accepted: 50737 Total Submissions: 264698 Difficulty: Hard
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is ["cats and dog", "cat sand dog"].
# Subscribe to see which companies asked this question

#comments: the words in dict can be repeated infinite times
#the string s can only be segmented by space and by order
#use dp + dfs to solve the problem
#use dp to prune dfs to speed up
# class Solution(object):
# 	def wordBreak(self, s, wordDict):
# 		"""
# 		:type s: str
# 		:type wordDict: Set[str]
# 		:rtype: List[str]
# 		"""
# 		#this problem uses dfs + dp
# 		#1.you can either save the dp two dimension first, and use it later
# 		#2.you can dfs while pruning through dp checking
# 		return self.dfs(s,wordDict)

# 	def dyn_prog(self, s, wordDict):
# 		n=len(s)
# 		dp=[False for i in range(n+1)]
# 		dp[0] = True
# 		for i in range(1,n+1):
# 			for j in range(i):
# 				if dp[j] and s[j:i] in wordDict:				
# 					dp[i] = True
# 					break
# 		return dp[-1]

# 	def dfs(self, s, wordDict):
# 		'''dfs method, run each loop'''
# 		'''for dfs, you can either from bottom to up,like what I did here;
# 		or top down, like use string as each result and keep as an class variable'''
# 		if self.dyn_prog(s, wordDict):
# 			res = []
# 			if len(s)==0: return ['']
# 			for i in range(1,len(s)+1):
# 				if s[:i] in wordDict:
# 					if i != len(s):
# 						for item in self.dfs(s[i:], wordDict):
# 							res.append(s[:i] + ' ' + item)
# 					else:
# 						for item in self.dfs(s[i:], wordDict):
# 							res.append(s[:i] + item)

# 			return res
# 		else:
# 			return []


# 		#this will be exploded if there are too many options at the end
# 		#n^2*n at least in some cases
# 		# n = len(s)
# 		# dp = [False for i in range(n+1)]
# 		# dp[0] = True
# 		# res = [[] for i in range(n+1)]
# 		# res[0] = ['']
# 		# for i in range(1, n+1):
# 		# 	for j in range(i+1):
# 		# 		if dp[j] and s[j:i] in wordDict:
# 		# 			dp[i] = True
# 		# 			for item in res[j]:
# 		# 				if j==0:
# 		# 					res[i].append(item + s[j:i])
# 		# 				else:
# 		# 					res[i].append(item + ' ' + s[j:i])

# 		# return res[-1]
																										
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
# 	print sk.wordBreak("", ["cat", "cats", "and", "sand", "dog"])



