# 2. Add Two Numbers My Submissions Question
# Total Accepted: 109212 Total Submissions: 506241 Difficulty: Medium
# You are given two linked lists representing two non-negative numbers.
 # The digits are stored in reverse order and each of their nodes contain a single digit. 
 # Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#classic question to check the listNode assign and value change, such as the following head and res match and diverge
# class Solution(object):
# 	def addTwoNumbers(self, l1, l2):
# 		"""
# 		:type l1: ListNode
# 		:type l2: ListNode
# 		:rtype: ListNode
# 		"""
# 		#should be TO(n), SO(1)
# 		up = False
# 		head1=l1
# 		head2=l2
# 		#object is mutable, so the change of res's attributes would change the head's attributes
# 		#now head and res refer to the same object, change res's partial attributes would change head's partial attributes
# 		#but when you refer res to another object, the two would diverge, and change res would NOT change head
# 		head = ListNode(0) 
# 		res = head
# 		while head1 is not None or head2 is not None:
# 			each_digit=0
# 			if head1 is not None:
# 				each_digit += head1.val
# 			if head2 is not None:
# 				each_digit += head2.val
# 			each_digit += up

# 			if each_digit<10:
# 				up=False
# 				res.next = ListNode(each_digit)
# 				#here we assign res to another ListNode, and head and res now diverge
# 				res= res.next
# 				if head1 is not None:
# 					head1=head1.next
# 				if head2 is not None:
# 					head2=head2.next
# 			else:
# 				up=True
# 				res.next=ListNode(each_digit-10)
# 				res=res.next
# 				if head1 is not None:
# 					head1=head1.next
# 				if head2 is not None:
# 					head2=head2.next
# 		#bugs here: there might be still one up left needed to be dealed with
# 		if up == True:
# 			res.next = ListNode(1)    		
# 		return head.next
			


# 92. Reverse Linked List II My Submissions Question
# Total Accepted: 59214 Total Submissions: 221428 Difficulty: Medium
# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Subscribe to see which companies asked this question




# class Solution:
#     # @param head, a ListNode
#     # @param m, an integer
#     # @param n, an integer
#     # @return a ListNode
#     def reverseBetween(self, head, m, n):
#         ''''''
#         if head == None or head.next == None:
#             return head

#         dummy = ListNode(0)
#         dummy.next = head

#         pre = dummy
#         cur = head
#         for i in range(m-1):
#             pre = cur
#             cur = cur.next
		
#         if cur is not None:
#             p1 = cur.next
#         if p1 is not None:
#             p2 = p1.next

#         for i in range(n-m):
#             p1.next = cur
#             cur = p1
#             p1 = p2
#             if p2 is not None:
#                 p2 = p2.next
		
#         pre.next.next = p1
#         pre.next = cur
		
			
#         return dummy.next




# 86. Partition List My Submissions Question
# Total Accepted: 54817 Total Submissions: 193320 Difficulty: Medium
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Subscribe to see which companies asked this question

# Show Tags


# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """



# 83. Remove Duplicates from Sorted List My Submissions Question
# Total Accepted: 92337 Total Submissions: 259503 Difficulty: Easy
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Subscribe to see which companies asked this question


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     # @param {ListNode} head
#     # @return {ListNode}
#     def deleteDuplicates(self, head):
#     	if head is None:
#     		return head

#     	pre = head
#     	cur = head.next
#     	while cur is not None:
#     		if cur.val > pre.val:
#     			pre = cur
#     			cur = cur.next
#     		else:
#     			#pre.val = cur.val
#     			pre.next = cur.next
#     			cur = cur.next
#     	return head
		

# 82. Remove Duplicates from Sorted List II My Submissions Question
# Total Accepted: 60528 Total Submissions: 233708 Difficulty: Medium
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Subscribe to see which companies asked this question

# Show Tags


# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
		

# 61. Rotate List My Submissions Question
# Total Accepted: 56511 Total Submissions: 254664 Difficulty: Medium
# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
		

# 19. Remove Nth Node From End of List My Submissions Question
# Total Accepted: 86284 Total Submissions: 307960 Difficulty: Easy
# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Subscribe to see which companies asked this question

# class Solution:
# 	# @param {ListNode} head
# 	# @param {integer} n
# 	# @return {ListNode}
# 	def count_head_order(self, head, n):
# 		'''this fucntion counting the x-th node from the head if it is n-th node from the end'''
# 		if head is None:
# 			return None
# 		i = 1
# 		while head.next is not None:
# 			head = head.next
# 			i += 1
# 		if i == 1:
# 			return None
# 		return (i - n + 1)

# 	def removeNthFromEnd(self, head, n):
# 		nh = self.count_head_order(head,n)
# 		if nh is None:
# 			return None
# 		if nh == 1:
# 			return head.next
# 		cur = head
# 		for i in range(nh - 2):
# 			cur = cur.next
# 		pre = cur
# 		cur =  cur.next
# 		curNext = cur.next
# 		pre.next = curNext
# 		return head
		


# 24. Swap Nodes in Pairs My Submissions Question
# Total Accepted: 75216 Total Submissions: 223207 Difficulty: Medium
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """


# 25. Reverse Nodes in k-Group My Submissions Question
# Total Accepted: 49488 Total Submissions: 187850 Difficulty: Hard
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
		

# 138. Copy List with Random Pointer My Submissions Question
# Total Accepted: 54702 Total Submissions: 212259 Difficulty: Hard
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# # Definition for singly-linked list with a random pointer.
# # class RandomListNode(object):
# #     def __init__(self, x):
# #         self.label = x
# #         self.next = None
# #         self.random = None

# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: RandomListNode
#         :rtype: RandomListNode
#         """
		

# 141. Linked List Cycle My Submissions Question
# Total Accepted: 86686 Total Submissions: 236463 Difficulty: Medium
# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         res = False
#         while head is not None:
#             if head.val != 's':
#             	head.val = 's'
#                 head = head.next
#             else:
#                 res = True
#                 break
#         return res 


# 142. Linked List Cycle II My Submissions Question
# Total Accepted: 62790 Total Submissions: 199610 Difficulty: Medium
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
		

# 143. Reorder List My Submissions Question
# Total Accepted: 55720 Total Submissions: 254913 Difficulty: Medium
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Subscribe to see which companies asked this question

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: void Do not return anything, modify head in-place instead.
#         """
		

# 146. LRU Cache My Submissions Question
# Total Accepted: 58461 Total Submissions: 376255 Difficulty: Hard
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Subscribe to see which companies asked this question

# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
		

#     def get(self, key):
#         """
#         :rtype: int
#         """
		

#     def set(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: nothing
#         """
#                                                                                                         