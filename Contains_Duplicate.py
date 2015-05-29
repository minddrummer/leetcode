'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
'''
class Solution:
		# @param {integer[]} nums
		# @param {integer} k
		# @return {boolean}
		def containsDuplicate(self, nums):
			if (len(nums) - len(set(nums))) >= 1:
				return True
			return False
				


if __name__=='__main__':
	nums0 = [1,2,3,4,5]
	nums1 = [2,2,3,4,5]
 	nums2 = [2,2,3,4,2]

 	test = Solution()
 	print test.containsDuplicate(nums0)
 	print test.containsDuplicate(nums1)
 	print test.containsDuplicate(nums2)
