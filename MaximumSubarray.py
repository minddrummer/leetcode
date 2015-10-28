# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cur_max = max(nums)
        for i in nums:
        	total += i
        	if total > cur_max:
        		cur_max = total
        	if total < 0:
        		total = 0
        return cur_max
        





if __name__ == '__main__':
	test1 = [1,2,3,4,5,6,-1,8]
	test1 = [-2,1,-3,4,-1,2,1,-5,4]
	test1 = [-2,-6,-1]

	sk = Solution()
	print sk.maxSubArray(test1)

