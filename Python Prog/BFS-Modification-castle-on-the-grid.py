#!/bin/python3

'''
https://www.hackerrank.com/challenges/castle-on-the-grid/problem


get the grid
create the visited count array which stores the value when that specfic cell is first reached
create a queue fro BFS
add first elem
pop elem, check if pooped elem == target elem return the number stored in visited count[x,y]
else increment +1  the value stored in visited_count[x,y]. now whatever is reached from here which is not previosly reached will have it's new inceremented value in its visited_count[x,y]
when doing bfs append all the valid pont to bottom, up, right and left of the current popped cell i.e range[(x+1,n),(x-1, -1, -1), (y+1,n), (y-1,-1,-1)]



3
.X.
.X.
...
0 0 0 2
Sample Output

3

Explanation

Here is a path that one could follow in order to reach the destination in  steps:

00,20,22,02

'''

import sys
from collections import deque

def minimumMoves(grid, visited_count, startx, starty, endx, endy):
    queue = deque([])
    queue.append((startx, starty))
    #print(queue)
    l = len(grid)
    while len(queue) != 0:
        curr = queue.popleft()
        x,y = curr
        #print(x,y)
        if curr == [endx, endy]:
            return visited_count[x][y]
        new_inc_val = visited_count[x][y]+1
        
        # move bottom
        for i in range(x+1,l):
            #print(i,y)
            if grid[i][y] == 'X':
                break
            else:
                if visited_count[i][y] == 0:  # if unvisited cell
                    visited_count[i][y] = new_inc_val
                    queue.append([i,y])
                    
        # move up
        for i in range(x-1,-1,-1):
            if grid[i][y] == 'X':
                break
            else:
                if visited_count[i][y] == 0:  # if unvisited cell
                    visited_count[i][y] = new_inc_val
                    queue.append([i,y])
        
        #move right
        for i in range(y+1,l):
            if grid[x][i] == 'X':
                break
            else:
                if visited_count[x][i] == 0:  # if unvisited cell
                    visited_count[x][i] = new_inc_val
                    queue.append([x,i])
        
        #move left
        for i in range(y-1, -1,-1):
            if grid[x][i] == 'X':
                break
            else:
                if visited_count[x][i] == 0:  # if unvisited cell
                    visited_count[x][i] = new_inc_val
                    queue.append([x,i])

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    #print(grid)
    #print(grid[2][2])
    startx, starty, endx, endy = map(int, input().strip().split(' '))
    visited_count = []
    for _ in range(n):
        visited_count.append([0]*n)
    #print(visited_count)
    res = minimumMoves(grid, visited_count, startx, starty, endx, endy)
    print(res)
    
