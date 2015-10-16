# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
   	def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #no extra space
        res = False
        while head is not None:
            if head.val is not None:
            	head.val = None
                head = head.next
            else:
                res = True
                break
        return res 

