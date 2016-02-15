# 50. Pow(x, n) My Submissions Question
# Total Accepted: 80737 Total Submissions: 289959 Difficulty: Medium
# Implement pow(x, n).
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def myPow(self, x, n):
# 		"""
# 		:type x: float
# 		:type n: int
# 		:rtype: float
# 		"""	
# 		#divide and conquer: TO(logN), SO(1)
# 		#the recursion call loop doesnot cost Space memory
# 		#at each step, there is constant space cost, so totally there is constant space memory cost
# 		if n<0: return 1/self.myPow(x, -n)
# 		if n==0: return 1
# 		if n==1: return x
# 		half=self.myPow(x, n/2)
# 		left=1
# 		if n%2: left=x
# 		return half*half*left
		

# 69. Sqrt(x) My Submissions Question
# Total Accepted: 82986 Total Submissions: 336246 Difficulty: Medium
# Implement int sqrt(int x).

# Compute and return the square root of x.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# class Solution(object):
# 	def mySqrt(self, x):
# 		"""
# 		:type x: int
# 		:rtype: int
# 		"""
# 		#divide and conquer TO(logN), SO(1)
# 		if x==0 or x==1: return x
# 		#but the following would sig improve speed
# 		#if you use index and iteration method, it should be quicker!!
# 		if (x/2+1)*(x/2+1) ==x: return x/2+1
# 		return self.dfs(x, 1, x/2+1)
# 	def dfs(self, x, left, right):
# 		# if right*right==x: return right
# 		if left*left==x or (left*left<x and right*right>x and right-left==1): return left		
# 		half=(left+right)/2
# 		if half*half>x:
# 			return self.dfs(x, left, half)
# 		elif half*half<x:
# 			return self.dfs(x, half, right)
# 		else:
# 			return half

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.mySqrt(0)
# 	print sk.mySqrt(1)
# 	print sk.mySqrt(2)
# 	print sk.mySqrt(3)
# 	print sk.mySqrt(10)
# 	print sk.mySqrt(100)



# 55. Jump Game My Submissions Question
# Total Accepted: 69067 Total Submissions: 248316 Difficulty: Medium
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
# Subscribe to see which companies asked this question

# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n=len(nums)
#         #==1 is special
#         if n==1: return True
#         max_pre = nums[0]
#         #doesnot count the last step: since as long as you reach it, that is fine
#         for i in range(n-1):
#             max_pre = max(nums[i], max_pre-1)
#             if max_pre==0: return False
#         return True			


# 45. Jump Game II My Submissions Question
# Total Accepted: 57770 Total Submissions: 231958 Difficulty: Hard
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.
# Subscribe to see which companies asked this question
# class Solution(object):
# 	def jump(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		'''this greedy is really magic'''
# 		last=0
# 		res=0
# 		current=0
# 		for i in range(len(nums)):
# 			#the index is out of the last
# 			if i > last:
# 				#last will be the current reach
# 				last = current
# 				#min steps +1
# 				res += 1
# 			current = max(current, i+nums[i])
# 		return res

# 121. Best Time to Buy and Sell Stock My Submissions Question
# Total Accepted: 85081 Total Submissions: 242394 Difficulty: Medium
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# class Solution(object):
# 	def maxProfit(self, prices):
# 		"""
# 		:type prices: List[int]
# 		:rtype: int
# 		the tricky thing is that you can only do one buy and sell on the total dataset!!
# 		"""
# 		#easy: track the lowest price, and forward compute the profit at each step
# 		#if the profit exceed the current profit, replace it
# 		if len(prices) <= 1:
# 			return 0
# 		max_p = 0
# 		low = prices[0]
# 		for i in range(1,len(prices)):
# 			if prices[i] < low: 
# 			    low = prices[i]
# 			else:
# 			    max_p = max(max_p, prices[i] - low)
# 		return max_p

# 122. Best Time to Buy and Sell Stock II My Submissions Question
# Total Accepted: 76339 Total Submissions: 185235 Difficulty: Medium
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Subscribe to see which companies asked this question
# class Solution(object):
# 	def maxProfit(self, prices):
# 		"""
# 		:type prices: List[int]
# 		:rtype: int
# 		now you can do many times, but you need to sell before buy
# 		that is you maximize all the possible profit there: so the
# 		greedy is just all the gap between i and i-1

# 		"""
# 		max_profit  = 0
# 		for i in range(1,len(prices)):
# 			if prices[i] >= prices[i-1]:
# 				max_profit += prices[i] - prices[i-1]
		
# 		return max_profit
		

# 3. Longest Substring Without Repeating Characters My Submissions Question
# Total Accepted: 124955 Total Submissions: 583785 Difficulty: Medium
# Given a string, find the length of the longest substring without repeating characters. For example,
# the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
# Subscribe to see which companies asked this question


# class Solution(object):
# 	def lengthOfLongestSubstring(self, s):
# 		"""
# 		:type s: str
# 		:rtype: int
# 		"""
# 		#greedy method: focus on the local, and hope for the right as a whole
# 		dct = {}
# 		n = len(s)
# 		maxlen = 0
# 		res = 0
# 		last = 0
# 		for i in  range(n):
# 			if s[i] not in dct:
# 				dct[s[i]] = [i]
# 				res += 1
# 			else:
# 				if dct[s[i]][-1]>=last:
# 					maxlen = max(maxlen, res)
# 					res = i - dct[s[i]][-1]
# 					last = dct[s[i]][-1]+1
# 					dct[s[i]].append(i)
# 				else:
# 					dct[s[i]].append(i)
# 					res += 1
# 		return max(maxlen, res)


# 11. Container With Most Water My Submissions Question
# Total Accepted: 67377 Total Submissions: 199641 Difficulty: Medium
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container.

# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		#very smart and interesting solution
		res= 0
		left = 0
		right = len(height)-1
		while left < right:
			water = min(height[left], height[right])*(right-left)
			if water > res: res = water
			if height[left]<height[right]:
				left += 1
			else:
				right -= 1
		return res

		

#                                                 		                                