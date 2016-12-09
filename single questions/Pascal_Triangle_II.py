# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
        	return [1]
        if rowIndex == 1:
        	return [1,1]
        tmpIndex = 1
        tmpLst = [1,1]	
        while tmpIndex  < rowIndex:
        	new_tmpLst = []
        	for i in range(len(tmpLst)-1):
        		new_tmpLst.append(tmpLst[i] + tmpLst[i+1])
        	new_tmpLst.append(1)
        	new_tmpLst = [1]+new_tmpLst
        	tmpLst = new_tmpLst
        	tmpIndex += 1
        return tmpLst


if __name__ == '__main__':
	test = Solution()
	print test.getRow(2)
	print test.getRow(3)
	print test.getRow(4)        



