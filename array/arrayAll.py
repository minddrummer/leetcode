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
#				#inplace delete one element in the list: del lst[i]
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

# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         TO(n),SO(1)
#         """
#         xpos = None
#         len_nums = len(nums)
#         for i in range(len_nums-2,-1,-1):
#         	if nums[i] < nums[i+1]:
#         		xpos = i
#         		break
#         if xpos is None:
#         	#reverse and return
#         	#whenever(no matter which name you named) you make an new assignment( '=' + a variable name), it will be a local variable inside the function!!seriously about this!
#         	#to reverse in place, has to switch the two in the array itself!
#         	end = len_nums/2
#         	for i in range(end):
#         		nums[i], nums[len_nums-1-i] = nums[len_nums-1-i], nums[i]
#         	return
		
#         X = nums[xpos]
#         for i in range(len_nums-1,xpos,-1):
#         	if nums[i] > X:
#         		ypos = i
#         		break
#         #switch
#         tmp = nums[xpos]
#         nums[xpos] = nums[ypos]
#         nums[ypos] = tmp
#         #reverse the rest
#         end2 = (len_nums-(xpos+1))/2
#         for i in range(end2):
#         	#to reverse in place, has to switch the two in the array itself!
#         	#Note could use the switch at the same time to save time, and be succint
#         	#python will first grab the right two, get values, and then assign to the left two, SO 	THERE IS NO MESS UP
#         	nums[xpos+1+i],nums[len_nums-1-i] = nums[len_nums-1-i], nums[xpos+1+i] 
#         # print nums
#         return 

# if __name__ == '__main__':
# 	sk  = Solution()
# 	s = [1,3,2]
# 	sk.nextPermutation(s)
# 	print s

# 	s = [3,2,1]
# 	sk.nextPermutation(s)
# 	print s

# 4Sum 
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


# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         #method1: double close O(n^3)--but not good enough
#         # nums.sort()
#         # count = len(nums)
#         # if count <= 3: return []
#         # res= []
#         # for i in range(count-3):
#         # 	#it is not about speed first, it is more about the repeated/rightness about the algorithm
#         # 	#not adding the following will result in duplicates in the return res
#         # 	if i == 0 or nums[i]>nums[i-1]:
# 	       #  	for j in range(i+1, count-2):
# 	       #  		#it is not about speed first, it is more about the repeated/rightness about the algorithm
# 		      #   	#not adding the following will result in duplicates in the return res
# 	       #  		if j==i+1 or nums[j]>nums[j-1]:
# 		      #   		left,right = j+1, count-1
# 		      #   		while left < right:
# 		      #   			if nums[i]+nums[j]+nums[left]+nums[right] == target:
# 		      #   				res.append([nums[i],nums[j],nums[left],nums[right]])
# 		      #   				right -= 1
# 		      #   				#this part is not about speed, it is more about remove duplicates and debuging....
# 		      #   				while nums[right]==nums[right+1] and left<right: right -=1
# 		      #   				left +=1
# 		      #   				#this part is not about speed, it is more about remove duplicates and debuging....
# 		      #   				while nums[left] == nums[left-1] and left<right: left+=1
# 		      #   			elif nums[i]+nums[j]+nums[left]+nums[right] > target:
# 		      #   				right -= 1
# 		      #   				#this part is more about speed
# 		      #   				while nums[right]==nums[right+1] and left<right: right -=1
# 		      #   			else:
# 		      #   				left += 1
# 		      #   				#this part is more about speed
# 		      #   				while nums[left] == nums[left-1] and left<right: left+=1
#        	# return res


# class Solution(object):
# 	def find_pair(self,sum2,key1,key2,res,count):
# 		pair1=sum2[key1]
# 		pair2=sum2[key2]
# 		for item1 in pair1:
# 			for item2 in pair2:
# 				each_count = {}
# 				for each_num in item1+item2:
# 					if each_num in each_count:
# 						each_count[each_num] += 1
# 					else:
# 						each_count[each_num] = 1
# 				over_limit = False			
# 				for each_num in each_count:
# 					if each_count[each_num] > count[each_num]:
# 						over_limit=True
# 						break
# 				if not over_limit:
# 					final_key = sorted(item1+item2)
# 					res[tuple(final_key)] = final_key

# 	def fourSum(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: List[List[int]]
# 		"""
# 		nums.sort()
# 		total = len(nums)
# 		if total <= 3: return []
# 		if total == 4 and sum(nums)== target: return [nums]
# 		count = {}
# 		for i in nums:
# 			if i not in count: count[i] = 1
# 			else: count[i] += 1
		
# 		#generate unique pair of sum of two and save it to a hashtable
# 		sum2 = {}		
# 		for i in range(total-1):
# 			#use the following would generate unique pairs!!
# 			if i==0 or nums[i]>nums[i-1]:
# 				for j in range(i+1,total):
# 					if j==i+1 or nums[j]>nums[j-1]:
# 						if nums[i]+nums[j] not in sum2:
# 							sum2[nums[i]+nums[j]] = [[nums[i],nums[j]]]
# 						else:
# 							sum2[nums[i]+nums[j]].append([nums[i],nums[j]])
# 		#match for each key value, also includes itself
# 		res = {}
# 		visited = {}
# 		for key in sum2:
# 			#counting itself
# 			if key*2==target:
# 				self.find_pair(sum2,key,key,res,count)
# 			#not counting iteself now
# 			elif target-key not in visited:
# 				#if the minus_left not matched any key in visited, just add the current key into visited dict
# 				visited[key]=0
# 			elif target-key in visited:
# 				self.find_pair(sum2,key,target-key,res,count)
# 		return res.values()



# if __name__ == '__main__':
# 	sk = Solution()
# 	print	sk.fourSum([1, 0, -1 ,0 ,-2 ,2], 0)


# Permutation Sequence
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
# 	def getPermutation(self, n, k):
# 		"""
# 		:type n: int
# 		:type k: int
# 		:rtype: str
# 		"""
# 		#use k and n relation to compute the number at each position
# 		#not to generate all the possible/Or starting from 1...n to change, which both will be computational expensive
# 		lst = range(1,n+1)
# 		pos_divide = []
# 		pos_1 = 1
# 		for i in lst:
# 			pos_1 = pos_1*i
# 			pos_divide.append(pos_1)
# 		pos_divide = pos_divide[::-1]
# 		left_k = k-1
# 		pos = 1
# 		res=''        
# 		while left_k > 0:
# 			lst_pos = left_k/pos_divide[pos]
# 			res=res+str(lst[lst_pos])
# 			lst.pop(lst_pos)
# 			left_k = left_k%pos_divide[pos]
# 			pos += 1
# 		#join inside has to be str, not other type of data
# 		res = res + ''.join(str(i) for i in lst)	
# 		return res
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.getPermutation(4,24)        



# Valid Sudoku 
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
#'''it is no repeat for all rows, all columns and all square of 3*3 partial square'''
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
				##here is so important to segment the list first, instead of segment each time below to improve the speed
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



# Trapping Rain Water 
# Total Accepted: 54854 Total Submissions: 176832 Difficulty: Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def trap(self, height):
# 		"""
# 		:type height: List[int]
# 		:rtype: int
# 		"""
# 		#this seems not so hard: from left count the max, from the right count the max
# 		#it is the first or the max, just make it as the value; take the min of the two, and use the min of max - value to get the water for each cell
# 		#it is TO(n), SO(n)
# 		# count = len(height)
# 		# if count <=2: return 0
# 		# left0 = height[0]
# 		# left_max = [left0]
# 		# for i in range(1,count):
# 		# 	if height[i]>left0:
# 		# 		left0 = height[i]
# 		# 		left_max.append(left0)
# 		# 	else:
# 		# 		left_max.append(left0)

# 		# right0 = height[-1]
# 		# right_max = [right0]
# 		# for i in range(count-2,-1,-1):
# 		# 	if height[i]>right0:
# 		# 		right0=height[i]
# 		# 		right_max.append(right0)
# 		# 	else:
# 		# 		right_max.append(right0)
# 		# right_max = right_max[::-1]
# 		# water = 0
# 		# for i in range(count):
# 		# 	water += min(right_max[i],left_max[i])-height[i]
# 		# return water

# 		#now we want a it is TO(n), SO(1) solution
# 		#divide into the left and right by the maxheight index
# 		max_index = 0
# 		count = len(height)
# 		if count <=2: return 0
# 		for i in range(count):
# 			if height[i]>height[max_index]: max_index = i
# 		water = 0
# 		#for the left
# 		peak = 0
# 		for i in range(max_index):
# 			if height[i]>peak: peak=height[i]
# 			else: water += peak-height[i]
# 		#for the right
# 		peak=0
# 		for i in range(count-1,max_index,-1):
# 			if height[i]>peak: peak=height[i]
# 			else: water += peak-height[i]
# 		return water



# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.trap([0,1,0,2,1,0,1,3,2,1,2,1])		


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
#			#list.insert method is happening in place!!
# 			digits.insert(0,1)
# 		return digits
# class Solution:
# 	def plusOne(self, digits):  
# 		up = 1
# 		for i in range(len(digits)-1, -1, -1):
# 			if up == 1:
# 				if digits[i] + up == 10:
# 					digits[i] = 0
# 					up = 1
# 				else:
# 					digits[i] += 1
# 					up = 0
# 			else:
# 				break
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
#use dynamic programming, TO(n), in order to get SO(1),you only need to save the last 3 results
# class Solution:
	# @param {integer} n
	# @return {integer}
	#method1: resursion dynamical programming: TO(n), SO(n)
	# global mm
	# mm = {}
	# mm[0] = 1
	# mm[1] = 1
	# def climbStairs(self, n):
	# 	'''dynamic programming has two version typically: iterative
	# 	and recursion:the following is recursion:::use recursion you 
	# 	have to save each result in a gobal variable to save the results to avoid exponential computational cost;
	# 	for the two methods: the speed varies from situation to situtation'''
	# 	if n == 0:
	# 		return mm[0]
	# 	if n == 1:
	# 		return mm[1]
	# 	if n-1 not in mm:
	# 		res1 = self.climbStairs(n-1)
	# 		mm[n-1] = res1
	# 	if n-2 not in mm:
	# 		res2 = self.climbStairs(n-2)
	# 		mm[n-2] = res2
	# 	return mm[n-1] + mm[n-2]
	#method2:iterative: TO(n),SO(1)
#     def climbStairs(self, n):
#     	if n<=1: return 1
#     	pre0=1
#     	pre1=1
#     	for i in range(2,n+1):
#     		cur = pre0+pre1
#     		#first assing pre0
#     		pre0=pre1
#     		#then change pre1 to cur
#     		pre1=cur
#     	return cur
			
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.climbStairs(2)
# 	print sk.climbStairs(3)
# 	print sk.climbStairs(100)


	
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
#         #movitation: gray code: we want the integer next to each other has only one difference in bit, that would be 
#         #important for some system to aviod ambuguity. binary encoding doesnot work
#         #gray code transfer directly to decimal value would not be the original sequence
#         #there is a forumal to generate this
#         #method1, direct, n xor n>>1(or n/2) will give us the gray code for this integer n
#         #return [i^(i>>1) for i in xrange(2**n)]
#         #there are different sets that could work for gray code--not only one encoding results
#         #use string, directly
#         # if n==0: return [0]
#         # res = ['']
#         # for i in range(1,n+1):
#         # 	#add 0
#         # 	tmp0 = ['0'+i for i in res]
#         # 	tmp1 = ['1'+i for i in res[::-1]]
#         # 	res =tmp0 + tmp1
#         # return [int(i,2) for i in res]
#         #can use integers directly, rather than string
#         # if n ==0 : return [0]
#         # L = [0,1]
#         # for i in xrange(2,n+1):
#         # 	#the first part is constant, no change
#         # 	#the second part add 1 at the left most
#         # 	left_shift1 = 1<<i-1
#         # 	L = L + [j+left_shift1 for j in L[::-1]]
#         # return L
# if __name__ == '__main__':
# 	sk =Solution()
# 	print sk.grayCode(2)


# Set Matrix Zeroes My Submissions Question
# Total Accepted: 53816 Total Submissions: 166394 Difficulty: Medium
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# click to show follow up.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# # Discuss
# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         #want TO(m*n) SO(1), mark the first row and col, so that we track which col and row would be 0
#         m = len(matrix)
#         n = len(matrix[0])
#         #the easy bug is missing checking and saving the first col and first row info, 
#         #because later,we will mess their info with other row/col info
#         row0 = False
#       	col0 = False
#       	for i in range(m):
#       		if matrix[i][0] == 0:
#       			col0=True
#       			break
#       	for j in range(n):
#       		if matrix[0][j] == 0:
#       			row0=True
#       			break
#         for i in range(1,m):
#         	for j in range(1,n):
#         		if matrix[i][j] == 0:
#         			matrix[i][0] = 0
#         			matrix[0][j] = 0
#         #donot change the first row and col first
#         for i in range(m):
#         	if matrix[i][0] == 0:
#         		if i!=0:
#         			matrix[i]=[0]*n 
#         for j in range(n):
#         	if matrix[0][j]==0:
#         		for i in range(1,m):
#         			matrix[i][j] = 0
#        	if row0:
#        		matrix[0] =[0]*n
#        	if col0:
#        		for i in range(m):
#        			matrix[i][0] = 0
#         return
# if __name__ == '__main__':
# 	sk = Solution()
# 	test = [[1,2,3],[4,5,0],[0,1,2]]
# 	sk.setZeroes(test)
# 	print test


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
#         #the trick here is tracking the total of all, and the current valid
#         #for the current valid:whenever the current is invalid, just reset the value to 0
#         #because of reset, we have to tracking the total sum
#         total=0
#         cur_total=0
#         pos = -1
#         for i in range(len(gas)):
#         	cur_total += gas[i] - cost[i]
#         	total += gas[i] - cost[i]
#         	if cur_total<0:
#         		cur_total=0
#         		pos=i
# 		#if total =0, you can make it; if total<0, then there is a failure        		
#        	if total<0:
#        		return -1
#    		return pos+1
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.canCompleteCircuit([4,5,6,9],[4,6,7,5])        



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
# 	def candy(self, ratings):
# 		"""
# 		:type ratings: List[int]
# 		:rtype: int
# 		"""
# 		count = len(ratings)
# 		if count <1:return 0
# 		res0 = [1]
		
# 		for i in xrange(1,count):
# 			if ratings[i]>ratings[i-1]:
# 				res0.append(res0[i-1]+1)
# 			else:
# 				res0.append(1)
# 		res1=[1]				
# 		for i in xrange(count-2,-1,-1):
# 			if ratings[i]>ratings[i+1]:
# 				res1.append(res1[count-(i+2)]+1)
# 			else:
# 				res1.append(1)
# 		#res1= res1[::-1]
# 		total = 0
# 		for i in xrange(count):
# 			total += max(res0[i],res1[count-1-i])
# 		return total

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.candy([0,1,2,3,4,5])
# 	print sk.candy([0,0,0,0])
# 	print sk.candy([])
# 	print sk.candy([0,0,0,1,1,1,1,0,0,0])
# 	print sk.candy([5,3,4,4,4,7,9,10,8,6])

# Single Number My Submissions Question
# Total Accepted: 103759 Total Submissions: 218673 Difficulty: Medium
# Given an array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems
#number can be binary computation, xor would be both 1 or both 0 be 0, only thing left would be the single value
# class Solution:
#     # @param A, a list of integer
#     # @return an integer
#     def singleNumber(self, A):
#     	res = 0
#     	for i in A:
#     		res = res^i
#     	return res

# if __name__ == '__main__':
#    sk = Solution()
#    print sk.singleNumber([1,1,2,3,3,8,9,9,8])    	
#    print sk.singleNumber([1])    	

# Single Number II 
# Total Accepted: 69349 Total Submissions: 191750 Difficulty: Medium
# Given an array of integers, every element appears three times except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Subscribe to see which companies asked this question
#method1: get an array of length of the nums[0],and count the 1 appear at each digits, skip all the counts that is
#mutiple of 3, and extract all the digits that are not %3 =0
#method2 as following: use binary for substittue of three-nary, whenever the 1 and 2 get 1 at the same time, make it as 0
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
#         	#t1 and a both have 1, so go as t2 having 1 as jingwei,combine with the previous existing t2's 1  
#             t2 = t2|(a&t1)
#             #has to update t2 first, because we need the old t1 to update t2; if we update t1 first,
#             #then if one number show twice, we will remove it first, and then update t2, that would be a problem
#             #only count 1 time, so use ^
#             t1 = t1^a
#             #check t3 get 1?
#             t3 = t1&t2
#             #whenever t3 has 1, make t1 and t2 the same digits as 0s
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
# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def removeDuplicates(self, nums):
#     	'''in place algorithm, cannot make a new array'''
#     	count = len(nums)
#     	if count<=1:return count
#     	i=1 
#     	while i<count:
#     	   if nums[i]==nums[i-1]:
#     	       del nums[i]
#     	       count -=1
#     	   else:
#     	       i += 1
#     	return count
		

# Remove Duplicates from Sorted Array II My Submissions Question
# Total Accepted: 60220 Total Submissions: 191996 Difficulty: Medium
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def removeDuplicates(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		c = len(nums)
# 		if c<=2: return c
# 		res = [nums[0]]
# 		#use a variable to count the repeated times
# 		repeat = 0
# 		#starts from the second place/not the 1st place to count
# 		i = 1
# 		while i < c:
# 			if nums[i]==nums[i-1]:
# 				repeat += 1
# 				if repeat == 2:
# 					del nums[i]
# 					repeat -= 1
# 					c -= 1
# 				else:
# 					i += 1
# 			else:
# 				repeat = 0
# 				i += 1
# 		return c

# if __name__ == '__main__':
# 	sk =Solution()
# 	#s = [3,3,3,1,1,1,1]
# 	s=[1,1,1,1,1]
# 	sk.removeDuplicates(s)
# 	print s


# =============================================================
# Search in Rotated Sorted Array II My Submissions Question
# Total Accepted: 51852 Total Submissions: 165205 Difficulty: Medium
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """
#         #method that could be on average log(n), but at worst would be O(n)
#         count = len(nums)
#         if count==0: return False
#         if nums[0]==target: return True
#         if count==1: return False
#         if nums[count/2]==target: return True

#         if nums[0]>nums[count/2]:
#         	if nums[0]>target and nums[count/2]<target:
#         		#on the right
#         		return self.search(nums[count/2+1:],target)
#         	else:
#         		#to the left
#         		return self.search(nums[1:count/2],target)
#         elif nums[0]<nums[count/2]:
#         	if nums[0]<target and nums[count/2]>target:
#         		#to the left
#         		return self.search(nums[1:count/2], target)
#         	else:
#         		#to the right
#         		return self.search(nums[count/2+1:],target)
#         else: #nums[0]=nums[count/2]
#         	#can either to the right or to the left
#         	#to the left
#         	if self.search(nums[1:count/2],target):
#         		return True
#         	#to the right
#          	if self.search(nums[count/2+1:],target):
#         		return True
#         	return False

		
# Search in Rotated Sorted Array My Submissions Question
# Total Accepted: 82275 Total Submissions: 280662 Difficulty: Hard
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Subscribe to see which companies asked this question
#O(n) is not the target speed, we want O(logn), SO(1)
#if it is just sorted, then you compare the half and the other half directly, without using binary search tree would work to get O(logn)
# class Solution(object):
# 	def search(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: int
# 		"""
# 		#check the first and the middle to decide which way to go
# 		#method1: only consider the relation between target VS first and middle
# 		#at worst, it can be O(n), but in general O(logn)
# 		# c = len(nums)	
# 		# if c==0: return -1
# 		# if c==1: 
# 		# 	if nums[0]==target: return 0 
# 		# 	else: return -1
# 		# if nums[0] == target:
# 		# 	return 0
# 		# if nums[c/2] == target:
# 		# 	return c/2
# 		# if c==2: return -1
# 		# #can only decide two situations
# 		# if nums[0]>target and nums[c/2]<target:
# 		# 	#can NOT assume that you will must find it
# 		# 	y=self.search(nums[(c/2+1):], target)
# 		# 	if y != -1:	
# 		   #  	return c/2+1+y
# 		   #  else:
# 		   #  	return y	
# 		# elif nums[0]<target and nums[c/2]>target:
# 		# 	x = self.search(nums[1:c/2], target)
# 		# 	if x != -1:	
# 		# 		return 1+x
# 		# 	else:
# 		# 		return -1
# 		# else:
# 		# 	x=self.search(nums[1:c/2], target)
# 		# 	if x != -1: return 1+x
# 		# 	y=self.search(nums[(c/2+1):], target)	
# 		# 	if y != -1: return c/2+1+y
# 		# 	return -1
# 		#method2: consider the relation between first VS middle point first,  and then VS target point
# 		#this method is truly O(log(n))
# 		count =len(nums)
# 		if count==0: return -1
# 		if nums[0]==target: return 0
# 		if count==1: return -1
# 		if nums[count/2]==target:return count/2
# 		if count==2:return -1
# 		#compare 0 and count/2 first
# 		if nums[0]>nums[count/2]:
# 			#mean that the rotated beginning is in the first half
# 			if nums[0]>target and nums[count/2]<target:
# 				tmp = self.search(nums[count/2+1:], target)
# 				if tmp != -1:
# 					return count/2+1+tmp
# 				else:
# 					return tmp
# 			else:
# 				tmp = self.search(nums[1:count/2], target)
# 				if tmp != -1:
# 					return 1+tmp
# 				else:
# 					return tmp
# 		else:
# 			#nums[0]<nums[count/2]
# 			#mean the rotated beginning is in the second half
# 			if nums[0]<target and nums[count/2]>target:
# 				tmp = self.search(nums[1:count/2], target)
# 				if tmp != -1:
# 					return 1+tmp
# 				else:
# 					return tmp
# 			else:
# 				tmp = self.search(nums[count/2+1:], target)
# 				if tmp != -1:
# 					return count/2+1+tmp
# 				else:
# 					return tmp

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.search([4,5,6,7,8,0,1,2], 2)
# 	print sk.search([2], 2)
# 	print sk.search([1,2,3,4,5,6,7], 2)
# 	print sk.search([], 2)
# 	print sk.search([3,4,6,-1,0,1], 2)
# 	print sk.search([1,3],2)


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
		

# Two Sum 
# Total Accepted: 164673 Total Submissions: 834667 Difficulty: Medium
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# Subscribe to see which companies asked this question

# class Solution(object):
# 	def twoSum(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: List[int]
# 		"""
		#nlog(n)::sort and check:but because return the index, you then have to get a match up of index in order to do this
		# lst = sorted(list(zip(nums, range(len(nums)))), key = lambda x:x[0])
		# #nums.sort()
		# count = len(nums)
		# left, right = 0, count-1
		# res = {}
		# while left < right:
		# 	if lst[left][0] + lst[right][0] == target:
		# 		if (lst[left][0] + lst[right][0]) not in res:
		# 			res[(lst[left][0],lst[right][0])] = (lst[left][1], lst[right][1])
		# 		right -= 1
		# 	elif lst[left][0] + lst[right][0] > target:
		# 		right -= 1
		# 	else:
		# 		left += 1
		# return res.values()
		# #
		#method2:O(n) unique -> duplicate
		# c_dct = {}
		# res = {}
		# for i in range(len(nums)):
		# 	if target-nums[i] not in c_dct:  
		# 		#here it is optional: not necessary to if nums[i] not in c_dct:
		# 		# if nums[i] not in c_dct:
		# 			c_dct[nums[i]] = i+1
		# 	else:
		# 		key = (min(target-nums[i], nums[i]), max(target-nums[i], nums[i]))
		# 		if key not in res: res[key] = [c_dct[target-nums[i]],i+1]
		# return res.values() #in the leetcode, you need to add res.values()[0] to get the first elements assume there is only one pair

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.twoSum([1,2,3,4,4,5,5,5,5,6,7,3,1],8)

# 3Sum
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
#         #sort nlog(n)
#         nums.sort()
#         count = len(nums)
#         if count <=2: return []
#         res = []
#         #O(n^2) following:
#         for i in xrange(count-2):
#         	#if the least value is bigger than 0, then it cannot be sum of 0
#         	if nums[i]>0: break
#         	if i == 0 or nums[i]>nums[i-1]:
# 	        	target = -nums[i]
# 	        	#because there are unique set, we donot have to count a number lots of times, so left is from i+1
# 	        	left, right = i+1, count-1
# 	        	while left<right:
# 	        		if nums[left]+nums[right] == target:
# 	        			#right use the dictionary key:value
# 	        			res.append([nums[i], nums[left],nums[right]])
# 	        			#if not return index, the below would be a problem here
# 	        			right -= 1
# 	        			left += 1
# 	        			while nums[right+1] == nums[right] and right > left: right -= 1
# 	        			while nums[left-1] == nums[left] and left < right: left += 1
# 	        		elif nums[left]+nums[right] > target:
# 	        			right -= 1
# 	        			while nums[right] == nums[right+1] and right > left: right -= 1
# 	        		else:
# 	        			left += 1
# 	        			while nums[left] == nums[left-1] and left < right: left += 1
# 	        		# print res.values()
#        	return res

		

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.threeSum([-1 ,0, 1, 2, -1, -4])
# 	# print sk.threeSum([-1 ,0,1, 0])
# 	print sk.threeSum([0,0,0])
# 	print sk.threeSum([0,0,0,0,0,0])

# 3Sum Closest 
# Total Accepted: 60330 Total Submissions: 217255 Difficulty: Medium
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# class Solution(object):
# 	def threeSumClosest(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: int
# 		"""
# 		#sort
# 		nums.sort()
# 		c = len(nums)
# 		if c <= 2: return 0
# 		if c == 3: return sum(nums)
# 		#initiate the res with the first 3 element sum:
# 		res =  abs(sum(nums[0:3]) - target)
# 		res_lst = nums[0:3]
# 		# no need to run all c, because you have to check left and right, these two count two
# 		for i in range(c-2):
# 			if i == 0 or nums[i]>nums[i-1]:
# 				left, right = i+1, c-1
# 				while left < right:
# 					if nums[i]+nums[left]+nums[right] - target == 0:
# 						return target
# 					elif nums[i]+nums[left]+nums[right] - target > 0:
# 						#compare values and save
# 						if abs(nums[i]+nums[left]+nums[right] - target) < res:
# 							#the bug is here::::: update both, not only one
# 							res = abs(nums[i]+nums[left]+nums[right] - target)
# 							res_lst = [nums[i],nums[left],nums[right]]
# 						#move right
# 						right -= 1
# 						while nums[right] == nums[right+1] and left < right: right -= 1
# 					else:
# 						#compare values and save 
# 						if abs(nums[i]+nums[left]+nums[right] - target) < res:
# 							res = abs(nums[i]+nums[left]+nums[right] - target)
# 							res_lst = [nums[i],nums[left],nums[right]]
# 						#move left
# 						left += 1
# 						while nums[left] == nums[left-1] and left < right: left+=1
# 		return sum(res_lst)



# if __name__ == '__main__':
# 	sk = Solution()
# 	# print sk.threeSumClosest([-1, 2 ,1 ,-4],1)
# 	# print sk.threeSumClosest([-1, 0 ,0 ,0],0)
# 	# print sk.threeSumClosest([0 ,0 ,0],0)
# 	# print sk.threeSumClosest(range(100),100)
# 	print sk.threeSumClosest([0,2,1,-3],1)













