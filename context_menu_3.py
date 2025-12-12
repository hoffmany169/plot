"""
Docstring for context_meunu_3
Using tkinter/Qt native menus (backend-specific)
For more native-looking menus, use the GUI backend's native widgets:
"""

import matplotlib
matplotlib.use('TkAgg')  # Use Tk backend
import matplotlib.pyplot as plt
import tkinter as tk

class TkContextMenu:
    def __init__(self, fig):
        self.fig = fig
        self.canvas = fig.canvas
        
        # Get the Tk root window
        self.root = self.canvas.manager.window
        
        # Create menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Save Image", command=self.save_image)
        self.menu.add_command(label="Copy Data", command=self.copy_data)
        self.menu.add_separator()
        self.menu.add_command(label="Properties", command=self.show_properties)
        
        # Bind right-click
        self.canvas.mpl_connect('button_press_event', self.on_right_click)
    
    def on_right_click(self, event):
        if event.button == 3:  # Right-click
            # Convert matplotlib coordinates to tkinter coordinates
            x_tk = self.root.winfo_pointerx() - self.root.winfo_rootx()
            y_tk = self.root.winfo_pointery() - self.root.winfo_rooty()
            self.menu.post(x_tk, y_tk)
    
    def save_image(self):
        self.fig.savefig('output.png')
        print("Image saved")
    
    def copy_data(self):
        print("Data copied to clipboard")
    
    def show_properties(self):
        print("Showing properties dialog")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
menu = TkContextMenu(fig)
plt.show()