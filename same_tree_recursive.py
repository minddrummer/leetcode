# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    # def depth(self,root):
    # 	if root is None:
    # 		return 0
    # 	else:
    # 		return max(self.depth(root.right), self.depth(root.left))+1

    def isSameTree(self, p, q):
        '''use recursive method to solve the problem'''
        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.right, q.right) & self.isSameTree(p.left, q.left)  

        #second way to code the issue:
        
        # if p is None and q is not None:
        #     return False
        # elif p is not None and q is None:
        #     return False
        # elif  p is None and q is None:
        #     return True
        # elif p.val != q.val:
        #     return False
        # else:
        #     return self.isSameTree(p.right, q.right) & self.isSameTree(p.left, q.left)
    	







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
	n00 = n0
	test = Solution()
	print test.depth(n0)
	print test.depth(n00)
	#print test.depth(n3)
	print test.isSameTree(n0, n1)

