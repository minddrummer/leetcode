# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}

    #the following is a better way for reversing, though the problem itself doesnot need reversing necessarily
    # def reverse(self, head):
    # 	orig_lst = []
    # 	pre = None
    # 	while head is not None:
    # 		orig_lst.append(head.val)
    # 		cur_next = head.next
    # 		head.next = pre
    # 		pre = head
    # 		head = cur_next
    		
    # 	return orig_lst, pre

    # def isPalindrome(self, head):
    #     lst, rev = self.reverse(head)
    #     lst1, rev2 = self.reverse(rev)

    #     return lst == lst1

    def isPalindrome(self, head):
        orig_lst = []
    	while head is not None:
    		orig_lst.append(head.val)
    		head = head.next
    		
    	return orig_lst == orig_lst[::-1]