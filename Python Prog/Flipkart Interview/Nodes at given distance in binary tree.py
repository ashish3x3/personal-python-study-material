
class Node(object):
	"""docstring for ClassName"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right =None
		self.parent = None
		self.visited = False

class KDistance(object):
	"""docstring for ClassName"""

	def __init__(self, root=None):
		self.root = root
		self.target = None
		self.k = -1
		# print root.left.val,root.right.val

	def findTarget(self,target, k):
		self.k = k
		# self.target = self._findTarUtil(target,self.root)
		# print self.target
		self.printKCloseNode(target,self.k)

	def printKCloseNode(self, root, k):
		# print root.val,k
		# if root != None:
			# print root, root.val, k
		if root == None or root.visited == True:
			return
		root.visited = True
		if k != 0:
			self.printKCloseNode(root.left, k-1)
			self.printKCloseNode(root.right, k-1)
			self.printKCloseNode(root.parent, k-1)
		else:
			print root.val,
			# root.visited = False
			return


	def _findTarUtil(self, t,root):
		if root:
			# self.node = root
			# print self.node, t, self.node == t, self.node.val
			print root.val,
			if root == t:
				print 'Found'
				return root
			# print 'going left', self.node.left
			self._findTarUtil(t,root.left)
			# print 'going right', self.node.right
			self._findTarUtil(t,root.right)

	# A function to do postorder tree traversal
	def printPreorder(self,root,t):

	    if root:

	        # First print the data of node
	        print(root.val),
	        if root == t:
	        	print 'found'
	        	return root

	        # Then recur on left child
	        self.printPreorder(root.left,t)

	        # Finally recur on right child
	        self.printPreorder(root.right,t)


a20 = Node(20)
a8  =  Node(8)
a22 =  Node(22)
a4  =  Node(4)
a12 =  Node(12)
a10 =  Node(10)
a14 =  Node(14)

a20.left = a8
a20.right = a22
a20.parent = None

a8.left = a4
a4.parent = a8
a8.right = a12
a12.parent = a8
a8.parent = a20
a22.parent = a20

a12.left = a10
a10.parent  =a12
a12.right = a14
a14.parent = a12


k = KDistance(a20)
# k.printPreorder(a20,a14)
# k.findTarget(a14, 3)
k.findTarget(a10, 4)

