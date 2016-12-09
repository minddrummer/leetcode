# # Given an array of integers, every element appears twice except for one. Find that single one.

# # Note:
# # Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# class Solution(object):
# 	def singleNumber(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		method: 1)brute-force 0.5*n^2 2)dictionary: need additional memory to save the dict 
# 		3)how to use no additional memory?
# 		"""

# 		dct={}
# 		for i in nums:
# 			if i not in dct:
# 				dct[i] = 0
# 			else:
# 				dct.pop(i, None)
# 		if len(dct) != 0:
# 			return dct.keys()[0]
# 		else:
# 			return None

#this has no using additional memory method
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	if len(A) == 0: return None
        res = 0
        for a in A:
            res = res ^ a
        return res

if __name__ == '__main__':
	test = Solution()
	print test.singleNumber([1,2,3,2,3])        
	#print test.singleNumber([1,2,3,2,3,1,4])        
	print test.singleNumber([])
	# print test.singleNumber([1,1,0])
	# print test.singleNumber([0,1,0])        



