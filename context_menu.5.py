"""
Docstring for context_menu.5
Complete example with hover effects
"""

import matplotlib.pyplot as plt
import numpy as np

class HoverContextMenu:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.menu_items = []
        self.active = False
        
        # Connect events
        self.cid1 = fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid2 = fig.canvas.mpl_connect('motion_notify_event', self.on_hover)
    
    def create_menu(self, x, y):
        self.clear_menu()
        
        options = [
            ('📊 Add Plot', self.add_plot, (x, y)),
            ('📌 Add Marker', self.add_marker, (x, y)),
            ('🗑️ Clear', self.clear_all, None),
            ('💾 Save', self.save_fig, None)
        ]
        
        for i, (text, func, args) in enumerate(options):
            # Create clickable text
            txt = self.ax.text(
                x + 0.02, y - i * 0.05,
                text,
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor="lightblue",
                         edgecolor="gray",
                         alpha=0.9),
                picker=True,
                zorder=100
            )
            txt._callback = func
            txt._args = args
            self.menu_items.append(txt)
        
        self.active = True
        self.fig.canvas.draw()
    
    def on_click(self, event):
        if event.button == 3 and event.inaxes == self.ax:
            self.create_menu(event.xdata, event.ydata)
        elif event.button == 1 and self.active:
            # Check if click was on a menu item
            for item in self.menu_items:
                if item.get_window_extent().contains(event.x, event.y):
                    if item._args:
                        item._callback(*item._args)
                    else:
                        item._callback()
                    self.clear_menu()
                    return
    
    def on_hover(self, event):
        if not self.active or not event.inaxes:
            return
        
        for item in self.menu_items:
            bbox = item.get_window_extent()
            if bbox.contains(event.x, event.y):
                item.set_bbox(dict(boxstyle="round,pad=0.3", 
                                  facecolor="yellow",
                                  edgecolor="black"))
            else:
                item.set_bbox(dict(boxstyle="round,pad=0.3", 
                                  facecolor="lightblue",
                                  edgecolor="gray"))
        self.fig.canvas.draw()
    
    def clear_menu(self):
        for item in self.menu_items:
            item.remove()
        self.menu_items.clear()
        self.active = False
        self.fig.canvas.draw()
    
    def add_plot(self, x, y):
        x_vals = np.linspace(x-1, x+1, 10)
        y_vals = np.sin(x_vals) + y
        self.ax.plot(x_vals, y_vals, 'r--')
    
    def add_marker(self, x, y):
        self.ax.plot(x, y, 'go', markersize=10)
    
    def clear_all(self):
        self.ax.clear()
        self.ax.plot(np.random.rand(10))
    
    def save_fig(self):
        self.fig.savefig('context_menu_plot.png')
        print("Figure saved!")

# Usage
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(np.random.rand(10), 'b-', linewidth=2)
menu = HoverContextMenu(fig, ax)
plt.title('Right-click for context menu')
plt.show()