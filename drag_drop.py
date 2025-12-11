import matplotlib.pyplot as plt

class DraggablePoint:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.point, = self.ax.plot([0.5], [0.5], 'ro', markersize=10)
        self.dragging = False
        
        # Connect events
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        
    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        # Check if click is near the point
        contains, _ = self.point.contains(event)
        if contains:
            self.dragging = True
    
    def on_motion(self, event):
        if not self.dragging or event.inaxes != self.ax:
            return
        # Update point position
        self.point.set_data([event.xdata], [event.ydata])
        self.fig.canvas.draw()
    
    def on_release(self, event):
        self.dragging = False

draggable = DraggablePoint()
plt.show()