# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	'''in place algorithm, cannot make a new array'''
    	if len(nums) == 0 or len(nums) == 1:
    		return len(nums)
    	# pres = nums[0]
    	# i = 1
    	# while i <= len(nums)-1:
    	# 	#print 'the pres now is :',  pres
    	# 	#print 'the index i is:', i
    	# 	if nums[i] == pres:
    	# 		#print 'the pop out number is : ', nums.pop(i) 
    	# 		nums.pop(i)
    	# 	else:
    	# 		pres = nums[i]
    	# 		i += 1
    	# return len(nums)
    	pres = nums[0]
    	count = 1
    	for i in nums[1:]:
    		if i > pres:
    			count += 1
    			pres = i
    	return count


if __name__ == '__main__':
	test =  Solution()
	print test.removeDuplicates([1,1,1,2,2,3])    	