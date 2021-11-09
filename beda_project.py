import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from skimage.io import imread, imshow
image1 = imread("C:\Users\ASUS\Desktop\African-savanna-elephant.jpg")
imshow(image1);
image2 = imread('African-savanna-elephant.jpg', as_gray=True)
imshow(image2);
#Shape of images
print(image1.shape)
print(image2.shape)
print(image1.size)
print(image2.size)
pixel_feat1 = np.reshape(image2, (1080 * 1920))
pixel_feat1

