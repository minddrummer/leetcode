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




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		lst = self.get_all_path(root)
		slst= []
		for item in lst:
			item = ''.join(str(i) for i in item)
			if len(item) != 0:
				slst.append(int(item))
		return reduce(lambda total,x: total+x, slst, 0)
		
	def get_all_path(self,root):
		if root is None:
			return [[]]
		res = []
		if root.right is None and root.left is None:
			res.append([root.val])
		if root.left is not None:
			for item in self.get_all_path(root.left):
				res.append([root.val] + item)
		if root.right is not None:		
			for item in self.get_all_path(root.right):
				res.append([root.val] + item)
		return res
			
if __name__ == '__main__':
	test = Solution()
	test.sumNumbers()












