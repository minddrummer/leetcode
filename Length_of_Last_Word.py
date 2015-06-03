'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example, 
Given s = "Hello World",
return 5.
'''

class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		##python way to do it
		# s = s.split()
		# #print s
		# if len(s) >= 1:
		# 	return len(s[-1])
		# else: 
		# 	return 0

		#more generic way to do this
		last = ''
		continue_white = True
		for i in range(1,len(s)+1):
			if s[-i] != ' ':
				continue_white = False
			if not continue_white:
				if s[-i] == ' ':
					break 
				last = last + s[-i]
		return len(last)

if __name__ == '__main__':
	test = Solution()
	print test.lengthOfLastWord('sdfsdver')        
	print test.lengthOfLastWord(' ') 
	print test.lengthOfLastWord('a') 
	print test.lengthOfLastWord(' b a ')        
