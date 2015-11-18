# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# # How many possible unique paths are there?
# Above is a 3 x 7 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.
# Subscribe to see which companies asked this question

#dynamic prorgamming, use grid index as the key for the dict, and find the sum of each


class Solution(object):
	# def __init__(self):
	# 	self.DCT = {}
	DCT = {}
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""

		if m<1 or n<1: return 0
		if m==1 and n == 1: 
			self.DCT[(m,n)] = 1
			return 1
		if (m,n) in self.DCT:
			return self.DCT[(m,n)]
		else:
			self.DCT[(m,n)] = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
			return self.DCT[(m,n)]




if __name__ == '__main__':
	sk = Solution()
	hl = Solution()
	print sk.uniquePaths(2,2)
	#print sk.uniquePaths(3,2)
	print hl.uniquePaths(7,3)
	#print sk.uniquePaths(7,7)
