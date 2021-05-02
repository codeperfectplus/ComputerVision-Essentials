import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImageOperation:
    """ Simple image operations using numpy arrays """
    def __init__(self, img_array: np.ndarray):
        self.img_array = img_array
        
    def color_to_gray(self):
        img = self.img_array
        gray = np.dot(img[...,:3], [0.299, 0.587, 0.144])
        return gray
    
    def color_inversion(self):
        inv_img = 255 - self.img_array
        return inv_img
    
    def color_reduction(self):
        
        im_32 = self.img_array // 32 * 32
        im_128 = self.img_array // 128 * 128
        
        im_red = np.concatenate((self.img_array, im_32, im_128), axis=1)
        return im_red        
    
    def gamma_correction(self):
        
        img = self.img_array
        img1 = 255.0 * (self.img_array / 255.0)**(1/2.2)
        img2 = 255.0 * (self.img_array / 255.0)**2.2
        
        return np.concatenate((img, img1, img2), axis=1)
    
    def slice_n_paste(self):
        
        src = np.resize(self.img_array, (128, 128))
        dst = np.resize(self.img_array, (256, 256)) // 4
        
        dst_copy = dst.copy()
        
        dst_copy[110:200, 110:200] = src[10:100, 10:100]
        return dst_copy
    
    def image_binarization(self):
        
        img = self.img_array
        gray = np.dot(img[...,:3], [0.299, 0.587, 0.144])
        thresh = 128
        max_val = 255.0
        
        im_bin = (gray > thresh) * max_val
    
        return im_bin
        
        
if __name__ == '__main__':
    image_path = './Media/apple.jpeg'
    img_array = np.array(Image.open(image_path))
    obj = ImageOperation(img_array)
    output = obj.gamma_correction()
    plt.imshow(output)
    plt.show()