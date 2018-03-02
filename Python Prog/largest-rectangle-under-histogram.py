
'''
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
https://www.hackerrank.com/challenges/largest-rectangle/problem


Largest Rectangular Area in a Histogram | Set 2
4.2
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)



1) Create an empty stack.

2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
……a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).

3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.



'''


#!/bin/python3

import sys

def largestRectangle(h):
    stack = []
    max_area = 0
    max_area_so_far = 0
    i = 0
    while i < len(h):
        #print('len(stack) ',len(stack))
        #if len(stack)!= 0:
            #print('stack[peek] ',h[stack[len(stack)-1]])
        #print('val ',h[i])
        if len(stack) == 0 or h[stack[len(stack)-1]] <= h[i]:
            stack.append(i)
            i+=1
            #print(stack)
        else:
            tp = stack[len(stack)-1]
            #print('tp else ',tp)
            #print('i else ',i)
            stack.pop()
            if len(stack) == 0:
                max_area = h[tp]*(i)
                #print('stack empty max ',max_area)
            else:
                max_area = h[tp]*(i - stack[len(stack)-1] -1)
                #print('else ',max_area)
                
        if max_area > max_area_so_far:
            max_area_so_far = max_area
    while len(stack) != 0:
        
        tp = stack[len(stack)-1]
        #print('tp ',tp)
        #print('idx ',i)
        stack.pop()
        if len(stack) == 0:
            max_area = h[tp]*(i)
            #print('stack empty ',max_area)
        else:
            max_area = h[tp]*(i - stack[len(stack)-1] -1)
            #print('else ',max_area)
                
        if max_area > max_area_so_far:
            max_area_so_far = max_area
    return max_area_so_far

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' '))) #[6, 2, 5, 4, 5, 1, 6]
    result = largestRectangle(h)
    print(result)
