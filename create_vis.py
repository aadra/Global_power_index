import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from math import pi

width = 0.65  # width of the bars (in radians)

# create the figure, dont change
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# angle positions, 0 to 360 with increments of 360/5
xo = list(range(0, 360, 360 / 5))
# Convert to radians and subtract half the width
# of a bar to center it.
x = [i * pi / 180 for i in xo]

# choose required set of data and title

# my data
#data = [46, 42.17, 41.6, 43.97031, 82.5]
#title='India'

#data = [80.8, 100, 50.83, 83.35, 90.3]
#title='USA'

#data = [59.6, 55.88, 81.12, 79.1101, 69.2]
#title='China'

#data = [76.4, 52.55, 83.7, 81.39821, 35.5]
#title='Russia'

data = [29, 52.26, 52.82, 51.95857, 84.6]
title='Brazil'


# set the labels for each bar, do not change
ax.set_xticks(x)
ax.set_xticklabels(['Military\nProwess', 'Productivity', 'Resource', 'Self-\nSufficiency', 'Morale'])
ax.set_thetagrids(xo, frac=1.15) # frac changes distance of label from circumference of circle

plt.ylim(0, 100) # sets range for radial grid

fig.suptitle(title, fontsize=20, y=0.5, x=0.1) # title of plot

plt.rgrids([20, 40, 60, 80, 100], angle=35, fontsize=10) # the numbers you see along radius, angle changes position


bars = ax.bar(x, data, width=width, align='center') # do the plotting

i = 0
for r, bar in zip(data, bars):
    bar.set_facecolor( cm.jet(r/max(data))) # set color for each bar, intensity proportional to height of bar
    bar.set_alpha(0.5) # make color partly transparent
    height = bar.get_height() # this is basically the radial height, or radius of bar

    # write value of each bar inside it
    # first param is angle, second is radius -10 makes it go inside the bar
    ax.text(x[i], height-10, '%0.2f'%data[i], ha='center', va='center', fontsize=11)
    i = i + 1

plt.savefig('examples/'+title+'.png')
