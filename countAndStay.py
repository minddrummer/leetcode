# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# Note: The sequence of integers will be represented as a string.


class Solution:
	# @param {integer} n
	# @return {string}
	def countAndSay(self, n):
		if n == 1: return '1'
		res = '1'
		for i in range(2,n+1):
			short = res[0]
			tmp = []
			pre = res[0]
			for num in res[1:]:
				if num == pre:
					short = short + num
				else:
					pre = num
					tmp.append(short)	
					short = pre	
			tmp.append(short)
			res = ''
			for item in tmp:
				times = len(item)
				res = res + str(times)+str(item[0])
		return res





if __name__ == '__main__':
	test = Solution()
	print test.countAndSay(2)        