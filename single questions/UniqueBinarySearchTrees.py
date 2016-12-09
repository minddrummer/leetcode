# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

#classic dynamic programming problem

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
		#here is tricky: because self.count is another function indepedent of numTrees, so the 'dct' will be local variable
        # to the count function, when dct is not local, python will search another higher level scope, which will be the class lelve, not the numTree functino
        #if you not define dct as gloabl, you have to put all things in one functino in order to make it work, dct accessable to the numTree function
        global dct
        dct = {}
        dct[0] = 1
        dct[1] = 1
        if n == 0: 
        	return 1
        if n == 1: 
        	return 1
        count = self.count(n)	
        return count

    def count(self,n):
        if n in dct:
        	return dct[n]
        count = 0
        for i in range(n):
        	count += self.count(i)*self.count(n-1-i)
        dct[n] = count
        return count


if __name__ == '__main__':
	sk = Solution()
	print sk.numTrees(1)
	print sk.numTrees(3)
	print sk.numTrees(4)
	print sk.numTrees(5)


