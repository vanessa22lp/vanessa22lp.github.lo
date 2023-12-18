import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(10), init_func=init, blit=True)
plt.show()