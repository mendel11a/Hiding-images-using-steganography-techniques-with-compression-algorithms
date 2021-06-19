import base64

from PIL import Image

import Welcome
from DCT import dct_compress
from LSB import Encode, Decode
from AES import encrypt, decrypt


def save_img_data_and_open(filename, img_data):
    with open(filename, 'wb') as f:
        f.write(base64.decodebytes(img_data))

    img = Image.open(filename)
    img.show()


if __name__ == '__main__':
    Welcome.welcome()

    stego_path = 'images/secret.jpg'
    in_path = "images/test200.jpg"
    out_path = "output/cover-after-lsb.png"

    choice = input("""Please select an option:\n- 1 for Encode.\n- 2 for Decode.\n""")

    if choice == "1":
        print("\n******* CHOSE 1 *******")

        print("DCT Compressing ...")
        stego_path = dct_compress(stego_path)
        print("-> Stego-image compressed.\n")

        print("Encoding ...")

        print("*** AES stego-image encrypting ...  ***")
        img_data = encrypt(stego_path)
        print("-> stego_image encrypted.\n")

        print("*** LSB Encoding stego-image into cover-image ***")
        Encode(in_path, img_data, out_path)
        print("-> Image Encoded Successfully.\n")

    elif choice == "2":
        print("\n******* CHOSE 2 *******")
        print("Decoding ...")

        print("*** LSB Decoding stego-image from cover-image ***")
        img_data = Decode(out_path)
        print("-> Image Decoded Successfully.\n")

        print("*** AES stego-image decrypting ...  ***")
        img_data = decrypt(img_data)
        print("-> stego_image encrypted.\n")

        print("Displaying secret image ...")
        filename = 'output/from-img-data.png'
        save_img_data_and_open(filename, img_data)

    else:
        print("Invalid choice")
        exit(1)
