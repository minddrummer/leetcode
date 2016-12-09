# 125. Valid Palindrome
# Total Accepted: 81196 Total Submissions: 355032 Difficulty: Easy
# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Note:
# Have you consider that the string might be empty? This is a good question 
# to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.
# Subscribe to see which companies asked this question



# class Solution:
# 	# @param {string} s
# 	# @return {boolean}
# 	def isPalindrome(self, s):
# 		#the following is slower, will run n+n+n times at least
# 		# if len(s) == 0:
# 		# 	return True
# 		# s = s.lower()
# 		# s = ''.join(x for x in s if x.isalnum())
# 		# return s == s[::-1]
		#method2 will run n times
# 		#if empty count it as True
# 		count = len(s)
# 		if count==0: return True
# 		left=0
# 		right=count-1
# 		while left<right:
# 			if s[left].isalnum() and s[right].isalnum():
# 				if s[left].lower()==s[right].lower():
# 					left +=1
# 					right-=1
# 				else:
# 					return False
# 			elif not s[left].isalnum() and s[right].isalnum():
# 				left += 1
# 			elif s[left].isalnum() and not s[right].isalnum():	
# 				right -=1
# 			else:
# 				left+=1
# 				right-=1
# 		return True

# class Solution:
# 	# @param {string} s
# 	# @return {boolean}
# 	def isPalindrome(self, s):
# 		s=s.lower()
# 		n=len(s)
# 		if n==0: return True
# 		left=0
# 		right=n-1
# 		lst = '0123456789abcdefghijklmnopqrstuvwxyz'
# 		while left<right:
# 			while s[left] not in lst and left<right:
# 				left +=1
# 			while s[right] not in lst and left<right:
# 				right-=1
# # 			print s[left],s[right]
# 			if s[left]==s[right]:
# 				left+=1
# 				right-=1
# 			else: return False
# 		return True
		

# 28. Implement strStr() My Submissions Question
# Total Accepted: 84227 Total Submissions: 355976 Difficulty: Easy
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {string} haystack
# 	# @param {string} needle
# 	# @return {integer}
#     def strStr(self, haystack, needle):
# 		#this method is brute-force, but good enough
# 		hl = len(haystack)
# 		nl = len(needle)
# 		if nl == 0: return 0
# 		i = 0
# 		j=0
# 		while i < hl:
# 			if haystack[i] == needle[j]:
# 				new_i = i
# 				match=True
# 				#need both condition
# 				while j<nl-1 and new_i<hl-1:
# 					new_i += 1
# 					j += 1
# 					if haystack[new_i]==needle[j]:
# 						continue
# 						# new_i+=1
# 						# j+=1
# 					else:
# 						match=False
# 						j=0
# 						break
# 				if match and j==nl-1: return i
# 				# if haystack[i:(i+nl)] == needle:
# 				# 	return i
# 			i += 1
# 			# 	else:
# 			# 		i = i + nl
# 			# else: 
# 			# 	i += 1    	
# 		return -1

# class Solution:
# 	# @param {string} haystack
# 	# @param {string} needle
# 	# @return {integer}
#     def strStr(self, haystack, needle):
# 		nh = len(haystack)
# 		nn = len(needle)
# 		if nn==0: return 0
# 		idx=0
# 		while idx<nh:
# 		    if haystack[idx:idx+nn] == needle: return idx
# 		    else: idx +=1
# 		return -1
			
# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.strStr('abaacdaa','aa')	

# 8. String to Integer (atoi) My Submissions Question
# Total Accepted: 80256 Total Submissions: 612069 Difficulty: Easy
# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
# spoilers alert... click to show requirements for atoi
# Subscribe to see which companies asked this question
# class Solution:
# 	# @param {string} str
# 	# @return {integer}
# 	def myAtoi(self, str):
# 		# four input: invalid, sign, 0-9 and space
# 		SIGN = 1
# 		NUM = 2
# 		SPACE = 3
# 		#
# 		transition = [[-1,1,2,0], #state with only space or tab
# 					  [-1,-1,2,-1], #state with space and +/-
# 					  [-1,-1,2,3], #state with space and +/- and number 0-9
# 					  [-1,-1,-1,3]] # state with space and +/1 and number and space after
# 		res=0
# 		sign = None
# 		lst =[]
# 		state = 0
		
# 		for i in range(len(str)):
# 			if str[i] in '+-': input = SIGN
# 			elif str[i] in '0123456789': input = NUM
# 			elif str[i] == ' ': input = SPACE
# 			else: input = None
			
# 			if input is None: break
# 			else:
# 				state = transition[state][input]
# 				if state == -1: break
# 				else:
# 					if str[i] in '+-': sign = str[i]
# 					elif str[i] == ' ': continue
# 					else: lst.append(str[i])
# 		if len(lst)>0:            
# 			if sign is None or sign == '+':
# 				res = int(''.join(lst))
# 				if res>2147483647: res = 2147483647
# 			else:
# 				res =  -int(''.join(lst))
# 				if res < -2147483648: res = -2147483648
# 		return res

# class Solution:
# 	# @param {string} str
# 	# @return {integer}
# 	def myAtoi(self, str):
# 		if len(str) == 0:
# 			return 0
# 		s = str
# 		#remove all the white space
# 		s = s.strip()
# 		num_lst = ['0','1','2','3','4','5','6','7','8','9','-','+']
# 		res = []
# 		i=0
# 		for letter in s:
# 			if letter in num_lst:
# 				#only allows one sign
# 				if i==0 and letter in ['-','+']:
# 					res.append(letter)
# 					i+=1
# 				# elif i==1 and letter in ['-','+']:
# 				# 	res=[]
# 				# 	break
# 				#more than one sign will break and stop counting
# 				elif i>0 and letter in ['+','-']:
# 					break
# 				else:
# 					i+=1
# 					res.append(letter)
# 			else:
# 				break
# 		#len0 or only sign will return 0				
# 		if len(res) == 0 or (len(res)==1 and res[0] in ['+','-']):
# 			return 0
# 		res = int(''.join(res))
# 		#adjust the final range
# 		if res > 2147483647:
# 		    return 2147483647
# 		if res < -2147483648:
# 		    return -2147483648
# 		return res


# 67. Add Binary My Submissions Question
# Total Accepted: 67706 Total Submissions: 261672 Difficulty: Easy
# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".
# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {string} a
# 	# @param {string} b
# 	# @return {string}
# 	def addBinary(self, a, b):
		#the shortest and pythonest way to finish the code
		#return 
		#if you save result into a list, will take SO(n), but if you 
		#make it as a int or str, it will take SO(1)
		# if len(a) >= len(b):
		# 	b = (len(a)-len(b))*'0' + b
		# else:
		# 	a = (len(b)-len(a))*'0' + a
		# res = ''
		# up = 0
		# for i in range(1,len(a)+1):
		# 	if int(a[-i]) + int(b[-i]) + up >= 2:
		# 		res = res + str((int(a[-i]) + int(b[-i]) + up)%2)
		# 		up = 1
		# 	else:
		# 		res = res + str(int(a[-i]) + int(b[-i]) + up)
		# 		#has to reset up here
		# 		up = 0
		# if up == 1:
		# 	res = res + '1'	
		# #x = bin(int(a,2)+int(b,2))[2:]	
		# return res[::-1]#, x

		#method 2: to int, add first, and the  transfer to string digits by digits
		# c = str(int(a) + int(b))[::-1]
		# # count = len(c)
		# res = ''
		# up = False
		# for i in c:
		# 	if i == '0':
		# 		if up: res = '1'+res
		# 		else: res = '0'+res
		# 		up = False
		# 	elif i == '1':
		# 		if up: 
		# 			res = '0' + res
		# 			up = True
		# 		else:
		# 			res = '1'+res
		# 			up = False
		# 	else:#=2
		# 		if up:
		# 			res = '1'+res
		# 		else:
		# 			res = '0'+res
		# 		up=True
		# if up:
		# 	res = '1'+res
		# return res		




# 5. Longest Palindromic Substring My Submissions Question
# Total Accepted: 85048 Total Submissions: 390023 Difficulty: Medium
# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems

# class Solution(object):
# 	def getP(self,s,l,r,count):
# 		while l>=0 and r<count and s[l]==s[r]:
# 			l-=1
# 			r+=1
# 		return s[l+1:r]
# 	def longestPalindrome(self, s):
# 		"""
# 		:type s: str
# 		:rtype: str
# 		"""
# 		method1: from middle to two side, get the most longest length
# 		TO(n^2), SO(n)
# 		p=''
# 		count=len(s)
# 		for i in range(count):
# 			p_odd = self.getP(s,i,i,count)
# 			if len(p_odd)>len(p): p = p_odd
# 			p_even = self.getP(s,i,i+1,count)
# 			if len(p_even)>len(p): p = p_even
# 		return p

		#method2:dynamic programming
		#To(n^2), SO(n^2)
		# P[i,j] = 1  if i ==j
  #       =  S[i] ==S[j]   if j = i+1
  #       =  S[i] == S[j] && P[i+1][j-1]  if j>i+1

		# n=len(s)
		# if n<=1: return s
		# dct={}
		# pan = ''
		# count = 0
		# #reverse index for j, not the typical going forward, but rather backward!
		# for i in range(n):
		# 	for j in range(0,i+1):
		# 		if j==i:
		# 			dct[(j,i)]=True
		# 		elif j==i-1:
		# 			dct[(j,i)]=s[i]==s[j]
		# 		else:
		# 			dct[(j,i)]=(s[i]==s[j] and dct[(j+1,i-1)])
		# 		if dct[(j,i)] and i-j+1>count:
		# 			count = i-j+1
		# 			pan = s[j:i+1]
		# return pan


# 10. Regular Expression Matching My Submissions Question
# Total Accepted: 65937 Total Submissions: 309819 Difficulty: Hard
# Implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# Some examples:
# isMatch("aa","a")  false
# isMatch("aa","aa")  true
# isMatch("aaa","aa")  false
# isMatch("aa", "a*")  true
# isMatch("aa", ".*")  true
# isMatch("ab", ".*")  true
# isMatch("aab", "c*a*b") true

class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		ns = len(s)
		np = len(p)
		dp = [[False for j in range(ns+1)] for i in range(np+1)]
		dp[0][0]=True
		for i in range(1,np+1):
			if p[i-1] == '*': dp[i][0] = dp[i-2][0]
		
		for i in range(1,np+1):
			for j in range(1,ns+1):
				if p[i-1] == '*':
					dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and (p[i-2]=='.' or p[i-2]==s[j-1]))
				elif p[i-1] == '.':
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = dp[i-1][j-1] and s[j-1]==p[i-1]
		return dp[-1][-1]

		
# class Solution(object):
# 	def isMatch(self, s, p):
# 		"""
# 		:type s: str
# 		:type p: str
# 		:rtype: bool
# 		"""
		
# 		#dynamical programming	
# 		dp = [[False for i in range(0,len(p)+1)] for j in range(0,len(s)+1)]
# 		dp[0][0]=True
# 		for i in range(len(p)+1):
# 			if i>=2 and p[i-1]=='*':
# 				dp[0][i]=dp[0][i-2]
# 		#start from the second place				
# 		for i in range(1,len(s)+1):
# 			for j in range(1,len(p)+1):
# 				if p[j-1]=='.':
# 					dp[i][j] = dp[i-1][j-1]
# 				elif p[j-1]=='*':
# 					dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
# 				else:
# 					dp[i][j]= dp[i-1][j-1] and s[i-1]==p[j-1]
# 		#put  i j here will get a bug
# 		return dp[len(s)][len(p)]

# if __name__ == '__main__':
# 	sk =Solution()
	# print sk.isMatch('aaaaaaaaaaaaab',"a*a*a*a*a*a*a*a*a*a*c")
	# print sk.isMatch('1',"1*")

# 44. Wildcard Matching My Submissions Question
# Total Accepted: 46918 Total Submissions: 284267 Difficulty: Hard
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# Some examples:
# isMatch("aa","a") false
# isMatch("aa","aa")  true
# isMatch("aaa","aa") false
# isMatch("aa", "*")  true
# isMatch("aa", "a*")  true
# isMatch("ab", "?*")  true
# isMatch("aab", "c*a*b") false


# class Solution(object):
# 	def isMatch(self, s, p):
# 		"""
# 		:type s: str
# 		:type p: str
# 		:rtype: bool
# 		"""
# 		spos=ppos=ss=0
# 		star=-1
# 		lens=len(s)
# 		lenp=len(p)
# 		while spos<lens:
# 			if ppos<lenp and (s[spos]==p[ppos] or p[ppos]=='?'):
# 				spos +=1; ppos+=1; 
# 				continue
# 			if ppos<lenp and p[ppos] == '*':
# 				star = ppos; ss=spos; ppos +=1;
# 				continue
# 			if star != -1:
# 				ppos = star+1; ss += 1; spos = ss;
# 				continue
# 			return False
# 		while ppos < lenp and p[ppos] == '*':
# 			ppos += 1
# 		if ppos == lenp: return True
# 		return False

# if __name__ == '__main__':
# 	sk = Solution()
# 	print sk.isMatch('aaaabaaaab', 'a*b*b' )
# 	print sk.isMatch('aaaaaaaab', 'a*b*b' )
# 	print sk.isMatch('aaaaaaaab', 'a*b*b***' )
# 	print sk.isMatch('aaaabbbaaaab', 'a*b*b***' )
# #use 'aaaabaaaab' vs 'a*b*b' as an example



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

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs)==0: return ''
#         minLen = min([len(string) for string in strs])
		
#         i=0
#         res =''
#         while i< minLen:
#             cur = strs[0][i]
#             breakLoop = False
#             for string in strs:
#                 if string[i] != cur:
#                     breakLoop = True
#                     break
#             if breakLoop: break
#             res += cur
#             i+=1
#         return res

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

# class Solution:
#     # @param s, a string
#     # @return a boolean
#     # @finite automation
#     def isNumber(self, s):
#         INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
#         #0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
#         transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
#                          [-1,  8, -1,  1,  4,  5],    #1 input is digits 
#                          [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
#                          [-1, -1, -1,  1,  2, -1],    #3 sign 
#                          [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
#                          [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
#                          [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
#                          [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
#                          [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space
#         state=0; i=0
#         while i<len(s):
#             inputtype = INVALID
#             if s[i]==' ': inputtype=SPACE
#             elif s[i]=='-' or s[i]=='+': inputtype=SIGN
#             elif s[i] in '0123456789': inputtype=DIGIT
#             elif s[i]=='.': inputtype=DOT
#             elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT
			
#             state=transitionTable[state][inputtype]
#             if state==-1: return False
#             else: i+=1
#         return state == 1 or state == 4 or state == 7 or state == 8
		

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
#         VALUE = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         ROMAN = [ 'M', 'CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
		
#         res = ''
		
#         for i in range(len(VALUE)):
#             while num>=VALUE[i]:
#                 num -= VALUE[i]
#                 res += ROMAN[i]
#         return 
		

# 13. Roman to Integer My Submissions Question
# Total Accepted: 65811 Total Submissions: 178393 Difficulty: Easy
# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# Subscribe to see which companies asked this question

# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         VALUE = [1000, 500, 100, 50, 10, 5, 1]
#         ROMAN = [ 'M', 'D','C', 'L','X','V','I']
#         valDict = dict(zip(ROMAN, VALUE))
#         lst = [valDict[i] for i in s]    
#         lst.append(1)
#         res = 0
#         i=0
#         while i <= len(lst)-2:
#             if lst[i] < lst[i+1]:
#                 res += lst[i+1]-lst[i]
#                 i += 2
#             else:
#                 res += lst[i]
#                 i+=1
#         return res
	

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
# 	# @param {integer} n
# 	# @return {string}
# 	def countAndSay(self, n):
# 		# should transform to string, and count each number in the string, and speak it
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


# class Solution(object):
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         n = str(n)
#         i=0
#         cur = None
#         count = 0
#         res = ''
#         while i <len(n):
#             if n[i] == cur:
#                 count += 1
#                 i +=1
#             else:
#                 if cur is not None:
#                     res += str(count)+cur
#                 cur = n[i]
#                 count = 1
#                 i += 1
#         #left over
#         res += str(count)+cur
#         return res		

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
# 	def isAnagram(self, s, t):
# 		"""
# 		:type s: str
# 		:type t: str
# 		:rtype: bool
# 		"""
# 		s_dict ={}
# 		for i in s:
# 			if i not in s_dict:
# 				s_dict[i] = 1
# 			else:
# 				s_dict[i] += 1
# 		for i in t:
# 			if i not in s_dict:
# 				return False
# 			else:
# 				s_dict[i] -=1
# 		for key in s_dict:
# 			if s_dict[key] != 0:
# 				return False
# 		return True



		

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
# 			res = res + strs_dict[key]
# 		return res
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         dct={}
#         for word in strs:
#             newWord = ''.join(sorted(word))
#             if newWord in dct: dct[newWord].append(word)
#             else: dct[newWord]=[word]
#         return dct.values()

# 71. Simplify Path My Submissions Question
# Total Accepted: 42843 Total Submissions: 204499 Difficulty: Medium
# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Subscribe to see which companies asked this question

# class Solution(object):
# 	def simplifyPath(self, path):
# 		"""
# 		:type path: str
# 		:rtype: str
# 		"""
# 		#TO(n), SO(n)
# 		#use stack
# 		res = ''
# 		# for l in path:
# 		# 	if l
# 		#use python processing string ability
# 		path = path.split('/')
# 		for l in path:
# 			if l =='':
# 				continue
# 			elif l =='.':
# 				continue
# 			elif l == '..':
# 				if len(res)==0:
# 					continue
# 				else:
# 					i = -1
# 					while res[i] != '/':
# 						i -= 1
# 					res	= res[0:i]				
# 			else:
# 				res += '/'+l
# 		if res == '': return '/'
# 		return res


# class Solution(object):
#     def simplifyPath(self, path):
#         """
#         :type path: str
#         :rtype: str
#         """
		
#         i=0
#		  #add one / is pretty smart!
#         path = path+'/'
#         n=len(path)
#         stack = []
#         lst=[]
#         while i<n-1:
#             if path[i] == '/':
#                 cur = i
#                 i +=1
#                 while path[i] != '/' and i<n: i+=1
#                 command = path[cur+1:i]
#                 if command == '.': continue
#                 elif command == '..': 
#                     if stack: stack.pop(-1)
#                     else: continue
#                 elif command == '': continue
#                 else:
#                     stack.append(command)
			
#         if stack:
#             res=''
#             for item in stack:
#                 res  += '/'+item 
#         else:
#             res = '/'
#         return res
# if __name__ == '__main__':
# 	sk = Solution()
# 	print  sk.simplifyPath("/a/./b/../../c/")
# 	print  sk.simplifyPath("/../")
# 	print  sk.simplifyPath("/home//foo")

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
# 		# mark and get the letter
# 		# last = ''
# 		# continue_white = True
# 		# for i in range(1,len(s)+1):
# 		# 	if s[-i] != ' ':
# 		# 		continue_white = False
# 		# 	if not continue_white:
# 		# 		if s[-i] == ' ':
# 		# 			break 
# 		# 		last = last + s[-i]
# 		# return len(last)       



# 		#the index way to do it
# 		lens= len(s)
# 		if lens==0: return 0
# 		start = -1
# 		i = 1
# 		while i <= lens:
# 			if s[-i] == ' ':
# 				i+=1
# 				continue
# 			else:
# 				start = i
# 				break
# 		if start == -1: return 0
# 		end = -1
# 		while i <= lens:
# 			if s[-i] != ' ':
# 				i += 1
# 				continue
# 			else:
# 				end = i
# 				break
# 		if end == -1:
# 			return lens-start+1
# 		else:
# 			return end - start

# class Solution:
# 	# @param {string} s
# 	# @return {integer}
# 	def lengthOfLastWord(self, s):
# 		n=len(s)
# 		if n==0: return 0
# 		i=0; count=0; cur =None
# 		while i<n:
# 			if s[i]!=' ':
# 				cur = i
# 				while i < n and s[i]!= ' ':
# 					i += 1
# 				count = i - cur
# 			else:
# 				i += 1
# 		#the following is when the lasting space would be counted as non-word situation		
# 		# if cur is None or i-cur!=count: return 0
# 		# else: return count
# 		return count

