# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 





class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
    	num_letter_dict = dict(zip(range(1,27), [chr(one) for one in range(97,123)]))
    	res_lst = []

    	while n/26 > 1:
    		print n%26
    		res_lst.append(n%26)
    		n = n - n%26
    	print n
    	if n != 26:		
    		res_lst.append(n%26)
    	else:
    		res_lst.append(26)

    	res_lst = res_lst[::-1]
    	print res_lst
    	res = ''
    	for i in res_lst:
    		res = res + num_letter_dict[i].upper()
    	return res
        

if __name__ == '__main__':
	test = Solution()
	print test.convertToTitle(1)
	print test.convertToTitle(28)        