# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# this is a dynamic programming program


class Solution:
    # @param {integer} n
    # @return {integer}
    global mm
    mm = {}
    mm[0] = 1
    mm[1] = 1
    def climbStairs(self, n):
    	if n == 0:
    		return mm[0]
    	if n == 1:
    		return mm[1]
    	if n-1 not in mm:
    		res1 = self.climbStairs(n-1)
    		mm[n-1] = res1
    	if n-2 not in mm:
    		res2 = self.climbStairs(n-2)
    		mm[n-2] = res2

    	return mm[n-1] + mm[n-2]
    	# 2 :11 2 
    	# 3: 111 12 21 
    	# 4: 1111 121 211 112 22 
    	# 5: 11111 221 
    	# 10: 22111111





if __name__ == '__main__':
	test = Solution()
	print test.climbStairs(0) #0
	print test.climbStairs(1) #1
	print test.climbStairs(2) #2
	print test.climbStairs(3) #3
	print test.climbStairs(4) #5

