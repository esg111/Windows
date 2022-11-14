import tkinter as tk
from time import sleep
from tkinter import Menu
from tkinter import Spinbox
from tkinter import ttk, scrolledtext
from tooltip import ToolTip

win = tk.Tk()

win.title("Python GUI")


def callbackFunc():
    print("New Element Selected")
    print(number_chosen.get())


def checkCallback():
    if chVarUn.get():
        checkBtn1.configure(state='disabled')
    else:
        checkBtn3.configure(state='normal')
    if chVarEn.get():
        checkBtn2.configure(state='disabled')
    else:
        checkBtn3.configure(state='normal')


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = 1
        progress_bar.update()
    progress_bar["value"] = 0


def start_progressbar():
    progress_bar.start()


def stop_progressbar():
    progress_bar.stop()


def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)


def _quit():
    win.quit()
    win.destroy()
    exit()


def _spin():
    value = spin.get()
    print(value)
    scroll.insert(tk.INSERT, value + '\n')


def _spin2():
    value = spin2.get()
    print(value)
    scroll.insert(tk.INSERT, value + '\n')


colors = ["Blue", "Gold", "Red"]

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Tab 3")

tabControl.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text='Mighty Python')
mighty.grid(column=0, row=0, padx=8, pady=4)

mighty2 = ttk.LabelFrame(tab2, text='Mighty Python')
mighty2.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text="A Label")
a_label.grid(column=0, row=0)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)


def click_me():
    action.configure(text='Hello' + name.get() + ' ' +
                          number_chosen.get())


action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(
    mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

number_chosen.bind("<<ComboboxSelected>>", callbackFunc())
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

chVarUn.trace('w', lambda unused0, unused1, unused2: checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2: checkCallback())

# spin = Spinbox(mighty, from_=0, to=10)
# spin = Spinbox(mighty, from_=0, to=10, width=5, bd=9)
# spin = Spinbox(mighty, from_=0, to=10, width=5, bd=9, command=_spin)
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=_spin)
spin.grid(column=0, row=2)
spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin2)
spin2.grid(column=1, row=2)

ToolTip(spin, 'This is a Spin Control')

scroll_w = 30
scroll_h = 3
scroll = scrolledtext.ScrolledText(mighty, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scroll.grid(column=0, row=5)

ToolTip(scroll, 'This is a ScrolledText widget')

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRed = tk.Radiobutton(mighty2, text=colors[col], variable=radVar,
                            value=col, command=radCall())
    curRed.grid(column=col, row=6, sticky=tk.W)

progress_bar = ttk.Progressbar(tab2, orient="horizontal", length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)

buttons_frame = ttk.LabelFrame(mighty2, text="ProgressBar")
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

ttk.Button(buttons_frame, text="Run Progressbar  ", command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text="Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text="Stop immediately  ", command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text="Stop after second  ", command=progressbar_stop_after()).grid(column=0, row=3,
                                                                                             sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in mighty2.winfo_children():
    child.grid_configure(padx=8, pady=2)

tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)

menu_bar = Menu(win)

win.configure(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')

name_entered.focus()

win.mainloop()
