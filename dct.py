import PIL.Image as Image
from scipy.fftpack import dct, idct
from skimage.io import imread, imsave
import numpy as np


# implement 2D DCT
def dct2(img):
    return dct(dct(img.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


def dct_compress(path):
    print("path in dct_compress :", path)
    img = imread(path)

    try:
        img = idct2(dct2(img))
        imsave("output/stego-after-dct.jpg", img)
        return "output/stego-after-dct.jpg"
    except Exception as ex:
        print(ex)
        exit(1)
