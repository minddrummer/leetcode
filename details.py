# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
# Subscribe to see which companies asked this question

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = [] #note that the initialized node will have an empty list!!

# class Solution(object):
# 	def cloneGraph(self, node):
# 		"""
# 		:type node: UndirectedGraphNode
# 		:rtype: UndirectedGraphNode
# 		"""
# 		#use either dfs or bfs
# 		#bfs following
# 		# if node is None: return None
# 		# dct={}
# 		# queue = [node]
# 		# head=node
# 		# #first copy node
# 		# while queue:
# 		#     cur = queue.pop(0)
# 		#     if cur not in dct:
# 		#         for neighbor in cur.neighbors:
# 		#             if neighbor not in dct: queue.append(neighbor)
# 		#         node_new = UndirectedGraphNode(cur.label)
# 		#         node_new.neighbors = cur.neighbors
# 		#         dct[cur] = node_new
# 		# #then copy the neigbors        
# 		# for key in dct:
# 		#     dupnode = dct[key]
# 		#     new_neighbor_lst=[]
# 		#     for neighbor in dupnode.neighbors:
# 		#         new_neighbor_lst.append(dct[neighbor])
# 		#     dupnode.neighbors = new_neighbor_lst
# 		# return dct[head]

# 		#bfs one time, use [] list instead of copy from original node
# 		if node is None: return None
# 		copy = UndirectedGraphNode(node.label) 
# 		dct={}
# 		dct[node] = copy
# 		queue = [node]
# 		head=node

# 		while queue:
# 			cur = queue.pop(0)
# 			for neighbor in cur.neighbors:
# 				if neighbor not in dct: 
# 					copy = UndirectedGraphNode(neighbor.label) 
# 					dct[neighbor] = copy
# 					dct[cur].neighbors.append(copy)
# 					queue.append(neighbor)
# 				else:
# 					dct[cur].neighbors.append(dct[neighbor])
			
			
# 		return dct[head]










