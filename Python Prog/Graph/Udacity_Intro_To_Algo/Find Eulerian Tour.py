# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

from collections import defaultdict

class Graph:
	def __init__(self, graph_list):
		self.graph = defaultdict(list)
		self.vertex = 0
		self.convert_graph(graph_list)

	def convert_graph(self, graph_list):
		known_vertex = set()
		cnt = 0
		for k, v in graph_list:
			if k not in known_vertex:
				known_vertex.add(k)
				cnt+=1
			if v not in known_vertex:
				known_vertex.add(v)
				cnt+=1
			self.addEdge(k, v)
		self.vertex = cnt
		# print(self.vertex)

	def addEdge(self, u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def DFSCount(self, v, visited):
		count = 1
		visited[v] =True
		for i in self.graph[v]:
			if visited[i] == False:
				count = count + self.DFSCount(i,visited)
		return count

	def removeEdge(self, u,v):
		# remove u from graph[v] and v from graph[u]
		for i, k in enumerate(self.graph[u]):
			if k == v:
				self.graph[u].pop(i)

		for i, k in enumerate(self.graph[v]):
			if k == u:
				self.graph[v].pop(i)

	def isValidNextEdge(self, u,v):
		# The edge u-v is valid in one of the following two cases:
		# If v is the only adjacent vertex of u
		if len(self.graph[u]) == 1:
			return True
		else:
			visited = [False]*(self.vertex+1)
			cnt = self.DFSCount(u, visited)
			# Remove edge (u, v) and after removing the edge, count vertices reachable from u
			self.removeEdge(u,v)
			visited = [False]*(self.vertex+1)
			cnt2 = self.DFSCount(u, visited)
			# Add the edge back to the graph
			self.addEdge(u, v)
			return False if cnt > cnt2 else True

	def print_graph(self):
		print(self.graph)

	def printEulerUtil(self, u, final_tour):
		# print('printEulerUtil ', u, final_tour)
		# Recur for all the vertices adjacent to this vertex
		# print('self.graph[u] ',self.graph[u])
		final_tour.append(u)
		# print('final tour ', final_tour)
		for v in self.graph[u]:
			# print('v n self.graph ', v)
			if self.isValidNextEdge(u,v):
				# print("... %d %d " %(u,v))
				# final_tour.append(u)
				#print('final tour ', final_tour)
				self.removeEdge(u,v)
				self.printEulerUtil(v, final_tour)

	def printEulerTour(self, final_tour, initial_u):
		# print(initial_u)
		u = initial_u
		# print('printEulerTour')
		# find the first odd degree vertex vertex
		for i in range(self.vertex):
			if len(self.graph[i]) %2 != 0:
				u = i
				break
		print("\n")
		self.printEulerUtil(u, final_tour)

def find_eulerian_tour(graph_list):
	graph = Graph(graph_list)
	#graph.print_graph()
	#graph.find_eulerian_tour()
	initial_u = graph_list[0][0]
	# print('initial_u ',initial_u)
	final_tour = []
	graph.printEulerTour(final_tour, initial_u)
	# your code here
	# find first odd degree node else 0
	# start from odd degree node check if any adjacent traversal is possible
		# u-v is possible if u-v has one path
		# if multiple path, check if u-v is non bridge
			# u-v is bridge if number of node reachable from u == number of node reachable from u after removing edge u-v . DFS will do
	# if u-v traversal is possible , add u-v to tour and remove edge u-v and move to v
	# repeat same for v
	return final_tour

graph_list = [(1, 2), (2, 3), (3, 1)]
res = find_eulerian_tour(graph_list)
print(res) # [1, 2, 3, 1]

graph_list = [(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
res = find_eulerian_tour(graph_list)
print(res) # [0, 1, 6, 3, 7, 1, 5, 4, 8, 9, 5, 2, 4, 0]

graph_list = [(1, 13), (1, 6), (6, 11), (3, 13),(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),(7, 14),  (10, 13)]
res = find_eulerian_tour(graph_list)
print(res) # [1, 13, 3, 2, 6, 1, 12, 4, 11, 6, 9, 7, 14, 5, 9, 8, 13, 10, 6, 0, 1]

graph_list = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
res = find_eulerian_tour(graph_list)
print(res) # [8, 16, 17, 3, 4, 12, 6, 5, 13, 17, 10, 1, 8, 18, 19, 2, 11, 14, 3, 18, 0, 1, 9, 7, 15, 13, 8]


'''
FAILURE: Test case input: [(1, 2), (2, 3), (3, 1)].


            Expected result: ...
FAILURE: Test case input: [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)].


            Expected result: ...
FAILURE: Test case input: [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)].


            Expected result: ...
FAILURE: Test case input: [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)].

'''