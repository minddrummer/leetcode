# Missing Number My Submissions Question Solution 
# Total Accepted: 20783 Total Submissions: 57958 Difficulty: Medium
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.class Solution(object):
class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = len(nums)
		count += 1
		total = (count-1)*count/2
		for i in nums:
			total -= i        
		return int(total)

if __name__ == '__main__':
	test1 = [0,1,3]
	test2 = [0,1,2]
	test3 = [0]
	sk = Solution()
	print sk.missingNumber(test1)
	print sk.missingNumber(test2)
	print sk.missingNumber(test3)

