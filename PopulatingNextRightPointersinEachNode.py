# Given a binary tree

#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL








# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
	def connect(self, root):
		"""
		:type root: TreeLinkNode
		:rtype: nothing
		"""
		#BFS could solve this problem, but the space will be proportional(equal) to Log(n+1)-1
		#method2 treated as linked list, and each time: connect parent's left or right to child
		if root is None:
			return				
		parent = root
		parent.next = None
		child = parent.left
		first_child = child
		while child is not None:
			if child == parent.left:
				child.next = parent.right
				child = child.next
			else:
				parent = parent.next
				if parent is not None:
					child.next = parent.left
					child = child.next
				else:
					parent = first_child
					child.next = None
					child = parent.left
					first_child = child



if __name__ == '__main__':
	#	test
	node1= TreeLinkNode(1)
	node2= TreeLinkNode(2)
	node3= TreeLinkNode(3)
	node4= TreeLinkNode(4)
	node5= TreeLinkNode(5)
	node6= TreeLinkNode(6)
	node7= TreeLinkNode(7)

	node1.left = node2
	node1.right = node3

	node2.left = node4
	node2.right = node5

	node3.left = node6
	node3.right = node7


	#
	sk = Solution()
	sk.connect(node1)
