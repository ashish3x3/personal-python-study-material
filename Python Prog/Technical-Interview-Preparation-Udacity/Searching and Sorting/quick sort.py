"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
import random

def shuffle(arr):
    l = len(arr)
    for i in range(l-1, 0, -1):
        j = random.randint(0,i)
        arr[i],arr[j] = arr[j], arr[i]
    return arr

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(arr,low,high):
	''' This will ignore all larger number than pivot from begining, and then when
		it finds first smaller number, it swaps it to the begining of the array and exchange with any lager number it ignored before. at the end all smaller number will be in the begining till i and all greater than i will be greate than pivot. then it put pivot at i+1 and return i+1 as pivot position
	'''
   i = ( low-1 )         # index of smaller element
   pivot = arr[high]     # pivot

   for j in range(low , high):

       # If current element is smaller than or
       # equal to pivot
       if   arr[j] <= pivot:

           # increment index of smaller element
           i = i+1
           arr[i],arr[j] = arr[j],arr[i]

   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def partion_arrray(alist, first, last):
	'''
	It won't work if you set pivot as last element to this function.i.e pivot = alist[last] and rightmark = last-1..Nedd to find out why
	'''
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done= True
       else:
           #temp = alist[leftmark]
           #alist[leftmark] = alist[rightmark]
           #alist[rightmark] = temp
           alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

   #temp = alist[first]
   #alist[first] = alist[rightmark]
   #alist[rightmark] = temp
   alist[rightmark], alist[first] = alist[first], alist[rightmark]

   return rightmark

def partition(alist,first,last):
   #shuffle(alist)
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def swap(arr, i, j):

    print i,j,arr
    arr[i],arr[j] = arr[j], arr[i]

def quicksort(array):
    quickSortHelper(array, 0, len(array)-1)
    print array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)