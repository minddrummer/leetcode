# 105. Construct Binary Tree from Preorder and Inorder Traversal My Submissions Question
# Total Accepted: 54633 Total Submissions: 197179 Difficulty: Medium
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# Subscribe to see which companies asked this question

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
# 	def buildTree(self, preorder, inorder):
# 		"""
# 		:type preorder: List[int]
# 		:type inorder: List[int]
# 		:rtype: TreeNode
# 		"""
# 		#recursion, TO(n^2), SO(n)
# 		if len(preorder) == 0: return None
# 		if len(preorder) == 1: return TreeNode(preorder[0])
# 		root = preorder[0]        
# 		root_index = inorder.index(root)
# 		root_left = self.buildTree(preorder[1:(root_index+1)], inorder[:root_index])
# 		root_right= self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
# 		root = TreeNode(root)
# 		root.left = root_left
# 		root.right = root_right
# 		return root


# 106. Construct Binary Tree from Inorder and Postorder Traversal My Submissions Question
# Total Accepted: 48313 Total Submissions: 171031 Difficulty: Medium
# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
# 	def buildTree(self, inorder, postorder):
# 		"""
# 		:type inorder: List[int]
# 		:type postorder: List[int]
# 		:rtype: TreeNode
# 		"""
# 		#recursion should be easy
# 		#TO(n^2), SO(n)		
# 		if len(inorder)==0: return
# 		if len(inorder)==1: return TreeNode(inorder[0])
# 		root=postorder[-1]
# 		root_index = inorder.index(root)
# 		#the # of nodes should be the same on both sides:::
# 		left = self.buildTree(inorder[:root_index], postorder[:root_index])
# 		right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
# 		root= TreeNode(root)
# 		root.left = left
# 		root.right = right
# 		return root

# 96. Unique Binary Search Trees My Submissions Question
# Total Accepted: 73389 Total Submissions: 200409 Difficulty: Medium
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# class Solution(object):
# 	#the problem is one-dimension dynamical programming
# 	#TO(n^2), SO(n)
#     def numTrees(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         global dct
#         dct = {}
#         dct[0] = 1
#         dct[1] = 1
#         if n == 0: 
#         	return 1
#         if n == 1: 
#         	return 1
#         count = self.count(n)	
#         return count

#     def count(self,n):
#         if n in dct:
#         	return dct[n]
#         count = 0
#         for i in range(n):
#         	count += self.count(i)*self.count(n-1-i)
#         dct[n] = count
#         return count


# 95. Unique Binary Search Trees II My Submissions Question
# Total Accepted: 48514 Total Submissions: 168626 Difficulty: Medium
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# class Solution(object):
# 	#dfs to emulate all the possible combinantions
# 	def dfs(self, start, end):
# 		if start>end: return [None]
# 		res= []
# 		for val in range(start,end+1):
# 			leftnodes = self.dfs(start, val-1)
# 			rightnodes = self.dfs(val+1, end)
# 			for i in leftnodes:
# 				for j in rightnodes:
# 					root = TreeNode(val)
# 					root.left = i
# 					root.right = j
# 					res.append(root)
# 		return res
# 	def generateTrees(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[TreeNode]
# 		"""
# 		if n==0: return []
# 		return self.dfs(1,n)


# 98. Validate Binary Search Tree My Submissions Question
# Total Accepted: 79069 Total Submissions: 384234 Difficulty: Medium
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# class Solution(object):
# 	def isValidBST(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: bool
# 		"""
# 		#recursion
# 		#2**32 interger, by half, so it is 2**31+1, -2**31-1
# 		return self.help(root, -2147483649, 2147483648)

# 	def help(self, root, minv, maxv):
# 		if root is None: return True
# 		if root.val<= minv or root.val>= maxv: return False
# 		return self.help(root.left, minv, min(root.val,maxv)) and self.help(root.right,  max(root.val, minv),  maxv)
# 		#or NO need to add max() and min because the BST's attributes!!
# 		return self.help(root.left, minv, root.val) and self.help(root.right,  root.val,  maxv)


# 108. Convert Sorted Array to Binary Search Tree My Submissions Question
# Total Accepted: 65801 Total Submissions: 182262 Difficulty: Medium
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Subscribe to see which companies asked this question

# # Show Tags
# # Show Similar Problems
class Solution(object):
	# def sortedArrayToBST(self, nums):
	#     """
	#     :type nums: List[int] #the ele are sorted in ascending order
	#     :rtype: TreeNode
	#     """
		#right now, it is TO(n), SO(n)-
		#SO(n): log(n) depth, each depth is x/2 size
		#if you use index for start and end, you would get log(n) SO
		# n = len(nums)
		# if n == 0: return None
		# half = n/2
		# root = TreeNode(nums[half])
		# root.left = self.sortedArrayToBST(nums[:half])
		# root.right = self.sortedArrayToBST(nums[half+1:])
		# return root

	#TO(n), SO(logn) using index,and has to write a helper function to put new argument
	# def sortedArrayToBST(self, nums):
	# 	return self.help(nums, 0, len(nums)-1)

	# def help(self, nums, start, end):
	# 	#when start is == end, still works
	# 	#when start>end, then has to return None to make the final nodes having all Nones
	# 	if start>end: return None
	# 	half=(start+end)/2
	# 	rootval=nums[half]
	# 	root=TreeNode(rootval)
	# 	root.left=self.help(nums, start, half-1)
	# 	root.right=self.help(nums, half+1, end)
	# 	return root

	#it seems that python's one function will directly go up one level-environment
	#not to the environment that directly calls it(within another function)??
	#that is the reason why if you want to refer to mutable object, you need to pass it as one argument
	#and since it is mutable, it will refer to the same object, rather than creating a new object
	#in this way, you would NOT cost extra space in the algorithm, but only referring to the same object
	
	# global nums
	# def sortedArrayToBST(self, nums):

	# 	return self.help(0, len(nums)-1)

	# def help(self, start, end):
	# 	#when start is == end, still works
	# 	#when start>end, then has to return None to make the final nodes having all Nones
	# 	if start>end: return None
	# 	half=(start+end)/2
	# 	rootval=nums[half]
	# 	root=TreeNode(rootval)
	# 	root.left=self.help(start, half-1)
	# 	root.right=self.help(half+1, end)
	# 	return root		
		

# 109. Convert Sorted List to Binary Search Tree My Submissions Question
# Total Accepted: 61915 Total Submissions: 209249 Difficulty: Medium
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
# 	#TO(n^2), SO(1)
# 	def length(self, head):
# 			count = 0
# 			while head:
# 				count += 1
# 				head= head.next
# 			return count
		
# 	def sortedListToBST(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: TreeNode
# 		"""
# 		#one method is convert linkedlist to array, it is fast: O(n), but extra space O(n)
# 		#if not cheating:::
# 		count = self.length(head)
# 		return self.help(head, 0, count-1)

# 	def help(self, head, start, end):
# 		if start>end: return None
# 		half= (start+end)/2
# 		head0= head
# 		count=0
# 		while count<half:
# 			head=head.next
# 			count+=1
# 		parent = TreeNode(head.val)
# 		left = self.help(head0, start, half-1)
# 		parent.left = left
# 		head = head.next
# 		parent.right = self.help(head, 0, end-half-1)
		
# 		return parent

# 111. Minimum Depth of Binary Tree My Submissions Question
# Total Accepted: 90598 Total Submissions: 301463 Difficulty: Easy
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     # @param {TreeNode} root
#     # @return {integer}
#     def minDepth(self, root):
#     	if root is None:
#     		return 0
#     	elif root.right is None and root.left is None:
#     		return 1
#     	elif root.right is None and root.left is not None:
#     		return self.minDepth(root.left) + 1
#     	elif root.right is not None and root.left is None:
#     		return self.minDepth(root.right) + 1
#     	else:	
#     		return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
		


# 104. Maximum Depth of Binary Tree My Submissions Question
# Total Accepted: 117617 Total Submissions: 250532 Difficulty: Easy
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {TreeNode} root
#     # @return {integer}
#     def maxDepth(self, root):
#     	if root is None:
#     		return 0
#     	return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 

		
# 112. Path Sum My Submissions Question
# Total Accepted: 87868 Total Submissions: 286424 Difficulty: Easy
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems

class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {boolean}
	# def all_sum(self, root):
	# 	if root is None:
	# 		return None
	# 	elif root.left is None and root.right is None:
	# 		return [root.val]
	# 	else:
	# 		res_lst = []
	# 		if root.left is not None:
	# 			left_lst = self.all_sum(root.left) 
	# 			left_lst = [item + root.val for item in left_lst]
	# 			res_lst = res_lst + left_lst
	# 		if root.right is not None:
	# 			right_lst = self.all_sum(root.right)
	# 			right_lst = [item + root.val for item in right_lst]
	# 			res_lst = res_lst + right_lst
	# 		return res_lst


	# def hasPathSum(self, root, sum):
	# 	sum_lst = self.all_sum(root)
	# 	res = False
	# 	if sum_lst is None:
	# 		return res
	# 	for item in sum_lst:
	# 		if item == sum:
	# 			return True
	# 	return res    
	#TO(n), SO(logN)
	# def hasPathSum(self, root, sum):
	# 	if root is None: return False
	# 	sum = sum - root.val
	# 	#if sum <0: return False--cannot add this, will produce wrong answer
	# 	#because you can get <0 sum
	# 	#if both side is None and sum=0, then no matter <0, >0 =0 sum, it would be true!! 
	# 	if root.left is None and root.right is None and sum ==0:
	# 		return True
	# 	else:
	# 		return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# 113. Path Sum II My Submissions Question
# Total Accepted: 70076 Total Submissions: 253921 Difficulty: Medium
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
# 	def pathSum(self, root, sum):
# 		"""
# 		:type root: TreeNode
# 		:type sum: int
# 		:rtype: List[List[int]]
# 		"""
# 		#TO(n), SO(logN)
# 		if root is None: return []
# 		sum = sum - root.val
# 		if root.left is None and root.right is None and sum == 0:
# 			return [[root.val]]
# 		else:
# 			res=[]
# 			left = self.pathSum(root.left, sum)
# 			right = self.pathSum(root.right, sum)
# 			for lst in left: 
# 				res.append([root.val]+lst)
# 			for lst in right: 
# 				res.append([root.val]+lst)	
# 			return res
		



# 116. Populating Next Right Pointers in Each Node My Submissions Question
# Total Accepted: 76934 Total Submissions: 211234 Difficulty: Medium
# Given a binary tree
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Note:
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
# Subscribe to see which companies asked this question

# # Definition for binary tree with next pointer.
# # class TreeLinkNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# #         self.next = None

# class Solution(object):
  #   def connect(self, root):
		# """
		# :type root: TreeLinkNode
		# :rtype: nothing
		# """
		# #BFS could solve this problem, but the space will be proportional(equal) to Log(n+1)-1
		# #method2 treated as linked list, and each time: connect parent's left or right to child
		# if root is None:
		# 	return				
		# parent = root
		# parent.next = None
		# child = parent.left
		# first_child = child
		# while child is not None:
		# 	if child == parent.left:
		# 		child.next = parent.right
		# 		child = child.next
		# 	else:
		# 		parent = parent.next
		# 		if parent is not None:
		# 			child.next = parent.left
		# 			child = child.next
		# 		else:
		# 			parent = first_child
		# 			child.next = None
		# 			child = parent.left
		# 			first_child = child
		# def connect(self, root):
		# 	if root:
		# 		parent = root; child=None; nextnode = None
		# 		while parent:
		# 			if parent.left: 
		# 				if child: child.next = parent.left
		# 				child = parent.left
		# 				if nextnode is None: nextnode = parent.left

		# 			if parent.right:
		# 				if child: child.next = parent.right
		# 				child = parent.right
		# 				if nextnode is None: nextnode = parent.right
		# 			parent=parent.next
		# 		self.connect(nextnode)

# 129. Sum Root to Leaf Numbers My Submissions Question
# Total Accepted: 67425 Total Submissions: 212143 Difficulty: Medium
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Return the sum = 12 + 13 = 25.

# class Solution(object):
	# def sumNumbers(self, root):
	# 	"""
	# 	:type root: TreeNode
	# 	:rtype: int
	# 	"""
	# 	#TO(n), SO(n)
	# 	lst = self.get_all_path(root)
	# 	slst= []
	# 	for item in lst:
	# 		item = ''.join(str(i) for i in item)
	# 		if len(item) != 0:
	# 			slst.append(int(item))
	# 	return reduce(lambda total,x: total+x, slst, 0)
		
	# def get_all_path(self,root):
	# 	if root is None:
	# 		return [[]]
	# 	res = []
	# 	if root.right is None and root.left is None:
	# 		res.append([root.val])
	# 	if root.left is not None:
	# 		for item in self.get_all_path(root.left):
	# 			res.append([root.val] + item)
	# 	if root.right is not None:		
	# 		for item in self.get_all_path(root.right):
	# 			res.append([root.val] + item)
	# 	return res

	#TO(n), SO(logn)	
	# def sumNumbers(self, root):
	# 	if root is None: return 0
	# 	return self.dfs(root, '')
	# 	# return sum(res)
	
	# def dfs(self,root, total):
	# 	#only return when there is a match:left and right are both 0
	# 	res=0
	# 	if root.left is None and root.right is None:
	# 		res += (int(total+str(root.val)))
	# 		return res
	# 	else:
	# 		if root.left:
	# 			#so all the left's final value are returning at this point 
	# 			res += self.dfs(root.left, total+str(root.val))
	# 		if root.right:
	# 			res += self.dfs(root.right, total+str(root.val))
	# 		return res
		

# 124. Binary Tree Maximum Path Sum My Submissions Question
# Total Accepted: 57763 Total Submissions: 254712 Difficulty: Hard
# Given a binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
# For example:
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return 6.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution(object):
	#if you want a int to be accessed by all the def function, we create
	# a class attribute!!!!
	# Solution.max = None---Not this one!!
	max = None
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""         
		if root is None: return 0
		Solution.max = root.val
		self.dfs(root)
		return Solution.max

	def dfs(self, root):
		if root is None: return 0
		# if root.left:
		left=self.dfs(root.left)
		# if root.right:
		right=self.dfs(root.right)
		total = root.val
		if left>0: total += left
		if right>0: total += right
		#tracking Solution.max
		Solution.max = max(Solution.max, total)
		#return half subtree, or only the root value no matter what
		if max(left, right)>0:
			return max(left, right) + root.val
		else:
			return root.val
	







