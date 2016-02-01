# 144. Binary Tree Preorder Traversal My Submissions Question
# Total Accepted: 103958 Total Submissions: 270118 Difficulty: Medium
# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
# Note: Recursive solution is trivial, could you do it iteratively?
# Subscribe to see which companies asked this question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # class Solution(object):
# # 	#recursion
# # 	# def preorderTraversal(self, root):
# # 	# 	if root is None:
# # 	# 		return []
# # 	# 	return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# # 	#non-recursion way
# # 	def preorderTraversal(self, root):
# # 		"""
# 		:type root: TreeNode
# 		:rtype: List[int]
# 		"""
		# stack = []
		# res = []
		# while len(stack) != 0 or root is not None:
		# 	if root is not None:
		# 		res.append(root.val)
		# 		if root.right is not None:
		# 			stack.append(root.right)
		# 		root = root.left
		# 	else:
		# 		root = stack.pop()
		# return res

		#more clear way to do it:
		#TO(n), SO(n)
		#add node.val, then add node.right first and node.left second to the stack
		# if root is None: return []
		# stack=[]
		# if root.right is not None: stack.append(root.right)
		# if root.left is not None: stack.append(root.left)
		# res=[root.val]
		# while len(stack) > 0:
		# 	node=stack.pop(-1)
		# 	if node.right is not None: stack.append(node.right)
		# 	if node.left is not None: stack.append(node.left)
		# 	res.append(node.val)
		# return res
				

# 94. Binary Tree Inorder Traversal My Submissions Question
# Total Accepted: 105771 Total Submissions: 275600 Difficulty: Medium
# Given a binary tree, return the inorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
# 	#recursion way
# 	# def inorderTraversal(self, root):
# 	# 	if root is None: return []
#  #        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
# 	def inorderTraversal(self, root):
# 		"""
# 		iteratively:::
# 		:type root: TreeNode
# 		:rtype: List[int]
# 		"""
		#TO(n),SO(n)
		#the hardship is that you donot add the right node to the stack first
		#you wait and only add the left node to the stack, until you get None left node
		#if then, you add the stack[-1].val to the res, and switch to the nearest right node, and continue on the right side
		#if the right side is also None, we move 1 level up and go to work on the 1-level-up node
		# stack = []
		# res = []
		# while len(stack) != 0 or root is not None:
		# 	if root is not None:
		# 		stack.append(root)
		# 		root =  root.left
		# 	else:
		# 		root = stack.pop()
		# 		res.append(root.val)
		# 		root = root.right
		# return res
		
# 145. Binary Tree Postorder Traversal My Submissions Question
# Total Accepted: 86388 Total Submissions: 251461 Difficulty: Hard
# Given a binary tree, return the postorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
# Note: Recursive solution is trivial, could you do it iteratively?
# Subscribe to see which companies asked this question

# Definition for a binary tree node.
# class TreeNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

# class Solution(object):
# 	# def postorderTraversal(self, root):
# 	# 	if root is None: return []
# 	# 	return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
# 	def add_left_nodes(self, root, stack):
# 		while root is not None:
# 			stack.append(root)
# 			if root.right is not None: stack.append(root.right)
# 			root=root.left
# 		#debug here	
# 		if len(stack)==0: return
# 		#here the code is the key, to make sure the stack collect the all the right nodes, and 
# 		#reach the nodes where both left and right children are Nones
# 		while stack[-1].left is not None or stack[-1].right is not None:
# 			node= stack[-1]
# 			if node.right is not None: stack.append(node.right)
# 			if node.left is not None: stack.append(node.left)


# 	def postorderTraversal(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: List[int]
# 		"""
# 		#one way to use hashtable to save info, this would be SO(n),TO(n)
# 		#but could we do better?

# 		res=[]
# 		stack=[]
# 		# add stack first
# 		self.add_left_nodes(root, stack)
# 		# print stack
# 		#set pre to be None
# 		pre=None
# 		# print stack
# 		while len(stack) != 0:
# 			node = stack[-1]
# 			# print res
# 			#if pre is a child of the current stack top, no mattter left or right
# 			if pre is node.right or pre is node.left:
# 				res.append(node.val)
# 				pre = stack.pop(-1)
# 			else:
# 				#donto want to add node first, so, add right, and then go to the left node
# 				#but it doesnot matter, since in the add_left_nodes, we will check the stack again to make sure 
# 				#that we go to the right place!
# 				#or it can be
# 				#node=stack.pop(-1)
# 				#self.add_left_nodes(node, stack)
# 				#pre=None
# 				if node.right is not None: stack.append(node.right)
# 				self.add_left_nodes(node.left, stack)
# 				# has reset pre to be None
# 				pre = None
# 		# print res		
# 		return res
# if __name__ == '__main__':
# 	node1=TreeNode(1)
# 	node2=TreeNode(2)
# 	node3=TreeNode(3)
# 	node1.left=node2
# 	node1.right=node3
# 	sk=Solution()
# 	print sk.postorderTraversal(node1)


# 107. Binary Tree Level Order Traversal II My Submissions Question
# Total Accepted: 67516 Total Submissions: 205902 Difficulty: Easy
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {TreeNode} root
#     # @return {integer[][]}
#     def depth(self, root):
#     	if root is None:
#     		return 0
#     	return max(self.depth(root.left), self.depth(root.right))+1

#     def levelOrderBottom(self, root):
#     	if root is None:
#     		return []
#     	res = [[root.val]]
#     	dep = self.depth(root)
#     	left = root.left
#     	right = root.right
#     	nodes = [left, right]
#     	for i in range(1,dep):
#     		level_res = []
#     		new_nodes = []
#     		for item in nodes:
#     			if item is not None:
#     				level_res.append(item.val)
#     				new_nodes.append(item.left)
#     				new_nodes.append(item.right)
#     		nodes = new_nodes
#     		res.append(level_res)

#     	return res[::-1]

#iterative version
# def levelOrderBottom(self, root):
#     	if root is None:
#     		return []
#     	stack=[root]
#     	res=[]
		#the trick here for stack is very  interesting!!
#     	while len(stack)>0:
#     	    each_res=[]
#     	    each_stack=[]
#     	    while len(stack)>0:
#     	        node=stack.pop(0)
#     	        each_res.append(node.val)
#     	        if node.left is not None: each_stack.append(node.left)
#     	        if node.right is not None: each_stack.append(node.right)
#             stack=each_stack
#             res.insert(0,each_res)
#         return res
# #recursive version:recursvion verion is actually not straight forward
# keep the res maintained(more Space memory), and whenever you meet a level node, add the corresponding element appened to  the res
# def preorder(self, root, level, res):
# 	if root:
# 		if len(res) < level+1: res.insert(0,[])
# 		res[-(level+1)].append(root.val)
# 		self.preorder(root.left, level+1, res)
# 		self.preorder(root.right, level+1, res)


# def levelOrderBottom(self, root):
# 	res=[]
# 	level=0
# 	self.preorder(root, level, res)
# 	return res





# 102. Binary Tree Level Order Traversal My Submissions Question
# Total Accepted: 85563 Total Submissions: 273295 Difficulty: Easy
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#iterative here: donot need to get the depth actually
# class Solution:
# 	# @param {TreeNode} root
# 	# @return {integer[][]}
# 	def depth(self, root):
# 		if root is None:
# 			return 0
# 		else:
# 			return max(self.depth(root.right), self.depth(root.left)) + 1

# 	def levelOrder(self, root):
# 		if root is None:
# 			return []
# 		d = self.depth(root)
# 		total_lst = []
# 		node_lst = [root]
# 		for i in range(d):
# 			print i
# 			level_val = []
# 			new_level_node_lst = []
# 			for each_node in node_lst:
# 				level_val.append(each_node.val)
				
# 				if each_node.left is not None:
# 					new_level_node_lst.append(each_node.left)
# 				if each_node.right is not None:
# 					new_level_node_lst.append(each_node.right)
# 			node_lst = new_level_node_lst
			
# 			if len(level_val) != 0:
# 				total_lst.append(level_val)
		
# 		return total_lst

#recursion: 
# class Solution:
# 	# @param {TreeNode} root
# 	# @return {integer[][]}
# 	def traverse(self, root, level, res):
# 	    if root:
#			#you can use either == level, or < level+1!
# 	        if len(res) == level: res.append([])
# 	        res[level].append(root.val)
# 	        self.traverse(root.left, level+1, res)
# 	        self.traverse(root.right, level+1, res)
# 	def levelOrder(self, root):
# 		res=[]
# 		self.traverse(root, 0,res)
# 		return res


# 107. Binary Tree Level Order Traversal II My Submissions Question
# Total Accepted: 67517 Total Submissions: 205903 Difficulty: Easy
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# Subscribe to see which companies asked this question


# class Solution:
#     # @param {TreeNode} root
#     # @return {integer[][]}
#     def depth(self, root):
#     	if root is None:
#     		return 0
#     	return max(self.depth(root.left), self.depth(root.right))+1

#     def levelOrderBottom(self, root):
#     	if root is None:
#     		return []
#     	res = [[root.val]]
#     	dep = self.depth(root)
#     	left = root.left
#     	right = root.right
#     	nodes = [left, right]
#     	for i in range(1,dep):
#     		level_res = []
#     		new_nodes = []
#     		for item in nodes:
#     			if item is not None:
#     				level_res.append(item.val)
#     				new_nodes.append(item.left)
#     				new_nodes.append(item.right)
#     		nodes = new_nodes
#     		res.append(level_res)
#     	return res[::-1]



# 103. Binary Tree Zigzag Level Order Traversal My Submissions Question
# Total Accepted: 52216 Total Submissions: 188386 Difficulty: Medium
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
# 	# def zigzagLevelOrder(self, root):
# 		"""
# 		:type root: TreeNode
# 		:rtype: List[List[int]]
# 		"""
# 		#iterative
# 		#method1: just reverse the each_res given the even condition
# 		# if root is None: return []
# 		# res=[]
# 		# queue = [root]
# 		# even = True
# 		# while len(queue) > 0:
# 		# 	each_queue=[]
# 		# 	each_res=[]
# 		# 	while len(queue)>0:
# 		# 		node=queue.pop(0)
# 		# 		each_res.append(node.val)
# 		# 		if node.left is not None: each_queue.append(node.left)
# 		# 		if node.right is not None: each_queue.append(node.right)
# 		# 	#only reverse the result would work
# 		# 	if not even:
# 		# 		each_res= each_res[::-1]
# 		# 	even = not even
# 		# 	queue=each_queue
# 		# 	res.append(each_res)
# 		# return res
# 		#method2: not reverse at the end, but re-structure the each_res generating order at each step
# 		# if root is None: return []
# 		# res=[]
# 		# queue = [root]
# 		# even = True
# 		# while len(queue) > 0:
# 		# 	each_queue=[]
# 		# 	each_res=[]
# 		# 	while len(queue)>0:
# 		# 		node=queue.pop(0)
# 		# 		if node.left is not None: each_queue.append(node.left)
# 		# 		if node.right is not None: each_queue.append(node.right)				
# 		# 		if even:
# 		# 			each_res.append(node.val)
# 		# 		else:
# 		# 			each_res.insert(0, node.val)
# 		# 	queue=each_queue
# 		# 	even = not even
# 		# 	res.append(each_res)
# 		# return res			
# 		#method3: not change the each_res order, but change the queue order at each step:this one  is more complicated, and not more efficient
# 		# if root is None: return []
# 		# res=[]
# 		# queue = [root]
# 		# even = True
# 		# while len(queue) > 0:
# 		# 	each_queue=[]
# 		# 	each_res=[]
# 		# 	while len(queue)>0:
# 		# 		node=queue.pop(-1)
# 		# 		each_res.insert(0,node.val)
# 		# 		if even: 
# 		# 			if node.right is not None: each_queue.append(node.right)				
# 		# 			if node.left is not None: each_queue.append(node.left)
# 		# 		else:
# 		# 			if node.left is not None: each_queue.append(node.left)
# 		# 			if node.right is not None: each_queue.append(node.right)				
# 		# 	queue=each_queue
# 		# 	even = not even
# 		# 	res.append(each_res)
# 		# return res


# 	#recursive method
# 	#add even variable
# 	#which way to go first , left/right? you need some simple exmaple to test it to get it clear:more efficient

# 	def preorder(self, root, level, res, even):
# 		if root:
# 			if len(res)<level+1: res.append([])
# 			if even:
# 				res[level].append(root.val)
# 			else:
# 				res[level].insert(0, root.val)
# 			self.preorder(root.left, level+1, res, not even)
# 			self.preorder(root.right, level+1, res, not even)

# 	def zigzagLevelOrder(self, root):
# 		res=[]
# 		even=True
# 		self.preorder(root, 0, res, even)
# 		return res


	  


# 100. Same Tree My Submissions Question
# Total Accepted: 105724 Total Submissions: 248338 Difficulty: Easy
# Given two binary trees, write a function to check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
# Subscribe to see which companies asked this question
# Show Tags
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		'''use recursive method to solve the problem'''
		#recursion
		#TO(n), SO(logn)--because you have to hold 1/2 nodes at each level's results, so at the ending level, it would be O(n) nodes
		#however, due to recursion's calling, first left,and then right, we dnot haveto remember all the results at each level at the same time
		#we only need each ending point's result; but:: we need to hold the log(n) level's memory, so the SO is log(n)
		# if p is None or q is None:
		#     if p is None and q is None:
		#         return True
		#     else:
		#         return False
		# else:
		#     if p.val != q.val:
		#         return False
		#     else:
		#         return self.isSameTree(p.right, q.right) & self.isSameTree(p.left, q.left)  
		#iteration
		# stack=[(p,q)]
		# while len(stack)>0:
		# 	each_stack=[]
		# 	while len(stack)>0:
		# 		pair = stack.pop(-1)
		# 		if pair[0] and pair[1]:
		# 			if pair[0].val != pair[1].val: return False
		# 			if bool(pair[0].left) ^ bool(pair[1].left): return False
		# 			if bool(pair[0].right) ^ bool(pair[1].right): return False
		# 			each_stack.append((pair[0].left, pair[1].left))
		# 			each_stack.append((pair[0].right, pair[1].right))
		# 		elif bool(pair[0]) ^ bool(pair[1]):
		# 			return False
		# 		else:
		# 			continue
		# 	stack=each_stack
		# return True

# 101. Symmetric Tree My Submissions Question
# Total Accepted: 90524 Total Submissions: 274211 Difficulty: Easy
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# Subscribe to see which companies asked this question
# Show Tags


# class Solution:
#     # @param {TreeNode} root
#     # @return {boolean}
#     #recursion
#   #   def help(self, left, right):
# 		# if (not left) and (not right): return True
# 		# if left and right and left.val == right.val:
# 		# 	return self.help(left.right, right.left) and self.help(left.left, right.right)
# 		# return False

#   #   def isSymmetric(self, root):
#   #   	if not root:
#   #   		return True
#   #   	else:
#   #   		return self.help(root.right,root.left)
#     #iteration
#     def isSymmetric(self, root):
#     	if root is None: return True
#     	stack = [root.left, root.right]
#     	while len(stack)>0:
#     		each_stack=[]
#     		while len(stack) > 0:
#     			#you can make it symmetric in the list;
#     			#you can like the above problem, make it as a pair
#     			left=stack.pop(0)
#     			right=stack.pop(-1)
#     			if left and right:
#     				if left.val != right.val:
#     					return False
#     				each_stack.insert(0,left.right)
#     				each_stack.insert(0,left.left)
#     				each_stack.append(right.left)
#     				each_stack.append(right.right)
#     			elif bool(left)^bool(right):
#     				return False
#     			else:
#     				continue
#     		stack = each_stack
#     	return True


# 110. Balanced Binary Tree My Submissions Question
# Total Accepted: 92809 Total Submissions: 279510 Difficulty: Easy
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems
# class Solution:
#     # @param {TreeNode} root
#     # @return {boolean}
#     # if you add depth here, it is easy to do it, but TO(n^2), SO(logN)
#     # def depth(self, root):
#     # 	'''
#     # 	return the depth for the current node
#     # 	'''
#     # 	if root is None:
#     # 		return 0
#     # 	else:
#     # 		d = max(self.depth(root.right), self.depth(root.left)) + 1
#     # 		return d
#     # def isBalanced(self, root):
#     # 	'''has to be for every node!'''
#     # 	if root is None:
#     # 		return True
#     # 	elif self.isBalanced(root.right) and self.isBalanced(root.left):
#     # 		return abs(self.depth(root.right) - self.depth(root.left)) <= 1
#     # 	else:
#     # 		return False
#     # we need TO(n) method:
#     def balanceHeight(self, root):
#     	''' we donot return the exact height, but whether the height for its two subtree balance or not
#     	#if balance returnt the HEIGHT; otherwise, return -1'''
#     	#TO(n)
#     	if not root:
#     		return 0
#     	left = self.balanceHeight(root.left)
#     	right = self.balanceHeight(root.right)
#     	if left < 0 or right < 0 or abs(left-right)>1: return -1
#     	return max(left,right)+1
#     def isBalanced(self, root):	
#     	return self.balanceHeight(root)>=0


# 114. Flatten Binary Tree to Linked List My Submissions Question
# Total Accepted: 71823 Total Submissions: 238265 Difficulty: Medium
# Given a binary tree, flatten it to a linked list in-place.
# For example,
# Given
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# click to show hints.
# Hints:
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
	# def flatten(self, root):
	# 	"""
	# 	:type root: TreeNode
	# 	:rtype: void Do not return anything, modify root in-place instead.
	# 	"""
	# 	#recursion: it is very smart and elegant to use recursion here
	# 	#the trick is that : we assume everything is going on right before the current step!!!
	#   TO(n), SO(logN)
	# 	if root is None: return
	# 	self.flatten(root.left)
	# 	self.flatten(root.right)

	# 	if root.left is None: return
	# 	tmp= root.left
	# 	while tmp.right is not None:
	# 		tmp = tmp.right
	# 	tmp.right=root.right
	# 	root.right=root.left
	# 	root.left = None
		

		#iteration
		#TO(n) , SO(logN)
		# stack=[]
		# while root is not None:
		# 	if root.right is not None: stack.append(root.right)
		# 	tmp = root.left
		# 	if tmp: 
		# 		root.right = tmp
		# 		root.left = None
		# 		root= tmp
		# 	else:
		# 		if len(stack)>0:
		# 			tmp0 = stack.pop(-1)
		# 			root.right = tmp0
		# 			root = tmp0
		# 		else:
		# 			root = None
			

# 116. Populating Next Right Pointers in Each Node My Submissions Question
# Total Accepted: 76392 Total Submissions: 209835 Difficulty: Medium
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
#     def connect(self, root):
# 		"""
# 		:type root: TreeLinkNode
# 		:rtype: nothing
# 		"""
# 		#BFS could solve this problem, but the space will be proportional(equal) to O
# 		#method2 treated as linked list, and each time: connect parent's left or right to child
# 		if root is None:
# 			return				
# 		parent = root
# 		parent.next = None
# 		child = parent.left
# 		first_child = child
# 		while child is not None:
# 			if child == parent.left:
# 				child.next = parent.right
# 				child = child.next
# 			else:
# 				parent = parent.next
# 				if parent is not None:
# 					child.next = parent.left
# 					child = child.next
# 				else:
# 					parent = first_child
# 					child.next = None
# 					child = parent.left
# 					first_child = child



# 117. Populating Next Right Pointers in Each Node II My Submissions Question
# Total Accepted: 54067 Total Submissions: 166295 Difficulty: Hard
# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
# Subscribe to see which companies asked this question
# # Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# class Solution(object):
	# def loop(self, parent, child):
	# 	while child is None and parent.next is not None:
	# 		parent = parent.next
	# 		child = parent.left if parent.left else parent.right
	# 	return parent, child
	# def connect(self, root):
	# 	"""
	# 	:type root: TreeLinkNode
	# 	:rtype: nothing
	# 	"""
	# 	#iteration: SO(1), TO(n)
	# 	if root is None: return 
	# 	parent = root
	# 	root.next = None
	# 	child = root.left
	# 	if child is None: child = root.right
	# 	firstchild = child #firstchild is not None at least at beginning
	# 	while firstchild is not None:
	# 		if child is parent.left:
	# 			nextchild=parent.right
	# 			parent, nextchild = self.loop(parent, nextchild)
	# 		else:
	# 			nextchild = None 
	# 			parent, nextchild = self.loop(parent, nextchild)
	# 		if nextchild:
	# 				child.next = nextchild
	# 				child = nextchild
	# 		else:
	# 			child.next = None
	# 			parent = firstchild
	# 			child = parent.left if parent.left else parent.right
	# 			parent, child = self.loop(parent, child)
	# 			firstchild = child

	#recursion is pretty nice and well-structured here
	# def connect(self, root):
	# 	if root:
	# 		parent=root; child = None; nextnode = None
	# 		while parent:
	# 			if parent.left:
	# 				if child: child.next = parent.left
	# 				child = parent.left
	# 				if nextnode is None: nextnode = parent.left
	# 			if parent.right:
	# 				if child: child.next = parent.right
	# 				child = parent.right
	# 				if nextnode is None: nextnode = parent.right
	# 			parent = parent.next
	# 		self.connect(nextnode)

# if __name__ == '__main__':
# 	sk = Solution()
# 	node1=TreeLinkNode(1)
# 	node2=TreeLinkNode(2)
# 	node3=TreeLinkNode(3)
# 	node4=TreeLinkNode(4)
# 	node5=TreeLinkNode(5)
# 	node1.left=node2
# 	node1.right = node3
# 	node2.left = node4
# 	node3.right = node5
# 	sk.connect(node1)
# 	# print node1.next
# 	# print node2.next.val
# 	# print node3.next is None
# 	# print node4.next.val
# 	# print node5.next is None


# 99. Recover Binary Search Tree My Submissions Question
# Total Accepted: 46634 Total Submissions: 181688 Difficulty: Hard
# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

# Subscribe to see which companies asked this question

# Show Tags

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """     					            		                                    			    	                        