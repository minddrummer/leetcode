# 78. Subsets My Submissions Question
# Total Accepted: 81871 Total Submissions: 270798 Difficulty: Medium
# Given a set of distinct integers, nums, return all possible subsets.
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# class Solution(object):
# 	#use dfs--recursion
# 	def subsets(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		nums = sorted(nums)	
# 		if len(nums)==0: return [[]]
# 		return self.dfs(nums)
# 	#TO(2^n)
# 	def dfs(self, nums):
# 		# if len(nums)==0: return [[]]
# 		if len(nums)==1: return [[],[nums[0]]]
# 		res_less_1 = self.dfs(nums[:-1])
# 		res=[]
# 		last = nums[-1]
# 		for item in res_less_1:
# 			#not use item, otherwise, you change res_less_1, and would be a bug then
# 			#make a copy of item by slicing all item[:]
# 			item0 = item[:]
# 			item0.append(last)
# 			res.append(item0)
# 		return res_less_1+res

# class Solution(object):
# 	def subsets(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		res = []
# 		self.dfs(nums, res)
# 		return res
		
# 	def dfs(self, lst, res):
# 		if len(lst)==0:
# 			res.append([])
# 			return 
# 		self.dfs(lst[1:], res)
# 		i = 0
# 		count = len(res)
# 		while i < count:
# 			item = res[i]
# 			res.append([lst[0]]+item)
# 			i+=1
# 		return 

# if __name__ == '__main__':
# 	# nums=[1,2,3]
# 	sk=Solution()
# 	print sk.subsets([1,2,3])		


# 90. Subsets II My Submissions Question
# Total Accepted: 58996 Total Submissions: 199541 Difficulty: Medium
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def subsetsWithDup(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		# nums = sorted(nums)
# 		if len(nums)==0: return [[]]
# 		count = {}
# 		new_nums=[]
# 		for i in nums:
# 			if i in count:
# 				count[i] += 1
# 			else:
# 				new_nums.append(i)
# 				count[i] = 1
# 		new_nums=sorted(new_nums)
# 		return self.dfs(new_nums, count)


# 	def dfs(self, nums, count):
# 		#note when len(nums)=1, there might be a bug if you go directly
# 		if len(nums)==1: 
# 			times = count[nums[0]]
# 			time=0
# 			res=[]
# 			while time<= times:
# 				res.append([nums[0]]*time)
# 				time+=1	
# 			return res

# 		res_1 = self.dfs(nums[:-1], count)
# 		res=[]
# 		last=nums[-1]
# 		times = count[last]
# 		for item in res_1:
# 			time=1
# 			while time<=times:
# 				res.append(item+[last]*time)
# 				time += 1
# 		return res_1+res

# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         return self.dfs(nums)
        
#     def dfs(self, lst):
#         if len(lst)==0: 
#             return [[]]
        
#         res = self.dfs(lst[1:])
#         newRes = []
#         for item in res:
#             newItem = [lst[0]]+item
#             if newItem not in res:
#                 newRes.append(newItem)
                
#         return newRes+res


# 46. Permutations My Submissions Question
# Total Accepted: 85174 Total Submissions: 247755 Difficulty: Medium
# Given a collection of distinct numbers, return all possible permutations.
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def permute(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
		#recursion, TO(n!)
# 		if len(nums)==0: return []
# 		if len(nums)==1: return [[nums[0]]]

# 		last = nums[-1]
# 		res_1= self.permute(nums[:-1])
# 		res=[]
# 		for item in res_1:
# 			for i in range(len(item)+1):
# 				new_item=item[:]
# 				new_item.insert(i, last)
# 				res.append(new_item)
# 		return res


# 47. Permutations II My Submissions Question
# Total Accepted: 60743 Total Submissions: 223569 Difficulty: Medium
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

# Subscribe to see which companies asked this question

# class Solution(object):
# 	def permuteUnique(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		#for the permuteUnique, we use the more formal way to achieve it
# 		#the formal way: we pick each value, and make it as a root of the binary tree for all the values in the list
# 		#then we would get all the permuations
# 		#if when we have duplicates, we just skip it as the root, we will find all the possible permutations in this case
# 		n=len(nums)
# 		if n==0: return []
# 		if n==1: return [nums]

# 		#inthis case ,sort
# 		nums.sort()

# 		res=[]
# 		pre = None
# 		for i in range(n):
			#if dupplicate, just skip it as the root again
			#but since for all other nodes and also the first nodes, 
			#you will still keep the dupilcates(but not as root), so
			#we will get the right results
# 			if nums[i] is pre: continue
# 			pre = nums[i]
# 			for item in self.permuteUnique(nums[:i]+nums[i+1:]):
# 				res.append(item+[nums[i]])
# 		return res



# 77. Combinations My Submissions Question
# Total Accepted: 65636 Total Submissions: 198530 Difficulty: Medium
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Subscribe to see which companies asked this question


# class Solution:
#     # @return a list of lists of integers
#     def combine(self, n, k):
#     	if n < k or k == 0: return []
#     	if k == 1: return [[i] for i in xrange(1,n+1)]    	
#     	res = []
#     	for i in xrange(n,0,-1):
#     		#because combination we donot care order
#     		#therefore, the point to make difference is to make the new-last value into the sequence
#     		#you will get all because the for loop, you will get all the RIGHT-k-length combine upto i
#     		for item in self.combine(i-1,k-1):
#     			res.append(item+[i])
#     	return res                                


# 17. Letter Combinations of a Phone Number My Submissions Question
# Total Accepted: 67797 Total Submissions: 246289 Difficulty: Medium
# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.    	


# class Solution(object):
# 	def letterCombinations(self, digits):
# 		"""
# 		:type digits: str
# 		:rtype: List[str]
# 		"""
# 		dct={'0':[' '], '1':['*'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],\
# 		'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

# 		if len(digits)==0: return []
# 		return self.dfs(digits, dct)

# 	def dfs(self, digits, dct):
# 		n=len(digits)
# 		if n==1: return dct[digits]
# 		res_1 = self.dfs(digits[1:], dct)

# 		lst = dct[digits[0]]
# 		res=[]
# 		for item in res_1:
# 			for letter in lst:
# 				res.append(letter+item)

# 		return res




