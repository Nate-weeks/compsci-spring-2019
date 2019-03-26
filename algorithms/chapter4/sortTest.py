''' sort big random arrays in different amounts of time
Nate Weeks February 2019
'''
import time
import random
from heapsort import heapsort
from bubblesort import bubbleSort

arr = []
for i in range(10000):
    arr.append(random.randint(1, 10000))

bBeginTime = time.time()
bubbleSort(arr)
bEndTime = time.time()

arr = []
for i in range(10000):
    arr.append(random.randint(1, 10000))

hBeginTime = time.time()
heapsort(arr)
hEndTime = time.time()

bubbletime = bEndTime - bBeginTime
heaptime = hEndTime - hBeginTime

print("bubble sort time on 10k items: {}".format(bubbletime))
print("heap sort time on 10k items: {}".format(heaptime))
