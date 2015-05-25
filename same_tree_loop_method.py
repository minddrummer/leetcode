# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def depth(self,root):
    	if root is None:
    		return 0
    	else:
    		return max(self.depth(root.right), self.depth(root.left))+1

    def isSameTree(self, p, q):

    	if self.depth(p) != self.depth(q):
    		return False
    	else:
    		is_same = True
    		d = self.depth(p)

    		node_lst_p = [p]
    		node_lst_q = [q]
    		for i in range(d):
    			new_node_lst_p = []
    			new_node_lst_q = []
    			if len(node_lst_q) != len(node_lst_q):
    				is_same = False
    				break
    			else:
    				num_node = len(node_lst_p)
    				for node_idx in range(num_node):
    					if node_lst_p[node_idx].val != node_lst_q[node_idx].val:
    						is_same = False
    						break
    					#first has to check structure, and then add the node to the new_node_lst
    					elif node_lst_p[node_idx].right is None and node_lst_q[node_idx].right is None:
    						pass
    					elif node_lst_p[node_idx].right is not None and node_lst_q[node_idx].right is not None:
    						new_node_lst_p.append(node_lst_p[node_idx].right)
    						new_node_lst_q.append(node_lst_q[node_idx].right)
    					elif node_lst_p[node_idx].left is None and node_lst_q[node_idx].left is None:
    						pass
    					elif node_lst_p[node_idx].left is not None and node_lst_q[node_idx].left is not None:
    						new_node_lst_p.append(node_lst_p[node_idx].left)
    						new_node_lst_q.append(node_lst_q[node_idx].left)
    					else:
    						is_same = False
    						break

    				if is_same:
    					node_lst_p = new_node_lst_p
    					node_lst_q = new_node_lst_q
    				else:
    					break
    		return is_same







if __name__ == '__main__':
	n0 = TreeNode(0)
	n1 = TreeNode(1)
	n9 = TreeNode(9)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n0.left = n1
	n0.right = n9
	n1.right = n2
	n2.left = n3
	n00 = n0
	test = Solution()
	print test.depth(n0)
	print test.depth(n00)
	#print test.depth(n3)
	print test.isSameTree(n0, n1)

