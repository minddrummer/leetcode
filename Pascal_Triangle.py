# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
    	if numRows == 0:
    		return []
    	if numRows == 1:
    		return [[1]]
    	if numRows == 2:
    		return [[1],[1,1]]
    	res = [[1],[1,1]]
    	tmpRowIdx = 2
    	tmpRow = res[1]

    	while tmpRowIdx < numRows:
    		new_tmpRow = []
    		for i in range(len(tmpRow)-1):
    			new_tmpRow.append(tmpRow[i]+tmpRow[i+1])
    		new_tmpRow.append(1)
    		new_tmpRow = [1] + new_tmpRow
    		res.append(new_tmpRow)
    		tmpRowIdx += 1
    		tmpRow =  new_tmpRow
    	return res


if __name__ == '__main__':
	test = Solution()
	test.generate(5)    	