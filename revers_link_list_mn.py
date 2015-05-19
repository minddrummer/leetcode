# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        ''''''
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = head
        for i in range(m-1):
            pre = cur
            cur = cur.next
        
        if cur is not None:
            p1 = cur.next
        if p1 is not None:
            p2 = p1.next

        for i in range(n-m):
            p1.next = cur
            cur = p1
            p1 = p2
            if p2 is not None:
                p2 = p2.next

        pre.next.next = p1
        pre.next = cur
            
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
    head = make_lst([1,2,3])
    sk = Solution()
    # print test.val
    # print test.next.val
    # print test.next.next.next.next.val
    head_R = sk.reverseBetween(head,3,3)
    # while head_R is not None:
    #     print head_R.val
    #     head_R  = head_R.next
    print head_R.val
    print head_R.next.val
    print head_R.next.next.val

