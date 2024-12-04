# Implement a custom colormap for a Matplotlib plot.


#import necessary libraries:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# create custom colormap using LinearSegmentedColormap
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]
no_of_colors = 256
colormapping = LinearSegmentedColormap.from_list('custom_cmap', colors, N=no_of_colors)
"""
        LinearSegmentedColormap.from_list() make a colormap using
        colors specified in the colors list.
"""

#generate random data
random_data = np.random.randn(10, 10)
"""
        np.random.randn() -> generates random numbers from a standard normal distribution
        standard normal distribution : mean=0 and standard deviation=1
"""

#plot 3D surface
fig, axes = plt.subplots(figsize=(10, 5))
color_ax = axes.imshow(random_data, cmap=colormapping)
        #color bar
color_bar = fig.colorbar(color_ax)
color_bar.set_label('value')

#plot values
axes.set_title('custom colormap for a Matplotlib plot')
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')

#show plot
plt.show()
