# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	link_dict = {}
    	d1 = headA
    	d2 = headB
    	res = None
    	if d1 is None or d2 is None:
    		return None
    	while d1 is not None:
    		link_dict[d1] = 1
    		d1 = d1.next
    	while d2 is not None:
    		if d2 in link_dict:
				res = d2
				break    			
    		d2 = d2.next
    	return res



# if __name__ == '__main__':
# 	test = Solution()
# 	test.getIntersectionNode()