import base64
from PIL import Image
from io import BytesIO


def encode_image(path):
    data = None
    with open(path, "rb") as image_file:
        print("image_file: ", image_file)
        data = base64.b64encode(image_file.read())
        print("stego_image encrypted")
    return str(data)


def decode_image(data, output_path):
    im = Image.open(BytesIO(base64.b64decode(data)))
    print("stego_image decrypted")
    im.save(output_path, 'PNG')
    im.show()


if __name__ == '__main__':
    print("encoding ...")
    data = encode_image("images/secret.jpg")
    print("data : ", data)
    print("type(data) : ", type(eval(data)))
    print("str(data) : ", str(data))

    print("decoding ...")
    decode_image(data, 'output/image1.png')
