''' bubblesort.py
bubblesort implementation Nate Weeks Feb 2019

>>> bubbleSort([1, 4, 7, 5, 2, 3, 9])
[1, 2, 3, 4, 5, 7, 9]
'''

def bubbleSort(arr):
    lastIndex = len(arr) - 1
    for i in range(len(arr)):
        swapindex = 0
        for index in range(lastIndex):
            if arr[index] > arr[index+1]:
                swapindex = index+1
                (arr[index], arr[swapindex]) = (arr[swapindex], arr[index])
        if swapindex == 0:
            break
        lastIndex -= 1
    return arr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
