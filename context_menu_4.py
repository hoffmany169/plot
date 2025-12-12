"""
Docstring for context_menu_4
 impler approach using annotations
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line, = ax.plot(range(10), 'b-')
menu_annotation = None

def on_right_click(event):
    global menu_annotation
    
    if event.button == 3 and event.inaxes == ax:
        # Remove previous menu if exists
        if menu_annotation:
            menu_annotation.remove()
        
        # Create menu as annotation
        menu_text = "Right-click options:\n1. Add point\n2. Remove point\n3. Reset"
        menu_annotation = ax.annotate(
            menu_text,
            xy=(event.xdata, event.ydata),
            xytext=(10, 10),
            textcoords='offset points',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.9),
            ha='left',
            va='bottom',
            fontsize=9
        )
        
        # Store click coordinates for actions
        ax._last_click = (event.xdata, event.ydata)
        
        fig.canvas.draw()
        
        # Set up single click handler for menu selection
        fig.canvas.mpl_connect('button_press_event', on_menu_select)

def on_menu_select(event):
    global menu_annotation
    
    if event.button == 1 and event.inaxes == ax and menu_annotation:
        # Check if click is near the annotation
        ann_pos = menu_annotation.xy
        dist = ((event.xdata - ann_pos[0])**2 + (event.ydata - ann_pos[1])**2)**0.5
        
        if dist < 0.5:  # Adjust threshold as needed
            # Here you could add logic to determine which option was clicked
            print("Menu option selected at:", event.xdata, event.ydata)
        
        # Remove menu after selection
        menu_annotation.remove()
        menu_annotation = None
        fig.canvas.draw()
        
        # Disconnect this temporary handler
        fig.canvas.mpl_disconnect(fig._menu_cid)

# Connect right-click
fig.canvas.mpl_connect('button_press_event', on_right_click)
plt.show()