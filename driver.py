import base64
from io import BytesIO

from PIL import Image

import welcome
from dct import dct_compress
from image_crypto import encode_image, decode_image
from lsb import Encode, Decode
from aes_test import encrypt, decrypt

if __name__ == '__main__':
    welcome.welcome()
    choice = input("""Please select an option:\n- 1 for Encode.\n- 2 for Decode.\n""")
    # key = bytes(token_hex(16), encoding='utf-8')  # creates random key of size 16

    print("Image path  = images/small.jpg")
    stego_path = 'images/secret.jpg'
    in_path = "images/test200.jpg"
    out_path = "output/cover-after-lsb.png"

    if choice == "1":
        print("******* CHOSE 1 *******")

        print("*** inside dct compress ***")
        path = dct_compress(stego_path)

        # print("*** image encrypt ***")
        # data = encode_image(path)

        print("*** image encode AES ***")
        data = encrypt(path)

        print("*** encode image lsb ***")
        Encode(in_path, data, out_path)

    elif choice == "2":
        print("******* CHOSE 2 *******")

        print("*** decode image lsb ***")
        decoded_img = Decode(out_path)

        # print("*** image decrypt ***")
        # decode_image(data, "output/stego-img.png")

        print("decoded_img after lsb-decode: ", decoded_img)

        print("*** image encode AES ***")
        data = decrypt(decoded_img)

        print("*** stego image ***")
        image = Image.open(BytesIO(base64.b64decode(data)))
        image.show()

    else:
        print("Invalid choice")
        exit(1)
