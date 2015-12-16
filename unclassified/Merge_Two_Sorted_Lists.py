# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	if l1 is None and l2 is None:
    		return None
    	elif l1 is None and l2 is not None:
    		return l2
    	elif l1 is not None and l2 is None:
    		return l1
    	else:
    		if l1.val >= l2.val:
	    		head = l2
	    		dummy = head
	    		l2 = l2.next
	    	else:
	    		head = l1
	    		dummy = head
	    		l1 = l1.next
    		while l1 is not None and l2 is not None:
    			if l1.val >= l2.val:
	    			head.next = l2
	    			l2 = l2.next
	    			head = head.next
		    	else:
		    		head.next = l1
	    			l1 = l1.next
	    			head = head.next
	    	if l1 is None:
	    		head.next = l2
	    	if l2 is None:
	    		head.next = l1
	    	return dummy







if __name__ == '__main__':
   test = Solution()
   test.mergeTwoLists()    	