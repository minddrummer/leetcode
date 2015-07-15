# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    	if root is None:
    		return 0
    	elif root.right is None and root.left is None:
    		return 1
    	elif root.right is None and root.left is not None:
    		return self.minDepth(root.left) + 1
    	elif root.right is not None and root.left is None:
    		return self.minDepth(root.right) + 1
    	else:	
    		return min(self.minDepth(root.right), self.minDepth(root.left)) + 1




