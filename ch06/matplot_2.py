from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def _destroyWindow():
    root.quit()
    root.destroy()


fig = Figure(figsize=(12, 8), facecolor='white')
x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]

axis1 = fig.add_subplot(221)
axis2 = fig.add_subplot(222, sharex=axis1, sharey=axis1)
axis3 = fig.add_subplot(223, sharex=axis1, sharey=axis1)
axis4 = fig.add_subplot(224, sharex=axis1, sharey=axis1)

axis1.plot(x_values, y_values)
axis1.set_xlabel('Horizontal Label 1')
axis1.set_ylabel('Vertical Label 1')
axis1.grid(linestyle='-')

axis2.plot(x_values, y_values)
axis2.set_xlabel('Horizontal Label 2')
axis2.set_ylabel('Vertical Label 2')
axis2.grid(linestyle='-')

axis3.plot(x_values, y_values)
axis3.set_xlabel('Horizontal Label 3')
axis3.set_ylabel('Vertical Label 3')
axis3.grid(linestyle='-')

axis4.plot(x_values, y_values)
axis4.set_xlabel('Horizontal Label 4')
axis4.set_ylabel('Vertical Label 4')
axis4.grid(linestyle='-')

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()