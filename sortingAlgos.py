from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import numpy as np
from SortAlgorithm import *

root = Tk()
root.title("Sorting Visualizer")
root.maxsize(1100, 800)
root.config(bg='#bdc3c7')

# variables
selected_alg = StringVar()
# global data array
data=[]
# global sizeVal
sizeVal=30
MainColor = '#34495e'

# warning box
def warningbox(obj, title, msg, val):
    messagebox.showwarning(title=title, message=msg)
    obj.delete(0, "end")
    obj.insert(0, str(val))

# draw data function
def drawData(data, clrArray):
    
    canvas.delete("all")
    c_height = 580
    c_width = 1000
    x_width = c_width / (len(data)+1)
    if sizeVal<=30:
        offset = 10
        spacing=20
    else:
        offset=10
        spacing=10
    normalizedData = [abs(i)/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 540
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=clrArray[i])
        canvas.create_text(x0, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

# generate function
def Generate():
    global data
    global sizeVal

    try:
        minVal = int(minEntry.get())
    except:
        minVal=1
        minEntry.delete(0, "end")
        minEntry.insert(0, minVal)

    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal=100
        maxEntry.delete(0, "end")
        maxEntry.insert(0, maxVal)

    try:
        sizeVal = int(sizeEntry.get())
    except:
        sizeVal=30
        sizeEntry.delete(0, "end")
        sizeEntry.insert(0, sizeVal)

    if sizeVal>50:
        sizeVal=30
        warningbox(sizeEntry, "Size limit exceeded", "Array size too large to be visualized in this window. Replaced with default size", sizeVal)

    if minVal<0:
        minVal=1
        warningbox(minEntry, "Min value too small", "Please input a valid min value less than max. Min will be set to 1", minVal)

    if maxVal>1000: 
        maxVal=1000
        warningbox(maxEntry, "Large max value", "Please input a valid max value greater than min. Max will be set to 1000", maxVal)

    if minVal>=maxVal:
        maxVal = abs(minVal)+2
        warningbox(maxEntry, "Value Error", "Please input a valid max value. A valid max val will be inserted for you", maxVal)

    data = []
    if sizeVal<4:
        sizeVal=20
        warningbox(sizeEntry, "Size value is too small", "We will adjust the size for you for better visualization", sizeVal)
        for _ in range(sizeVal):
            data.append(round(random.uniform(minVal, maxVal),3))
        drawData(data, [MainColor for x in range(len(data))])
    else:
        for _ in range(sizeVal):
            data.append(random.randrange(minVal, maxVal+1))
        drawData(data, [MainColor for x in range(len(data))])

# button hover effect
def on_enter(e):
    sort_button['background'] = '#dff9fb'
    sort_button['foreground'] = '#34495e'

def on_leave(e):
    sort_button['background'] = '#2c3e50'
    sort_button['foreground'] = 'white'


# sorting algorithm function
def sortingAlgo():
    global data

    if algMenu.get()=="Bubble Sort":
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get()=='Selection Sort':
        selection_sort(data, drawData, speedScale.get())
    elif algMenu.get()=='Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())
    else:
        MergeSort(data, drawData, speedScale.get())


# frame/base layout
UI_frame = Frame(root, width=1000, height=200, bg='#34495e')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1000, height=580, bg='#ecf0f1')
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI Area

# Row[0]
Label(UI_frame, text="Algorithm: ", fg="white", bg="#34495e").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.0, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select speed (in sec)")
speedScale.grid(row=0, column=2, padx=10, pady=5)

sort_button = Button(UI_frame, text="Start sorting", fg="white", command=sortingAlgo, bg='#2c3e50')
sort_button.grid(row=0, column=3, padx=5, pady=5, sticky=W)
sort_button.bind('<Enter>', on_enter)
sort_button.bind('<Leave>', on_leave)

# Row[1]
Label(UI_frame, text="Size(limit=50):", fg="white", bg="#34495e").grid(row=1, column=0, padx=5, pady=5,sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min-Val(limit=0):", fg="white", bg="#34495e").grid(row=1, column=2, padx=5, pady=5,sticky=E)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5,sticky=W)

Label(UI_frame, text="Max-Val(limit=1000):", fg="white", bg="#34495e").grid(row=1, column=4, padx=5, pady=5,sticky=E)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=E)

generate_button = Button(UI_frame, text="Generate Array", fg="white", command=Generate, bg='#2c3e50')
generate_button.grid(row=1, column=6, padx=5, pady=5)

root.mainloop()