# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

#leetcode is about greedy, but I figure out one dynamic solution??
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

if __name__ == '__main__':
	sk = Solution()
	#test1
	print sk.maxProfit([1,2,3])

	#test2
	print sk.maxProfit([3,2,1])

	#test3
	print sk.maxProfit([3,2,1,10])