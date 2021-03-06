# -*- coding: utf-8 -*-
"""Lab2_part_3 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uofQXcjrwVTnVqkPxAvBKMtSFEbgOCRS
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab2/damage_mask.png
!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab2/damage_cameraman.png
!ls

#DISCLAIMER = THIS CODE TAKES A LONG TIME TO RUN, IF YOU WOULD LIKE IT TO WORK A LOT FASTER, REDUCE THE NUMBER IN THE GAUSSIAN FOR LOOP (5 or 10 is enough to see a noticeable difference in the photo)
import numpy as np 
from skimage import io, exposure, img_as_ubyte, filters
import matplotlib.pyplot as plt

img = io.imread('damage_cameraman.png', as_gray=True)
msk = io.imread('damage_mask.png', as_gray=True)
final_img = io.imread('damage_cameraman.png', as_gray=True)

height = np.size(final_img,0)
width = np.size(final_img,1)

bad_pixels = []

for i in range(height):
  for j in range(width):
    if msk[i][j].all() == 0:
      bad_pixels.append((i,j))

gaussian = img
for i in range(20):
  gaussian = filters.gaussian(gaussian)
  for y in range(len(gaussian)):
    for x in range(len(gaussian[y])):
      if (y,x) not in bad_pixels:
        gaussian[y][x] = img[y][x]

print("Original Image Below")
plt.imshow(img,cmap='gray')
plt.show()
print("Gaussian Inpainting Image Below")
plt.imshow(gaussian,cmap='gray')
plt.show()

