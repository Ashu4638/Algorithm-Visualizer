from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from  algorithms.insertionSort import insertion_sort
from algorithms.selectionSort import selection_sort
from algorithms.LinearSearch import Linear_search
from algorithms.BinarySearch import Binary_Search
from algorithms.quickSort import quickSort



class APP:
    def __init__(self):
        self.window = Tk()
        self.window.title("Algorithm Visualizer")
        self.window.geometry("1000x600")
        self.window.configure(bg="#ffffff")
        self.algorithm_name = StringVar()
        self.algo_list = ['Bubble Sort', 'Insertion Sort','Selection Sort', 'Merge Sort','Quick Sort','Linear Search', 'Binary Search']

        self.speed_name = StringVar()
        self.speed_list = ['Fast', 'Medium', 'Slow']
        self.data = []
        self.init_gui()
        # self.drawData(self,self.data, self.colorArray)
        # self.generate()
        # self.set_speed()
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
        self.window.resizable(False, False)
        self.window.mainloop()


    def init_gui(self):
        self.canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas2 = Canvas(
            self.window,
            bg = "#321444",
            height =545,
            width = 705,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas2.place(x = 290,y=0)
        self.background_img = PhotoImage(file=f"background.png")
        self.background = self.canvas.create_image(
            500.0, 300.0,
            image=self.background_img)

        self.img0 = PhotoImage(file=f"img0.png")
        self.b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.generate,
            relief="flat")

        self.b0.place(
            x=23, y=183,
            width=121,
            height=38)

        self.img1 = PhotoImage(file=f"img1.png")
        self.b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.sort,
            relief="flat")

        self.b1.place(
            x=161, y=183,
            width=100,
            height=39)

        self.canvas.create_text(
            135.0, 573.5,
            text="Developed by : Ashutosh Koli",
            fill="#ffffff",
            font=("OxygenMono-Regular", int(12.0)))

        self.canvas.create_text(
            567.5, 571.0,
            text="Vishwakarma Institute of Technology, Pune",
            fill="#ffffff",
            font=("Offside-Regular", int(12.0)))

        self.canvas.create_text(
            126.5, 124.0,
            text="Speed",
            fill="#ffffff",
            font=("Oxygen-Bold", int(12.0)))

        self.speed_menu = ttk.Combobox(self.window, textvariable=self.speed_name, values=self.speed_list)
        self.speed_menu.place(x=60, y=140)
        self.speed_menu.current(0)

        self.canvas.create_text(
            131.0, 61.5,
            text="Select Algorithm",
            fill="#ffffff",
            font=("Oxygen-Bold", int(12.0)))
        # UI_frame = Frame(window, width=900, height=300, bg="PURPLE")
        # UI_frame.grid(row=0, column=0, padx=10, pady=5)
        self.algo_menu = ttk.Combobox(self.window, textvariable=self.algorithm_name, values=self.algo_list)
        self.algo_menu.grid(row=0, column=0, padx=60, pady=75)
        self.algo_menu.current(0)

    def drawData(self,data, colorArray):
        self.canvas2.delete("all")
        self.canvas2_width = 705
        self.canvas2_height = 545
        x_width = self.canvas2_width / (len(data) + 1)
        offset = 4
        spacing = 2
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = self.canvas2_height - height * 390
            x1 = (i + 1) * x_width + offset
            y1 = self.canvas2_height
            self.canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            self.canvas2.create_text(((x0 + x1) / 2, (y0 + y1) / 2), text=str(data[i]))

        self.window.update_idletasks()

    def generate(self):
        self.canvas2.delete("all")
        self.data = []
        for i in range(0, 10):
            random_value = random.randint(10, 150)
            self.data.append(random_value)

        self.drawData(self.data, [BLUE for x in range(len(self.data))])

    def set_speed(self):
        if self.speed_menu.get() == 'Slow':
            return 1.0
        elif self.speed_menu.get() == 'Medium':
            return 0.1
        else:
            return 0.001

    def sort(self):

        timeTick = self.set_speed()

        if self.algo_menu.get() == 'Bubble Sort':
            bubble_sort(self.data, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Merge Sort':
            merge_sort(self.data, 0, len(self.data) - 1, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Insertion Sort':
            insertion_sort(self.data, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Selection Sort':
            selection_sort(self.data, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Quick Sort':
            low = 0
            high = len(self.data) - 1
            quickSort(self.data,low, high, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Linear Search':
            Linear_search(self.data, self.drawData, timeTick,self.canvas2)
        elif self.algo_menu.get() == 'Binary Search':
            Binary_Search(self.data, self.drawData, timeTick,self.canvas2)

