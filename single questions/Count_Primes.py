class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
    	#the alogorithm would be slow in this way::
    	# if n == 2:
    	# 	return 0    	
    	# num = 0
    	# for i in range(3,n):
    	# 	is_prime = True
    	# 	for x in range(2,1+i/2):
    	# 		if i%x == 0:
    	# 			is_prime = False
    	# 			break
    	# 		if x*x>i:
    	# 			break
    	# 	if is_prime:
    	# 		num += 1
    	# return num
    	isPrime = [True]*len(range(n-2))
    	
    	for i in range(2, 1+n/2):
    		#print i
    		if i*i > n:
    			break
    		if not isPrime[i-2]: 
    			continue
    		for j in range(i*i, n, i):
    			if j >= n:
    				break
    			#print j
    			isPrime[j-2] = False

    	count = 0
    	for i in range(2,n):
    		if isPrime[i-2]:
    			count += 1
    	return count

# public int countPrimes(int n) {
#    boolean[] isPrime = new boolean[n];
#    for (int i = 2; i < n; i++) {
#       isPrime[i] = true;
#    }
#    // Loop's ending condition is i * i < n instead of i < sqrt(n)
#    // to avoid repeatedly calling an expensive function sqrt().
#    for (int i = 2; i * i < n; i++) {
#       if (!isPrime[i]) continue;
#       for (int j = i * i; j < n; j += i) {
#          isPrime[j] = false;
#       }
#    }
#    int count = 0;
#    for (int i = 2; i < n; i++) {
#       if (isPrime[i]) count++;
#    }
#    return count;
# }

#```````````````````````````
#better solution:
# class Solution:
#     # @param {integer} n
#     # @return {integer}
#     def countPrimes(self, n):
#         isPrime = [True] * max(n, 2)
#         isPrime[0], isPrime[1] = False, False
#         x = 2
#         while x * x < n:
#             if isPrime[x]:
#                 p = x * x
#                 while p < n:
#                     isPrime[p] = False
#                     p += x
#             x += 1
#         return sum(isPrime)

if __name__ == '__main__':
	test = Solution()
	#print test.countPrimes(2)
	print test.countPrimes(5)
	print test.countPrimes(7)
	print test.countPrimes(88888)

