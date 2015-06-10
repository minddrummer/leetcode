# Write a function that takes an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight)
# For example, the 32-bit integer '11' has binary representation 
#00000000000000000000000000001011
# so the function should return 3



class Solution:
	# @param n, an integer
	# @return an integer
	def compute_2_index(self, n):
		i = 0
		if n == 0:
			return 0
		while True:
			if n < 2**i:
				break
			i += 1			
		return i - 1
	def hammingWeight(self, n):
		'''
		first transfer to binary number,
		then count the 1s in there
		'''
		count = 0
		while n - 2**self.compute_2_index(n) >=0:
			count += 1
			n = n - 2**self.compute_2_index(n)
		return count


if __name__ == '__main__':
	test = Solution()
	print test.compute_2_index(11)
	print test.hammingWeight(11)