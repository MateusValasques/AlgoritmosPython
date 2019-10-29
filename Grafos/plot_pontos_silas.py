import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
import sys
import re

file_name = "map.osm.txt"
x = list()
y = list()
with open(file_name) as fp:
    for line in fp:
        points = re.findall(r'[-+]?\d+.\d+', line)
        x.append(float(points[1]))
        y.append(float(points[2]))
print(points)
plt.plot(x, y, 'ro')

fig, ax = plt.subplots()

p, = plt.plot(x, y, 'o')

cursor = Cursor(ax,
                horizOn = True, 
                vertOn = True,
                color = 'green',
                linewidth = 2.0)

def onclick (event):
    x1, y1 = (event.xdata, event.ydata)
    print(x1, y1)

    
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()