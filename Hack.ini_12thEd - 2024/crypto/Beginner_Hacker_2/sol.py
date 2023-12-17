from Crypto.Util.number import bytes_to_long, long_to_bytes
from string import printable
import random

#Found the first key by xoring the first encrypted text with 'shellmates{'

key0 = b' ^Q\xbd\x82*\xf4\xbbh\x1f\x98'
enc = b'S64\xd1\xeeG\x95\xcf\rl\xe3n\x7f\x013\xd3\xf4M\x80\xff<@\xcd\x18h\te\xe2\xa3d\xad\x9f\r/\xf6X\x7f\x0cb\xcf\xe3O\x8d\xd2\x00J\xd9\x18W\x15b\xe2\xc0d\xbd\xde7V\xebn\x7f\x1d\x1f\xe2\xc6G\xc4\xe4-s\xc7V'

def encrypt(plaintext, key):
    ciphertext = b''
    ciphertext = ciphertext.join([long_to_bytes(plaintext[i] ^ key[i%len(key)]) for i in range(len(plaintext))])
    
    return ciphertext

def unshuffle(shuffled_message, key):
    random.seed(bytes_to_long(key))
    l = list(range(len(shuffled_message)))
    random.shuffle(l)
    out = [''] * len(shuffled_message)
    for i, x in enumerate(l):
        out[x] = chr(shuffled_message[i])
    return ''.join(out)


for i in range(256):

    key = key0 + long_to_bytes(i)
    mess = encrypt(enc, key)
    #print(long_to_bytes(mess[-1]))


    try:
        mess.decode()
        if(long_to_bytes(mess[-1]) != b'}'):
            raise Exception()
        flag=mess
        keyT=key
    except:
        None
print(flag)
pt = flag[11:-1]
flag = unshuffle(pt, keyT)
print('shellmates{' + flag + '}')