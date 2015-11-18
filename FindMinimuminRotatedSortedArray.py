# Suppose a sorted array is rotated at some pivot unknown 
#to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.
# Subscribe to see which companies asked this question



class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        start = nums[0]
        for i in nums[1:]:
        	if start <i:
        		continue
        	if start > i:
        		start = i
        		break
        return start



if __name__ == '__main__':
	sk = Solution()
	print sk.findMin([4,5 ,6 ,7, 0, 1 ,2])