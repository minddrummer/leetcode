# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution:
	# @param {integer[]} nums
	# @return {string[]}
	def summaryRanges(self, nums):
		if len(nums) == 0:
			return []
		if len(nums) == 1:
			return [str(nums[0])]
		len_nums = len(nums)
		spe = '->'
		i = nums[0]
		res = []
		count = 1
		for pos in range(1,len_nums):
			cur = nums[pos]
			i  += 1
			if cur == i:
				count += 1
				continue
			else:
				if count == 1:
					res.append(str(i-1))
				else:
					res.append(str(i-count)+spe+str(i-1))
				i = cur
				count = 1
		if count == 1:
			res.append(str(i))
		else:
			res.append(str(i-count+1)+spe+str(i))
			
		return res








if __name__ == '__main__':
   test  = Solution()
   print test.summaryRanges([1,2,3,5,6,7,10])    	