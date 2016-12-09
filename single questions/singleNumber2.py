# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:

# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         dct = {}
#         for i in nums:
#         	if i not in dct:
#         		dct[i] = 1
#         	else:
#         		dct.pop(i)
#         return dct.keys()	
 
# class Solution:
#     # @param {integer[]} nums
#     # @return {integer[]}
#     def singleNumber(self, nums):
#         xor = reduce(lambda x, y : x ^ y, nums)
#         lowbit = xor & -xor
#         a = b = 0
#         for num in nums:
#             if num & lowbit:
#                 a ^= num
#             else:
#                 b ^= num
#         return [a, b]        



class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
    	xor = 0
    	for num in nums:
    		xor ^= num
    	lowbit = xor & -xor

    	a = b = 0
    	for num in nums:
    		if lowbit & num:
    			a ^= num
    		else:
    			b ^= num
    	return [a,b]			


if __name__ == '__main__':
	test1 = [1,2,3,1,3,2,4,5]

	test2 = [1,2,3,3]
	s = Solution()
	print s.singleNumber(test1)
	print s.singleNumber(test2)



