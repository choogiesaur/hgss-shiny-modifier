import tkinter as tk
from tkinter import filedialog, Text
import os

import ndspy.rom
import ndspy.codeCompression as comp

root = tk.Tk()

def openFile():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File",
        filetypes=(("NDS Roms","*.nds"), ("All files", "*.*"))
    )

canvas = tk.Canvas(root, height=400, width=700, bg='gainsboro')
canvas.pack()

frame = tk.Frame(root, bg="gainsboro")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(frame, text="Open File", padx=10, pady=5, fg="black", bg="gainsboro", command = openFile )
openFile.pack(side='left')

root.mainloop()