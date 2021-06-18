from secrets import token_hex

from Crypto.Cipher import AES
import base64
import PIL.Image as Image
import io


def imageToData(img_path):
    with open(img_path, "rb") as imageFile:
        data = base64.b64encode(imageFile.read())
        return data


def encrypt(key, data):
    enc_cipher = AES.new(key, AES.MODE_EAX)
    encrypted_data = enc_cipher.encrypt(data)
    return enc_cipher, encrypted_data


def dec_AES(key, encrypted_data):
    encrypted_data = bytes(encrypted_data, encoding='utf-8')
    print("type encrypted_data to byte :\n", type(encrypted_data))
    enc_cipher = AES.new(key, AES.MODE_EAX)
    dec_cipher = AES.new(key, AES.MODE_EAX, enc_cipher.nonce)
    decrypted_data = dec_cipher.decrypt(encrypted_data)

    b = base64.b64decode(decrypted_data)
    img = Image.open(io.BytesIO(b))
    img.show()
    img.save("images/img1.jpg")

    return decrypted_data


def enc_AES(key, image_path):
    data = imageToData(image_path)
    cipher, encrypted_data = encrypt(key, data)
    print("type of encrypted_data :\n", type(encrypted_data))
    print("type of encrypted_data to string :\n", type(str(encrypted_data)))
    encrypted_data = str(encrypted_data[2: -1])

    return cipher, encrypted_data


if __name__ == "__main__":
    key = bytes(token_hex(16), encoding='utf-8')  # creates random key of size 16
    print("key : ", key)
    data = imageToData('images/test50.jpg')

    print("&&& image string before encryption :", len(data))
    print("&&&" * 5)

    cipher, encrypted_data = encrypt(key, data)
    decrypted_data = dec_AES(cipher, encrypted_data)
    print('*' * 5)
    print("encrypted_data :", len(encrypted_data))
    print("encrypted_data :", type(encrypted_data))
    print('*' * 5)

    print("decrypted_data :", len(decrypted_data))
    print("decrypted_data :", type(decrypted_data))
    print('*' * 5)

    print("decrypted_data :", decrypted_data)
