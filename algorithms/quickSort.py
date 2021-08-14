import random
import time
# from  App import APP
# Importing colors from colors.py
import App
from colors import *


def partition(arr, low, high, drawData, timeTick):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        col = []
        for x in range(len(arr)):
            if x == j or x == i:
                col.append(YELLOW)
            else:
                col.append(BLUE)
        col[high] = LIGHT_GRAY
        drawData(arr, col)


        time.sleep(timeTick)
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    drawData(arr, [LIGHT_GRAY if x == i+1 or x == high else BLUE for x in range(len(arr))])
    time.sleep(timeTick)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high, drawData, timeTick):

    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high, drawData,timeTick)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1, drawData, timeTick)
        quickSort(arr, pi + 1, high, drawData, timeTick)
        drawData(arr, [ BLUE for x in range(len(arr))])

