# Advanced-Disk-Scheduling-Simulator
 A Python-based GUI application for visualizing and analyzing different disk scheduling algorithms, including FCFS, SSTF, SCAN, and C-SCAN.

Overview-
The Advanced Disk Scheduling Simulator is a Python application designed to help users understand the working of various disk scheduling algorithms through visualization and animation. It allows users to input disk requests and the initial head position, choose a scheduling algorithm, and observe how the disk head moves while servicing requests.

The simulator supports the following disk scheduling algorithms:
✔ FCFS (First Come, First Served)
✔ SSTF (Shortest Seek Time First)
✔ SCAN
✔ C-SCAN (Circular SCAN)

🎯 Features
✅ User-friendly GUI built using Tkinter.
✅ Visualization of Disk Head Movement using Matplotlib animations.
✅ Support for Multiple Algorithms: FCFS, SSTF, SCAN, and C-SCAN.
✅ Total Seek Time Calculation for performance comparison.
✅ Real-Time Disk Access Simulation.

⚙️ Technology Used
Python: Primary programming language.

Tkinter: For the Graphical User Interface (GUI).

Matplotlib: For animating disk head movements.

NumPy: For mathematical calculations.

🚀 Installation & Setup
Prerequisites
Ensure you have Python 3.x installed on your system.

Step 1: Clone the Repository

git clone https://github.com/your-username/disk-scheduling-simulator.git
cd disk-scheduling-simulator
Step 2: Install Dependencies

pip install -r requirements.txt
(If requirements.txt is not available, manually install dependencies:)

pip install matplotlib numpy
Step 3: Run the Simulator
python final.py


🎥 How to Use
1️⃣ Enter disk requests as comma-separated values (e.g., 98, 183, 37, 122, 14, 124, 65, 67).
2️⃣ Enter the initial head position.
3️⃣ Select an algorithm from the dropdown menu.
4️⃣ Click "Run Simulation" to visualize disk head movement.
5️⃣ View total seek time and analyze algorithm efficiency.

