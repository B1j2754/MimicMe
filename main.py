import threading
import queue
import cv2_display
import gui
import psutil
import os

# Create a queue for communication
q = queue.Queue()

# Set priority function to keep cv2 running smoothly even if unfocused
p = psutil.Process(os.getpid())
p.nice(psutil.REALTIME_PRIORITY_CLASS)  # Or psutil.REALTIME_PRIORITY_CLASS if needed

def cv2_thread(q):
    print(cv2_display.window_cv2(q))

def gui_thread(q):
    gui.window_tk(q)

# Create threads for both functions
thread_1 = threading.Thread(target=cv2_thread, args=(q,))
#thread_2 = threading.Thread(target=gui_thread, args=(q,))

# Start both threads
thread_1.start()
#thread_2.start()
gui_thread(q)

# Wait for both threads to finish
thread_1.join()
#thread_2.join()