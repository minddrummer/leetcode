class Solution:
	# @param {string} haystack
	# @param {string} needle
	# @return {integer}
	# def strStr(self, haystack, needle):
	#     if needle in haystack:
	#         return haystack.index(needle)
	#     else:
	#         return -1
	#     


	def strStr(self, haystack, needle):
		hl = len(haystack)
		nl = len(needle)
		if nl == 0:
			return 0
		i = 0
		while i <= hl-1:
			if haystack[i] == needle[0]:
				if haystack[i:(i+nl)] == needle:
					return i
			i += 1
		return -1

if __name__ == '__main__':
	test =  Solution()
	print test.strStr('acs', 'cs')
