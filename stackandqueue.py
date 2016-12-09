# 20. Valid Parentheses My Submissions Question
# Total Accepted: 88789 Total Submissions: 314280 Difficulty: Easy
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# Subscribe to see which companies asked this question
# class Solution:
# 	# @param {string} s
# 	# @return {boolean}
# 	def isValid(self, s):
# 		#use stack to finish this problem
# 		#TO(n) SO(n)
# 		forward = ['(','{','[']
# 		backward = [')','}',']']
# 		pair_dict = {'(':')','{':'}','[':']'}
# 		# s = list(s)
# 		target_lst = []
# 		for l in s:
# 			if l in forward:
# 				target_lst.append(l)
# 			elif l in backward:
# 				if len(target_lst) == 0:
# 					return False
# 				elif pair_dict[target_lst[-1]] == l:
# 					target_lst.pop(-1)
# 				else:
# 					return False
# 		if len(target_lst) == 0:
# 			return True
# 		else:
# 			return False
		
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         n = len(s)
#         if n<=1: return False 
#         backP = [')','}',']']
#         forwP = ['(','{','[']
#         PDict = {')':'(','}':'{',']':'['}
#         stack = []
#         for i in range(n):
#             if s[i] in forwP:
#                 stack.append(s[i])
#             else:
#                 if len(stack)==0: return False
#                 else:
#                     nearP = stack.pop(-1)
#                     if PDict[s[i]] == nearP:
#                         continue
#                     else:
#                         return False
#         if len(stack)==0: return True
#         else: return False

# 32. Longest Valid Parentheses My Submissions Question
# Total Accepted: 54652 Total Submissions: 249120 Difficulty: Hard
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# Subscribe to see which companies asked this question

#the problem is that you have to segment the string, and find the part first valid, and second longest
# class Solution(object):
# 	def longestValidParentheses(self, s):
# 		"""
# 		:type s: str
# 		:rtype: int
# 		"""
# 		#there are three ways to finish this problem
# 		#1 stack; 2 dp 3 two scans
# 		#1stack:#tracking the index of the ( and the last of )
# 		# last = -1
# 		# stack =[]
# 		# res = 0

# 		# for i in range(len(s)):
# 		# 	#if "(",push the index
# 		# 	if s[i]=='(':
# 		# 		stack.append(i)
# 		# 	else:
# 		# 		#if stack is 0, then set the last to the current index i
# 		# 		if len(stack)==0:
# 		# 			last=i
# 		# 		#if stack not 0	
# 		# 		else:
# 		# 			#stack first pop the last index
# 		# 			stack.pop(-1)
# 		# 			#if then stack is 0, that means all ( have been cleared out,
# 		# 			#so the length would be i -last
# 		# 			if len(stack)==0:
# 		# 				res=max(res, i-last)
# 		# 			#if stack not 0, that means that there are some ( is preventing
# 		# 			#so use the current index i - the last index of the stack	
# 		# 			else:
# 		# 				res=max(res, i-stack[-1])
# 		# return res

		#scan twice, 1 scan ) as ending max; and second scan ( as ending max
		# last=-1
		# depth=0
		# res=0
		# for i in range(len(s)):
		# 	if s[i]=='(':
		# 		depth +=2
		# 	else:
		# 		depth -=2
		# 		if depth<0:
		# 			depth=0
		# 			last=i
		# 		elif depth==0:
		# 			res=max(res, i-last)
		# sr= s[::-1]
		# depth=0
		# last = -1
		# for i in range(len(s)):
		# 	if sr[i]==')':
		# 		depth +=2
		# 	else:
		# 		depth -=2
		# 		if depth<0:
		# 			depth =0
		# 			last = i
		# 		elif depth==0:
		# 			res=max(res, i-last)
		# return res

		#dynamic programming
# class Solution(object):
# 	def longestValidParentheses(self, s):
# 		"""
# 		:type s: str
# 		:rtype: int
# 		"""
		
# 		stack = []
# 		lastIdx = -1
# 		res = 0
		
# 		for i in range(len(s)):
# 			if s[i] == '(':
# 				stack.append(i)
# 			else: 
# 				# for ")"
# 				if len(stack) == 0:
# 					lastIdx = i
# 				else:
# 					#nearIdx not using 
# 					nearIdx = stack.pop(-1)
# 					if len(stack)==0:
# 						res = max(res, i-lastIdx)
# 					else:
# 						res = max(res, i-stack[-1])
# 		return res

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.longestValidParentheses(")()((()())(()()")
# 	print sk.longestValidParentheses("()()")
# 	print sk.longestValidParentheses("())")
# 	print sk.longestValidParentheses("))))())()()(()")

# 84. Largest Rectangle in Histogram My Submissions Question
# Total Accepted: 52844 Total Submissions: 224499 Difficulty: Hard
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# Subscribe to see which companies asked this question

# class Solution(object):
# 	def largestRectangleArea(self, heights):
# 		"""
# 		:type heights: List[int]
# 		:rtype: int
# 		"""
# 		#add 0 to the end artificially
# 		#TO(n), SO(n), very smart method!
# 		heights.append(0)
# 		stack = []
# 		hestack = []
# 		res=0
# 		for i in range(len(heights)):
# 			if len(stack)==0 or hestack[-1]<=heights[i]:
# 				stack.append(i)
# 				hestack.append(heights[i])
# 			elif hestack[-1]>heights[i]:
# 				while len(hestack)>0 and hestack[-1]>heights[i]:
# 					tmphe = hestack.pop(-1)
# 					tmpindex = stack.pop(-1)
# 					res= max(res, tmphe*(i-tmpindex))
# 				# if heights[i]>hestack[]
# 				hestack.append(heights[i])
# 				stack.append(tmpindex)
# 		return res
# if __name__ == '__main__':
# 	sk=Solution()
# 	print sk.largestRectangleArea([2,1,5,6,2,3])
# 	print sk.largestRectangleArea([2,1,5,6,2,3,2,2])




# 150. Evaluate Reverse Polish Notation My Submissions Question
# Total Accepted: 58084 Total Submissions: 255877 Difficulty: Medium
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# Subscribe to see which companies asked this question


# class Solution(object):
# 	def evalRPN(self, tokens):
# 		"""
# 		:type tokens: List[str]
# 		:rtype: int
# 		"""
# 		#TO(n), SO(logn)--best case is SO(1), worst case is SO(n)
# 		operator = ['+','-','*','/']
# 		stack =[]
# 		for i in tokens:
# 			if i not in operator:
# 				stack.append(int(i))
# 			else:
# 				num1=stack.pop(-1)
# 				num2=stack.pop(-1)
# 				if i == "+":
# 					tmp=num1+num2
# 				elif i == '-':
# 					tmp=num2-num1
# 				elif i == '*':
# 					tmp=num1*num2
# 				else:
# 					if (num2>0 and num1<0) or (num2<0 and num1>0):	
# 						#python for negative division is taking value to the floor, so when it is 
# 						#wrong when you get true float division values
# 						#reverse to positive, and then take the negate
# 						tmp=-((-num2)/num1)
# 					else:
# 						tmp=num2/num1
# 				# print tmp
# 				stack.append(tmp)
# 		return stack[-1]

# if __name__ == '__main__':
# 	sk=Solution()
# 	# print sk.evalRPN(["2", "1", "+", "3", "*"])
# 	print sk.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		operator = set(['+','-','*','/'])
		stack = []
		if len(tokens)==0: return None
		
		for i in range(len(tokens)):
			if tokens[i] in operator:
				rightNum = stack.pop(-1)
				leftNum = stack.pop(-1)
				if tokens[i] == '+':
					tmp = leftNum + rightNum
				elif tokens[i] == '-':
					tmp = leftNum - rightNum
				elif tokens[i] == '*':
					tmp = leftNum * rightNum
				else:      
					if (leftNum>0 and rightNum<0) or (leftNum<0 and rightNum>0):
						tmp = -(leftNum/(-rightNum))
					else:
						tmp = leftNum/rightNum
				stack.append(tmp)
			else:
				stack.append(int(tokens[i]))
		return stack[-1]

##prime number factorization
# def primeFactor(num):
# 	if num <=2: return [num]
# 	res = []
# 	for i in range(2, (num/2)+1):
# 		if num%i == 0:
# 			res.append(i)
# 			res = res + primeFactor(num/i)
# 			break
# 		else:
# 			continue
# 	if len(res) ==0: res = [num]
# 	return res

# print primeFactor(2)
# print primeFactor(100)
# print primeFactor(100000)
# print primeFactor(13)



