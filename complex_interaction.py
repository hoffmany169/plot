"""
Docstring for complex_interaction

7. Backend Requirements
For full interactivity, use appropriate backends:

Jupyter Notebook: %matplotlib notebook or %matplotlib widget

Desktop apps: matplotlib.use('TkAgg') (or Qt5Agg, WXAgg, etc.)

Web apps: Use mpld3 or plotly for web-based interactivity
"""

import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

# Add slider
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(ax_slider, 'Freq', 0.1, 30.0, valinit=1)

def update(val):
    line.set_ydata(np.sin(2*np.pi*freq_slider.val*t))
    fig.canvas.draw_idle()

freq_slider.on_changed(update)
plt.show()