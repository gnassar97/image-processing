# -*- coding: utf-8 -*-
"""Lab_3_part_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zYdR5cnw85GBjHSa5QMlKYIj5vF4ZhT3
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab3/ex1.jpg
!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab3/ex2.jpg
!ls

import numpy as np 
from skimage import io, exposure, img_as_ubyte, filters
import matplotlib.pyplot as plt
import scipy as sp
import math
import random

img = io.imread("ex1.jpg", as_gray=True).astype(np.float32)

height = np.size(img,0)
width = np.size(img,1)

kernel_g = np.zeros(((2*height+1),(2*width+1)),np.float32)
kernel_c = np.zeros(((2*height+1),(2*width+1)),np.float32)
x_input = int(input("X Value: "))
y_input = int(input("Y Value: "))
sigma_value = int(input("Sigma Value: "))
final_img_gaussian = np.copy(img)
final_img_cauchy = np.copy(img)
gaussian_img = filters.gaussian(final_img_gaussian,sigma_value)

kernel_h = 2*height+1
kernel_w = 2*width+1

for i in range(kernel_h):
  for j in range(kernel_w):
    kernel_g[i,j] = math.exp(-((j-width)*(j-width)+(i-height)*(i-height))/(sigma_value*sigma_value))
    kernel_c[i,j] = 1/(1+((j-width)*(j-width)+(i-height)*(i-height))/(sigma_value*sigma_value))
    



y = height - y_input
x = width - x_input
used_y = height + y
used_x = width + x

gaussian_mask = kernel_g[y:used_y,x:used_x]
cauchy_mask = kernel_c[y:used_y,x:used_x]

g_img_weight2 = np.multiply(final_img_gaussian, 1-gaussian_mask)

for y in range(len(final_img_gaussian)):
  for x in range(len(final_img_gaussian[y])):
    final_img_gaussian[y][x] = gaussian_mask[y][x] * gaussian_img[y][x] + (1 - gaussian_mask[y][x])*img[y][x] 

for y in range(len(final_img_cauchy)):
  for x in range(len(final_img_cauchy[y])):
    final_img_cauchy[y][x] = gaussian_img[y][x] * cauchy_mask[y][x] + (1 - cauchy_mask[y][x])*img[y][x] 


plt.imshow(img, cmap = 'gray'),plt.title("Original Image"),plt.xticks([]),plt.yticks([])
plt.show()

plt.imshow(final_img_gaussian, cmap = 'gray'),plt.title("Gaussian Locally Blurred Image"),plt.xticks([]),plt.yticks([])
plt.show()

plt.imshow(final_img_cauchy, cmap = 'gray'),plt.title("Cauchy Locally Blurred Image"),plt.xticks([]),plt.yticks([])
plt.show()