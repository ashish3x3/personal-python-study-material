
from collections import OrderedDict

class LRUCache(object):
	"""docstring for LRUCache"""
	def __init__(self, size):
		self.cache = OrderedDict()
		self.size = size

	def printCache(self):
		print self.cache

	def get(self,key):
		try:
			val = self.cache.pop(key)
			self.cache[key] = val
			return val
		except KeyError:
			return -1

	def put(self, key, val):
		try:
			self.cache.pop(key)
		except KeyError:
			print len(self.cache)
			if len(self.cache) >= self.size:
				self.cache.popitem(last=False)
		self.cache[key] = val


cache = LRUCache(3)
cache.put('a',2)
cache.printCache()
cache.put('b',3)
cache.printCache()
cache.put('c',4)
cache.printCache()
cache.put('d',5)
cache.printCache()

cache.put('e',85)
cache.printCache()

print cache.get('a')
print cache.get('c')
print cache.get('d')
cache.printCache()
cache.put('f',85)
cache.printCache()



'''
OrderedDict([('a', 2)])
OrderedDict([('a', 2), ('b', 3)])
OrderedDict([('a', 2), ('b', 3), ('c', 4)])
OrderedDict([('b', 3), ('c', 4), ('d', 5)])
OrderedDict([('c', 4), ('d', 5), ('e', 85)])
-1
4
5
OrderedDict([('e', 85), ('c', 4), ('d', 5)])
OrderedDict([('c', 4), ('d', 5), ('f', 85)])

'''