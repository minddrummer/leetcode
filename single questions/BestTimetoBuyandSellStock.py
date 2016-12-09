# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.


#now it is about operating only once: get max gap for the post-prior pairs

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) <= 1:
			return 0
		max_p = 0
		low = prices[0]
		for i in range(1,len(prices)):
			if prices[i] < low: 
				low = prices[i]
			else:
				max_p = max(max_p, prices[i] - low)
		return max_p



if __name__ == '__main__':
	sk = Solution()
	#test1
	print sk.maxProfit([1,2,3])

	#test2
	print sk.maxProfit([3,2,1])

	#test3
	print sk.maxProfit([3,2,1,10])
	print sk.maxProfit([3,1,1,4,7,5,10])