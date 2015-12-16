# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 
# 	00000010100101000001111010011100), return 964176192 
# (represented in binary as 00111001011110000010100101000000).




class Solution:
	# @param n, an integer
	# @return an integer
	def compute_bit_digits(self, n):
		i = 0
		while True:
			if 2**i > n:
				break
			i += 1
		return i-1
	def convert_10_to_bits(self, n):
		digit_num = self.compute_bit_digits(n)
		if n == 0:
			bits = ['0'] 
		else:
			bits = ['1'] + digit_num*['0']
		while n - 2**digit_num > 0:
			n = n - 2**digit_num
			digit_num = self.compute_bit_digits(n)
			bits[-(digit_num+1)] = '1'
		if len(bits) < 32:
			bits = (32 - len(bits))*['0'] + bits
		return ''.join(bits)
	def reverseBits(self, n):
		bits = self.convert_10_to_bits(n)
		re_bits = bits[::-1]
		#print bits
		#print re_bits
		num_10 = 0
		#re_bits = '00000000000000000000000000001010'	
		for i in range(len(re_bits)):
			num_10 += 2**(31-i)*int(re_bits[i])
		return num_10


if __name__ == '__main__':
	test  = Solution()
	print test.compute_bit_digits(10)
	print test.convert_10_to_bits(10)
	print test.reverseBits(43261596)
