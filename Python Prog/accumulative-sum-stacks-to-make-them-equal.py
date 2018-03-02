# https://www.hackerrank.com/challenges/equal-stacks/problem

from collections import deque

'''
Create another array that contains the heights of all the stacks. This is so we don't have to repeatedly sum the blocks in the stacks.

While the stacks don't all have the same height compute the maximum height, find the index of the elem in heights that has that value then pop off the first elem in the corresponding stack and subtract from the height stored in heights array.

'''

m = map(int, input().strip().split(' '))

def ret_queue():
    return deque(int(i) for i in input().strip().split(' '))

s1 = ret_queue()
s2 = ret_queue()
s3 = ret_queue()

#print(s1,s2,s3)

stack = [s1,s2,s3]
height = [sum(s1),sum(s2),sum(s3)]

#print(stack)
#print(height)

def all_same():
    return height[0] == height[1] == height[2]


while not all_same():
    max_ht = height.index(max(height))
    #print(max_ht)
    #print(height[max_ht], stack[max_ht])
    height[max_ht]-= stack[max_ht].popleft()
    
print(height[0])
    
    
    
    
'''
from collections import deque

def read_queue():
    return deque(map(int, input().strip().split()))

nstacks = len(input().split())
stacks = [read_queue() for i in range(nstacks)]
heights = list(map(sum, stacks))

while len(set(heights)) > 1:
    ihighest = heights.index(max(heights))
    heights[ihighest] -= stacks[ihighest].popleft()

print(heights[0])

'''
    
    
    
    
    
    
    
    