
# Python program print Eulerian Trail in a given Eulerian or Semi-Eulerian Graph
# http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/

from collections import defaultdict


class Graph:
	def __init__(self, v):
		self.graph = defaultdict(list)
		self.vertex = v

	def addEdge(self, u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def removeEdge(self, u,v):
		# remove u from graph[v] and v from graph[u]
		for i, k in enumerate(self.graph[u]):
			if k == v:
				self.graph[u].pop(i)

		for i, k in enumerate(self.graph[v]):
			if k == u:
				self.graph[v].pop(i)

	def DFSCount(self, v, visited):
		count = 1
		visited[v] =True
		for i in self.graph[v]:
			if visited[i] == False:
				count = count + self.DFSCount(i,visited)
		return count

	def isValidNextEdge(self, u,v):
		# The edge u-v is valid in one of the following two cases:
		# If v is the only adjacent vertex of u
		if len(self.graph[u]) == 1:
			return True
		else:
			visited = [False]*(self.vertex)
			cnt = self.DFSCount(u, visited)
			# Remove edge (u, v) and after removing the edge, count vertices reachable from u
			self.removeEdge(u,v)
			visited = [False]*self.vertex
			cnt2 = self.DFSCount(u, visited)
			# Add the edge back to the graph
			self.addEdge(u, v)
			return False if cnt > cnt2 else True

	'''
	Method to check if all non-zero degree vertices are
	connected. It mainly does DFS traversal starting from
 	node with non-zero degree
 	'''
	def isConnected(self):
		visited =[False]*(self.V)
		for i in range(self.V):
			if len(self.graph[i]) > 1:
				break
		if i == self.V-1:
			return True
		self.DFSUtil(i,visited)

		for i in range(self.V):
			if visited[i]==False and len(self.graph[i]) > 0:
				return False

		return True

		'''The function returns one of the following values
       0 --> If grpah is not Eulerian
       1 --> If graph has an Euler path (Semi-Eulerian)
       2 --> If graph has an Euler Circuit (Eulerian)  '''
	def isEulerian(self):
		# Check if all non-zero degree vertices are connected
		if self.isConnected() == False:
			return 0
		else:
			#Count vertices with odd degree
			odd = 0
			for i in range(self.V):
				if len(self.graph[i]) % 2 !=0:
					odd +=1

			'''If odd count is 2, then semi-eulerian.
			If odd count is 0, then eulerian
			If count is more than 2, then graph is not Eulerian
 			Note that odd count can never be 1 for undirected graph'''
			if odd == 0:
				return 2
			elif odd == 2:
				return 1
			elif odd > 2:
				return 0

	def printEulerUtil(self, u):
		# Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
			if self.isValidNextEdge(u,v):
				print("%d %d " %(u,v))
				self.removeEdge(u,v)
				self.printEulerUtil(v)

	def printEulerTour(self):
		u = 0
		# find the first odd degree vertex vertex
		for i in range(self.vertex):
			if len(self.graph[i]) %2 != 0:
				u = i
				break
		print("\n")
		self.printEulerUtil(u)

	# Function to run test cases
	def test(self):
		res = self.isEulerian()
		if res == 0:
			 print "graph is not Eulerian"
		elif res ==1 :
			print "graph has a Euler path"
		else:
			print "graph has a Euler cycle"

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

# create graph with adgency list
g1 = Graph(4)
g1.addEdge(0,1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour()

g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.printEulerTour()

g3 = Graph (5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(3, 2)
g3.addEdge(3, 1)
g3.addEdge(2, 4)
g3.printEulerTour()














