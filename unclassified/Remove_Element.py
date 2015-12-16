# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.




class Solution:
	# @param {integer[]} nums
	# @param {integer} val
	# @return {integer}

	def removeElement(self, nums, val):
		
		res =[]
		#print len(nums)
		for i in range(len(nums)):
			if nums[i] != val:
				res.append(nums[i])
			#print i
		return len(res)





if __name__ == '__main__':
	
	test = Solution()
	#test.fuck(10)
	print test.removeElement([1,2,3],2)
	print test.removeElement([1,2,3,2,2,5],2)
		