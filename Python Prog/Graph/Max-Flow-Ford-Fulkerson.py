
# Code
# http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

# Explanation 4 part series
# https://www.youtube.com/watch?v=PY0LL_-jqa0

# Graph class
	# __init__
	# bfs
	# ford fulkerson

#graph initialization matrix
# object instantiation
# call ford fulkerson

'''
Ford fulkerson Algo
1. Find augmenting path from S to T
2. Find resedual capacity ..bottlenack link
3. Then transfer that much(resedual capacity) flow from S to T along that augmenting path
4. Then create resedual graph from current flow network and repeat steps 1-4 till no more path




Resedual graph
It tells how much capacity is left in the network also creates the back edge with transferred flow
In finding augmenting path we consoder both forwrd edges and backward edges (in DFS ) to fnd path from S to T i.e we use the resedual graph to find the path

Also in some case bcz of our first choice we may not have enough capacity in a link in next apth, so in that case we can borrwo from the previous path
-- in such case we make an anti-parallel edge in opposite direction with the flow we transfered in previous path

'''
class Graph:
	def __init__(self, graph):
		self.graph = graph
		self.ROW = len(self.graph)
		self.COL = len(self.graph[0])

	def bfs(self,s, t, parent): # O(V^2)
		# mark all visited as False
		visited = [False]*self.ROW

		# create queue for BFS
		queue = []

		queue.append(s)
		visited[s] = True

		while len(queue) != 0: # O(v) in worst case each vertes will be queued atleast once
			u = queue.pop(0)

			# get all the adjacent nodes for u
			for ind, val in enumerate(self.graph[u]): # O(V) max V-1 vertes this node can be connected to

				# if the next node is not visited and there is a positive flow from u to v
				if visited[ind] == False and self.graph[u][ind] > 0:
					visited[ind] = True # mark the node visited
					parent[ind] = u # add previous node as parent of this node
					queue.append(ind) # add this node to queue

		return True if visited[t] == True else False

	def ford_fulkerson(self, s, t): # dfs = O(V^2) * finding resedual capacity = O(V) => # O(V^3)
		parent = [-1]*self.ROW
		max_flow = 0

		while self.bfs(s, t, parent): # find augmenting path # O(V^2)

			# print path
			v = t  # v = destination
			while v != s: # not equal to source s   # O(V)
				print parent[v], '-->', v, graph[parent[v]][v]  # graph[parent[v]][v] PRINTS THE LINK WEIGHT FROM PARENT[V] --> V
				v = parent[v]

			# find the resedual capacity
			res_flow = float('inf')
			v = t
			while v != s:  # O(V)
				res_flow = min(res_flow, self.graph[parent[v]][v])
				print res_flow
				v = parent[v]

			max_flow+= res_flow

			# update resedual graph along that path and also add back edges
			v = t
			while v != s: # O(V)
				self.graph[parent[v]][v]-= res_flow
				self.graph[v][parent[v]]+= res_flow
				v = parent[v]
		return max_flow



graph = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]];
ff = Graph(graph)
# parent  = [-1]*len(graph)
# print ff.bfs(0,5,parent)
# print parent
# v = 5  # v = destination
# while v != 0: # not equal to source s
# 	print parent[v], '-->', v, graph[parent[v]][v]
# 	v = parent[v]
# print 0

source = 0
sink = 5
print ff.ford_fulkerson(source, sink)


'''
3 --> 5 20
1 --> 3 12
0 --> 1 16
20
12
12
4 --> 5 4
2 --> 4 14
0 --> 2 13
4
4
4
3 --> 5 8
4 --> 3 7
2 --> 4 10
0 --> 2 9
8
7
7
7
23
'''

'''
True
[-1, 0, 0, 1, 2, 3]
3 --> 5 20
1 --> 3 12
0 --> 1 16
0
'''




