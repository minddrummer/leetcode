# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37

	



class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
    	v1 = [int(i) for i in version1.split('.')]
    	v2 = [int(i) for i in version2.split('.')]
    	if len(v1) > len(v2):
    		apdx = [0]*(len(v1) -len(v2))
    		v2 = v2 + apdx
    	elif len(v1) < len(v2):
    		apdx = [0]*(len(v2) -len(v1))
    		v1 = v1 + apdx
    	else:
    		pass
    	res = 0
    	for i in range(len(v1)):
    		s1 = v1[i]
    		s2 = v2[i]
    		if s1>s2:
    			res = 1
    			break
    		elif s1<s2:
    			res = -1
    			break
    		else:
    			continue
    	return res


if __name__ == '__main__':
	test = Solution()
	print test.compareVersion('1.2','1.2')
	print test.compareVersion('1.2','1.3')

