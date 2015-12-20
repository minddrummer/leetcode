# Given two integers n and k, return all possible combinations of 
#k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#choose k out of n, return all the outcomes

#essentially dfs!! 
#you search through i=n's all possible combinations, then move to i=n-1
#because you want to describe it as unique path in dfs, but we donot mark searched for each number
#so we have to create a loop that avoid searched numbers, that is the reason to make i decreases each time
#the computational complexity here is: n^min(k,n-k)--it is proportional to the total # of possible combs
#because of when n<k, you donot have to worry about when k is close to n

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
    	if n < k or k == 0: return []
    	if k == 1: return [[i] for i in xrange(1,n+1)]    	
    	if n == k: return [[for i in xrange(1,n+1)]]

    	res = []
    	for i in xrange(n,0,-1):
    		#dfs here, finish i's all comb, then move to i-1's all comb
    		for item in self.combine(i-1,k-1):
    			res.append(item+[i])
    	return res




if __name__ == '__main__':
	sk = Solution()
	#test1
	print sk.combine(5,3)        
	#test2
	print sk.combine(3,3)        
	#test3
	print sk.combine(6,3)
	print sk.combine(6,6)        
	