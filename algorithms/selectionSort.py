# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *


def selection_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        min = i

        for j in range(i+1, size):
            drawData(data, [LIGHT_GRAY if x == j + 1 else YELLOW if x == min else BLUE for x in range(len(data))])
            time.sleep(timeTick)
            if data[j] < data[min]:
                min = j

        if min != i:
            drawData(data, [LIGHT_GRAY if x == i  else YELLOW if x == min else BLUE for x in range(len(data))])
            time.sleep(timeTick)
            temp = data[min]
            data[min] = data[i]
            data[i] = temp


    drawData(data, [BLUE for x in range(len(data))])