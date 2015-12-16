'''
this code is using the following algm:
generate all the possible results, and then find each result in string s,
if there is a match, return the index, otherwise jump to the next combination in L:
for large number of elements in L, this would be  rather less efficient.
the right way to move from s to L, get  a sliding window in s, and check from s to L
this algm will tranfer to a linear computation time.
'''
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].



class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def __init__(self):
		self.word_comb = None
		self.s = None

	def gen_word_comb(self, words):
		'''
		words has to be a list
		use recursive function
		'''
		if len(words) <= 1:
			yield words
		else:
			for item in self.gen_word_comb(words[1:]):
				for i in range(len(words)):
					yield item[:i] + words[0:1] + item[i:]

		# if len(words) <= 1:
		# 	return [words]

		# else:
		# 	first_word = words[0:1]
		# 	#print first_word
		# 	rest_words = words[1:]
		# 	words_comb = []
		# 	for item in self.gen_word_comb(rest_words):
		# 		for i in xrange(len(words)):
		# 	#		print item[:i]
		# 			words_comb.append(item[:i]+first_word+item[i:])
		# 	return words_comb
		# if len(words) <= 1:
		# 	yield [words]
		# 	#return [words]
		# else:
		# 	word_comb = []
		# 	first_word = [words[0]]
		# 	rest_words = words[1:]
		# 	rest_words_comb = self.gen_word_comb(rest_words)
		# 	for item in rest_words_comb:
		# 		for i in range(0,len(item)+1):
		# 			#print item
		# 			#print first_word
		# 			word_comb.append(item[:i] + first_word + item[i:])
		# 	yield word_comb
		# 	#return word_comb
		

	def concatenate(self, word_comb):
		word_concate_lst = []
		for item in word_comb:
			if len(item) == 0:
				pass
			else:	
				word_concate = reduce(lambda total,x: str(total)+str(x), item)
				word_concate_lst.append(word_concate)
		return word_concate_lst

	def findSubstring(self, s, words):
		word_comb = self.gen_word_comb(words)
		word_concate_lst = self.concatenate(word_comb)
		s_index =[]
		print word_concate_lst
		for item in word_concate_lst:
			print item
			s_index.append(s.find(item))
		return s_index

	def generator(slef, x):
		yield [x]

if __name__ == '__main__':
	# s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
	# words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
	s = 'a'
	words = ['a','b']
	#words = []
	test = Solution()
	for item in test.gen_word_comb(['a','b','c']):
		print item
	for item in test.gen_word_comb([1]):
		print item
	print '----------'
	for x in test.generator([4,5]):
		print x
	#print test.findSubstring(s, words)










