import numpy as np 
from scipy import ndimage, misc
from skimage import io, exposure, img_as_ubyte
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

sample_data = 'test.jpg'


def main():
    img_input = img_as_ubyte(io.imread(sample_data, True))
    p1(img_input)   
    
    
def p1(img_input):
    my_histo(img_input)
    ski_histo(img_input)

    
def my_histo(file_input):
    img_array = np.zeros(256, dtype=int)

    for i in file_input:
        for j in i:
            img_array[j]+=1

    plt.xlim(0,256)
    plt.plot(img_array)    
    plt.show()

            
def ski_histo(file_input):
    img_ski = exposure.histogram(file_input, nbins=256)

    plt.xlim(0,256)
    plt.plot(img_ski[1], img_ski[0])
    plt.show()
  
  
main()