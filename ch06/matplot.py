from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def _destroyWindow():
    root.quit()
    root.destroy()


fig = Figure(figsize=(12, 8), facecolor='white')

axis = fig.add_subplot(211)

x_values = [1, 2, 3, 4]
y_values = [5, 7, 6, 8]
axis.plot(x_values, y_values)

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

axis.grid(linestyle='-')

axis1 = fig.add_subplot(212)

xValues1 = [1, 2, 3, 4]
yValues1 = [7, 5, 8, 6]
axis1.plot(xValues1, yValues1)
axis1.grid()

root = tk.Tk()
# root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
