# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve
# this problem.





class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
    	#```````if you directly assign the value to 'nums', the thing it works is that:
    	#nums[-k:] + nums[:-k] create two copys from nums, and assign the new object
    	#to the 'nums' variable again; and now 'nums' refers to the new object; so now the
    	#nums is a local variable
    	#nums = nums[-k:] + nums[:-k]

    	#the following code. the left side refers to the origin variable 'nums', so it will be 
    	#a global variable references!!!!!!
		if len(nums) == 0:
            nums[:] = nums[:]
        else:
            k = k%len(nums)
            nums[:] = nums[-k:] + nums[:-k]

if __name__ == '__main__':
	test = Solution()
	nums = [1,2,3,4,5,6,7]
	test.rotate(nums,3)
	num0 = [1,2]
	test.rotate(num0,3)