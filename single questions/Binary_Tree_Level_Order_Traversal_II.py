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





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def depth(self, root):
    	if root is None:
    		return 0
    	return max(self.depth(root.left), self.depth(root.right))+1

    def levelOrderBottom(self, root):
    	if root is None:
    		return []
    	res = [[root.val]]
    	dep = self.depth(root)
    	left = root.left
    	right = root.right
    	nodes = [left, right]
    	for i in range(1,dep):
    		level_res = []
    		new_nodes = []
    		for item in nodes:
    			if item is not None:
    				level_res.append(item.val)
    				new_nodes.append(item.left)
    				new_nodes.append(item.right)
    		nodes = new_nodes
    		res.append(level_res)

    	return res[::-1]


if __name__ == '__main__':
	test = Solution()
	test.levelOrderBottom()