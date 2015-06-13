# Google: 90% of our engineers use the software you wrote (Homebrew), but you cannot invert a binary tree on a whiteboard so fuck off
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		if root is None:
			return None
		tmp = root.left
		root.left = self.invertTree(root.right)
		root.right = self.invertTree(tmp)
		return root









if __name__ == '__main__':
	n0 = TreeNode(0)
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(2)
	n4 = TreeNode(3)
	n5 = TreeNode(3)
	n6 = TreeNode(2)
	n0.left = n1
	n0.right = n2
	n1.left = n3
	n1.right = n4
	n2.left = n5
	test = Solution()
	print n0.right.val
	print n0.left.val
	n99 = test.invertTree(n0)
	print n99.right.val
	print n99.left.val






