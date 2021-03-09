# -*- coding: utf-8 -*-
"""Lab_4_part_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dadfZsWxCD0zitbB8x1V8daglaulCC0F
"""

import os
from sklearn.cluster import KMeans
from scipy import spatial
from skimage import io, color, img_as_float
import numpy as np
import matplotlib.pyplot as plt
from math import floor

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab4/lena.png
!ls

# Finds the closest colour in the palette using kd-tree.
def nearest(palette, colour):
    dist, i = palette.query(colour)
    return palette.data[i]

# Make a kd-tree palette from the provided list of colours
def makePalette(colours):
    #print(colours)
    return spatial.KDTree(colours)

# Dynamically calculates and N-colour palette for the given image
# Uses the KMeans clustering algorithm to determine the best colours
# Returns a kd-tree palette with those colours
def findPalette(image, nColours):
    img = image.ravel().reshape(-1,3)
    kmean = KMeans(n_clusters=nColours, max_iter=1000).fit(img)
    colours = kmean.cluster_centers_
    return makePalette(colours)
  


def FloydSteinbergDitherColor(img, palette):
#***** The following pseudo-code is grabbed from Wikipedia: https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering.  
#   for each y from top to bottom ==>(height)
#    for each x from left to right ==> (width)
#       oldpixel  := pixel[x][y]
#       newpixel  := nearest(oldpixel) # Determine the new colour for the current pixel
#       pixel[x][y]  := newpixel 
#       quant_error  := oldpixel - newpixel
#       pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error * 7 / 16
#       pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error * 3 / 16
#       pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error * 5 / 16
#       pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error * 1 / 16
  for i in range(len(img)):
    for j in range(len(img)):
      prev_red, prev_green, prev_blue = img[i][j]
      new_red, new_green, new_blue = nearest(palette, img[i][j])

      img[i][j][0] = new_red
      img[i][j][1] = new_green
      img[i][j][2] = new_blue

      quant_error_red = prev_red - new_red
      quant_error_blue = prev_blue - new_blue
      quant_error_green = prev_green - new_green

      if i < len(img) - 1:
        img[i+1][j][0] = img[i+1][j][0] + quant_error_red*(7/16)
        img[i+1][j][1] = img[i+1][j][1] + quant_error_green*(7/16)
        img[i+1][j][2] = img[i+1][j][2] + quant_error_blue*(7/16)

      if j < len(img) - 1:
        img[i][j+1][0] = img[i][j+1][0] + quant_error_red*(5/16)
        img[i][j+1][1] = img[i][j+1][1] + quant_error_green*(5/16)
        img[i][j+1][2] = img[i][j+1][2] + quant_error_blue*(5/16)
        
      if i > 0 and j < len(img) - 1:
        img[i-1][j+1][0] = img[i-1][j+1][0] + quant_error_red*(3/16)
        img[i-1][j+1][1] = img[i-1][j+1][1] + quant_error_green*(3/16)
        img[i-1][j+1][2] = img[i-1][j+1][2] + quant_error_blue*(3/16)

      if j < len(img) - 1 and i < len(img) - 1:
        img[i+1][j+1][0] = img[i+1][j+1][0] + quant_error_red*(1/16)
        img[i+1][j+1][1] = img[i+1][j+1][1] + quant_error_green*(1/16)
        img[i+1][j+1][2] = img[i+1][j+1][2] + quant_error_blue*(1/16)
    

        
    return img


if __name__ == "__main__":
  
    nColours = 8 # The number colours: change to generate a dynamic palette

    imfile = "lena.png"

    
    image = io.imread(imfile)

    # Strip the alpha channel if it exists
    image = image[:,:,:3]

    # Convert the image from 8bits per channel to floats in each channel for precision
    image = img_as_float(image)

    # Dynamically generate an N colour palette for the given image
    palette = findPalette(image, nColours)
    colours = palette.data
    
    colours = img_as_float([colours.astype(np.ubyte)])[0]
    
    img = FloydSteinbergDitherColor(image, palette)

    plt.imshow(img)
    plt.show()

