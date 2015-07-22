# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.






# class Solution:
#     # @param {integer[]} nums1
#     # @param {integer} m
#     # @param {integer[]} nums2
#     # @param {integer} n
#     # @return {void} Do not return anything, modify nums1 in-place instead.
#     def merge(self, nums1, m, nums2, n):
#     	#n1c = 0
#     	if n == 0: return nums1
		
#     	size_1 = m
#     	j = 0
#     	for n2 in nums2:
			
#     		i = 0
#     		ending = True
#     		while i < size_1:
#     			if nums1[i] > n2:
#     				tmp = nums1[i:]
#     				nums1[i] = n2
#     				nums1[(i+1):] = tmp
#     				size_1 = len(nums1)
#     				ending = False
#     				break
#     			i += 1
#     		if ending == True:
#     			for item in nums2[j:]:
#     				nums1.append(item)
#     			break
#     		j += 1

#     	return nums1	
class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		tmp = [0 for i in range(m+n)]
		i =0 ; j = 0 ; k = 0
		while i <m and j <n:
			if A[i] <B[j]:
				tmp[k] = A[i]; i+=1
			else:
				tmp[k] = B[j]; j+=1
			k += 1
		if i == m:
			while j <n:
				tmp[k] = B[j]; j+=1;k+=1
		else:
			while i <m:
				tmp[k] = A[i]; i+=1;k+=1
		
		thres = len(A)
		for i in range(m+n):
			if i < thres:
				A[i] = tmp[i]
			else:
				A.append(tmp[i])
		if i < thres-1:
			for x in range(thres-1-i):
				A.pop(-1)

		# tmp = [0 for i in range(m + n)]
		# i = 0; j = 0; k = 0
		# while i < m and j < n:
		# 	if A[i] <= B[j]:
		# 		tmp[k] = A[i]; i += 1
		# 	else:
		# 		tmp[k] = B[j]; j += 1
		# 	k += 1
		# if i == m:
		# 	while k < m + n:
		# 		tmp[k] = B[j]; k += 1; j += 1
		# else:
		# 	while k < m + n:
		# 		tmp[k] = A[i]; i += 1; k += 1
		
		# thres = len(A)
		# for i in range(0, m + n):
		# 	if i < thres:
		# 		A[i] = tmp[i]
		# 	else:
		# 		A.append(tmp[i])
		
		# if i < thres-1:
		# 	for x in range(thres-1-i):
		# 		A.pop(-1)


if __name__ == '__main__':
	test = Solution()
	A = [1,2,3,99,100]
	test.merge(A,3,[3,4,100],3)    	
	print A