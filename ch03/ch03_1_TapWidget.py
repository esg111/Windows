import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python Gui")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text= "Tab 2")

tabControl.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text='Enter a name:')
a_label.grid(column=0, row=0, sticky='W')
win.mainloop()