# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"



class Solution(object):
	def binaryTree_dfs(self, l,r,item, res):
		if l>r:
			return None
		if l == 0 and r == 0:
			res.append(item)
		if l > 0:
			self.binaryTree_dfs(l-1,r,item+'(',res)
		if r > 0:
			self.binaryTree_dfs(l,r-1,item+')',res)

	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n == 0:
			return []
		res = []
		self.binaryTree_dfs(n,n,'',res)
		return res

if __name__ == '__main__':
	sk = Solution()
	print sk.generateParenthesis(3)

