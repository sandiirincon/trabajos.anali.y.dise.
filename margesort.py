import random
import math
import time

def merge(left,right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    else:
        result.extend(right)
    return result

def mergesort(m):
    left = []
    right = []
    result = []
    t1 = time.time()
    if len(m) <=1:
        return m
    middle = len(m)/2

    left = m[:middle]
    right = m[middle:]

    left = mergesort(left)
    right = mergesort(right)

    if left[-1] > right[0]:
        result = merge(left, right)
    else:
        result = left + right
    print time.time()-t1
    return result


p = random.sample(range(30),20)
print p
print mergesort(p)