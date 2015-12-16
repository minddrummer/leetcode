# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
    	if head is None:
    		return head
    	#head is not touched, so it can be returned
    	pre = head
    	cur = head.next
    	while cur is not None:
    		#this is because the list is sorted, so just need to judge >
    		if cur.val > pre.val:
    			pre = cur
    			cur = cur.next
    		else:
    			#how to remove a node from a list: just let its value to be the next's, and its next to be the next's next
    			#that is an efficient way to achieve this goal!!
    			pre.val = cur.val
    			pre.next = cur.next
    			cur = cur.next
    	return head




        