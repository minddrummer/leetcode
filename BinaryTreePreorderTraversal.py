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

#recursively
# def preorderTraversal(self, root):
# 	if root is None:
#             return []
#     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		stack = []
		res = []
		while len(stack) != 0 or root is not None:
			if root is not None:
				res.append(root.val)
				if root.right is not None:
					stack.append(root.right)
				root = root.left
			else:
				root = stack.pop()
		return res



if __name__ == '__main__':
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node1.left = node2
	node1.right = node3
	sk = Solution()
	print sk.preorderTraversal(node1)
		




