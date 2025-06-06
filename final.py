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
    ax.set_title(f"{algorithm_name} Disk Scheduling Visualization", fontsize=14, fontweight='bold')
    ax.set_xlabel("Cylinder Number", fontsize=12)
    ax.set_ylabel("Request Order", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    line, = ax.plot([], [], marker='o', linestyle='-', color='orangered', markersize=8, linewidth=2)

    def update(frame):
        x_data = seek_sequence[:frame+1]
        y_data = list(range(len(x_data)))
        line.set_data(x_data, y_data)
        return line,
    
    ani = animation.FuncAnimation(fig, update, frames=len(seek_sequence), interval=300, blit=True, repeat=False)
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

root = tk.Tk()
root.title("Disk Scheduling Simulator")

style = ttk.Style(root)
style.theme_use("clam")

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

root.mainloop()

