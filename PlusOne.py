# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
	# @param {integer[]} digits
	# @return {integer[]}
	def plusOne(self, digits):  
		up = 1
		for i in range(len(digits)-1, -1, -1):
			if digits[i] + up == 10:
				digits[i] = 0
				up = 1
			elif i != len(digits) - 1 and up == 0:
				break
			else:	
				digits[i] = digits[i] + 1
				up = 0 
			
		if up == 1:
			digits.insert(0,1)
		return digits


		# num  = ''.join([str(i) for i in digits])
		# res = ''
		# up = 0
		# for i in range(len(digits)-1, -1, -1):
		# 	if up == 0 and i != len(digits)-1:
		# 		res = res + num[0:i+1][::-1]
		# 		break
		# 	if i == len(digits)-1 and int(num[i]) + 1 >= 10:
		# 		res = res + '0'
		# 		up = 1
		# 	elif i == len(digits)-1 and int(num[i]) + 1 < 10:
		# 		res = res + str(int(num[i]) + 1)
		# 		up = 0
		# 	elif i != len(digits)-1 and int(num[i]) + up >= 10:
		# 		res = res + '0'
		# 		up = 1
		# 	elif i != len(digits)-1 and int(num[i]) + up < 10:
		# 		res = res + str(int(num[i]) + up)
		# 		up = 0
		# 	else:
		# 		pass
		# if up == 1:
		# 	res = res + '1'
		# res = [int(item) for item in list(res[::-1])]
		# return res


if __name__ == '__main__':
	test = Solution()
	print test.plusOne([1,2,3])