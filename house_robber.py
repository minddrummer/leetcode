# You are a professional robber planning to rob houses along a street. Each house has a certain 
# amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent
# houses have security system connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine 
# the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
    	'''
    	this is a dynamic programming question; 
    	dp: it is you segment the big problem into small steps; and solve the small question before you
    	move into the next steps
    	'''
    	# if len(nums) == 0:
    	# 	return 0
    	# dp = {}
    	# dp[0] = 0
    	# dp[1] = nums[0]
    	# for i in range(1, len(nums)):
    	# 	dp[i+1] = max(nums[i]+dp[i+1-2], dp[i+1-1])

    	# max_value = 0
    	# for key in dp:
    	# 	max_value = max(max_value, dp[key])
    	# return max_value
    	if len(nums) == 0: return 0
    	pre = 0
    	max_value = nums[0]
    	for i in range(1, len(nums)):
    		tmp = max(nums[i]+ pre, max_value)
    		pre = max_value
    		max_value = tmp

    	return max_value

if __name__ == '__main__':
	test = Solution()
	print test.rob([1,2,1,7,2,4,10])