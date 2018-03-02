
from collections import OrderedDict

class LRUCache:
	# init a orderedDict to hold cache in order of insert-delete
	def __init__(self, M):
		self.cache = OrderedDict()
		self.maxSize = M

	# set cache key = value, if key already exist update it and push it to begining
	def set(self, key, value):
		try:
			self.cache.pop(key)
		except:
			print 'in except',len(self.cache),self.maxSize
			if len(self.cache) >= self.maxSize:
				self.cache.popitem(last=False)

		self.cache[key] = value

	# get the key and push it to begining
	def get(self, key):
		try:
			val = self.cache.pop(key)
			self.cache[key] = val
		except:
			pass
		return val

	def printCache(self):
		print self.cache


cache = LRUCache(3)
cache.printCache()

cache.set('a',2)
cache.printCache()

cache.set('b',3)
cache.printCache()

cache.set('c',3)
cache.printCache()

cache.get('a')
cache.printCache()

cache.set('d',3)
cache.printCache()
















