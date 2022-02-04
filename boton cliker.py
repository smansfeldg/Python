from tkinter import *
from threading import Thread
import time


release = True
limit = 100


def click_callback():
    global release
    release = False
    while not release and int(text.get()) < limit:
        time.sleep(0.1)
        text.set(str(int(text.get())+1))

def release_callback(e):
    global release
    release = True



root = Tk()

root.geometry('320x240')
root.title("Cliker")
root.resizable(False, False)

text = StringVar()
button = Button(root, textvariable=text)
button.pack(expand=True, fill=BOTH)
text.set('0')

button.bind('<Button-1>', lambda e: Thread(target=click_callback, daemon=True).start())
button.bind('<ButtonRelease-1>', release_callback)

root.mainloop()
