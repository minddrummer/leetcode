# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    # @param {integer} n
    # @return {boolean}
    # def squared_sum(self, n):
    # 	n = str(n)
    # 	squared_sum = 0
    # 	for num in n:
    # 		squared_sum += int(num)*int(num)
    # 	return squared_sum
    # def make_tuple(self,n):
    # 	return tuple(sorted(list(str(n))))

    # def isHappy(self, n):
    # 	squared = self.squared_sum(n)
    # 	if squared == 1:
    # 		return True
    # 	loop_set = {self.make_tuple(n)}

    # 	if self.make_tuple(squared) not in loop_set:
    # 		loop_set.add(self.make_tuple(squared))
    # 	else:
    # 		return False

    # 	while squared != 1:
    # 		n = squared
    # 		squared = self.squared_sum(n)
    # 		if self.make_tuple(squared) not in loop_set:
    # 			loop_set.add(self.make_tuple(squared))
    # 		else:
    # 			return False
    # 			#return squared
    # 	return True	

    ##the below is a faster way:::
    def squared_sum(self, n):
    	n = str(n)
    	return sum([int(num)*int(num) for num in n])

    def isHappy(self, n):
    	squared = self.squared_sum(n)
    	if squared == 1:
    		return True
    	if n == squared:
    		return False
    	loop_set = {n, squared}

    	while squared != 1:
    		n = squared
    		squared = self.squared_sum(n)
    		if squared not in loop_set:
    			loop_set.add(squared)
    		else:
    			return False
    			#return squared
    	return True	


if __name__ == '__main__':
	test = Solution()
	print test.isHappy(19)
	print test.isHappy(1)
	print test.isHappy(1123)



        