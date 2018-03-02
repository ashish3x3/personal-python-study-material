


class Node(object):
 	def __init__(self, val):
 		self.val = val
 		self.next = None

class Solution:

 	def __init__(self, head=None):
 		self.head = head

 	def addElemFront(self, val):
 		newNode = Node(val)
 		newNode.next = self.head
 		self.head = newNode

 	def addElemEnd(self,val):
 		self.ptr = self.head
 		self.prev = self.head
 		while self.ptr != None:
 			self.prev = self.ptr
 			self.ptr = self.ptr.next
 		newNode = Node(val)
 		self.prev.next = newNode

 	def delElem(self, front=True):
 		slef.ptr = self.head
 		self.head = self.head.next
 		self.ptr.next = None

 	def printList(self):
 		self.ptr = self.head
 		while self.ptr != None:
 			print self.ptr.val,
 			self.ptr = self.ptr.next
 		print '\n'

 	def findLongestPath(self, list1, list2):
 		self.prev1 = self.prev2 = None
 		self.next1 = self.next2 = None
 		sum1 = sum2 = 0

 		self.next1 = list1
 		self.prev1 = list1
 		self.next2 = list2
 		self.prev2 = list2

 		finalSum = 0
 		self.headOfFinalPath = None

 		while self.next1!=None or self.next2 != None:

 			while self.next1!=None and self.next2 != None and self.next1.val != self.next2.val:
	 			if self.next1.val < self.next2.val:
	 				self.sum1 += self.next1.val
	 				self.next1 = self.next1.next
	 			elif self.next1.val > self.next2.val:
	 				self.sum2 += self.next2.val
	 				self.next2 = self.next2.next
 			else:
 				if sum1 > sum2:
 					finalSum += sum1
 				else:
 					finalSum += sum2

 				if self.prev1 == list1 and self.prev2 == list2:
 					if sum1 > sum2:
 						self.headOfFinalPath = self.prev1
 					else:
 						self.headOfFinalPath = self.prev2
 				else:

 					if sum1 > sum2:
 						# we do this step bcz in case final path starts from other than this route head, we know from this prev we have to go to other route and not follow the same route... like 3,4,5,33 ... we can traverse 3-4-5 if this is longest path but for other route
 										   8,2,5,12 we know we have to move to route with 33,,so 5 will point to 33..so that when traversing it will be 8-2-5-33..i.e we nw we have to change route in case oher route came out to be significat one. we do it for fail safe
 						self.prev2 = self.prev1.next
 					else:
 						self.prev1 = self.prev2.next

 				sum1 = sum2 = 0
 				self.next1 = self.next1.next
 				self.next2 = self.next2.next


list1 = Node(1)
sol = Solution(list1)
sol.addElemEnd(3)
sol.addElemEnd(30)
sol.addElemEnd(90)
sol.addElemEnd(120)
sol.addElemEnd(240)
sol.addElemEnd(511)
sol.printList()


list2 = Node(0)
sol = Solution(list2)
sol.addElemEnd(3)
sol.addElemEnd(12)
sol.addElemEnd(32)
sol.addElemEnd(90)
sol.addElemEnd(125)
sol.addElemEnd(240)
sol.addElemEnd(511)
sol.printList()





























