# -*- coding: utf-8 -*-
"""Lab7_Part0_H04_eclass.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rv3tSsybk-7AdTF9GH7bmI4TRa11UYdb

**Parts that you should complete are specified by ```#TODO```.

In this assignment we will use SLIC algorithm for image segmentation. You should use ```skimage.segmentation.slic```. Afterwards, we will use RAG merging algorithm with different thresholds.

You should do the following steps:
- Apply the SLIC algorithm on the image. Set ```n_segments=20``` and ```compactness=20.0```. Show the result.  
- Afterwards, run the RAG mergin algorithm with threshold 10 on the edges. Show the output. You should use the functions [graph.rag_mean_color](https://scikit-image.org/docs/dev/api) and [graph.cut_threshold](https://scikit-image.org/docs/dev/api/skimage.future.graph.html#skimage.future.graph.cut_threshold). Afterwards, you should use the function ```display_edges``` (provided in the notebook) to show the graph on the image.


- The last cell shows the outputs for different values of threshold. Explain the role of the threshold parameter, and justify the outputs. Write down your answer in the part specified by ```TODO:answer```.
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab7/horse.jpg
!ls

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from skimage import data, io, segmentation, color
from skimage import io, filters, img_as_ubyte
from scipy.signal import convolve2d as conv2
from skimage.color import rgb2hsv
from skimage.future import graph
import scipy.ndimage
import skimage
from skimage.measure import regionprops
from skimage import draw
import math
#from lab7util import *
def display_edges(image, g, threshold):
    """Draw edges of a RAG on its image
 
    Returns a modified image with the edges drawn.Edges are drawn in green
    and nodes are drawn in yellow.
 
    Parameters
    ----------
    image : ndarray
        The image to be drawn on.
    g : RAG
        The Region Adjacency Graph.
    threshold : float
        Only edges in `g` below `threshold` are drawn.
 
    Returns:
    out: ndarray
        Image with the edges drawn.
    """
    image = image.copy()
    plt.imshow(image)
    for edge in g.edges:#g.edges_iter():
      try:
          n1, n2 = edge
          #print(g[n1][n2]['weight'])
          if g[n1][n2]['weight'] < threshold :
            r1, c1 = rag.nodes[n1]['centroid'] #map(int, rag.nodes[n1]['centroid'])
            r2, c2 = rag.nodes[n2]['centroid'] #map(int, rag.nodes[n2]['centroid'])
    
            line  = plt.plot([c1,c2],[r1,r2])#draw.line(r1, c1, r2, c2)
            circle = plt.Circle((r1,c1),20)
    
            # if g[n1][n2]['weight'] < threshold :
            #     image[line] = 0,1,0
            # image[circle] = 1,1,0
      except:
        pass
    return image

img_name = "horse.jpg"
img = io.imread(img_name)
plt.figure()
plt.imshow(img)
plt.show()

#TODO: Apply the SLIC algorithm on the image. Show the result.
slic_img = segmentation.slic(img, n_segments = 20, compactness = 20.0)
plt.imshow(slic_img)
plt.show()

#TODO: run the RAG mergin algorithm with threshold 10 on the edges. Show the output.

labels = segmentation.slic(img, n_segments= 20, compactness= 20.0)
rag = graph.rag_mean_color(img, labels)
output = graph.cut_threshold(labels, rag, 10)

regions = regionprops(labels)
for region in regions:
  rag.nodes[region['label']]['centroid'] = region['centroid']

edges = display_edges(output,rag,10)



plt.imshow(labels), plt.title("the edges (after applying threshold)")
plt.show()
plt.imshow(output),plt.title("final output (threshold = 10)")
plt.show()



"""#TODO:answer

Explain the role of the threshold parameter, and justify the outputs. Write down your answer in the part specified by TODO:answer.



"""

The threshold parameter determines the minimum strength that an edge requires to remain as an edge, any region that has a smaller edge weight than the threshold is merged. The higher the threshold, the more edges are combined. 

In the above example (on the right side, the output images), when the threshold increases in the output images, weaker edges are combined, and the number of these edges that are being combined increases as the threshold value is increased. This is why you see the areas of the image merging until there are significantly less than the original image.

On the left side of the above example, the display_edges function is drawing edges below the threshold value. As the threshold value increases, more edges qualify to be drawn as below the threshold. These are the edges that would be combined in the output images.