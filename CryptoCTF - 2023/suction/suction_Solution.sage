from sage.all import factor
from sage.rings.fast_arith import prime_range
from Crypto.Util.number import long_to_bytes,bytes_to_long
import sympy
from os import urandom


#random number that is 3 bytes long, to optimize the search for the modulus N
Rand = bytes_to_long(urandom(3))
#Produces about 10 possible Modulus numbers to work with instead of 256, in this case

Primes= sage.rings.fast_arith.prime_range(1,Rand)



print('length of PrimeList = '+str(len(Primes)))

r=8

PKEY = 55208723145458976481271800608918815438075571763947979755496510859604544396672

n = bytes_to_long(long_to_bytes(PKEY)[ : - (16 - r) // 8 ]) << 8
e= bytes_to_long(long_to_bytes(PKEY)[- (16 - r) // 8 : ]) << 8


enc = 127194641882350916936065994389482700479720132804140137082316257506737630761 << 8


LN=[]
List_D_N_E=[]
Lfac=[]


for i in range(n,n+256):

    if sympy.isprime(i):
        continue
        
    C=True
    
    for j in Primes:
    
        if (i%j)==0:
        
            C=False
            break
    print('Step : '+ str(i-n) +' / 256')
    
    if(C):
    
        fac = factor(i)
        
        if (len(long_to_bytes(fac[0][0])) == (128 // 8)):
        
            print(fac)
            LN.append(i)
            Lfac.append(fac)
            
print()

print('length LN='+str(len(LN)))


LD=[]

for i in Lfac:

    for j in range(e,e+256):
    
        if not(sympy.isprime(j)):
        
            continue
            
        p = i[0][0]
        q = i[1][0]
        phi = (p-1) * (q-1)
        
        D = pow(j,-1,phi)
        
        LD.append((D,p*q,j))
        

print('length LD='+str(len(LD)))

for D in LD:

    for j in range(enc,enc+256):
    
        plain = pow(j,int(D[0]),int(D[1]))
        
        try:
        
            print('Decrypted Flag : {' + long_to_bytes(plain).decode() + '}')
            print('Encrypted Flag : ' + str(long_to_bytes(j)))
            
        except:
        
            None




