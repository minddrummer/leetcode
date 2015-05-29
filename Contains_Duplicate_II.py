'''
Given an array of integers and an integer k, return true if and only if there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is 
at most k.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
       	if (len(nums) - len(set(nums))) != 1:
       		return False   
       	
       	for i in range(len(nums)):
       		init_num = nums[i]
       		rest_nums = nums[(i+1):]
       		try:
       			cp_num_index = rest_nums.index(init_num)
       			gap_index = cp_num_index + 1
       			break
       		except ValueError:
       			continue
       	if gap_index > k:
       		return False
       	return True


if __name__=='__main__':
 nums0 = [1,2,3,4,5]
 nums1 = [2,2,3,4,5]
 nums2 = [2,2,3,4,2]

 test = Solution()
 print test.containsNearbyDuplicate(nums0, 1)
 print test.containsNearbyDuplicate(nums1, 1)
 print test.containsNearbyDuplicate(nums2, 1)
