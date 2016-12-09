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
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         pre = ListNode(0)
#         head = pre
#         up = False
#         while l1 or l2:
#             res = 0
#             if l1: res += l1.val
#             if l2: res += l2.val
#             res += up
#             up = True if res>=10 else False
#             cur = ListNode(res%10)
#             pre.next = cur
#             pre = cur
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         if up: pre.next = ListNode(1)
#         return head.next
			

# 92. Reverse Linked List II My Submissions Question
# Total Accepted: 59214 Total Submissions: 221428 Difficulty: Medium
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
# Note:
# Given m, n satisfy the following condition:
# 1 <=m <= n <= length of list.
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseBetween(self, head, m, n):
#         """
#         :type head: ListNode
#         :type m: int
#         :type n: int
#         :rtype: ListNode
#         """
#         if head is None: return None
#         head0 = ListNode(0)
#         head0.next = head
#         cutNode = head0
		
#         pos = 1
#         while pos<=n:
#             if pos<m: 
#                 cutNode = head
#                 head = head.next
#             if pos==m:
#                 preNode = startNode = head
#                 head = head.next
#             if pos>m:
#                 tmp = head.next
#                 head.next = preNode
#                 preNode = head
#                 head = tmp
#             pos += 1
		
#         startNode.next = head
#         cutNode.next =  preNode
#         return head0.next
		



# 86. Partition List My Submissions Question
# Total Accepted: 54817 Total Submissions: 193320 Difficulty: Medium
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# Subscribe to see which companies asked this question
# Show Tags


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         if head is None or head.next is None: return head
#         p1 = ListNode(0)
#         head1=p1
#         p2 = ListNode(0)
#         head2=p2
#         while head is not None:
#         	if head.val <x:
#         		p1.next=head
#         		p1=p1.next
#         		head=head.next
#         		#has to reset the p1's next node to remove the bug of loop
#         		p1.next=None
#         	else:
#         		p2.next=head
#         		p2=p2.next
#         		head=head.next
#         		#has to reset the p2's next node to remove the bug of loop
#         		p2.next=None
#        	p1.next=head2.next
#        	return head1.next

# class Solution(object):
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         if head is None: return None
#         less0 = less = ListNode(0)
#         more0 = more = ListNode(0)
		
#         while head:
#             if head.val>=x:
#                 more.next = head
#                 more = head
#                 head = head.next
				
#             else:
#                 less.next = head
#                 less = head
#                 head = head.next
#         less.next = more0.next
#         more.next = None
#         return less0.next
		
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
#time1
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
#time2: my own way, it is more clear to understand the whole process, and also quicker

# class Solution:
#     # @param {ListNode} head
#     # @return {ListNode}
#     def deleteDuplicates(self, head):
#     	#boundary when 0 or 1 actually
#     	if head is None or head.next is None: return head
#     	#assgin value and intial the state
#     	value = head.val
#     	preNode = head
#     	res=preNode
#     	head = head.next
#     	while head is not None:
#     	    if value == head.val:
#     	        preNode.next = head.next
#     	        head = head.next
#     	    else:
#     	        value = head.val
#                 preNode = head
#                 head = head.next
#         return res 
						

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
# 	def deleteDuplicates(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		if head is None or head.next is None: return head
# 		#pre-linked  a node
# 		res = ListNode(0)
# 		#linked to head
# 		res.next = head
# 		#set node0, node0 is a safe node in the linked-list
# 		node0 = res
# 		#preNode is the true node start to check on, it is not safe
# 		preNode = head
# 		#head node now is the second possible duplicate valued node here
# 		#and it is the current head node
# 		head = head.next
# 		value = preNode.val
# 		while head is not None:
# 			if head.val>value:
# 				#if the current head is higher than previous::
# 				#move node0 to preNode to make it safe, move preNode to current head node
# 				#and update value, and move head to the next node
# 				node0 = preNode
# 				preNode=head
# 				value = head.val
# 				head = head.next
# 			else:
# 				#if the preNode and the current head node has the same value, we delete the two, set preNode as the node0
# 				preNode=node0
# 				node0.next=head.next
# 				head = head.next
# 		return res.next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None: return head
#         dum = ListNode(float('-inf'))
#         dum.next = head
		
#         #initialization
#         pre0, pre1 = dum, head
#         head = head.next
#         dup = False
		
#         #main loop
#         while head:
#             if head.val == pre1.val:
#                 dup = True
#             else:
#                 if dup:
#                     pre0.next = head
#                     dup = False
#                 else:
#                     pre0 = pre1
#                 pre1 = head
#             head = head.next
#         #the left over
#         if dup: pre0.next = None
#         else: pre1.next = None
		
#         return dum.next

# 61. Rotate List My Submissions Question
# Total Accepted: 56511 Total Submissions: 254664 Difficulty: Medium
# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
# 	def rotateRight(self, head, k):
# 		"""
# 		:type head: ListNode
# 		:type k: int
# 		:rtype: ListNode
# 		"""
# 		if head is None or k==0 or head.next is None: return head
# 		count = 0
# 		res = ListNode(0)
# 		res.next = head
# 		while head is not None:
# 			count += 1
# 			head = head.next

# 		head = res.next
# 		#if k >= count
# 		k = k%count
# 		if k==0: return head
# 		#if k<count
# 		preNode = res
# 		i = 1
# 		#how to rightly figure the times out to get the right bounday
# 		#1 test/cases 2.logic for ending, and minusing and adding
# 		while i <= count-k:
# 			#after the loop, head will be in the right-count kth pos
# 			#preNode is in the left count-k pos
# 			preNode = head
# 			head = head.next
# 			i += 1
# 		preNode.next = None
# 		head1 = res.next
# 		res.next = head
# 		#boudary
# 		while i < count:
# 			head = head.next
# 			i+=1
# 		head.next = head1
# 		return res.next




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
# 	#one pass solution:
# 	#very intellegent solution:becaseu one pass, we set two point, the gap is n
# 	#and they move at the same time until the first one arrive to the end
# 	def removeNthFromEnd(self, head, n):
# 		if head is None: return head
# 		res = ListNode(0)
# 		p=res
# 		res.next = head
# 		#after make p as the initial node, there is NO need for special situation/boundary clarification
# 		q=head
# 		for i in range(n):
# 			q=q.next
# 		while q is not None:
# 			p=p.next
# 			q=q.next
# 		p.next = p.next.next 
# 		return res.next

	#this is not the one-pass solution
	# def count_head_order(self, head, n):
	# 	'''this fucntion counting the x-th node from the head if it is n-th node from the end'''
	# 	if head is None:
	# 		return None
	# 	i = 1
	# 	while head.next is not None:
	# 		head = head.next
	# 		i += 1
	# 	if i == 1:
	# 		return None
	# 	return (i - n + 1)

	# def removeNthFromEnd(self, head, n):
	# 	nh = self.count_head_order(head,n)
	# 	if nh is None:
	# 		return None
	# 	if nh == 1:
	# 		return head.next
	# 	cur = head
	# 	for i in range(nh - 2):
	# 		cur = cur.next
	# 	pre = cur
	# 	cur =  cur.next
	# 	curNext = cur.next
	# 	pre.next = curNext
	# 	return head
		


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
# 	def swapPairs(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		if head is None or head.next is None: return head
# 		res = ListNode(0)
# 		head0 = res
# 		res.next = head
# 		while head is not None:
# 			p = head
# 			q = head.next
# 			if q is not None:
# 				head=head.next.next
# 				head0.next = q
# 				q.next = p
# 				#the bug here is that when you end with p is still valid and the odd Nodes
# 				#therefore, make p linked to head.next.next now
# 				#but linked to head doesnot bring bugs(the infinite loop) here
# 				p.next=head
# 				head0=p
# 			else:
# 				break
# 		return res.next


			


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
# 	def hasCycle(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: bool
# 		"""
# 		#method1: SO(1):set a value to indicate visited or not
# 		#but how do you know the value is unique, and could applied into all cases
# 		# res = False
# 		# while head is not None:
# 		#     if head.val != 's':
# 		#     	head.val = 's'
# 		#         head = head.next
# 		#     else:
# 		#         res = True
# 		#         break
# 		# return res 
# 		#method2: use slow and quicker pointed, and the quicker will
# 		#finally meets slower p after entering the loop
# 		#you judge the two nodes after quicker point's each step of the two steps

# 		if head is None: return False
# 		s = head
# 		q = head.next
# 		while q is not None:
# 			s = s.next
# 			q = q.next
# 			if q is not None:
# 				if s is q: return True
# 				else:
# 					q = q.next
# 					if q is not None and s is q: return True
# 		return False		

# class Solution(object):
# 	def hasCycle(self, head):
# 	    slow = quick = head
# 	    while quick:
# 	        quick = quick.next
# 	        if quick is slow: return True
# 	        if quick:
# 	            quick = quick.next
# 	            if quick is slow: return True
# 	            slow = slow.next
# 	    return False
			
				

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
# 	def detectCycle(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		#method1 is ok, but there is bug, that is when q and s1 meet at the first node of q, rather than the second node of q
# 		#so you need to track whether meet at step1 or step2::
# 		if head is None or head.next is None: return None
# 		s1 = head
# 		q = head.next
# 		loop = False
# 		step1=False
# 		while q is not None:
# 			s1=s1.next
# 			q=q.next
# 			if q is not None:
# 				if s1 is q:
# 					loop =True
# 					step1=True
# 					break
# 				else:
# 					q=q.next
# 					if q is not None and s1 is q: 
# 						loop=True
# 						break
# 		if not loop:
# 			return None
# 		#move s1 additional 1 step
# 		if not step1:
# 			s1=s1.next
# 		#set s2 from the head
# 		s2=head
# 		#move s1 and s2 at the same time, until they meet
# 		while s1 is not s2:
# 			s1=s1.next
# 			s2=s2.next
# 		return s1

		#you can actually prove that s1 and p will eventually meet in the cycle for sure
		#even we only check the steps2 for p, rather than step1+step2 for p(this method is quick when we only need the cycle True or false)
		# def detectCycle(self, head):
		# """
		# :type head: ListNode
		# :rtype: ListNode
		# """
		# if head is None or head.next is None: return None
		# s1 = head
		# q = head.next
		# loop = False
		# while q is not None:
		# 	s1=s1.next
		# 	q=q.next
		# 	if q is not None and q.next is not None:
		# 	    q=q.next
		# 	    if s1 is q:
		# 	        loop =True
		# 	        break
		# 	else:
		# 	    break
			
		# if not loop:
		# 	return None
		# #move s1 additional 1 step
		# s1=s1.next
		# #set s2 from the head
		# s2=head
		# #move s1 and s2 at the same time, until they meet
		# while s1 is not s2:
		# 	s1=s1.next
		# 	s2=s2.next
		# return s1
		
# class Solution(object):
# 	def detectCycle(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: ListNode
# 		"""
# 		if head is None: return None
# 		slow = quick = head
		
# 		while quick:
# 			quick = quick.next
# 			if quick is None: return None
# 			quick = quick.next
# 			slow = slow.next
# 			if quick is slow: break
		
# 		new = head
# 		while slow:
# 			if slow is new: return new
# 			slow = slow.next
# 			new = new.next
		
		
	
# 143. Reorder List My Submissions Question
# Total Accepted: 55720 Total Submissions: 254913 Difficulty: Medium
# Given a singly linked list L: L0 L1 Ln-1 Ln,
# reorder it to: L0 Ln L1 Ln-1 L2 Ln-2
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
# 	def reorderList(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: void Do not return anything, modify head in-place instead.
# 		"""
# 		#because we want inplace, SO(n), we cannot create a new list
# 		#we cut in the middle, reverse the second half, and then move the two list to the end
# 		if head is None or head.next is None: return
# 		count = 0
# 		head1=head
# 		while head is not None:
# 			count+=1
# 			head=head.next
# 		#middle is counting, not indexing
# 		#put the last one in head1, it is easy for coding
# 		middle = (count+1)/2
# 		count=1
# 		# res = ListNode(0)
# 		# res.next = head
# 		head= head1
# 		while count < middle:
# 			#do n times, now head is at the begining of the second half
# 			head=head.next
# 			count += 1
# 		#cut head1's end to None::: this is a possible bug
# 		tmp = head.next
# 		head.next = None
# 		head=tmp

# 		head2=ListNode(0)
# 		head2.next=head
# 		#reverse head2
# 		pre = head2
# 		while head is not None:
# 			tmp=head.next
# 			head.next=pre
# 			pre = head
# 			head=tmp
# 		head2.next.next = None
# 		head2.next = pre
# 		head2=head2.next

# # 		res=ListNode(0)
# # 		head=head1
# 		while head1 is not None and head2 is not None:
# 			tmp1 = head1.next
# 			head1.next=head2
# 			tmp2 = head2.next
# 			head2.next =tmp1
# 			head1=tmp1
# 			head2=tmp2
# 		#no need for change the head, because we return nothing	
# # 		head = head1	
# 		return 
		

# 138. Copy List with Random Pointer My Submissions Question
# Total Accepted: 54702 Total Submissions: 212259 Difficulty: Hard
# A linked list is given such that each node contains an additional random pointer
 # which could point to any node in the list or null.
# Return a deep copy of the list.
# Subscribe to see which companies asked this question
# Show Tags
# Show Similar Problems

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: RandomListNode
#         :rtype: RandomListNode
#         """
#         if head is None: return None
        
#         cur = head
#         while cur:
#             curCopy = RandomListNode(cur.label)
#             tmp = cur.next
#             cur.next = curCopy
#             curCopy.next = tmp
#             cur = tmp
        
#         cur = head
#         while cur:
#             if cur.random:
#                 cur.next.random = cur.random.next
#             cur = cur.next.next
        
#         root = cur = head.next
#         while cur:
#             head.next = head.next.next
#             head = head.next
#             if cur.next is None: break
#             cur.next = cur.next.next
#             cur = cur.next
#         return root




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
# class ListNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None

# class Solution(object):
# 	def reverseKGroup(self, head, k):
# 		"""
# 		:type head: ListNode
# 		:type k: int
# 		:rtype: ListNode
# 		"""
# 		dummy =  ListNode(0)
# 		dummy.next = head
		
# 		cur = probe = head
# 		new = pre = dummy
# 		while True:
# 		    i=1
# 		    while probe and i<=k:
# 		        probe = probe.next
# 		        i += 1
# 		    if i<=k: break
		    
# 		    j=1
# 		    while j<=k:
# 		        tmp = cur.next     
# 		        cur.next = pre
# 		        pre = cur
# 		        cur = tmp
# 		        j+=1
# 		    tmp = new.next
# 		    new.next = pre
# 		    tmp.next = cur
# 		    new = pre = tmp
# 		return dummy.next
# if __name__ == '__main__':
# 	sk=Solution()
# 	node1=ListNode(1)
# 	node2=ListNode(2)
# 	node3=ListNode(3)
# 	node4=ListNode(4)
# 	# node5=ListNode(5)
# 	node1.next=node2
# 	node2.next=node3
# 	node3.next=node4
# 	# node4.next=node5
# 	node = sk.reverseKGroup(node1,2)
# 	while node is not None:
# 		print node.val
# 		node=node.next


# 146. LRU Cache My Submissions Question
# Total Accepted: 58461 Total Submissions: 376255 Difficulty: Hard
# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Subscribe to see which companies asked this question

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.cap = capacity
        self.dict = {}
        self.tail = Node(0, 0)
        self.head = self.tail
        

    def get(self, key):
        """
        :rtype: int
        """
        entry = self.dict.get(key)
        if entry:
            self.renew(entry)
            return entry.val
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            entry = self.dict[key]
            entry.val = value
            self.renew(entry)
        else:
            entry = Node(key, value)
            self.dict[key] = entry
            self.head.pre = entry
            entry.next = self.head
            self.head = entry
            if self.size < self.cap:
                #if the size is still not over cap, add more nodes
                self.size += 1
            else:
                #remove the last node in the double linked list
                lastNode = self.tail.pre
                self.tail.pre = lastNode.pre
                lastNode.pre.next = self.tail
                lastNode.pre = None
                lastNode.next = None
                del self.dict[lastNode.key]
    
    def renew(self, entry):
        if entry is not self.head:
            entry.pre.next = entry.next
            entry.next.pre = entry.pre
            entry.next = self.head
            self.head.pre = entry
            entry.pre = None
            self.head = entry