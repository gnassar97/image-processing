# -*- coding: utf-8 -*-
"""Lab1_part_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19RzCRvEp9bJPTdkKbIq7tY7dyR0-ddmG
"""

!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab1/day.jpg
!wget -q -nc https://raw.githubusercontent.com/pseprivamirakbarnejad/cmput206lab/master/Lab1/night.jpg
!ls

import numpy as np
from skimage import io, exposure, img_as_ubyte
import matplotlib.pyplot as plt
import math

day = "day.jpg"
night = "night.jpg"

def main():

    day_input = img_as_ubyte(io.imread(day, as_gray = True))
    night_input = img_as_ubyte(io.imread(night, as_gray = True))
   
    
    day_histo = scipy_histo(day_input)
    
    night_histo = scipy_histo(night_input)
    
    
    plt.legend(('day.jpg','night.jpg'), loc=2)
    plt.show()

    BC(day_histo[0], night_histo[0])
   

def scipy_histo(image):

    library_histo = exposure.histogram(image, nbins=256)
    plt.xlim(0,256)
    plt.ylim(0,10000)
    plt.plot(library_histo[0])
    return library_histo


def BC(histo_1, histo_2):
    
    histo_1 = normalization(histo_1)
    histo_2 = normalization(histo_2)

    summation = 0

    for i in range(len(histo_1)):
        summation += math.sqrt((histo_1[i]*histo_2[i]))

    print("The calculated Bhattacharyya Coefficient is: ",summation)
    
def normalization(hist):
    cumulative = 0
    for i in hist:
        cumulative += i

    normal_histo = np.zeros(256)
    for i in range(len(normal_histo)):
        normal_histo[i] = hist[i]/cumulative
      
    return normal_histo

main()