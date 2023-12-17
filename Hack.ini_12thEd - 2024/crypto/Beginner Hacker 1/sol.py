from Crypto.Util.number import bytes_to_long, long_to_bytes
from string import printable
import random

#Found the first key by xoring the first encrypted text with 'shellmates{'

key0 = b'o^W\xe3\x10\x04\xfb\xd9\x12\xc9}'
enc = b'\x1c62\x8f|i\x9a\xadw\xba\x06N\x85\x08+d\xb0C[\xa9\xed|\x8dM\x12\xb4\\\r$\xbct4\x9e\xaaM\x872\x0b\x85.\x12\x00\xa2iW\xa4\xb4W\xfd3 \xa3\x00\x0b\x08\xb1O \x9e\x9ag\xbbN^\xa7'

def encrypt(plaintext, key):
    ciphertext = b''
    ciphertext = ciphertext.join([long_to_bytes(plaintext[i] ^ key[i%len(key)]) for i in range(len(plaintext))])
    
    return ciphertext




for i in range(256):
    for j in range(256):
        key = key0 + long_to_bytes(i) + long_to_bytes(j)
        mess = encrypt(enc, key)
        #print(long_to_bytes(mess[-1]))


        try:
            mess.decode()
            if(long_to_bytes(mess[-1]) != b'}'):
                raise Exception()
            print(mess)
        except:
            None
