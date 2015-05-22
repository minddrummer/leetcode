# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def depth(self, root):
    	'''
    	return the depth for the current node
    	'''
    	if root is None:
    		return 0
    	else:
    		d = max(self.depth(root.right), self.depth(root.left)) + 1
    		return d



    def isBalanced(self, root):
    	'''has to be for every node!'''
    	if root is None:
    		return True
    	elif self.isBalanced(root.right) and self.isBalanced(root.left):
    		return abs(self.depth(root.right) - self.depth(root.left)) <= 1
    	else:
    		return False

    	
    	

if __name__ == '__main__':
	n0 = TreeNode(0)
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n0.left = n1
	n1.right = n2
	n2.left = n3
	test = Solution()
	print test.isBalanced(n0)




        