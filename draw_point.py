"""
Docstring for examp_1

button_press_event - mouse button pressed

button_release_event - mouse button released

motion_notify_event - mouse motion

scroll_event - mouse wheel scroll
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
line, = ax.plot(x, y)

def on_click(event):
    if event.inaxes:
        print(f'Mouse click at ({event.xdata:.2f}, {event.ydata:.2f})')
        # Add a point at click location
        ax.plot(event.xdata, event.ydata, 'ro')
        fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()