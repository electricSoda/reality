import win32gui, win32process, psutil
import pygetwindow as pw

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
    
def closeWindow():
    curr = processName()
    for process in psutil.process_iter():
        if process.name() == curr:
            process.kill()
# Testing
if __name__ == "__main__":
    import time
    time.sleep(0.5)
    closeWindow()