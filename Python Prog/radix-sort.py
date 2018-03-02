
from collections import defaultdict
import collections

def radix_sort(arr, mod):
    arr2 = defaultdict(list)
    for num in arr:
        #print(num,mod)
        idx = (num/mod)%10
        #print(idx)
        arr2[idx].append(num)
        #print(arr2)
        
    return form_array(arr2)

def form_array(arr2):
    arr = []
    keylist = arr2.keys()
    keylist.sort()
    #od = collections.OrderedDict(sorted(arr2.items()))
    for key in keylist:
        for x in arr2[key]:
            arr.append(x)
    #print('return arr ',arr)
    return arr
    
def radixSort(arr):
    mx = max(arr)
    exp = 1
    while (mx/exp) > 0:
        arr = radix_sort(arr, exp)
        exp*=10
    return arr
    
#arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
arr = map(int, raw_input().strip().split(' '))
arr = radixSort(arr)
print(arr)





'''

(26, 1)
6
defaultdict(<type 'list'>, {6: [26]})
(75, 1)
5
defaultdict(<type 'list'>, {5: [75], 6: [26]})
(1, 1)
1
defaultdict(<type 'list'>, {1: [1], 5: [75], 6: [26]})
(44, 1)
4
defaultdict(<type 'list'>, {1: [1], 4: [44], 5: [75], 6: [26]})
(254, 1)
4
defaultdict(<type 'list'>, {1: [1], 4: [44, 254], 5: [75], 6: [26]})
(14, 1)
4
defaultdict(<type 'list'>, {1: [1], 4: [44, 254, 14], 5: [75], 6: [26]})
(9, 1)
9
defaultdict(<type 'list'>, {1: [1], 4: [44, 254, 14], 5: [75], 6: [26], 9: [9]})
(25, 1)
5
defaultdict(<type 'list'>, {1: [1], 4: [44, 254, 14], 5: [75, 25], 6: [26], 9: [9]})
(7, 1)
7
defaultdict(<type 'list'>, {1: [1], 4: [44, 254, 14], 5: [75, 25], 6: [26], 7: [7], 9: [9]})
(35, 1)
5
defaultdict(<type 'list'>, {1: [1], 4: [44, 254, 14], 5: [75, 25, 35], 6: [26], 7: [7], 9: [9]})
('return arr ', [1, 44, 254, 14, 75, 25, 35, 26, 7, 9])
(1, 10)
0
defaultdict(<type 'list'>, {0: [1]})
(44, 10)
4
defaultdict(<type 'list'>, {0: [1], 4: [44]})
(254, 10)
5
defaultdict(<type 'list'>, {0: [1], 4: [44], 5: [254]})
(14, 10)
1
defaultdict(<type 'list'>, {0: [1], 1: [14], 4: [44], 5: [254]})
(75, 10)
7
defaultdict(<type 'list'>, {0: [1], 1: [14], 4: [44], 5: [254], 7: [75]})
(25, 10)
2
defaultdict(<type 'list'>, {0: [1], 1: [14], 2: [25], 4: [44], 5: [254], 7: [75]})
(35, 10)
3
defaultdict(<type 'list'>, {0: [1], 1: [14], 2: [25], 3: [35], 4: [44], 5: [254], 7: [75]})
(26, 10)
2
defaultdict(<type 'list'>, {0: [1], 1: [14], 2: [25, 26], 3: [35], 4: [44], 5: [254], 7: [75]})
(7, 10)
0
defaultdict(<type 'list'>, {0: [1, 7], 1: [14], 2: [25, 26], 3: [35], 4: [44], 5: [254], 7: [75]})
(9, 10)
0
defaultdict(<type 'list'>, {0: [1, 7, 9], 1: [14], 2: [25, 26], 3: [35], 4: [44], 5: [254], 7: [75]})
('return arr ', [1, 7, 9, 14, 25, 26, 35, 44, 254, 75])
(1, 100)
0
defaultdict(<type 'list'>, {0: [1]})
(7, 100)
0
defaultdict(<type 'list'>, {0: [1, 7]})
(9, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9]})
(14, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14]})
(25, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25]})
(26, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25, 26]})
(35, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25, 26, 35]})
(44, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25, 26, 35, 44]})
(254, 100)
2
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25, 26, 35, 44], 2: [254]})
(75, 100)
0
defaultdict(<type 'list'>, {0: [1, 7, 9, 14, 25, 26, 35, 44, 75], 2: [254]})
('return arr ', [1, 7, 9, 14, 25, 26, 35, 44, 75, 254])
[1, 7, 9, 14, 25, 26, 35, 44, 75, 254]

'''