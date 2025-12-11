import matplotlib.pyplot as plt

# Using pick events
fig, ax = plt.subplots()
points = ax.plot([1, 2, 3], [1, 4, 9], 'bo', picker=5)  # 5 pixels tolerance

def on_pick(event):
    artist = event.artist
    xdata, ydata = artist.get_data()
    ind = event.ind[0]
    print(f'Picked point at ({xdata[ind]}, {ydata[ind]})')

fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()