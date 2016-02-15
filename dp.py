# 120. Triangle My Submissions Question
# Total Accepted: 62417 Total Submissions: 212709 Difficulty: Medium
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# class Solution(object):
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
        


# 53. Maximum Subarray My Submissions Question
# Total Accepted: 97791 Total Submissions: 271579 Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

# click to show more practice.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         total = 0
#         cur_max = max(nums)
#         for i in nums:
#         	total += i
#         	if total > cur_max:
#         		cur_max = total
#         	if total < 0:
#         		total = 0
#         return cur_max


# 132. Palindrome Partitioning II My Submissions Question
# Total Accepted: 46174 Total Submissions: 217410 Difficulty: Hard
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# class Solution(object):
#     def minCut(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        


# 85. Maximal Rectangle My Submissions Question
# Total Accepted: 38061 Total Submissions: 165316 Difficulty: Hard
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """

# 123. Best Time to Buy and Sell Stock III My Submissions Question
# Total Accepted: 51305 Total Submissions: 200248 Difficulty: Hard
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
        

# 97. Interleaving String My Submissions Question
# Total Accepted: 45241 Total Submissions: 205565 Difficulty: Hard
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Subscribe to see which companies asked this question

# Show Tags

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """

# 87. Scramble String My Submissions Question
# Total Accepted: 42305 Total Submissions: 162870 Difficulty: Hard
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
        

# 64. Minimum Path Sum My Submissions Question
# Total Accepted: 62940 Total Submissions: 184697 Difficulty: Medium
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
        

# 72. Edit Distance My Submissions Question
# Total Accepted: 52314 Total Submissions: 187031 Difficulty: Hard
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character

# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
        
# 91. Decode Ways My Submissions Question
# Total Accepted: 61299 Total Submissions: 357609 Difficulty: Medium
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        

# 115. Distinct Subsequences My Submissions Question
# Total Accepted: 46914 Total Submissions: 166243 Difficulty: Hard
# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def numDistinct(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
        

# 139. Word Break My Submissions Question
# Total Accepted: 77794 Total Submissions: 317862 Difficulty: Medium
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

# Subscribe to see which companies asked this question

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: bool
#         """
        

# 140. Word Break II My Submissions Question
# Total Accepted: 50737 Total Submissions: 264698 Difficulty: Hard
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

# Subscribe to see which companies asked this question

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: List[str]
#         """
#                                                                                                         