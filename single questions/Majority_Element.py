# Given an array of size n, find the majority element. The majority element is the element that 
# appears more than n/2 time
# You may assume that the array is non-empty and the majority element always exist in the array.



class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def majorityElement(self, nums):
		res = {}
		thres = len(nums)/2
		for i in nums:
			if i not in res:
				res[i] = 1
			else:
				res[i] += 1
			if res[i] > thres:
				break
		return i			





if __name__ == '__main__':
	test = Solution()
	print test.majorityElement([1,2,2])
