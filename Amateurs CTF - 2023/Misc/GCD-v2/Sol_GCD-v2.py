import sys
sys.set_int_max_str_digits(100000)

L=[]


NUM = 128

#More primes = faster, but I coudn't add more primes due to server telling me off.
#And so I had to rely on luck, which is why this script runs forever till it luckily does the job
#(5 times is usually enough unless you're very unlucky)
p0 = 2*3*5*7*11*13*17*19*23*29*31*37*41*43*47*53*59*61*67*71*73*79*83*89*97
y = pow(p0,100)
x0=0

from pwn import *
while(True):
    r = remote('amt.rs',31693)


    for i in range(16):
        r.sendlineafter(": ",str(x0)+' '+str(y))
        
        s=r.recvuntil('\n').decode()
        
        p= int(s.split('\n')[0])
        print(p)
        if(len(bin(p))<=130): 
# bit number less than 128, 130 is here because bin() returns '0b' + str(bits) 
# so u gotta take those 2 extra '0b' into account

            x0 += p
            L.append(p)


    r.sendlineafter(": ",str(p-x0))
    s=r.recvuntil('\n').decode()
    if("amateursCTF" in s):
        break
print(s)