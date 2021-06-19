from PIL import Image
from scipy.fftpack import dct, idct
from skimage.io import imread, imsave


# implement 2D DCT
def dct2(img):
    return dct(dct(img.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


def dct_compress(path):
    jpg_formats = ['jpg', 'jpeg', 'JPG', 'JPEG']
    valid_formats = ['jfif', 'JFIF', 'bmp', 'BMP', 'jp2', 'JP2']
    imagePath, imageFormat = path.split(".")

    if imageFormat not in jpg_formats and imageFormat not in valid_formats:
        raise ValueError("Invalid image format for DCT compression.")

    if imageFormat in valid_formats:
        new_path = imagePath + '-to-jpg.jpg'
        temp_img = Image.open(r'' + path)
        temp_img.save(new_path)
        path = new_path

    img = imread(path)
    try:
        img = idct2(dct2(img))
        imsave("output/stego-after-dct.jpg", img)
        return "output/stego-after-dct.jpg"
    except Exception as ex:
        print(ex)
        exit(1)
