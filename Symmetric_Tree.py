#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def help(self, left, right):
		if (not left) and (not right): return True
		if left and right and left.val == right.val:
			return self.help(left.right, right.left) and self.help(left.left, right.right)
		return False

    def isSymmetric(self, root):
    	if not root:
    		return True
    	else:
    		return self.help(root.right,root.left)

	




if __name__ == '__main__':
	n0 = TreeNode(0)
	n1 = TreeNode(1)
	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)
	n5 = TreeNode(3)
	n6 = TreeNode(2)
	n0.left = n1
	n0.right = n2
	n1.left = n3
	n1.right = n4
	n2.left = n5
	#n2.right = n6
	test = Solution()
	#print test.depth(n0)
	#print test.depth(n00)
	#print test.depth(n3)
	print test.isSymmetric(n0)





