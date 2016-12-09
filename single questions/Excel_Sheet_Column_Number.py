# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
    	s = s.lower()
    	letter_dict = dict(zip([chr(one) for one in range(97,123)], range(1,27)))
        #print letter_dict
        s_len = len(s)
        total = 0
        for i in range(s_len):
        	#print letter_dict[s[i]]
        	#print 26**(s_len-i-1)
        	total += letter_dict[s[i]]*26**(s_len-i-1)
        return total

if __name__ == '__main__':
	test = Solution()
	print test.titleToNumber('aa')