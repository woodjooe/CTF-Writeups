from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES


enc = open('enc','rb').read()


def aes_dec(key, ct):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.decrypt(ct)
    

enc = [enc[i:i + AES.block_size] for i in range(0, len(enc), AES.block_size)]
pt = enc.copy()

for i in range(len(enc)-1, 0, -1):
    print(i)
    pt[i] = aes_dec(enc[i-1],pt[i])

pt[0] = aes_dec(pt[-1],pt[0])

flag = b''
flag = flag.join(pt)

print(flag)
