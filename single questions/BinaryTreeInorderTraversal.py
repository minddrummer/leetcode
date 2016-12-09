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

# ##Recursive is very easy:
# def inorderTraversal(self, root):
#     """
#     :type root: TreeNode
#     :rtype: List[int]
#     """
#     if root is None:
#         return []
#     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        iteratively:::
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while len(stack) != 0 or root is not None:
        	if root is not None:
        		stack.append(root)
        		root =  root.left
        	else:
        		root = stack.pop()
        		res.append(root.val)
        		root = root.right
        return res

