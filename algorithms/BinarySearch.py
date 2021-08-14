# We need the time module to create some time difference between each comparison
import random
import time
# from  App import APP
# Importing colors from colors.py
import App
from colors import *


def Binary_Search(data, drawData, timeTick,canvas2):
    size = len(data)
    flag = random.choice([1,2])
    if flag == 1:
        key = random.choice(data)
    else:
        key = random.randint(10,150)

    low = 0
    high = len(data) - 1
    data = sorted(data)
    flag = 0
    while(low <= high):
        mid = int((high + low) / 2)

        drawData(data, [YELLOW if x == mid else BLUE for x in range(len(data))])
        canvas2.create_rectangle(100, 50, 300, 100, fill=YELLOW)
        canvas2.create_text(((100 + 300) / 2, (50 + 100) / 2), text="Key = " + str(key))
        canvas2.update()
        time.sleep(timeTick)
        if(data[mid] == key):
            flag = 1
            break
        elif(data[mid] > key):
            high = mid - 1
        else:
            low = mid + 1
    if flag == 1:
        drawData(data, [LIGHT_GRAY if x == mid else BLUE for x in range(len(data))])

        canvas2.create_rectangle(100, 50, 300, 100, fill=YELLOW)
        canvas2.create_text(((100 + 300) / 2, (50 + 100) / 2), text="Key = " + str(key) + " Found at Pos "+ str(mid + 1) )
        canvas2.update()
    else:
        drawData(data, [BLUE for x in range(len(data))])

        canvas2.create_rectangle(100, 50, 300, 100, fill=YELLOW)
        canvas2.create_text(((100 + 300) / 2, (50 + 100) / 2), text="Key = " + str(key) + " Not Found")
        canvas2.update()


