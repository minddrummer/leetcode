# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Hint:

# Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
# Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
# There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)





class Solution(object):
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num >= 2**31-1:
			print 'the input in invalid'
			return None
		pass

	def generate_str(self, ns):
		'''ns is a string with exact three digits'''
		slst = ['One', 'Two','Three','Four','Five','Six','Seven','Eight','Nine']
		dlst = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen', 'Nineteen']
		tylst = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
		sdct = dict(zip(range(1,10), slst))
		ddct = dict(zip(range(10,20), dlst))
		tydct = dict(zip(range(2,10), tylst))
		res = []
		if ns[0] != '0':
			if ns[0] == '1':
				res.append(sdct[int(ns[0])] + ' Hundred')
			else:
				res.append(sdct[int(ns[0])] + ' Hundreds')
		if ns[1] != '0':
			print ns
			if ns[1] == '1':
				res.append(ddct[int(ns[1:])])
				return res
			else:
				res.append(tydct[int(ns[1])])
		if ns[2] != '0':
			res.append(sdct[int(ns[2])])
		return res

	def seg(self,num):
		if num < 1000:
			ns = str(num)
		else:
			ns = str(num)
		pass





if __name__ == '__main__':
	test = Solution()
	print test.generate_str('123')        
	print test.generate_str('019')
	print test.generate_str('112')        
