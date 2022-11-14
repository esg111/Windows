from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def _destroyWindow():
    root.quit()
    root.destroy()


fig = Figure(figsize=(12, 5), facecolor='white')

axis = fig.add_subplot(111)

xValues = [1, 2, 3, 4]

yValues0 = [6, 7.5, 8, 7.5]
yValues1 = [5.5, 6.5, 50, 6]
yValues2 = [6.5, 7, 8, 7]
yAll = [yValues0, yValues1, yValues2]

minY = min([y for yValues in yAll for y in yValues])

yUpperLimit = 20

maxY = max([y for yValues in yAll for y in yValues if y > yUpperLimit])

axis.set_ylim(minY, maxY)
axis.set_xlim(min(xValues), max(xValues))

t0 = axis.plot(xValues, yValues0)
t1 = axis.plot(xValues, yValues1)
t2 = axis.plot(xValues, yValues2)

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

axis.grid()
fig.legend([t0, t1, t2], ['First line', 'Second line', 'Third line'], loc='upper right')

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()