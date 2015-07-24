# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".



class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if len(a) >= len(b):
        	b = (len(a)-len(b))*'0' + b
        else:
        	a = (len(b)-len(a))*'0' + a
        res = ''
        up = 0
        for i in range(1,len(a)+1):
        	if int(a[-i]) + int(b[-i]) + up >= 2:
        		res = res + str((int(a[-i]) + int(b[-i]) + up)%2)
        		up = 1
        	else:
        		res = res + str(int(a[-i]) + int(b[-i]) + up)
        		#has to reset up here
        		up = 0
        if up == 1:
        	res = res + '1'	
        #use the python code to check the answer
    	#the shortest and pythonest way to finish the code
        #x = bin(int(a,2)+int(b,2))[2:]	
        return res[::-1]#, x


if __name__ == '__main__':
	test = Solution()
	print test.addBinary('11','11')        