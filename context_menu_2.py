"""
Docstring for context_menu_2
Custom context menu using patches (more visually integrated)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.text import Text

class PatchContextMenu:
    def __init__(self, ax):
        self.ax = ax
        self.fig = ax.figure
        self.menu_patches = []
        self.menu_texts = []
        self.menu_visible = False
        
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
    
    def on_click(self, event):
        if event.button == 3 and event.inaxes == self.ax:
            self.show_menu(event.xdata, event.ydata)
        elif self.menu_visible:
            self.hide_menu()
    
    def show_menu(self, x, y):
        self.hide_menu()
        
        # Menu background
        menu_bg = patches.Rectangle(
            (x, y), 0.3, 0.2,
            facecolor='white',
            edgecolor='black',
            alpha=0.9,
            zorder=100
        )
        self.ax.add_patch(menu_bg)
        self.menu_patches.append(menu_bg)
        
        # Menu options
        options = [
            ('Zoom In', self.zoom_in),
            ('Zoom Out', self.zoom_out),
            ('Reset View', self.reset_view),
            ('Add Point', self.add_point)
        ]
        
        for i, (label, action) in enumerate(options):
            text = Text(
                x + 0.02, y + 0.15 - i*0.05,
                label,
                picker=True,
                zorder=101,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray")
            )
            text._action = action
            text._args = (x, y)
            self.ax.add_artist(text)
            self.menu_texts.append(text)
        
        self.menu_visible = True
        self.fig.canvas.draw()
    
    def on_pick(self, event):
        if hasattr(event.artist, '_action'):
            event.artist._action(*event.artist._args)
            self.hide_menu()
    
    def hide_menu(self):
        for patch in self.menu_patches:
            patch.remove()
        for text in self.menu_texts:
            text.remove()
        self.menu_patches.clear()
        self.menu_texts.clear()
        self.menu_visible = False
        self.fig.canvas.draw()
    
    def zoom_in(self, x, y):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        self.ax.set_xlim(xlim[0]*0.8, xlim[1]*0.8)
        self.ax.set_ylim(ylim[0]*0.8, ylim[1]*0.8)
        self.fig.canvas.draw()
    
    def zoom_out(self, x, y):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        self.ax.set_xlim(xlim[0]*1.2, xlim[1]*1.2)
        self.ax.set_ylim(ylim[0]*1.2, ylim[1]*1.2)
        self.fig.canvas.draw()
    
    def reset_view(self, x, y):
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
    
    def add_point(self, x, y):
        self.ax.plot(x, y, 'go', markersize=10)
        self.fig.canvas.draw()

# Usage
fig, ax = plt.subplots()
ax.plot(range(10), 'b-')
menu = PatchContextMenu(ax)
plt.show()