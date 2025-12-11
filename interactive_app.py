import matplotlib.pyplot as plt
import numpy as np 

class InteractivePlot:
    def __init__(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)
        self.x = np.linspace(0, 10, 100)
        self.line, = self.ax1.plot(self.x, np.sin(self.x))
        
        # Connect multiple events
        self.cid_press = self.fig.canvas.mpl_connect(
            'button_press_event', self.on_click)
        self.cid_move = self.fig.canvas.mpl_connect(
            'motion_notify_event', self.on_move)
        
    def on_click(self, event):
        if event.inaxes == self.ax1:
            # Update second plot with clicked x-value
            y = np.sin(self.x * event.xdata/5)
            self.ax2.clear()
            self.ax2.plot(self.x, y)
            self.fig.canvas.draw()

    def on_move(self, event):
        if event.inaxes == self.ax1:
            # Show coordinates in title
            self.ax1.set_title(f'x={event.xdata:.2f}, y={event.ydata:.2f}')
            self.fig.canvas.draw()

interactive = InteractivePlot()
plt.show()