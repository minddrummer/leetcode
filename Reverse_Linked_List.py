# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseList(self, head):
		if head is None or head.next is None:
			return head

		cur_node = head 
		next_node = head.next
		head.next = None
		while next_node is not None:
			#first make the loop_node as the next-next node
			loop_node = next_node.next
			#then link the next_node to the cur_node
			next_node.next = cur_node
			#then make the cur_node as the next_node
			cur_node = next_node
			#last, make the current next node as the next-next node
			next_node = loop_node
			#move on to the next loop, judging again whether the next_node now is None or not.
		#after the while loop, make the head as the cur_node and return it
		head = cur_node
		return head

if __name__ == '__main__':
	test = make_lst([1,2,3,4,5])
	# print test.val
	# print test.next.val
	# print test.next.next.next.next.val
	head1 = ListNode(1)
	head1.next = ListNode(2)

	cur_node = head1
	next_node = head1.next
	#this refers to the head1 object in the memory, and change of head1.next is changing the attributes of head1(and also cur_node), 
	#but not the next_node, which points to ListNode(2)----this is huge
	head1.next = None
	print cur_node.val
	print next_node.val
	print head1.next
	print next_node.val
	print cur_node.val
	print head1.val
	print cur_node.next
	print next_node.next





