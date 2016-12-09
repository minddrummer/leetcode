# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} n
	# @return {ListNode}
	def count_head_order(self, head, n):
		'''this fucntion counting the x-th node from the head if it is n-th node from the end'''
		if head is None:
			return None
		i = 1
		while head.next is not None:
			head = head.next
			i += 1
		if i == 1:
			return None
		return (i - n + 1)

	def removeNthFromEnd(self, head, n):
		'''remove the nth node from the end counting'''
		'''the key??the node is existing object, and so is the node.next, and change the chain will transfer to the beginning node
		since the head.next node would point to the same object for the pre.Node(if it hasnot been changed!)'''
		nh = self.count_head_order(head,n)
		if nh is None:
			return None
		#method 1
		# dummy = ListNode(0)
		# dummy.next = head
		# pre = dummy
		# cur = pre.next
		# curNext = cur.next
		# for i in range(nh - 1):
		# 	pre = pre.next
		# 	cur = pre.next
		# 	curNext = cur.next
		# #remove the nh-th node
		# pre.next = curNext

		# return dummy.next

		#method 2
		if nh == 1:
			return head.next
		cur = head
		for i in range(nh - 2):
			cur = cur.next
		#remove the nh-th node
		pre = cur
		cur =  cur.next
		curNext = cur.next
		pre.next = curNext

		return head



def make_lst(lst):
	head = None
	node_lst = []
	for i in range(len(lst)):   
		#print i
		if i == 0:
			node_lst.append(ListNode(lst[i]))
			node_lst.append(ListNode(lst[i+1]))
			cur_node = node_lst[i]
			cur_node.next = node_lst[i+1]
		elif i < (len(lst)-1):
			node_lst.append(ListNode(lst[i+1]))
			cur_node = node_lst[i]
			cur_node.next = node_lst[i+1]
		elif i == (len(lst)-1):
			node_lst[i-1].next = node_lst[i]
		
	head = node_lst[0]
	return head




if __name__ == '__main__':
	#test1
	head0 = ListNode(1)
	test = Solution()
	print test.count_head_order(head0, 1)
	removehead = test.removeNthFromEnd(head0, 1)
	while removehead is not None:
		print removehead.val
		removehead = removehead.next
	#test2
	head = make_lst([1,2])
	print test.count_head_order(head,2)
	removehead = test.removeNthFromEnd(head, 2)
	while removehead is not None:
		print removehead.val
		removehead = removehead.next    



