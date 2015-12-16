# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.



class Solution:
	# @param {string} str
	# @return {integer}
	def myAtoi(self, str):
		if len(str) == 0:
			return 0
		s = str
		s = s.strip()
		num_lst = ['0','1','2','3','4','5','6','7','8','9','-']
		res = []
		for letter in s:
			if letter in num_lst:
				res.append(letter)
		if len(res) == 0:
			return 0
		res1 = []
		#print res
		
		res1.append(res[0])

		for i in res[1:]:
		    if i != '-':
		        res1.append(i)
		#print res1
		if len(res1) == 1 and '-' in res1:
		    return 0
		#print res1
		res1 = int(''.join(res1))
		return res1


if __name__ == '__main__':
	test = Solution()
	print test.myAtoi('-abc')
	print test.myAtoi('1')