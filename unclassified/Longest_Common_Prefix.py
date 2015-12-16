class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
    		return ''
        min_len = min([len(s) for s in strs])
        comm_str = ''
        for i in range(min_len):
        	lst = [s[i] for s in strs]
        	ele = lst[0]
        	all_true = True
        	for l in lst:
        		if l==ele:
        			continue
        		else:
        			all_true = False
        			break
        	if all_true:
        		comm_str = comm_str+ele
        	else:
        		break
        return comm_str


if __name__ == '__main__':
	strs = ['abc', 'abcde', 'abd', 'absdefsfef']
	test = Solution()
	print test.longestCommonPrefix(strs)