class Solution:
    # @return a string
    def convert(self, s, nRows):
        if  nRows <= 1:
            return s
        #note the most typicall error here is that you mess up with index with the length
        n = nRows
        bn = n - 2 + n
        fn = len(s)
        res = ''
        for i in range(n):
            if i == 0 or i == n-1:
                loop = 0
                while bn*loop + i <= fn-1:
                    res = res + s[bn*loop + i]
                    loop += 1
            else:
                loop = 0
                while (bn*loop + i <= fn-1):
                    res = res + s[bn*loop+i]
                    #note the most typicall error here is that you mess up with index with the length
                    if (bn*loop+i+(n-1-i)*2) <= fn-1:
                        res = res + s[bn*loop+i+(n-1-i)*2]
                    loop += 1
        return res

if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    test = Solution()
    print test.convert(s, 3)
    print '`````````````'
    print test.convert(s, 4)
    print '`````````````'
    print test.convert(s, 5)