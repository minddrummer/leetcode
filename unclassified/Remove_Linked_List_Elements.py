# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
    	pre = ListNode(0)
    	pre.next = head
    	dummy = pre
    	if head is None:
    		return None
    	while head is not None:
    		if head.val == val:
    			head = head.next
    			pre.next = head
    		else:
    			pre = head
    			head = head.next
    	return dummy.next

   


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
    head = make_lst([1,2,3,4,5,4])
    test = Solution()
    # print test.val
    # print test.next.val
    print head.next.next.next.val
    head_R = test.removeElements(head,4)
    # while head_R is not None:
    #     print head_R.val
    #     head_R  = head_R.next
    print head_R.next.next.next.val


