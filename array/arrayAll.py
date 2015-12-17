# Remove Element
# Total Accepted: 90410 Total Submissions: 278908 Difficulty: Easy
# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} val
#     # @return {integer}
#     def removeElement(self, nums, val):
#     	if len(nums) == 0: return 0
#     	#the piont is that how to manage array in place and with S_O(1)??
#     	#use while loop, point to each index, and use pop to remove the responding element
#     	#tracking the index pos and the length of the array dynamically
#     	#method 1: remove the matched ele
#         i = 0
#         count = len(nums)
#         while i < count:
#         	if nums[i] == val:
#         		#nums.pop(i)#this might reduce the speed
#         		del nums[i]
#         		count -= 1
#         	else:
#         		i += 1	
#         return count
#         #method ??: move all the element ahead--but for array, each time it can take up to T_O(n), so totally T_O(n^2)
        


# Next Permutation 
# Total Accepted: 53088 Total Submissions: 208120 Difficulty: Medium
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 to 1,3, 2
# 3,2,1 to  1,2,3
# 1,1,5  to 1,5,1
# Subscribe to see which companies asked this question
#for example the order of {1,2,3} is : 123, 132, 213, 231,312, 321

# Show Tags
# Show Similar Problems
#12345 is the smallest, and 54321 is the biggest
#so image a number and its next, from right side, find the 1st digit X that is
#smaller than its right, --because other than this digit on the right , it is like 54321-the biggest
#then find the one Y just bigger than X, next time,  it will be starting from Y, and swtich the two, and then
#do the revsering order of these digits on the right (because it is already sorted, no need for sorting, just reversing)
#what if there is an euqal? we need to find the Y strictly > X

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        TO(n),SO(1)
        """
        xpos = None
        len_nums = len(nums)
        for i in range(len_nums-2,-1,-1):
        	if nums[i] < nums[i+1]:
        		xpos = i
        		break
        if xpos is None:
        	#reverse and return
        	#whenever(no matter which name you named) you make an new assignment( '=' + a variable name), it will be a local variable inside the function!!seriously about this!
        	#to reverse in place, has to switch the two in the array itself!
        	end = len_nums/2
        	for i in range(end):
        		nums[i], nums[len_nums-1-i] = nums[len_nums-1-i], nums[i]
        	return
        
        X = nums[xpos]
        for i in range(len_nums-1,xpos,-1):
        	if nums[i] > X:
        		ypos = i
        		break
        #switch
        tmp = nums[xpos]
        nums[xpos] = nums[ypos]
        nums[ypos] = tmp
        #reverse the rest
        end2 = (len_nums-(xpos+1))/2
        for i in range(end2):
        	#to reverse in place, has to switch the two in the array itself!
        	#Note could use the switch at the same time to save time, and be succint
        	#python will first grab the right two, get values, and then assign to the left two, SO 	THERE IS NO MESS UP
        	nums[xpos+1+i],nums[len_nums-1-i] = nums[len_nums-1-i], nums[xpos+1+i] 
        # print nums
        return 

if __name__ == '__main__':
	sk  = Solution()
	s = [1,3,2]
	sk.nextPermutation(s)
	print s

	s = [3,2,1]
	sk.nextPermutation(s)
	print s

# 4Sum My Submissions Question
# Total Accepted: 56316 Total Submissions: 250031 Difficulty: Medium
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie a<= b<= c <= d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
# Subscribe to see which companies asked this question



# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """



# Permutation Sequence My Submissions Question
# Total Accepted: 44522 Total Submissions: 186765 Difficulty: Medium
# The set [1,2,3,..,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

# Subscribe to see which companies asked this question



# class Solution(object):
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """

# Valid Sudoku My Submissions Question
# Total Accepted: 57231 Total Submissions: 199636 Difficulty: Easy
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# Subscribe to see which companies asked this question                

# class Solution:
# 	# @param {character[][]} board
# 	# @return {boolean}
# 	def isValidSudoku(self, board):
# 		res = True
# 		for i in range(9):
# 			tmp = []
# 			for j in range(9):
# 				if board[i][j] != '.': #and board[i][j]>=1 and board[i][j]<=9:
# 					if board[i][j] not in tmp:
# 						tmp.append(board[i][j])
# 					else:
# 						res = False
# 						return res
# 		for i in range(9):
# 			tmp = []
# 			for j in range(9):
# 				if board[j][i] != '.':# and board[j][i]>=1 and board[j][i]<=9:
# 					if board[j][i] not in tmp:
# 						tmp.append(board[j][i])
# 					else:
# 						res = False
# 						return res
		
# 		#ssquare = []
# 		for i in range(3):
# 			for j in range(3):
# 				s0 = board[(3*i):(3*i+3)]
# 				ss = []
# 				for item in s0:
# 					ss= ss + item[(3*j):(3*j+3)]
# 				tmp = []
# 				for item in ss:
# 					if item != '.':# and item>=1 and item<=9:
# 						if item not in tmp:
# 							tmp.append(item)
# 						else:
# 							res = False
# 							return res
# 		return res	



# Trapping Rain Water My Submissions Question
# Total Accepted: 54854 Total Submissions: 176832 Difficulty: Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Subscribe to see which companies asked this question


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
        


# Rotate Image My Submissions Question
# Total Accepted: 54462 Total Submissions: 164249 Difficulty: Medium
# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

# Subscribe to see which companies asked this question

# Show Tags

# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """



# Plus One My Submissions Question
# Total Accepted: 76780 Total Submissions: 241904 Difficulty: Easy
# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# Discuss

# class Solution:
# 	def plusOne(self, digits):  
# 		up = 1
# 		for i in range(len(digits)-1, -1, -1):
# 			if digits[i] + up == 10:
# 				digits[i] = 0
# 				up = 1
# 			elif i != len(digits) - 1 and up == 0:
# 				break
# 			else:	
# 				digits[i] = digits[i] + 1
# 				up = 0 
			
# 		if up == 1:
# 			digits.insert(0,1)
# 		return digits



# Climbing Stairs My Submissions Question
# Total Accepted: 84084 Total Submissions: 236761 Difficulty: Easy
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Subscribe to see which companies asked this question

# Show Tags
# Have you met this question in a real interview? Yes  No
# Discuss

# class Solution:
#     # @param {integer} n
#     # @return {integer}
#     global mm
#     mm = {}
#     mm[0] = 1
#     mm[1] = 1
#     def climbStairs(self, n):
#     	if n == 0:
#     		return mm[0]
#     	if n == 1:
#     		return mm[1]
#     	if n-1 not in mm:
#     		res1 = self.climbStairs(n-1)
#     		mm[n-1] = res1
#     	if n-2 not in mm:
#     		res2 = self.climbStairs(n-2)
#     		mm[n-2] = res2

#     	return mm[n-1] + mm[n-2]
    
# Gray Code My Submissions Question
# Total Accepted: 48915 Total Submissions: 142225 Difficulty: Medium
# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.

# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

# Subscribe to see which companies asked this question


# class Solution(object):
#     def grayCode(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """


# Set Matrix Zeroes My Submissions Question
# Total Accepted: 53816 Total Submissions: 166394 Difficulty: Medium
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# Discuss

# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """

# Gas Station My Submissions Question
# Total Accepted: 52562 Total Submissions: 198745 Difficulty: Medium
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

# Subscribe to see which companies asked this question

# Show Tags

# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         """
#         :type gas: List[int]
#         :type cost: List[int]
#         :rtype: int
#         """

# Candy My Submissions Question
# Total Accepted: 45474 Total Submissions: 211263 Difficulty: Hard
# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Subscribe to see which companies asked this question

# Show Tags

# class Solution(object):
#     def candy(self, ratings):
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """

# Single Number My Submissions Question
# Total Accepted: 103759 Total Submissions: 218673 Difficulty: Medium
# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# class Solution:
#     # @param A, a list of integer
#     # @return an integer
#     def singleNumber(self, A):
#     	#if len(A) == 0: return None
#         res = 0
#         for a in A:
#             res = res ^ a
#         return res

# Single Number II My Submissions Question
# Total Accepted: 69349 Total Submissions: 191750 Difficulty: Medium
# Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Subscribe to see which companies asked this question

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         t1 = 0
#         t2 = 0
#         t3 = 0
#         for a in nums:
#             t2 = t2|(a&t1)
#             t1 = t1^a
#             t3 = t1&t2
#             t1 = t1&(~t3)
#             t2 = t2&(~t3)
#         return t1

# Remove Duplicates from Sorted Array My Submissions Question
# Total Accepted: 98967 Total Submissions: 309169 Difficulty: Easy
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

# Subscribe to see which companies asked this question


# # Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# # Do not allocate extra space for another array, you must do this in place with constant memory.

# # For example,
# # Given input array nums = [1,1,2],

# # Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def removeDuplicates(self, nums):
#     	'''in place algorithm, cannot make a new array'''
#     	if len(nums) == 0 or len(nums) == 1:
#     		return len(nums)
#     	pres = nums[0]
#     	i = 1
#     	while i <= len(nums)-1:
#     		#print 'the pres now is :',  pres
#     		#print 'the index i is:', i
#     		if nums[i] == pres:
#     			#print 'the pop out number is : ', nums.pop(i) 
#     			nums.pop(i)
#     		else:
#     			pres = nums[i]
#     			i += 1
#     	return len(nums)
    	

# Remove Duplicates from Sorted Array II My Submissions Question
# Total Accepted: 60220 Total Submissions: 191996 Difficulty: Medium
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        

# Search in Rotated Sorted Array II My Submissions Question
# Total Accepted: 51852 Total Submissions: 165205 Difficulty: Medium
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

# Subscribe to see which companies asked this question


# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """
        
# Search in Rotated Sorted Array My Submissions Question
# Total Accepted: 82275 Total Submissions: 280662 Difficulty: Hard
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Subscribe to see which companies asked this question


# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
        

# Median of Two Sorted Arrays My Submissions Question
# Total Accepted: 76033 Total Submissions: 430337 Difficulty: Hard
# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Subscribe to see which companies asked this question

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
        

# Longest Consecutive Sequence My Submissions Question
# Total Accepted: 54947 Total Submissions: 178939 Difficulty: Hard
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        

# Two Sum My Submissions Question
# Total Accepted: 164673 Total Submissions: 834667 Difficulty: Medium
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# Subscribe to see which companies asked this question

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        

# 3Sum My Submissions Question
# Total Accepted: 89729 Total Submissions: 509590 Difficulty: Medium
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},

#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
        

# 3Sum Closest My Submissions Question
# Total Accepted: 60330 Total Submissions: 217255 Difficulty: Medium
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """












