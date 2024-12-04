# Generate 3D surface plots with custom color maps and shading.


#import necessary libraries:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#generate random data using numpy:
x = np.linspace(1, 10, 10)
y = np.linspace(9, 10 ,10)
x, y = np.meshgrid(x, y)
"""
        there are several mathematical function like:
        Sine Function -> z=sin(sqrt(x^2+y^2)) -> used to represent waves or oscillations
        Gaussian Function -> z=exp(-(x^2+y^2)/2) -> for probability distributions
        Sinusoidal Waves -> z=sin(x)cos(y) -> create wave patterns in two directions
        we use sine function to make 3d surface
"""
z = np.sin(np.sqrt(x**2 + y**2))

# create custom colormap using LinearSegmentedColormap
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]
no_of_colors = 256
colormapping = LinearSegmentedColormap.from_list('custom_cmap', colors, N=no_of_colors)
"""
        LinearSegmentedColormap.from_list() make a colormap using
        colors specified in the colors list.
"""

#plot 3D surface
fig = plt.figure(figsize=(10, 5)) #size will be 10x5 (inch)
axes = fig.add_subplot(111, projection='3d')
        #surface with colormap
surface = axes.plot_surface(x, y, z, cmap=colormapping)

#color bar
color_bar = fig.colorbar(surface, ax=axes, shrink=0.5)
color_bar.set_label('color scale')

#plot values
axes.set_title('3D surface plots with custom color maps and shading')
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_zlabel('z-axis')

#show plot
plt.show()