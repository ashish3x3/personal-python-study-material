# create a stack class with push , pop and getMax
# push will add the elem to stack and check if it is greater than the already stored max value
# del will check if max elem is deleted and find parent of max from dict (prevMax->newMax) and make it the new max (getmax return this new max now)

from collections import defaultdict
import sys
f = sys.stdin

class Stack:
	def __init__(self):
		#print(' init called ')
		self.stack = []
		self.parent = defaultdict()
		self.mx = -float('inf')

	def get_max(self):
		return self.mx

	def push(self, elem):
		self.stack.append(elem)
		#print elem
		#print self.stack
		if elem > self.mx:
			if elem in self.parent:
				self.parent[elem].append(self.mx)
			else:
				self.parent[elem] = [self.mx]
			#self.parent[elem] = self.mx
			self.mx = elem


	def pop(self):
		v = self.stack.pop()
		if v == self.mx:
			if(len(self.parent[self.mx]) > 1):
				self.parent[self.mx].pop()
				self.mx = self.parent[self.mx]
			else:
				self.mx = self.parent[self.mx]


stack = Stack()
stack.push(10)
stack.pop()
stack.push(20)
stack.pop()
stack.push(26)
stack.push(20)
stack.pop()
print stack
print stack.get_max() # 26
stack.push(91)
print stack.get_max() # 91

# print '........'
# T = int(f.readline().strip())
# print(T)
#print '........'
#for x in xrange(N):
#	print x

# for _ in xrange(T):
# 	x = f.readline().strip().split(' ')
# 	x = [int(x) for x in x]
# 	if int(x[0]) == 1:
# 		# print 'x0,x1 ',x[0], x[1]
# 		stack.push(x[1])
# 	elif int(x[0]) == 2:
# 		stack.pop()
# 	else:
# 		print(stack.get_max())
