import tkinter
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import Menu

win = tk.Tk()

win.title("Python GUI")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

tabControl.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)

mighty2 = ttk.LabelFrame(tab2, text='Mighty Python')
mighty2.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text="A Label")
a_label.grid(column=0, row=0)


def click_me():
    action.configure(text='Hello' + name.get() + ' ' + number_chosen.get())


ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)


def callbackFunc(event):
    print("New Element Selected")
    print(number_chosen.get())


ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(
    mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)
number_chosen.bind("<<ComboboxSelected>>", callbackFunc)
name_entered.focus()

chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()

checkBtn1 = tk.Checkbutton(mighty2, text='Disabled', variable=chVarDis, state='disabled')
checkBtn1.select()
checkBtn2 = tk.Checkbutton(mighty2, text='UnChecked', variable=chVarUn)
checkBtn2.deselect()
checkBtn3 = tk.Checkbutton(mighty2, text='Enabled', variable=chVarEn)
checkBtn3.select()

checkBtn1.grid(column=0, row=4)
checkBtn2.grid(column=1, row=4)
checkBtn3.grid(column=2, row=4)


def checkCallback(*ignoredArgs):
    if chVarUn.get():
        checkBtn1.configure(state='disabled')
    else:
        checkBtn3.configure(state='normal')
    if chVarEn.get():
        checkBtn2.configure(state='disabled')
    else:
        checkBtn3.configure(state='normal')


chVarUn.trace('w', lambda unused0, unused1, unused2: checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2: checkCallback())

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

colors = ["Blue", "Gold", "Red"]


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRed = tk.Radiobutton(mighty2, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRed.grid(column=col, row=6, sticky=tk.W)

buttons_frame = ttk.LabelFrame(mighty2, text="Labels in a Frame")
buttons_frame.grid(column=0, row=7, padx=20, pady=30)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=2, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=30, pady=30)


def _quit():
    win.quit()
    win.destroy()
    exit()


menu_bar = Menu(win)

win.configure(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')

name_entered.focus()

win.mainloop()
