# d Search Word - Data structure design Total Accepted: 6550 Total Submissions: 32157 My Submissions Question Solution 
# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.



class WordDictionary:
	# initialize your data structure here.
	def __init__(self):
		

	# @param {string} word
	# @return {void}
	# Adds a word into the data structure.
	def addWord(self, word):
		

	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the data structure. A word could
	# contain the dot character '.' to represent any one letter.
	def search(self, word):
		if '.' not in word:
			if word in self.val:
				return True
			else:
				return False
		else:
			for i in range(len(word)):
				if word[i] != '.':
					if '.' not in word[i+1:]:
						if word in self.val:
							return True
						else:
							return False
					else:
						continue
				else:
					new_val = []
					for item in self.val:
						if len(item)-1 >= i:
							item = list(item)
							item[i] = '.'
							new_val.append(''.join(item))
						else:
							new_val.append(item)
					self.val = new_val        
			if word in self.val:
				return True
			else:
				return False
		

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")