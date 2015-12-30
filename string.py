# 125. Valid Palindrome My Submissions Question
# Total Accepted: 81196 Total Submissions: 355032 Difficulty: Easy
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.

# Subscribe to see which companies asked this question


# class Solution:
#     # @param {string} s
#     # @return {boolean}
#     def isPalindrome(self, s):
#     	if len(s) == 0:
#     		return True
#     	s = s.lower()
#     	s = ''.join(x for x in s if x.isalnum())
#     	return s == s[::-1]



# 28. Implement strStr() My Submissions Question
# Total Accepted: 84227 Total Submissions: 355976 Difficulty: Easy
# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# Discuss



# class Solution:
#     # @param {string} haystack
#     # @param {string} needle
#     # @return {integer}
#     def strStr(self, haystack, needle):
# 		hl = len(haystack)
# 		nl = len(needle)
# 		if nl == 0:
# 		    return 0
# 		i = 0
# 		while i <= hl-1:
# 			if haystack[i] == needle[0]:
# 				if haystack[i:(i+nl)] == needle:
# 					return i
# 			i += 1
# 			# 	else:
# 			# 		i = i + nl
# 			# else: 
# 			# 	i += 1    	
# 		return -1
        


# 8. String to Integer (atoi) My Submissions Question
# Total Accepted: 80256 Total Submissions: 612069 Difficulty: Easy
# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

# spoilers alert... click to show requirements for atoi.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems


# class Solution:
# 	# @param {string} str
# 	# @return {integer}
# 	def myAtoi(self, str):
# 		if len(str) == 0:
# 			return 0
# 		s = str
# 		s = s.strip()
# 		num_lst = ['0','1','2','3','4','5','6','7','8','9','-']
# 		res = []
# 		for letter in s:
# 			if letter in num_lst:
# 				res.append(letter)
# 		if len(res) == 0:
# 			return 0
# 		res1 = []
# 		#print res
		
# 		res1.append(res[0])
# 		for i in res[1:]:
# 		    if i != '-':
# 		        res1.append(i)
# 		#print res1
# 		if len(res1) == 1 and '-' in res1:
# 		    return 0
# 		#print res1
# 		res1 = int(''.join(res1))
# 		return res1


# 67. Add Binary My Submissions Question
# Total Accepted: 67706 Total Submissions: 261672 Difficulty: Easy
# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {string} a
#     # @param {string} b
#     # @return {string}
#     def addBinary(self, a, b):
#     	#the shortest and pythonest way to finish the code
#         #return 
        
#         if len(a) >= len(b):
#         	b = (len(a)-len(b))*'0' + b
#         else:
#         	a = (len(b)-len(a))*'0' + a
#         res = ''
#         up = 0
#         for i in range(1,len(a)+1):
#         	if int(a[-i]) + int(b[-i]) + up >= 2:
#         		res = res + str((int(a[-i]) + int(b[-i]) + up)%2)
#         		up = 1
#         	else:
#         		res = res + str(int(a[-i]) + int(b[-i]) + up)
#         		#has to reset up here
#         		up = 0
#         if up == 1:
#         	res = res + '1'	
#         #x = bin(int(a,2)+int(b,2))[2:]	
#         return res[::-1]#, x


# 5. Longest Palindromic Substring My Submissions Question
# Total Accepted: 85048 Total Submissions: 390023 Difficulty: Medium
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """


# 10. Regular Expression Matching My Submissions Question
# Total Accepted: 65937 Total Submissions: 309819 Difficulty: Hard
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true


# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
        


# 44. Wildcard Matching My Submissions Question
# Total Accepted: 46918 Total Submissions: 284267 Difficulty: Hard
# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
        

# 14. Longest Common Prefix My Submissions Question
# Total Accepted: 79040 Total Submissions: 295620 Difficulty: Easy
# Write a function to find the longest common prefix string amongst an array of strings.

# Subscribe to see which companies asked this question

# Show Tags

# class Solution:
#     # @param {string[]} strs
#     # @return {string}
#     def longestCommonPrefix(self, strs):
#         if len(strs) == 0:
#     		return ''
#         min_len = min([len(s) for s in strs])
#         comm_str = ''
#         for i in range(min_len):
#         	lst = [s[i] for s in strs]
#         	ele = lst[0]
#         	all_true = True
#         	for l in lst:
#         		if l==ele:
#         			continue
#         		else:
#         			all_true = False
#         			break
#         	if all_true:
#         		comm_str = comm_str+ele
#         	else:
#         		break
#         return comm_str


# 65. Valid Number My Submissions Question
# Total Accepted: 38762 Total Submissions: 328128 Difficulty: Hard
# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

# class Solution(object):
#     def isNumber(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
        

# 12. Integer to Roman My Submissions Question
# Total Accepted: 51285 Total Submissions: 141110 Difficulty: Medium
# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
        

# 13. Roman to Integer My Submissions Question
# Total Accepted: 65811 Total Submissions: 178393 Difficulty: Easy
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# Subscribe to see which companies asked this question

# public class Solution {
#     public int romanToInt(String s) {  
  
#     if(s==null || s.length()==0)  
#         return 0;  
#     int res = 0;  
#     for(int i=0;i<s.length();i++)  
#     {  
#         switch(s.charAt(i))  
#         {  
#             case 'I':  
#                 if(i<s.length()-1 && (s.charAt(i+1)=='V'||s.charAt(i+1)=='X'))  
#                 {  
#                     res -= 1;  
#                 }  
#                 else  
#                 {  
#                     res += 1;  
#                 }  
#                 break;  
#             case 'V':  
#                 res += 5;  
#                 break;  
#             case 'X':  
#                 if(i<s.length()-1 && (s.charAt(i+1)=='L'||s.charAt(i+1)=='C'))  
#                 {  
#                     res -= 10;  
#                 }  
#                 else  
#                 {  
#                     res += 10;  
#                 }  
#                 break;  
#             case 'L':  
#                 res += 50;  
#                 break;  
#             case 'C':  
#                 if(i<s.length()-1 && (s.charAt(i+1)=='D'||s.charAt(i+1)=='M'))  
#                 {  
#                     res -= 100;  
#                 }  
#                 else  
#                 {  
#                     res += 100;  
#                 }  
#                 break;  
#             case 'D':  
#                 res += 500;  
#                 break;  
#             case 'M':  
#                 res += 1000;  
#                 break;  
#             default:  
#                 return 0;  
#         }  
#     }  
#     return res;  
# } 
# }


# 38. Count and Say My Submissions Question
# Total Accepted: 65463 Total Submissions: 241667 Difficulty: Easy
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

# Subscribe to see which companies asked this question

# class Solution:
#     # @param {integer} n
#     # @return {string}
#     def countAndSay(self, n):
# 		if n == 1: return '1'
# 		res = '1'
# 		for i in range(2,n+1):
# 			short = res[0]
# 			tmp = []
# 			pre = res[0]
# 			for num in res[1:]:
# 				if num == pre:
# 					short = short + num
# 				else:
# 					pre = num
# 					tmp.append(short)	
# 					short = pre	
# 			tmp.append(short)
# 			res = ''
# 			for item in tmp:
# 				times = len(item)
# 				res = res + str(times)+str(item[0])
# 		return res
        

# 242. Valid Anagram My Submissions Question
# Total Accepted: 47204 Total Submissions: 119459 Difficulty: Easy
# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Subscribe to see which companies asked this question

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        

# 49. Group Anagrams My Submissions Question
# Total Accepted: 59431 Total Submissions: 231519 Difficulty: Medium
# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# For the return value, each inner list's elements must follow the lexicographic order.
# All inputs will be in lower-case.
# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {string[]} strs
# 	# @return {string[]}
# 	def anagrams(self, strs):
# 		strs_dict = {}
# 		for item in strs:
# 			letter_com = ''.join(sorted(item))
# 			strs_dict[letter_com] = strs_dict.get(letter_com,[])
# 			strs_dict[letter_com].append(item)
# 		res = []
# 		for key in strs_dict:
# 			if len(strs_dict[key]) >=2:
# 				res = res + strs_dict[key]
# 		return res

# 71. Simplify Path My Submissions Question
# Total Accepted: 42843 Total Submissions: 204499 Difficulty: Medium
# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def simplifyPath(self, path):
#         """
#         :type path: str
#         :rtype: str
#         """
        

# 58. Length of Last Word My Submissions Question
# Total Accepted: 76539 Total Submissions: 270996 Difficulty: Easy
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.

# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {string} s
# 	# @return {integer}
# 	def lengthOfLastWord(self, s):
# 		##python way to do it
# 		# s = s.split()
# 		# #print s
# 		# if len(s) >= 1:
# 		# 	return len(s[-1])
# 		# else: 
# 		# 	return 0

# 		last = ''
# 		continue_white = True
# 		for i in range(1,len(s)+1):
# 			if s[-i] != ' ':
# 				continue_white = False
# 			if not continue_white:
# 				if s[-i] == ' ':
# 					break 
# 				last = last + s[-i]
# 		return len(last)                                                                                		            	