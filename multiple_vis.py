import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from math import pi
import matplotlib as mpl


def create_figure(all_data): # takes in data and title and creates and saves plot

    width = 0.45  # width of the bars (in radians)

    # create the figure, dont change
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    # angle positions, 0 to 360 with increments of 360/5
    xo = list(range(0, 360, 360 / 5))
    # Convert to radians and subtract half the width
    # of a bar to center it.
    x = [i * pi / 180 for i in xo]

    # set the labels for each bar, do not change
    ax.set_xticks(x)
    ax.set_xticklabels(['Military\nProwess', 'Productivity', 'Resource', 'Self-\nSufficiency', 'Morale'])
    ax.set_thetagrids(xo, frac=1.15) # frac changes distance of label from circumference of circle

    plt.ylim(0, 100) # sets range for radial grid

    fig.suptitle("India \n1993-2012", fontsize=20, y=0.5, x=0.1) # title of plot

    plt.rgrids([20, 40, 60, 80, 100], angle=33, fontsize=10) # the numbers you see along radius, angle changes position

    colorList = [];

    count = -1
    for key in all_data:
        count = count + 1
        data = all_data[key]
        mylist = [item+0.5*(count-len(all_data)/2)/len(all_data) for item in x]
        bars = ax.bar(mylist, data, width=width, align='center') # do the plotting
        i = 0
        for r, bar in zip(data, bars):
            bar.set_facecolor( cm.jet(0.8*count/len(all_data))) # set color for each bar, intensity proportional to height of bar
            colorList.append(cm.jet(0.8*count/len(all_data)))
            #bar.set_alpha(0.2) # make color partly transparent
            
            height = bar.get_height() # this is basically the radial height, or radius of bar

            # write value of each bar inside it
            # first param is angle, second is radius -10 makes it go inside the bar
        
            if i == 3 and count == 0:
                ax.text(mylist[i]-width/4*3, height+5, key, ha='center', va='center', fontsize=11)
            if i == 3 and count == len(all_data)-1:
                ax.text(mylist[i]+width/4*3, height-5, key, ha='center', va='center', fontsize=11)
            i = i + 1

    
    plt.savefig('examples/multiple.png')
        
def main(): # your main function
    
    all_data = {} # this is a dictionary
    # in a dictionary, you have keys and values
    # eg. data["title"] = [1, 2, 3]
    # means that for key = "title", the corresponding data is [1, 2, 3]
    # you can have any type of key and value
    # here i am using string key and list(array) value
    
    all_data["1993"] = [56, 50.61, 73.28, 60.81, 56.95]
    all_data["1994"] = [54, 52.1, 73.33, 62.2, 56.95]
    all_data["1995"] = [52, 53.12, 73.08, 64.63, 56.94]
    all_data["1996"] = [50, 52.99, 73.57, 65.67, 55.94]
    all_data["1997"] = [52, 54.92, 73.52, 67.13, 58.94]
    all_data["1998"] = [54, 54.56, 74.84, 67.61, 59.67]
    all_data["1999"] = [60, 55.44, 74.59, 70.79, 59.67]
    all_data["2000"] = [60, 55.92, 75.29, 71.07, 58.48]
    all_data["2001"] = [58, 53.42, 76.10, 71.06, 57.48]
    all_data["2002"] = [56, 56.99, 76.30, 72.09, 60.24]
    all_data["2003"] = [54, 58.55, 76.52, 72.8, 64.24]
    all_data["2004"] = [56, 61.39, 76.55, 76.24, 64.13]
    all_data["2005"] = [56, 68.91, 77.68, 78.098, 64.8]
    all_data["2006"] = [50, 69.81, 77.23, 80.96, 70.08]
    all_data["2007"] = [46, 77.48, 76.83, 85.62, 72.9]
    all_data["2008"] = [52, 76.59, 76.85, 88.62, 75.83]
    all_data["2009"] = [58, 79.94, 76.35, 94.45, 82.4]
    all_data["2010"] = [54, 88.67, 75.86, 95.59, 80.7]
    all_data["2011"] = [50, 92.29, 75.96, 95.66, 95.76]
    all_data["2012"] = [46, 92.8, 77.4, 95.76, 82.6]
        
    # now i will iterate over contents of dictionary
    # the process below does not necessarily produce stuff in same order as i entered
    # but that doesn't matter, does it?
    
    #for key in all_data: # for each key in dictionary, key is title and dict[key] is the array of values
    #    create_figure(key, all_data[key]) # send the stuff that keeps changing from plot to plot, ie data and title
    create_figure(all_data)
    
# default python syntax 
if __name__ == "__main__":
    main()
    
