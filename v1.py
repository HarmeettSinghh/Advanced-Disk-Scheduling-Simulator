# # # import matplotlib.pyplot as plt
# # # import matplotlib.animation as animation
# # # import numpy as np
# # # from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu

# # # # Sample FCFS algorithm implementation
# # # def fcfs_scheduling(requests, head_start):
# # #     seek_sequence = [head_start] + requests
# # #     seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
# # #     return seek_sequence, seek_time

# # # # Function to animate disk scheduling movements
# # # def animate_disk_movement(seek_sequence):
# # #     fig, ax = plt.subplots()
# # #     ax.set_xlim(0, max(seek_sequence) + 10)
# # #     ax.set_ylim(0, 1)
# # #     ax.set_yticks([])
# # #     ax.set_title("Disk Scheduling Visualization")
# # #     line, = ax.plot([], [], marker='o', linestyle='-')

# # #     def update(frame):
# # #         line.set_data(seek_sequence[:frame+1], [0] * (frame+1))
# # #         return line,
    
# # #     ani = animation.FuncAnimation(fig, update, frames=len(seek_sequence), interval=500, blit=True)
# # #     plt.show()

# # # # GUI Setup
# # # def run_simulation():
# # #     requests = list(map(int, request_input.get().split(',')))
# # #     head_start = int(head_start_input.get())
# # #     algo = selected_algo.get()
    
# # #     if algo == "FCFS":
# # #         seek_sequence, seek_time = fcfs_scheduling(requests, head_start)
# # #         animate_disk_movement(seek_sequence)
# # #         result_label.config(text=f"Total Seek Time: {seek_time}")

# # # root = Tk()
# # # root.title("Disk Scheduling Simulator")

# # # Label(root, text="Disk Requests (comma-separated):").grid(row=0, column=0)
# # # request_input = Entry(root)
# # # request_input.grid(row=0, column=1)

# # # Label(root, text="Initial Head Position:").grid(row=1, column=0)
# # # head_start_input = Entry(root)
# # # head_start_input.grid(row=1, column=1)

# # # Label(root, text="Algorithm:").grid(row=2, column=0)
# # # algo_options = ["FCFS"]
# # # selected_algo = StringVar(root)
# # # selected_algo.set("FCFS")
# # # OptionMenu(root, selected_algo, *algo_options).grid(row=2, column=1)

# # # Button(root, text="Run Simulation", command=run_simulation).grid(row=3, columnspan=2)
# # # result_label = Label(root, text="")
# # # result_label.grid(row=4, columnspan=2)

# # # root.mainloop()



# # import matplotlib.pyplot as plt
# # import matplotlib.animation as animation
# # import numpy as np
# # from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Frame
# # import tkinter as tk

# # # FCFS Algorithm
# # def fcfs_scheduling(requests, head_start):
# #     seek_sequence = [head_start] + requests
# #     seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
# #     return seek_sequence, seek_time

# # # SSTF Algorithm
# # def sstf_scheduling(requests, head_start):
# #     sequence = [head_start]
# #     pending = requests[:]
# #     while pending:
# #         next_request = min(pending, key=lambda x: abs(sequence[-1] - x))
# #         sequence.append(next_request)
# #         pending.remove(next_request)
# #     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
# #     return sequence, seek_time

# # # SCAN Algorithm
# # def scan_scheduling(requests, head_start, disk_size=200, direction="left"):
# #     left = [r for r in requests if r < head_start] + [0]
# #     right = [r for r in requests if r >= head_start] + [disk_size-1]
# #     sequence = ([head_start] + sorted(left, reverse=True) + sorted(right)) if direction == "left" else ([head_start] + sorted(right) + sorted(left, reverse=True))
# #     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
# #     return sequence, seek_time

# # # C-SCAN Algorithm
# # def cscan_scheduling(requests, head_start, disk_size=200):
# #     left = [r for r in requests if r < head_start]
# #     right = [r for r in requests if r >= head_start]
# #     sequence = [head_start] + sorted(right) + [disk_size-1, 0] + sorted(left)
# #     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
# #     return sequence, seek_time

# # # Function to animate disk scheduling movements
# # def animate_disk_movement(seek_sequence):
# #     fig, ax = plt.subplots()
# #     ax.set_xlim(0, max(seek_sequence) + 10)
# #     ax.set_ylim(0, len(seek_sequence))
# #     ax.set_title("Disk Scheduling Visualization")
# #     line, = ax.plot([], [], marker='o', linestyle='-')

# #     def update(frame):
# #         x_data = seek_sequence[:frame+1]
# #         y_data = list(range(len(x_data)))  # Moving Y-Axis for better visualization
# #         line.set_data(x_data, y_data)
# #         return line,
    
# #     ani = animation.FuncAnimation(fig, update, frames=len(seek_sequence), interval=500, blit=True)
# #     plt.show()

# # # GUI Setup with Dark Mode
# # def toggle_theme():
# #     if root.option_get('theme', 'light') == 'light':
# #         root.tk_setPalette(background='#2E2E2E', foreground='white')
# #         theme_button.config(bg='#555', fg='white')
# #     else:
# #         root.tk_setPalette(background='SystemButtonFace', foreground='black')
# #         theme_button.config(bg='SystemButtonFace', fg='black')

# # def run_simulation():
# #     requests = list(map(int, request_input.get().split(',')))
# #     head_start = int(head_start_input.get())
# #     algo = selected_algo.get()
    
# #     if algo == "FCFS":
# #         seek_sequence, seek_time = fcfs_scheduling(requests, head_start)
# #     elif algo == "SSTF":
# #         seek_sequence, seek_time = sstf_scheduling(requests, head_start)
# #     elif algo == "SCAN":
# #         seek_sequence, seek_time = scan_scheduling(requests, head_start)
# #     elif algo == "C-SCAN":
# #         seek_sequence, seek_time = cscan_scheduling(requests, head_start)
# #     else:
# #         result_label.config(text="Invalid Algorithm")
# #         return
    
# #     animate_disk_movement(seek_sequence)
# #     result_label.config(text=f"Total Seek Time: {seek_time}")

# # root = Tk()
# # root.title("Disk Scheduling Simulator")

# # frame = Frame(root)
# # frame.pack(pady=10)

# # Label(frame, text="Disk Requests (comma-separated):").grid(row=0, column=0)
# # request_input = Entry(frame)
# # request_input.grid(row=0, column=1)

# # Label(frame, text="Initial Head Position:").grid(row=1, column=0)
# # head_start_input = Entry(frame)
# # head_start_input.grid(row=1, column=1)

# # Label(frame, text="Algorithm:").grid(row=2, column=0)
# # algo_options = ["FCFS", "SSTF", "SCAN", "C-SCAN"]
# # selected_algo = StringVar(root)
# # selected_algo.set("FCFS")
# # OptionMenu(frame, selected_algo, *algo_options).grid(row=2, column=1)

# # Button(frame, text="Run Simulation", command=run_simulation).grid(row=3, columnspan=2)
# # result_label = Label(frame, text="")
# # result_label.grid(row=4, columnspan=2)

# # theme_button = Button(root, text="Toggle Dark Mode", command=toggle_theme)
# # theme_button.pack(pady=5)

# # root.mainloop()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np
# from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Frame
# import tkinter as tk

# # FCFS Algorithm
# def fcfs_scheduling(requests, head_start):
#     seek_sequence = [head_start] + requests
#     seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
#     return seek_sequence, seek_time

# # SSTF Algorithm
# def sstf_scheduling(requests, head_start):
#     sequence = [head_start]
#     pending = requests[:]
#     while pending:
#         next_request = min(pending, key=lambda x: abs(sequence[-1] - x))
#         sequence.append(next_request)
#         pending.remove(next_request)
#     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
#     return sequence, seek_time

# # SCAN Algorithm
# def scan_scheduling(requests, head_start, disk_size=200, direction="left"):
#     left = [r for r in requests if r < head_start] + [0]
#     right = [r for r in requests if r >= head_start] + [disk_size-1]
#     sequence = ([head_start] + sorted(left, reverse=True) + sorted(right)) if direction == "left" else ([head_start] + sorted(right) + sorted(left, reverse=True))
#     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
#     return sequence, seek_time

# # C-SCAN Algorithm
# def cscan_scheduling(requests, head_start, disk_size=200):
#     left = [r for r in requests if r < head_start]
#     right = [r for r in requests if r >= head_start]
#     sequence = [head_start] + sorted(right) + [disk_size-1, 0] + sorted(left)
#     seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
#     return sequence, seek_time

# # Function to animate disk scheduling movements
# def animate_disk_movement(seek_sequence):
#     fig, ax = plt.subplots()
#     ax.set_xlim(0, max(seek_sequence) + 10)
#     ax.set_ylim(0, len(seek_sequence))
#     ax.set_title("Disk Scheduling Visualization")
#     line, = ax.plot([], [], marker='o', linestyle='-')

#     def update(frame):
#         x_data = seek_sequence[:frame+1]
#         y_data = list(range(len(x_data)))  # Moving Y-Axis for better visualization
#         line.set_data(x_data, y_data)
#         return line,
    
#     ani = animation.FuncAnimation(fig, update, frames=len(seek_sequence), interval=500, blit=True)
#     plt.show()

# # GUI Setup with Dark Mode
# def toggle_theme():
#     global dark_mode
#     dark_mode = not dark_mode
#     if dark_mode:
#         root.config(bg='#2E2E2E')
#         frame.config(bg='#2E2E2E')
#         result_label.config(bg='#2E2E2E', fg='white')
#         theme_button.config(bg='#555', fg='white')
#         for widget in frame.winfo_children():
#             if isinstance(widget, Label) or isinstance(widget, Button):
#                 widget.config(bg='#2E2E2E', fg='white')
#             elif isinstance(widget, Entry):
#                 widget.config(bg='#555', fg='white', insertbackground='white')
#     else:
#         root.config(bg='SystemButtonFace')
#         frame.config(bg='SystemButtonFace')
#         result_label.config(bg='SystemButtonFace', fg='black')
#         theme_button.config(bg='SystemButtonFace', fg='black')
#         for widget in frame.winfo_children():
#             if isinstance(widget, Label) or isinstance(widget, Button):
#                 widget.config(bg='SystemButtonFace', fg='black')
#             elif isinstance(widget, Entry):
#                 widget.config(bg='white', fg='black', insertbackground='black')

# def run_simulation():
#     requests = list(map(int, request_input.get().split(',')))
#     head_start = int(head_start_input.get())
#     algo = selected_algo.get()
    
#     if algo == "FCFS":
#         seek_sequence, seek_time = fcfs_scheduling(requests, head_start)
#     elif algo == "SSTF":
#         seek_sequence, seek_time = sstf_scheduling(requests, head_start)
#     elif algo == "SCAN":
#         seek_sequence, seek_time = scan_scheduling(requests, head_start)
#     elif algo == "C-SCAN":
#         seek_sequence, seek_time = cscan_scheduling(requests, head_start)
#     else:
#         result_label.config(text="Invalid Algorithm")
#         return
    
#     animate_disk_movement(seek_sequence)
#     result_label.config(text=f"Total Seek Time: {seek_time}")

# root = Tk()
# root.title("Disk Scheduling Simulator")
# dark_mode = False

# frame = Frame(root)
# frame.pack(pady=10)

# Label(frame, text="Disk Requests (comma-separated):").grid(row=0, column=0)
# request_input = Entry(frame)
# request_input.grid(row=0, column=1)

# Label(frame, text="Initial Head Position:").grid(row=1, column=0)
# head_start_input = Entry(frame)
# head_start_input.grid(row=1, column=1)

# Label(frame, text="Algorithm:").grid(row=2, column=0)
# algo_options = ["FCFS", "SSTF", "SCAN", "C-SCAN"]
# selected_algo = StringVar(root)
# selected_algo.set("FCFS")
# OptionMenu(frame, selected_algo, *algo_options).grid(row=2, column=1)

# Button(frame, text="Run Simulation", command=run_simulation).grid(row=3, columnspan=2)
# result_label = Label(frame, text="")
# result_label.grid(row=4, columnspan=2)

# theme_button = Button(root, text="Toggle Dark Mode", command=toggle_theme)
# theme_button.pack(pady=5)

# root.mainloop()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from tkinter import ttk

# FCFS Algorithm
def fcfs_scheduling(requests, head_start):
    seek_sequence = [head_start] + requests
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

# SSTF Algorithm
def sstf_scheduling(requests, head_start):
    sequence = [head_start]
    pending = requests[:]
    while pending:
        next_request = min(pending, key=lambda x: abs(sequence[-1] - x))
        sequence.append(next_request)
        pending.remove(next_request)
    seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# SCAN Algorithm
def scan_scheduling(requests, head_start, disk_size=200, direction="left"):
    left = [r for r in requests if r < head_start] + [0]
    right = [r for r in requests if r >= head_start] + [disk_size-1]
    sequence = ([head_start] + sorted(left, reverse=True) + sorted(right)) if direction == "left" else ([head_start] + sorted(right) + sorted(left, reverse=True))
    seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# C-SCAN Algorithm
def cscan_scheduling(requests, head_start, disk_size=200):
    left = [r for r in requests if r < head_start]
    right = [r for r in requests if r >= head_start]
    sequence = [head_start] + sorted(right) + [disk_size-1, 0] + sorted(left)
    seek_time = sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))
    return sequence, seek_time

# Function to animate disk scheduling movements
def animate_disk_movement(seek_sequence, algorithm_name):
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(seek_sequence) + 10)
    ax.set_ylim(0, len(seek_sequence))
    ax.set_title(f"{algorithm_name} Disk Scheduling Visualization")
    ax.set_xlabel("Cylinder Number")
    ax.set_ylabel("Request Order")
    line, = ax.plot([], [], marker='o', linestyle='-')

    def update(frame):
        x_data = seek_sequence[:frame+1]
        y_data = list(range(len(x_data)))
        line.set_data(x_data, y_data)
        return line,
    
    ani = animation.FuncAnimation(fig, update, frames=len(seek_sequence), interval=500, blit=True)
    plt.show()

# GUI Setup
def run_simulation():
    requests = list(map(int, request_input.get().split(',')))
    head_start = int(head_start_input.get())
    algo = selected_algo.get()
    
    if algo == "FCFS":
        seek_sequence, seek_time = fcfs_scheduling(requests, head_start)
    elif algo == "SSTF":
        seek_sequence, seek_time = sstf_scheduling(requests, head_start)
    elif algo == "SCAN":
        seek_sequence, seek_time = scan_scheduling(requests, head_start)
    elif algo == "C-SCAN":
        seek_sequence, seek_time = cscan_scheduling(requests, head_start)
    else:
        result_label.config(text="Invalid Algorithm")
        return
    
    animate_disk_movement(seek_sequence, algo)
    result_label.config(text=f"Total Seek Time: {seek_time}")

def toggle_theme():
    if root.option_get("theme", "") == "dark":
        root.tk.call("set_theme", "light")
    else:
        root.tk.call("set_theme", "dark")

root = tk.Tk()
root.title("Disk Scheduling Simulator")

style = ttk.Style(root)
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

frame = ttk.Frame(root, padding=10)
frame.pack(pady=10)

request_label = ttk.Label(frame, text="Disk Requests (comma-separated):")
request_label.grid(row=0, column=0)
request_input = ttk.Entry(frame)
request_input.grid(row=0, column=1)

head_label = ttk.Label(frame, text="Initial Head Position:")
head_label.grid(row=1, column=0)
head_start_input = ttk.Entry(frame)
head_start_input.grid(row=1, column=1)

algo_label = ttk.Label(frame, text="Algorithm:")
algo_label.grid(row=2, column=0)
algo_options = ["FCFS", "SSTF", "SCAN", "C-SCAN"]
selected_algo = tk.StringVar(root)
selected_algo.set("FCFS")
algo_dropdown = ttk.Combobox(frame, textvariable=selected_algo, values=algo_options, state="readonly")
algo_dropdown.grid(row=2, column=1)

run_button = ttk.Button(frame, text="Run Simulation", command=run_simulation)
run_button.grid(row=3, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, columnspan=2, pady=5)

theme_button = ttk.Button(root, text="Toggle Dark Mode", command=toggle_theme)
theme_button.pack(pady=5)

root.mainloop()
