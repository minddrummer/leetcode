# Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.


class Solution:
	# @param {string[]} strs
	# @return {string[]}
	def anagrams(self, strs):
		strs_dict = {}
		for item in strs:
			letter_com = ''.join(sorted(item))
			strs_dict[letter_com] = strs_dict.get(letter_com,[])
			strs_dict[letter_com].append(item)
		res = []
		for key in strs_dict:
			if len(strs_dict[key]) >=2:
				res = res + strs_dict[key]
		return res



if __name__ == '__main__':
	test =Solution()
	case0 = ['ab','ba','cd','de','ed']
	case1 =['abc']
	case2 = ['']
	#print test.anagrams(case0)
	print test.anagrams(case2)
	#test.(case1)		        



