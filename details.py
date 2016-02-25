# # Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# # OJ's undirected graph serialization:
# # Nodes are labeled uniquely.
# # We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# # As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# # The graph has a total of three nodes, and therefore contains three parts as separated by #.
# # First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# # Second node is labeled as 1. Connect node 1 to node 2.
# # Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# # Visually, the graph looks like the following:
# #        1
# #       / \
# #      /   \
# #     0 --- 2
# #          / \
# #          \_/
# # Subscribe to see which companies asked this question

# # Definition for a undirected graph node
# # class UndirectedGraphNode(object):
# #     def __init__(self, x):
# #         self.label = x
# #         self.neighbors = [] #note that the initialized node will have an empty list!!

# # class Solution(object):
# # 	def cloneGraph(self, node):
# # 		"""
# # 		:type node: UndirectedGraphNode
# # 		:rtype: UndirectedGraphNode
# # 		"""
# # 		#use either dfs or bfs
# # 		#bfs following
# # 		# if node is None: return None
# # 		# dct={}
# # 		# queue = [node]
# # 		# head=node
# # 		# #first copy node
# # 		# while queue:
# # 		#     cur = queue.pop(0)
# # 		#     if cur not in dct:
# # 		#         for neighbor in cur.neighbors:
# # 		#             if neighbor not in dct: queue.append(neighbor)
# # 		#         node_new = UndirectedGraphNode(cur.label)
# # 		#         node_new.neighbors = cur.neighbors
# # 		#         dct[cur] = node_new
# # 		# #then copy the neigbors        
# # 		# for key in dct:
# # 		#     dupnode = dct[key]
# # 		#     new_neighbor_lst=[]
# # 		#     for neighbor in dupnode.neighbors:
# # 		#         new_neighbor_lst.append(dct[neighbor])
# # 		#     dupnode.neighbors = new_neighbor_lst
# # 		# return dct[head]

# # 		#bfs one time, use [] list instead of copy from original node
# # 		if node is None: return None
# # 		copy = UndirectedGraphNode(node.label) 
# # 		dct={}
# # 		dct[node] = copy
# # 		queue = [node]
# # 		head=node

# # 		while queue:
# # 			cur = queue.pop(0)
# # 			for neighbor in cur.neighbors:
# # 				if neighbor not in dct: 
# # 					copy = UndirectedGraphNode(neighbor.label) 
# # 					dct[neighbor] = copy
# # 					dct[cur].neighbors.append(copy)
# # 					queue.append(neighbor)
# # 				else:
# # 					dct[cur].neighbors.append(dct[neighbor])
# # 		return dct[head]

# ####################details####################

# 7. Reverse Integer My Submissions Question
# Total Accepted: 124242 Total Submissions: 527052 Difficulty: Easy
# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# click to show spoilers.

# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {integer} x
# 	# @return {integer}
# 	def reverse(self, x):
# 		if x < 0:
# 			sign = -1
# 		else:
# 			sign = 1
# 		x = str(abs(x))
# 		res = int(x[::-1])
# 		res = res*sign
# 		#print type(res)
# 		#print(res > 2**32-1)
# 		if (res > 2**31-1) or (res < -2**31):
# 			res = 0
# 		return res

# 9. Palindrome Number My Submissions Question
# Total Accepted: 107838 Total Submissions: 349492 Difficulty: Easy
# Determine whether an integer is a palindrome. Do this without extra space.
# click to show spoilers.

# Subscribe to see which companies asked this question
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    	#need extra space
        # return str(x) == str(x)[::-1]
        #no extra space: manipulate the numbers to get the results
        if x<0: return False
        d=1
        while x/d>=10:
        	d *= 10 #find the largest d first
        while x > 0: #loop in x and d, until x is smaller than 10
        #when x is <10, d will be 1, so it magically work 
        	first = x/d
        	resid = x%10
        	if first != resid: return False
        	x=x%d
        	x=x/10
        	d=d/100
        return True
if __name__ == '__main__':
	sk  =Solution()
	print sk.isPalindrome(4224)      
	print sk.isPalindrome(422)      

# 57. Insert Interval My Submissions Question
# Total Accepted: 52971 Total Submissions: 227560 Difficulty: Hard
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Subscribe to see which companies asked this question
# # Definition for an interval.
# # class Interval(object):
# #     def __init__(self, s=0, e=0):
# #         self.start = s
# #         self.end = e

# class Solution(object):
#     def insert(self, intervals, newInterval):
#         """
#         :type intervals: List[Interval]
#         :type newInterval: Interval
#         :rtype: List[Interval]
#         """
# 56. Merge Intervals My Submissions Question
# Total Accepted: 59780 Total Submissions: 242942 Difficulty: Hard
# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Subscribe to see which companies asked this question
# # Definition for an interval.
# # class Interval(object):
# #     def __init__(self, s=0, e=0):
# #         self.start = s
# #         self.end = e

# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """

# 76. Minimum Window Substring My Submissions Question
# Total Accepted: 54001 Total Submissions: 261262 Difficulty: Hard
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# Subscribe to see which companies asked this question
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """

# 43. Multiply Strings My Submissions Question
# Total Accepted: 54769 Total Submissions: 239866 Difficulty: Medium
# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note: The numbers can be arbitrarily large and are non-negative.

# Subscribe to see which companies asked this question
# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """

# 30. Substring with Concatenation of All Words My Submissions Question
# Total Accepted: 49974 Total Submissions: 244017 Difficulty: Hard
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter).

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# class Solution:
# 	# @param {string} s
# 	# @param {string[]} words
# 	# @return {integer[]}
# 	def findSubstring(self, s, words):
# 		#words = sorted(words)
# 		words_dict = dict(((x, words.count(x)) for x in set(words)))
# 		n = len(words)
# 		m = len(words[0])
# 		string_len = m*n
# 		match_index = []
		
# 		i = 0
# 		while string_len+i <= len(s):
# 			dict2 ={}
# 			item = s[i:(string_len+i)]
			
# 			count = 0
# 			for j in range(0,len(item),m):
# 				ele = item[j:(j+m)]
# 				if ele not in words_dict:
# 					break
# 				else:
# 					dict2[ele]=dict2.get(ele,0)+1  
# 					if dict2[ele] > words_dict[ele]:
# 						break
# 				count +=1
# 			if count == n:
# 				match_index.append(i)
# 			i+=1		
			
# 		return match_index

# 118. Pascal's Triangle My Submissions Question
# Total Accepted: 74889 Total Submissions: 230039 Difficulty: Easy
# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# Subscribe to see which companies asked this question
# class Solution:
#     # @param {integer} numRows
#     # @return {integer[][]}
#     def generate(self, numRows):
#         if numRows == 0:
#     		return []
#     	if numRows == 1:
#     		return [[1]]
#     	if numRows == 2:
#     		return [[1],[1,1]]
#     	res = [[1],[1,1]]
#     	tmpRowIdx = 2
#     	tmpRow = res[1]

#     	while tmpRowIdx < numRows:
#     		new_tmpRow = []
#     		for i in range(len(tmpRow)-1):
#     			new_tmpRow.append(tmpRow[i]+tmpRow[i+1])
#     		new_tmpRow.append(1)
#     		new_tmpRow = [1] + new_tmpRow
#     		res.append(new_tmpRow)
#     		tmpRowIdx += 1
#     		tmpRow =  new_tmpRow
#     	return res


# 119. Pascal's Triangle II My Submissions Question
# Total Accepted: 67495 Total Submissions: 214140 Difficulty: Easy
# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {integer} rowIndex
#     # @return {integer[]}
#     def getRow(self, rowIndex):
#         if rowIndex == 0:
#         	return [1]
#         if rowIndex == 1:
#         	return [1,1]
#         tmpIndex = 1
#         tmpLst = [1,1]	
#         while tmpIndex  < rowIndex:
#         	new_tmpLst = []
#         	for i in range(len(tmpLst)-1):
#         		new_tmpLst.append(tmpLst[i] + tmpLst[i+1])
#         	new_tmpLst.append(1)
#         	new_tmpLst = [1]+new_tmpLst
#         	tmpLst = new_tmpLst
#         	tmpIndex += 1
#         return tmpLst

# 54. Spiral Matrix My Submissions Question
# Total Accepted: 52533 Total Submissions: 238442 Difficulty: Medium
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# Subscribe to see which companies asked this question
# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """


# 59. Spiral Matrix II My Submissions Question
# Total Accepted: 47781 Total Submissions: 139985 Difficulty: Medium
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# Subscribe to see which companies asked this question

# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """

# 6. ZigZag Conversion My Submissions Question
# Total Accepted: 76862 Total Submissions: 329817 Difficulty: Easy
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# Subscribe to see which companies asked this question

# Show Tags
# class Solution:
#     # @return a string
#     def convert(self, s, nRows):
#         if  nRows <= 1:
#             return s
#         n = nRows
#         bn = n - 2 + n
#         fn = len(s)
#         res = ''
#         for i in range(n):
#             if i == 0 or i == n-1:
#                 loop = 0
#                 while bn*loop + i <= fn-1:
#                     #print s[bn*loop + i]
#                     res = res + s[bn*loop + i]
#                     loop += 1
#             else:
#                 loop = 0
#                 while (bn*loop + i <= fn-1):
#                     #print s[bn*loop + i]
#                     res = res + s[bn*loop+i]

#                     if (bn*loop+i+(n-1-i)*2) <= fn-1:
#                         #print (bn*loop+i+(n-1-i)*2)
#                         #print s[bn*loop+i+(n-i)*2]
#                         res = res + s[bn*loop+i+(n-1-i)*2]
#                     loop += 1
#         return res


# 29. Divide Two Integers My Submissions Question
# Total Accepted: 60335 Total Submissions: 390167 Difficulty: Medium
# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

# Subscribe to see which companies asked this question
# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
        


# 68. Text Justification My Submissions Question
# Total Accepted: 30326 Total Submissions: 192418 Difficulty: Hard
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.

# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.

# class Solution(object):
#     def fullJustify(self, words, maxWidth):
#         """
#         :type words: List[str]
#         :type maxWidth: int
#         :rtype: List[str]
#         """
        

# 149. Max Points on a Line My Submissions Question
# Total Accepted: 53334 Total Submissions: 380608 Difficulty: Hard
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Subscribe to see which companies asked this question

# Show Tags


# # Definition for a point.
# # class Point(object):
# #     def __init__(self, a=0, b=0):
# #         self.x = a
# #         self.y = b

# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """









