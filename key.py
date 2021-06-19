import pickle
import random
import string


def store_key():
    key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
    outputFile = 'key.data'
    fw = open(outputFile, 'wb')
    pickle.dump(key, fw)
    fw.close()
    return key


def load_key():
    inputFile = 'key.data'
    fd = open(inputFile, 'rb')
    key = pickle.load(fd)
    fd.close()
    return key

# if __name__ == '__main__':
#     store_key()
#     load_key()

