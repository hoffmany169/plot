import matplotlib.pyplot as plt

plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.draw()

# Plot updates will now be immediate
ax.plot([0, 4], [0, 8], 'r--')
plt.draw()