"""
Docstring for context_menu_1

Using matplotlib's built-in widgets
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

class ContextMenu:
    def __init__(self, fig):
        self.fig = fig
        self.menu_visible = False
        self.menu_buttons = []
        
        # Connect right-click event
        self.cid = fig.canvas.mpl_connect('button_press_event', self.on_click)
    
    def on_click(self, event):
        self.cur_event = event
        if event.button == 3:  # Right-click
            self.show_menu(event.xdata, event.ydata)
    
    def show_menu(self, x, y):
        # Remove previous menu if exists
        self.hide_menu()
        
        # Convert data coordinates to figure coordinates
        ax = self.cur_event.inaxes if hasattr(self.cur_event, 'inaxes') else None
        if ax:
            trans = ax.transData
            x_fig, y_fig = trans.transform([x, y])
            inv = self.fig.transFigure.inverted()
            x_fig, y_fig = inv.transform([x_fig, y_fig])
        else:
            x_fig, y_fig = 0.5, 0.5
        
        # Create menu buttons
        options = ['Copy Coordinates', 'Add Marker', 'Clear Markers', 'Save Plot']
        actions = [self.copy_coords, self.add_marker, self.clear_markers, self.save_plot]
        
        for i, (opt, action) in enumerate(zip(options, actions)):
            # Create button at calculated position
            btn_ax = plt.axes([x_fig, y_fig - i*0.05, 0.15, 0.04])
            btn = Button(btn_ax, opt)
            btn.on_clicked(lambda e, a=action: (self.hide_menu(), a(x, y)))
            self.menu_buttons.append((btn_ax, btn))
        
        self.menu_visible = True
        plt.draw()
    
    def hide_menu(self):
        for ax, btn in self.menu_buttons:
            ax.remove()
        self.menu_buttons.clear()
        self.menu_visible = False
        plt.draw()
    
    def copy_coords(self, x, y):
        print(f"Coordinates: ({x:.2f}, {y:.2f})")
    
    def add_marker(self, x, y):
        self.cur_event.inaxes.plot(x, y, 'ro')
        plt.draw()
    
    def clear_markers(self, x, y):
        for line in self.cur_event.inaxes.lines[1:]:  # Keep original plot
            line.remove()
        plt.draw()
    
    def save_plot(self, x, y):
        self.fig.savefig('plot_with_context.png')
        print("Plot saved!")

# Usage
fig, ax = plt.subplots()
ax.plot(np.random.rand(10))
menu = ContextMenu(fig)
plt.show()