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






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def all_sum(self, root):
    	if root is None:
    		return None
    	elif root.left is None and root.right is None:
    		return [root.val]
    	else:
    		res_lst = []
    		if root.left is not None:
    			left_lst = self.all_sum(root.left) 
    			left_lst = [item + root.val for item in left_lst]
    			res_lst = res_lst + left_lst
    		if root.right is not None:
    			right_lst = self.all_sum(root.right)
    			right_lst = [item + root.val for item in right_lst]
    			res_lst = res_lst + right_lst
    		return res_lst


    def hasPathSum(self, root, sum):
    	sum_lst = self.all_sum(root)
    	res = False
    	for item in sum_lst:
    		if item == sum:
    			return True
    	return res    


if __name__ == '__main__':
	n0 = TreeNode(0)
	n1 = TreeNode(1)
	n9 = TreeNode(9)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n0.left = n1
	n0.right = n9
	n1.right = n2
	n2.left = n3
	test = Solution()
	print test.all_sum(n0)
	print test.hasPathSum(n0, 6)
	print test.hasPathSum(n0, 8)
	print test.hasPathSum(n0, 9)
