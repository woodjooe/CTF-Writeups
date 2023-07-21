from pwn import *
r = remote('amt.rs',31692)


NUM = 2048

y=pow(2,NUM)
for j in range(10):
    L=[]
    x0 = 0
    for i in range(1412):
        r.sendlineafter(": ",str(x0)+' '+str(y))
        
        s=r.recvuntil('\n').decode()
        
        p= int(s.split('\n')[0])
        print(p)
        if(p!=y):

            x0 += p
            
            L.append(p)


    r.sendlineafter(": ",str(y-x0))
s=r.recvuntil('\n').decode()
print(s)