from PIL import Image


def jpg2png(in_path, out_path):
    im1 = Image.open(r'' + in_path)
    im1.save(r''+out_path)
