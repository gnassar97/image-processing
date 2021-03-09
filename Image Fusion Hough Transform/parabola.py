# -*- coding: utf-8 -*-
"""lab8_part1_H04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cg2r6Aa0Z2a1labTO7pJ5zdwBmPZEQLM
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab8/parabola_horz.png
!ls

import numpy as np
import cv2
from sklearn.cluster import KMeans
from skimage.color import gray2rgb
import scipy.ndimage.filters as filters
from matplotlib import pyplot as plt

"""# Compute accumulator for parabola detection

A parabola with vertical axis is defined by the equation:

$(x − h)^2 = 4a(y − k)$

while one with horizontal axis is defined as:

$(y − k)^2 = 4a(x − h)$

where *`(h, k)`* is the center and *`a`* controls the width or spread of the parabola.

To simplify the problem, both parabolas have horizontal axes and are centered vertically so you only need to find *`a`* and *`h`* using the second equation.

1. choose suitable minimum and maximum values for *`a`* and *`h`* along with the number of values *`num_a`* and *`num_h`* to sample the respective intervals. Note that the two parabolas have different orientations so that *`a < 0`* for one and *`a > 0`* for the other.
2. create vectors *`a_vec`* and *`h_vec`* of sizes *`num_a`* and *`num_h`* respectively containing all possible values of *`a`* and *`h`* (hint: *`np.linspace`*)
3. create the accumulator array of size *`num_a`* $\times$ *`num_h`* containing all zeros and of type *uint64*
4. find locations of all edge pixels in the input image (hint: *`np.nonzero`*)
5. iterate over the edge pixels and fill up the accumulator array

  5.1. for each edge pixel *`x, y`*, iterate over all values of *`a`* and calculate the *`h`* corresponding to each *`a`* using the equation
$(y − k)^2 = 4a(x − h)$

  5.2. find the index of this `h` within `h_vec` which will give the column index for accumulator while the index of *`a`* within *`a_vec`* gives the corresponding row index.

  5.3. increment the accumulator entry corresponding to this row and column index by 1
6. filled accumulator array should look similar to this:
<img src="https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab8/parabola_horz_accumulator.png">


"""

def hough_parabola_horz(img, k):
  """
  add your code here
  """
  
  return accumulator, a_vec, h_vec

"""# Find the locations of two distinct local maxima in the accumulator array

1. choose a suitable integer *`n`* such that top *`n`* maxima will include pixels from both maxima

2. find the top *`n`* maxima (hint: *`np.argsort`*) and fill in *`max_idx`* which is a *`2 x n`* array containing the *`x, y`* coordinates of the *n* maxima. A binary image showing the maxima should look like this:
<img src="https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab8/parabola_horz_maxima.png">

3. use KMeans clustering to find 2 clusters among these *`n`* points:

    https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203

4. obtain the centers of the two clusters (hint: *`kmeans.cluster_centers_`*) that correspond to the indices of the two *`a, h`* pairs

5. extract the corresponding *`a, h`* values from *`a_vec`* and *`h_vec`*

6. the detected parabolas when drawn on the input image should closely overlay the source parabolas:

<img src="https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab8/parabola_horz_detections.png">

"""

def find_maxima(accumulator, a_vec, h_vec):
  """
  add your code here
  """

  maxima_img = np.zeros_like(accumulator).astype(np.uint8)
  for (x, y) in max_idx:
      maxima_img[x, y] = 255

  plt.figure()
  plt.title('Accumulator Maxima')
  plt.imshow(maxima_img, cmap='gray')
  plt.axis('off')

  return a1, h1, a2, h2

"""**Do not change anything in the following code**"""

def draw_parabola_horz(t_vec, num_t, a, h, k, img_w, img_h, out_img, col):
    for t_idx in range(num_t):
        t = t_vec[t_idx]

        y = 2 * a * t + k
        x = a * t * t + h

        if img_w > x > 0 and img_h > y > 0:
            out_img[int(y), int(x)] = col

        y = k - 2 * a * t

        if img_w > x > 0 and img_h > y > 0:
            out_img[int(y), int(x)] = col

img = cv2.imread('parabola_horz.png', 0)
img_h, img_w = img.shape

# vertically centered parabolas
k = img_h / 2

accumulator, a_vec, h_vec = hough_parabola_vert(img, k)

a1, h1, a2, h2 = find_maxima(accumulator, a_vec, h_vec)

t_min, t_max, num_t = 0, 100, 10000
t_vec = np.linspace(t_min, t_max, num_t)

detections_img = gray2rgb(img)
draw_parabola_horz(t_vec, num_t, a1, h1, k, img_w, img_h, detections_img, (0, 255, 0))
draw_parabola_horz(t_vec, num_t, a2, h2, k, img_w, img_h, detections_img, (0, 255, 0))

accumulator_img = accumulator.astype(np.float32) / np.amax(accumulator)

plt.figure()
plt.title('Input image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.figure()
plt.title('Accumulator')
plt.imshow(accumulator_img, cmap='gray')
plt.axis('off')

plt.figure()
plt.title('Detected Parabolas')
plt.imshow(detections_img, cmap='gray')
plt.axis('off')