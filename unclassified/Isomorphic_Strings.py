# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.


		# the following method is too time consuming:using more basic algorithm
		# s = list(s)
		# t = list(t)
		# set_s = set(s)
		# set_t = set(t)
		# if len(set_s) != len(set_t):
		# 	return False
		# s_lst = sorted([sum([item == ele for ele in s]) for item in set_s])
		# t_lst = sorted([sum([item == ele for ele in t]) for item in set_t])
		# if s_lst != t_lst:
		# 	return False
		# return True

class Solution:
	# @param {string} s
	# @param {string} t
	# @return {boolean}
	def isIsomorphic(self, s, t):
		s = list(s)
		t = list(t)
		#the right and quick way here is to create dict, and add the new element to the dict
		#if the key is there, check whether there is a match; if not, return False
		#and you have to create 2 dicts, because the relation is two-direction.
		match_dict0 = {}
		match_dict1 = {}
		for i in range(len(s)):
			es = s[i]
			et = t[i]
			if es not in match_dict0:
				if et not in match_dict1:
						match_dict0[es] = et
						match_dict1[et] = es
				else:
					if match_dict1[et] != es:
						return False
			else:
				if match_dict0[es] != et:
					return False
		return True


if __name__ == '__main__':

	test = Solution()
	print test.isIsomorphic('egg', 'add')
	print test.isIsomorphic('paper', 'title')
	print test.isIsomorphic('foo', 'bar')
	print test.isIsomorphic('ab', 'aa')