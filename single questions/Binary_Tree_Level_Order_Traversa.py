# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def depth(self, root):
		if root is None:
			return 0
		else:
			return max(self.depth(root.right), self.depth(root.left)) + 1

	def levelOrder(self, root):
		if root is None:
			return []
		d = self.depth(root)
		total_lst = []
		node_lst = [root]
		for i in range(d):
			level_val = []
			new_level_node_lst = []
			for each_node in node_lst:
				level_val.append(each_node.val)
				
				if each_node.left is not None:
					new_level_node_lst.append(each_node.left)
				if each_node.right is not None:
					new_level_node_lst.append(each_node.right)
			node_lst = new_level_node_lst
			
			if len(level_val) != 0:
				total_lst.append(level_val)
		
		return total_lst
			





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
	#print test.depth(n3)
	print test.levelOrder(n0)


