'''
an implementation of a minimum binary heap
Nate Weeks February 2019
https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82
https://www.geeksforgeeks.org/binary-heap/
'''

class MinHeapVertex:
    def __init__(self, arr):
        self.array = arr

    def buildHeap(self):
        i = len(self.array) // 2 - 1
        while i >= 0:
            self.heapify(i)
            i -= 1
        return self.array

    def heapify(self, i):
        index = i
        leftChild = 2*i + 1;
        rightChild = leftChild + 1;
        maxIndex = len(self.array)
        if leftChild < maxIndex and self.array[leftChild][2] < self.array[index][2]:
            index = leftChild
        if rightChild < maxIndex and self.array[rightChild][2] < self.array[index][2]:
            index = rightChild
        if index != i:
            (self.array[index], self.array[i]) = (self.array[i], self.array[index])
            self.heapify(index)
        return self.array

    def pop(self):
        poppedItem = self.array[0]
        self.array = self.array[1:]
        self.heapify(0)
        return poppedItem

    def percUp(self,i):
        while i > 0:
            if self.array[i][2] < self.array[i // 2][2]:
                tmp = self.array[i // 2]
                self.array[i // 2] = self.array[i]
                self.array[i] = tmp
            i = i // 2

    def push(self, item):
        self.array.append(item)
        self.percUp(len(self.array) - 1)
