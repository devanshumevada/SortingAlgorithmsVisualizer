import tkinter as tk 
from tkinter import ttk
import random
from algos import bubble_sort, insertion_sort, selection_sort

root = tk.Tk()
root.title('Visualize Sorting Algorithms')
root.maxsize(900, 600)
root.config(bg='black')

selected_algorithm = tk.StringVar()

data = []

# Helper Functions
def generate():
    print(f"Selected Algorithm is {selected_algorithm.get()}")
    try:
        minimum_value = int(minimum_entry.get())
    except:
        minimum_value = 0

    try:
        maximum_value = int(maximum_entry.get())
    except:
        maximum_value = 50

    try:
        size = int(size_entry.get())
    except:
        size = 10

    
    if minimum_value < 0:
        minimum_value = 0

    if maximum_value > 100:
        maximum_value = 100

    if size > 30 or size < 3:
        size = 30

    if minimum_value > maximum_value:
        minimum_value, maximum_value = maximum_value, minimum_value

    global data
    data=[]
    #Resetting Data so that everytime generate button is clicked, new 10 items gets added to the data list not get appended to the list existing before
    for _ in range(size):
        data.append(random.randrange(minimum_value, maximum_value))
    draw_data(data, ['red' for _ in range(len(data))])


def normalize_data(data):
    return [number / max(data) for number in data]


def draw_data(data,color):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 600
    horizontal_width = canvas_width / (len(data) + 1)
    offset = 30 
    spacing = 10
    for i, height in enumerate(normalize_data(data)):
        # Top Left Coordinates

        x0 = i * horizontal_width + offset + spacing
        y0 = canvas_height - height * 350

        #Bottom Right coordinates
        x1 = (i+1) * horizontal_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0 + (horizontal_width/2), y0, anchor=tk.SW, text=str(data[i]))
    root.update()


def start_visualizer():
    if algorithm_selection_dropbox.get() == 'Bubble Sort':
        bubble_sort(data,draw_data,speedScale.get())
    elif algorithm_selection_dropbox.get() == 'Insertion Sort':
        insertion_sort(data, draw_data, speedScale.get())
    elif algorithm_selection_dropbox.get() == 'Selection Sort':
        selection_sort(data, draw_data, speedScale.get())

# Setting up controller group
controller_frame = tk.Frame(root, width=600, height=200, bg='grey')
controller_frame.grid(row=0, column=0, padx=5, pady=5)

# Setting up Canvas for drawing
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=1, column=0, padx=5, pady=5)

# Setting up Controllers for changing various constrains
# Row - 0
tk.Label(controller_frame, text='Selected Algorithm: ', bg='lightgreen' ).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
algorithm_selection_dropbox = ttk.Combobox(controller_frame, textvariable=selected_algorithm, values=['Bubble Sort', 'Insertion Sort','Selection Sort'])
algorithm_selection_dropbox.grid(row=0, column=1, padx=5, pady=5)
algorithm_selection_dropbox.current(0)

tk.Button(controller_frame, text='Generate', command=generate).grid(row=2, column=0, padx=5, pady=5)

# Row - 1
tk.Label(controller_frame, text='Size: ', bg='lightgreen' ).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
size_entry = tk.Entry(controller_frame)
size_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

tk.Label(controller_frame, text='Minimum: ', bg='lightgreen' ).grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
minimum_entry = tk.Entry(controller_frame)
minimum_entry.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)

tk.Label(controller_frame, text='Maximum: ', bg='lightgreen' ).grid(row=1, column=4, sticky=tk.W, padx=5, pady=5)
maximum_entry = tk.Entry(controller_frame)
maximum_entry.grid(row=1, column=5, sticky=tk.W, padx=5, pady=5)

speedScale = tk.Scale(controller_frame,from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=tk.HORIZONTAL, label='Select The Speed')
speedScale.grid(row=0, column=2, padx=3, pady=3)
tk.Button(controller_frame, text='Start',command=start_visualizer ,bg='red').grid(row=0, column=3, padx=3, pady=5)






root.mainloop()