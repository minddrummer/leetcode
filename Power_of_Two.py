
# Given an integer, write a function to determine if it is a power of two.





class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
    	#given the order of the if statement, this will work: for n == 1
    	if n == 1:
    		return True
    	elif n%2 != 0 or n == 0:
    		return False
    	else:
    		n = n/2
    		return self.isPowerOfTwo(n)
        


if __name__ == '__main__':
	test =Solution()
	print test.isPowerOfTwo(4)        
	print test.isPowerOfTwo(5)        