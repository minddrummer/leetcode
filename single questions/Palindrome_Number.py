# Determine whether an integer is a palindrome. Do this without extra space.




class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]



if __name__ == '__main__':
	test = Solution()
	test.isPalindrome()        