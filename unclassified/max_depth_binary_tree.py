# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
    	'''
    	use recursive fucntion to call itself, from right and left, plus 1 for the current depth; that is it
    	'''

    	if root is None:
    		return 0
    	return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 



