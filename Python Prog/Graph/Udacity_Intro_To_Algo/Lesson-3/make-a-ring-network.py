def make_ring(ring, i, j):
	if i not in ring:
		ring[i] = {}
	ring[i][j] = 1

	if j not in ring:
		ring[j] = {}
	ring[j][i] = 1
	return ring

ring = {}
n = 5
for i in range(n):
	make_ring(ring, i, (i+1)%n)
print(ring) # {0: {1: 1, 4: 1}, 1: {0: 1, 2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1, 4: 1}, 4: {0: 1, 3: 1}}
# print number of edges
cnt = 0
for x,y in ring.iteritems():
	print(x,y)
	cnt+=len(y.keys())
print(cnt//2)
print(sum(len(ring[node]) for node in ring.keys())//2)

'''
(0, {1: 1, 4: 1})
(1, {0: 1, 2: 1})
(2, {1: 1, 3: 1})
(3, {2: 1, 4: 1})
(4, {0: 1, 3: 1})

5

'''