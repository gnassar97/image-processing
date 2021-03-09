# -*- coding: utf-8 -*-
"""Lab2_part_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WWdInNbJDl8C3tWQ2IYCfhKHtvj4Msqs
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab2/moon.png
!ls

#Your Code
import numpy as np 
from skimage import io, exposure, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.filters import rank
from skimage.morphology import disk

img = io.imread('moon.png')  

img_laplacian = np.zeros (img.shape, dtype = int)
laplacian = np.array([
    [-1, -1, -1], 
    [-1,  8, -1], 
    [-1, -1, -1]
])
for x in range(1, img.shape[0] - 1):
    for y in range(1, img.shape[1] - 1):
        value = laplacian * img[(x - 1):(x + 2), (y - 1):(y + 2)]
        img_laplacian[x, y] = min(255, max(0, value.sum ()))

img_custom1 = np.zeros(img.shape, dtype = int)
custom1 = np.array([
    [0, 0, 0], 
    [0, 1, 0], 
    [0, 0, 0]
])
for x in range(1, img.shape[0] - 1):
    for y in range(1, img.shape[1] - 1):
        value = custom1 * img[(x - 1):(x + 2), (y - 1):(y + 2)]
        img_custom1[x, y] = min(255, max(0, value.sum ()))

img_custom2 = np.zeros(img.shape, dtype = int)
custom2 = np.array([
    [0, 0, 0], 
    [0, 0, 1], 
    [0, 0, 0]
])
for x in range(1, img.shape[0] - 1):
    for y in range(1, img.shape[1] - 1):
        value = custom2 * img[(x - 1):(x + 2), (y - 1):(y + 2)]
        img_custom2[x, y] = min(255, max(0, value.sum ()))

img_mean = np.zeros(img.shape, dtype = int)
mean_filter = np.array([
    [1/9, 1/9, 1/9], 
    [1/9, 1/9, 1/9], 
    [1/9, 1/9, 1/9]
])
for x in range(1, img.shape[0] - 1):
  for y in range(1, img.shape[1] - 1):
    value =  mean_filter * img[(x - 1):(x + 2), (y - 1):(y + 2)]
    img_mean[x, y] = min(255, max(0, value.sum ()))


#image + (image - image * convol)

part4 = img + (img - img_mean)

#selem = disk(20)
#normal_result = rank.mean(img, selem=selem)

#part4b = img + (img - normal_result)


print("Original Image Below")
plt.imshow(img, cmap="gray")
plt.show()
print("Laplacian Filtered Image Below")
plt.imshow(img_laplacian, cmap="gray")
plt.show()
print("First Custom Filtered Image Below")
plt.imshow(img_custom1, cmap="gray")
plt.show()
print("Second Custom Filtered Image Below")
plt.imshow(img_custom2, cmap="gray")
plt.show()
print("Convolution Filtered Image Below")
plt.imshow(part4, cmap="gray")
plt.show()
#print("Mean Filtered Image Below")
#plt.imshow(img_mean, cmap="gray")
#plt.show()
#print("Testing")
#plt.imshow(normal_result, cmap="gray")
#plt.show()
#print("Testing")
#plt.imshow(part4b, cmap="gray")
#plt.show()
