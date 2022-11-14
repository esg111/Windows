import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep  # careful - this can freeze the GUI
from ch05.ch05_OOP_1 import ToolTip

GLOBAL_CONST = 42


def _msgBox():
    msg.showinfo('Python Message Info Box',
                 'A Python GUI created using tkinter:\nThe year is 2019.')


def usingGlobal():
    global GLOBAL_CONST
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777


class OOP:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.create_widgets()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100

    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.mighty2.configure(text='Blue')
        elif radSel == 1:
            self.mighty2.configure(text='Gold')
        elif radSel == 2:
            self.mighty2.configure(text='Red')
            self.mighty2.Frames(bg='red')

    def checkCallback(self, *ignoredArgs):
        if self.chVarUn.get():
            self.check3.configure(state='disabled')
        else:
            self.check3.configure(state='normal')
        if self.chVarEn.get():
            self.check2.configure(state='disabled')
        else:
            self.check2.configure(state='normal')

    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' +
                                   self.number_chosen.get())

    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')

    ####################################################################
    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1, fill="both")

        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')

        self.name = tk.StringVar()
        name_entered = ttk.Entry(mighty, width=12, textvariable=self.name)
        name_entered.grid(column=0, row=1, sticky='W')

        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)

        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin)
        self.spin.grid(column=0, row=2)

        ToolTip(self.spin, 'This is a Spin Control')

        self.scrol_w = 30
        self.scrol_h = 3
        self.scrol = scrolledtext.ScrolledText(mighty, width=self.scrol_w, height=self.scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

        ToolTip(self.scrol, 'This is a ScrolledText widget')

        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)

        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.select()
        check3.grid(column=2, row=0, sticky=tk.W)

        chVarUn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())
        chVarEn.trace('w', lambda unused0, unused1, unused2: self.checkCallback())

        colors = ["Blue", "Gold", "Red"]

        self.radVar = tk.IntVar()

        self.radVar.set(99)

        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar,
                                    value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)  # row=6

        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            self.progress_bar["value"] = 0

        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ",
                   command=self.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(buttons_frame, text=" Start Progressbar  ",
                   command=self.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(buttons_frame, text=" Stop immediately ",
                   command=self.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(buttons_frame, text=" Stop after second ",
                   command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')

        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=2, pady=2)

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.win.iconbitmap('pyc.ico')

        strData = self.spin.get()
        print("Spinbox value: " + strData)

        usingGlobal()

        name_entered.focus()


oop = OOP()
oop.win.mainloop()
