# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 2
# [1,3,5,6], 2 1
# [1,3,5,6], 7 4
# [1,3,5,6], 0 0





class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
        	return 0 
        for i in range(len(nums)-1):
        	if nums[i] == target:
        		return i
        	if nums[i] < target and nums[i+1] > target:
        		return i+1
        if nums[-1] == target:
        	return len(nums)-1
        return len(nums)

if __name__ == '__main__':
	sk = Solution()
	print sk.searchInsert([0,1,2],3)
	print sk.searchInsert([0,1,4],3)
	print sk.searchInsert([0,1,4],-3)
