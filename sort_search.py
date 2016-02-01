# # 88. Merge Sorted Array My Submissions Question
# # Total Accepted: 85726 Total Submissions: 288705 Difficulty: Easy
# # Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# # Note:
# # You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# # Subscribe to see which companies asked this question


# # class Solution:
# # 	# @param A  a list of integers
# # 	# @param m  an integer, length of A
# # 	# @param B  a list of integers
# # 	# @param n  an integer, length of B
# # 	# @return nothing
# # 	def merge(self, A, m, B, n):
# 		#should not use the fooloowing code:
# 		#use T n, S 1: by insert B into A: usieng python list.insert(index, obj) method
# 		#it will insert the element into A with constant time and space TO(1) SO(1)
# 		#list.pop(index), del list[index], list.remove(value)(erorr if value not in list), list.insert(index, value) all constant time and space in python by its default method
# # 		tmp = [0 for i in range(m+n)]
# # 		i =0 ; j = 0 ; k = 0
# # 		while i <m and j <n:
# # 			if A[i] <B[j]:
# # 				tmp[k] = A[i]; i+=1
# # 			else:
# # 				tmp[k] = B[j]; j+=1
# # 			k += 1
# # 		if i == m:
# # 			while j <n:
# # 				tmp[k] = B[j]; j+=1;k+=1
# # 		else:
# # 			while i <m:
# # 				tmp[k] = A[i]; i+=1;k+=1
		
# # 		thres = len(A)
# # 		for i in range(m+n):
# # 			if i < thres:
# # 				A[i] = tmp[i]
# # 			else:
# # 				A.append(tmp[i])
# # 		if i < thres-1:
# # 			for x in range(thres-1-i):
# # 				A.pop(-1)
		
		


# # 21. Merge Two Sorted Lists My Submissions Question
# # Total Accepted: 105169 Total Submissions: 306001 Difficulty: Easy
# # Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# # Subscribe to see which companies asked this question
# # # Definition for singly-linked list.
# # # class ListNode:
# # #     def __init__(self, x):
# # #         self.val = x
# # #         self.next = None

# # class Solution:
# #     # @param {ListNode} l1
# #     # @param {ListNode} l2
# #     # @return {ListNode}
# #     def mergeTwoLists(self, l1, l2):
# #     	if l1 is None and l2 is None:
# #     		return None
# #     	elif l1 is None and l2 is not None:
# #     		return l2
# #     	elif l1 is not None and l2 is None:
# #     		return l1
# #     	else:
# #     		if l1.val >= l2.val:
# # 	    		head = l2
# # 	    		dummy = head
# # 	    		l2 = l2.next
# # 	    	else:
# # 	    		head = l1
# # 	    		dummy = head
# # 	    		l1 = l1.next
# #     		while l1 is not None and l2 is not None:
# #     			if l1.val >= l2.val:
# # 	    			head.next = l2
# # 	    			l2 = l2.next
# # 	    			head = head.next
# # 		    	else:
# # 		    		head.next = l1
# # 	    			l1 = l1.next
# # 	    			head = head.next
# # 	    	if l1 is None:
# # 	    		head.next = l2
# # 	    	if l2 is None:
# # 	    		head.next = l1
# # 	    	return dummy


# # 23. Merge k Sorted Lists My Submissions Question
# # Total Accepted: 73157 Total Submissions: 324219 Difficulty: Hard
# # Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# # Subscribe to see which companies asked this question
# # # Definition for singly-linked list.
# # # class ListNode(object):
# # #     def __init__(self, x):
# # #         self.val = x
# # #         self.next = None

# # class Solution(object):
# # 	def mergeKLists(self, lists):
# # 		"""
# # 		:type lists: List[ListNode]
# # 		:rtype: ListNode
# # 		"""
# # 	#there are several methods
# # 	#divide and conquner sort, (n1+..nk)log(k), SO(1)        
# # 	#merge by two: k*n1+k*n2+...(k-1)*n3...+nk
# # 	#heap: (n1+..nk)log(k), SO(1)        

# # 		heap=[]
# # 		for node in lists:
# # 			#remove all nodes that are None
# # 			if node: heap.append((node.val, node))
# # 		heapq.heapify(heap)
# # 		dummy = ListNode(0)
# # 		head=dummy
# # 		#for list, while could run as long as there are elements in the list
# # 		while heap:
# # 			min_node=heapq.heappop(heap)	
# # 			dummy.next=min_node[1]
# # 			dummy=dummy.next
# # 			#new_node can be None here
# # 			new_node = min_node[1].next
# # 			#only push new node if it is not None!!
# # 			if new_node: heapq.heappush(heap, (new_node.val, new_node))
# # 		return head.next


# # 147. Insertion Sort List My Submissions Question
# # Total Accepted: 63206 Total Submissions: 222211 Difficulty: Medium
# # Sort a linked list using insertion sort.
# # Subscribe to see which companies asked this question

# # # Definition for singly-linked list.
# # # class ListNode(object):
# # #     def __init__(self, x):
# # #         self.val = x
# # #         self.next = None

# # class Solution(object):
# #     def insertionSortList(self, head):
# #         """
# #         :type head: ListNode
# #         :rtype: ListNode
# #         """
		

# # 148. Sort List My Submissions Question
# # Total Accepted: 63162 Total Submissions: 263787 Difficulty: Medium
# # Sort a linked list in O(n log n) time using constant space complexity.
# # Subscribe to see which companies asked this question
# # # Definition for singly-linked list.
# # # class ListNode(object):
# # #     def __init__(self, x):
# # #         self.val = x
# # #         self.next = None

# # class Solution(object):
# #     def sortList(self, head):
# #         """
# #         :type head: ListNode
# #         :rtype: ListNode
# #         """
# 	#use divide and conquer method-or merge two sorted linkedlist, and applied to the linkedlist would work


# # 75. Sort Colors My Submissions Question
# # Total Accepted: 84990 Total Submissions: 250463 Difficulty: Medium
# # Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# # Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# # Note:
# # You are not suppose to use the library's sort function for this problem.
# # click to show follow up.
# # Subscribe to see which companies asked this question

# # class Solution(object):
# #     def sortColors(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: void Do not return anything, modify nums in-place instead.
# #         """
# #        	len_nums = len(nums)
# #         cur=white=0
# #         blue = len_nums-1
# #         while cur <= blue:
# #         	if nums[cur] == 2:
# #         		nums[cur] = nums[blue]
# #         		nums[blue] = 2
# #         		blue -= 1        	
# #         	elif nums[cur] == 1:
# #         		cur += 1
# #         	else:
# #         		nums[cur] = nums[white]
# #         		nums[white] = 0
# #         		white += 1
# #         		cur += 1
				
														


# # 41. First Missing Positive My Submissions Question
# # Total Accepted: 57246 Total Submissions: 244351 Difficulty: Hard
# # Given an unsorted integer array, find the first missing positive integer.

# # For example,
# # Given [1,2,0] return 3,
# # and [3,4,-1,1] return 2.

# # Your algorithm should run in O(n) time and uses constant space.

# # Subscribe to see which companies asked this question

# # class Solution(object):
# # 	def firstMissingPositive(self, nums):
# # 		"""
# # 		:type nums: List[int]
# # 		:rtype: int
# # 		"""
# # 		#if there is no missing from 1 to n, then n+1 returned, and there should be no 0/negates
# # 		n = len(nums)
# # 		for i in range(n):
# # 			#put all values <= as n+2
# # 			if nums[i]<=0: nums[i] = n+2
# # 		for i in range(n):
# # 			#now if a value <= n, what we do?
# # 			#make the corresponding value's index-1 as the negative value
# # 			#then we just count the first postive value's index +1
# # 			if abs(nums[i])<= n:
# # 				index= abs(nums[i])-1
# # 				nums[index] = -abs(nums[index])
# # 		for i in range(n):
# # 			if nums[i]>0: return i+1
# # 		return n+1


# 34. Search for a Range My Submissions Question
# Total Accepted: 71888 Total Submissions: 252717 Difficulty: Medium
# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# [1,2,3],2---return [1,1]
# return [3, 4].
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def searchRange(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: List[int]
# 		"""
# 		#  TO(log n), SO(1)
# 		return self.searchRange(nums, target, 0, len(nums)-1)

# 	def search(self, nums, target, start, end):
# 		if start>end or (start==end and target != nums[start]): return [-1, -1]
# 		if start==end and target == nums[start]: return [start, end]
# 		res = [-1, -1]
# 		half = (start+end)/2
# 		if nums[start]<=target and nums[half]>=target:
# 			left = self.search(nums, target, start, half)
# 			if left !=[-1,-1]: res = left
# 		if nums[end]>= target and nums[half]<=target:
# 			#we are not slicing, so the index has +1 here!!
# 			right = self.search(nums,target, half+1, end)
# 			if right != [-1,-1]:
# 				if res != [-1,-1]: res[1]=right[1]
# 				else: res = right
# 		return res

# 35. Search Insert Position My Submissions Question
# Total Accepted: 91532 Total Submissions: 249621 Difficulty: Medium
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

# Subscribe to see which companies asked this question
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         #log(n), 1
#         if len(nums) ==0: return 0
#         res=self.search(nums,target, 0, len(nums)-1)
#         if res==-1: return 0
#         if res==-2: return len(nums)
#         return res
#     def search(self, nums, target, start, end):
#     	if nums[start]>target: return -1
#     	if nums[end]<target: return -2
#     	if nums[start]==target: return start
#     	if nums[end]==target: return end
#     	half = (start+end)/2
#     	#now start<target and end >target
#     	left = self.search(nums, target, start, half)
#     	# right=None
#     	# if half+1<=end:
#     	right = self.search(nums,target, half+1, end)
#     	if left == -1: return -1
#     	if left == -2 and right ==-1: return half+1
#     	if right == -2: return -2
#     	return max(left, right)



# 74. Search a 2D Matrix My Submissions Question
# Total Accepted: 68689 Total Submissions: 207728 Difficulty: Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		m=len(matrix)
		n=len(matrix[0])
		if m==0 or n==0: return False
		return self.searchRow(matrix, target, 0, m-1)


	def searchRow(self, matrix, target,start, end):
		if matrix[start][0] == target: return True
		if matrix[end][-1] == target: return True
		if matrix[start][0]>target: return False
		if matrix[end][-1]<target: return False

		if matrix[start][0]<target and matrix[start][-1]>=target:
			return self.searchCol(matrix, target, start, 0, len(matrix[start])-1)
		if matrix[end][0]<=target and matrix[end][-1]>target:
			return self.searchCol(matrix, target, end, 0, len(matrix[end])-1)
		half=(start+end)/2
		return self.searchRow(matrix, target, start, half) or self.searchRow(matrix, target, half+1, end)

	def searchCol(self, matrix, target, row, start, end):
		if matrix[row][start]==target: return True
		if matrix[row][end]==target: return True
		if matrix[row][start]>target: return False
		if matrix[row][end]<target: return False

		half= (start+end)/2
		return self.searchCol(matrix, target, row, start, half) or self.searchCol(matrix, target, row, half+1, end)







				
		
				





		

