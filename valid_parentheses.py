#'(', ')', '{', '}', '[' and ']'

class Solution:
	# @param {string} s
	# @return {boolean}
	def isValid(self, s):
		forward = ['(','{','[']
		backward = [')','}',']']
		pair_dict = {'(':')','{':'}','[':']'}
		s = list(s)
		target_lst = []
		for l in s:
			if l in forward:
				target_lst.append(pair_dict[l])
			elif l in backward:
				if len(target_lst) == 0:
					return False
				elif target_lst[-1] == l:
					target_lst.pop(-1)
				else:
					return False
		if len(target_lst) == 0:
			return True
		else:
			return False



if __name__  == '__main__':
	test = Solution()
	print test.isValid('(sfsd)[sdfsd]')   
	print test.isValid('{(sfsd)[sdfsd]}')   
	print test.isValid('{(sfs[d)[sd]fsd]}')   