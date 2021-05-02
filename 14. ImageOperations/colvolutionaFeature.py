""" Convolutional Operations on Image using numpy """

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ConvolutionalOperations:
    def __init__(self, image_path):
        self.image_path = image_path

    def _color_to_gray(self):
        gray_img = np.array(Image.open(self.image_path).convert('L'))
        return gray_img
        
    
    
if __name__ == '__main__':
    image_path = './Media/apple.jpeg'
    obj = ConvolutionalOperations(image_path)
    output = obj._color_to_gray()
    plt.imshow(output)
    plt.show()