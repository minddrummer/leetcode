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
			Solution.DCT[(m,n)] = 1
			return 1
		if (m,n) in Solution.DCT:
			return Solution.DCT[(m,n)]
		else:
			Solution.DCT[(m,n)] = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
			return Solution.DCT[(m,n)]

#here, it is not divergeing because the datatype is mutable, and the instace's a refering to the class's
class Test():
	a = []
	def add(self, b):
		self.a.append(b)
h = Test()
print h.a
print Test.a
h.add(5)
print h.a
print Test.a
#Test.add(77)
#print h.a
#print Test.a
#when it is a list/dct, because of the refernce, instacne and class have the same result, change one will change other's
Test.a = 100
print h.a
print Test.a
#now you change to int, and the instance method will not work


###class and instance's class attributes will differ/diverge here
###when you call self.a within the function, it creates a instance.attributes, because it is integer, it is immutable
class Test():
	a = 1
	def add(self, b):
		self.a += b

hl = Test()
print hl.a, Test.a	
#diverge here
hl.a = 99
print hl.a, Test.a	
#diverge here
Test.a =100
print hl.a, Test.a	
hl.add(1000)
#doesnot matter, still diverage
print hl.a,Test.a



if __name__ == '__main__':
	sk = Solution()
	hl = Solution()
	print sk.uniquePaths(2,2)
	print Solution.DCT
	#print sk.uniquePaths(3,2)
	print hl.uniquePaths(7,3)
	#print sk.uniquePaths(7,7)
	print Solution.DCT