"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def b_search(arr, low,high,val):
    if low>high:
        return -1
    mid = int((high+low)/2)   # mid = (high+low)//2
    if arr[mid]==val:
        return mid
    if arr[mid]>val:
        return b_search(arr,low, mid-1,val)
    else:
        return b_search(arr,mid+1, high,val)

def binary_search(input_array, value):
    """Your code goes here."""
    return b_search(input_array, 0, len(input_array), value)
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

'''
-1
4
'''