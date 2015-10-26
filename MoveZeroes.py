class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums) <= 1:
			return
		i = 0
		j = len(nums) - 1
		while i < j:
			if nums[i] == 0:
				nums[i:] = nums[i+1:]+[0] 
				i -= 1   
				j -= 1 
			i+=1	
		

if __name__ == '__main__':
	sk = Solution()
	test1= [1,2,0,3]
	sk.moveZeroes(test1)       
	print test1 



