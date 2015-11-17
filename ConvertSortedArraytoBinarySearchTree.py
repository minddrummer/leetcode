# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST
#bst attributes: the left are all< the node and the right are all > node

#this one is actually very useful

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int] #the ele are sorted in ascending order
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0: return None
        half = n/2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half+1:])

        return root

if __name__ == '__main__':
	sk =Solution()
	node = sk.sortedArrayToBST([1,2,3])






