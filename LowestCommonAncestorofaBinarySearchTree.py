# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {TreeNode}
	def match_node(self, node, root):
		if root is None:
			return None
		elif root is node:
			return [node]
		elif self.match_node(node, root.left) is not None and self.match_node(node, root.left)[-1] is node:
			return [root]+self.match_node(node, root.left)
		elif self.match_node(node, root.right) is not None and self.match_node(node, root.right)[-1] is node:
			return [root]+self.match_node(node, root.right)
		else:
			return None
			
		# if root is None:
		# 	return None
		# if root is node:
		# 	return [node]
		# else:
		# 	if self.match_node(node, root.left) is None and self.match_node(node, root.right) is None:
		# 		return None
		# 	elif self.match_node(node, root.left) is not None and self.match_node(node, root.right) is None:
		# 		if self.match_node(node, root.left)[-1] is node:
		# 			return [root]+self.match_node(node, root.left)
		# 		else:
		# 			return None
		# 	elif self.match_node(node, root.left) is None and self.match_node(node, root.right) is not None:
		# 		if self.match_node(node, root.right)[-1] is node:
		# 			return [root]+self.match_node(node, root.right)
		# 		else:
		# 			return None
		# 	else:
		# 		if self.match_node(node, root.left)[-1] is node:
		# 			return [root]+self.match_node(node, root.left)
		# 		if self.match_node(node, root.right)[-1] is node:
		# 			return [root]+self.match_node(node, root.right)

	def lowestCommonAncestor(self, root, p, q):
		p_lst = self.match_node(p,root)[::-1]
		q_lst = self.match_node(q,root)
		for node in p_lst:
			for sec in q_lst:
				if node == sec:
					return node


if __name__ == '__main__':
	test = Solution()
