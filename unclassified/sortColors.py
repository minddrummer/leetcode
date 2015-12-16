# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# click to show follow up.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       	len_nums = len(nums)
        cur=white=0
        blue = len_nums-1

        while cur <= blue:
        	if nums[cur] == 2:
        		nums[cur] = nums[blue]
        		nums[blue] = 2
        		blue -= 1        	
        	elif nums[cur] == 1:
        		cur += 1
        	else:
        		nums[cur] = nums[white]
        		nums[white] = 0
        		white += 1
        		cur += 1
        		

     



if __name__ == '__main__':
	sk = Solution()
	test1 = [0,1,2,1,0,2]
	sk.sortColors(test1)
	print test1

	test2 = [0,1,2,1,0]
	sk.sortColors(test2)
	print test2
