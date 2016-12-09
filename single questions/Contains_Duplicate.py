'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
1)the method implemented in more python
two general stategy:
2)use a set, and check the set with each element, hash it, if element already in the set, return True
the time-complex is O(n), the space-complex is O(n)
3)sort the array, if the next to each other are equal, return True
the time-complex is O(n*log(n)), the space complex is O(1)
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
