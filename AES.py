# AES 256 encryption/decryption using pycryptodome library

import base64
from io import BytesIO
from base64 import b64encode, b64decode
import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image

from key import store_key, load_key
from cipher_object import store_object, load_object


def get_msg(path):
    with open(path, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    return str(converted_string)


def encrypt(path):
    plain_text = get_msg(path)
    key = store_key()

    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the key
    private_key = hashlib.scrypt(
        key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    cipher_object = {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }
    store_object(cipher_object)

    encrypted = b64encode(cipher_text).decode('utf-8')
    return encrypted


def decrypt(encrypted):
    key = load_key()
    enc_dict = load_object()

    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    # cipher_text = b64decode(enc_dict['cipher_text'])
    cipher_text = b64decode(encrypted)
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the key and salt
    private_key = hashlib.scrypt(
        key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    return eval(decrypted)


# if __name__ == '__main__':
#     # # # # # # # # ENCRYPTING  # # # # # # # #
#
#     # plaintext = input("message: ")
#     path = "images/secret.jpg"
#     # plaintext = get_msg("images/secret.jpg")
#
#     print("encrypting...")
#     # First let us encrypt secret message
#     encrypted = encrypt(path)
#     # print(encrypted["cipher_text"])
#     print("encrypted: ", encrypted)
#
#     # # # # # # # # DECRYPTING  # # # # # # # #
#
#     # Let us decrypt using our original key
#     print("decrypting...")
#     decrypted = bytes.decode(eval(decrypt(encrypted)))
#     # print('*' * 30)
#     # print("encrypted['cipher_text']: ", encrypted['cipher_text'])
#     print("decrypted: ", decrypted)
#     print("type decrypted: ", type(decrypted))
#
#     image = Image.open(BytesIO(base64.b64decode(decrypted)))
#     image.show()
