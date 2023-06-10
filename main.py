# IMPORTS
import win32gui, win32process, psutil
import pygetwindow as pw

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

import math
import numpy as np
import pprint
import sys
import os

import categories

# HELPER FUNCTIONS
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def processName():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        print("ERROR")
        return None
    
def windowTitle():
    try:
        return pw.getActiveWindow().title
    except:
        print("ERROR")
        return None

def format(seconds: float):
    if seconds <60:
        return "{}s".format(math.floor(seconds))
    elif seconds >=60 and seconds <3600:
        return "{}m{}s".format(math.floor((seconds/60)%60), math.floor(seconds%60))
    return "{}h{}m{}s".format(math.floor((seconds/3600)%24), math.floor((seconds/60)%60), math.floor(seconds%60))

def plot():
    global wedges, labels
    fig.clear()
    wedges, labels = plt.pie(list(activities.values()), labels=list(activities.keys()), startangle=0, colors = colors, radius = 0.75)
    c.draw()

def onPick(event):
    if wedges == None or labels == None: return
    for (a, b) in zip(wedges, labels):
        if a.contains_point([event.x, event.y]):
            info.configure(text=format(activities[b._text]))       
            info.place(x=event.x+20, y=h-event.y+5) 
            canvas.place(relx=.5, rely=.5,anchor= CENTER)     
            
def hideInfo(e):
    info.place_forget()

# LIFETIME CYCLE LOOP
def cycle():
    global tick, currentWindow
    if running:
        category = categories.getType(processName(), windowTitle())
        
        if category != "Timer":
            if category not in activities: activities[category] = 0
            activities[category] += 1 

        plot()
        
        tick += 1
        root.after(1000, cycle)



# VARIABLE INITIALIZATION
activities = {}
colors=['#f66d44', '#feae65', '#e6f69d', '#aadea7', '#64c2a6', '#2d87bb']

root = Tk()
w,h = 450, 450
xOffset = int(root.winfo_screenwidth())
running = True
tick = 0

DPI = 100

wedges, labels = None, None

# WIDGETS - ORDER MATTERS: No matter what you do, the last widget initialized
# is the one that is highest on the stack (meaning it shows up on top of
# the rest of the widgets), and the first widget initialized at the bottom of the stack
fig, ax = plt.subplots(figsize=((w)/DPI, (h)/DPI), dpi = DPI, picker=True) # picker = True is VERY IMPORTANT!!! (it makes our plot be pickable and the event, "pick_event" be able to fire
plt.pie([1], colors=colors) # initial pie chart
plt.rcParams.update({'font.size': 10}) # font size

c = FigureCanvasTkAgg(fig, master = root) # connecting the plt pie chart to tkinter
canvas = c.get_tk_widget()

info = Label(root, text="")

canvas.place(relx=.5, rely=.5,anchor= CENTER)

# CONFIGURATION
root.title("reality")
root.attributes("-alpha", 0.99)
root.geometry(f"{w}x{h}+{xOffset}+50")
root.configure(background='white')

favicon = PhotoImage(file = resource_path("favicon.png")) 
root.iconphoto(False, favicon)

def close_window():
    try: 
        plt.close('all')
        running = False
        root.after_cancel(root)
        root.destroy()
    except:
        pass

# CALLBACKS
root.bind("<Leave>", hideInfo)
root.protocol("WM_DELETE_WINDOW", close_window)
fig.canvas.mpl_connect("motion_notify_event", onPick)

root.after(1000, cycle)
root.mainloop()




