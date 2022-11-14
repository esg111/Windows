import tkinter as tk
from tkinter import *

win = tk.Tk()


def BtnClick():
    result.configure(text=input_text.get(), anchor=W)


input_text = tk.StringVar()

input_text_entered = Entry(win, width=15, textvariable=input_text)
input_text_entered.grid(column=0, row=0, padx=10, pady=10)

btn = Button(win, text='입력', command=BtnClick)
btn.grid(column=1, row=0)

text_label = Label(win, width=15, text='출력결과', anchor=W)
text_label.grid(column=0, row=1)

result = Label(win, text="")
result.grid(column=1, row=1)

win.title("Python GUI")
win.geometry('250x100')
win.mainloop()
