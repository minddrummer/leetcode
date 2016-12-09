# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
    	'''
    	it is compute the factorial's 0
    	'''
    	count = 0
    	i = 1
    	while 5**i <= n:
    		count += n/5**i
    		i += 1
    	return count

if __name__ == '__main__':
	test = Solution()
	print test.trailingZeroes(5)        