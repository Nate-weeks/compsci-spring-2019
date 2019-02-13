'''implementation of heap sort using binary-heap object
Nate Weeks February 2019
>>> heapsort([4,6,8,4,9,6,78,32])
[4, 4, 6, 6, 8, 9, 32, 78]
'''

from minheap import MinHeap

def heapsort(arr):
    heap = MinHeap(arr)
    heap.buildHeap()
    sortedArray = []
    while heap.array != []:
        sortedArray.append(heap.pop())
    return sortedArray

def main():
    print(heapsort([4,6,8,4,9,6,78,32]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
