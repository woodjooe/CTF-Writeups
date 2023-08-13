from sage.all import *
from sympy.ntheory.modular import crt as CRT


p = 405734656915788488250405171387699093906649032815685839648728080811180207524779040664581122340856619750116364457460001971951448415312550641490896597753634855174633021441

a = 23
b = 212486593712632143318141733524336347751188720294097180245719133013331493427073883408912136676914952088416774177852634330429527249196067184013614965377830383431113072232

fac = list(factor(p-1))
rs, ms = [], []
print(fac[:-1])
i=0
t=len(fac)-1
for q, e in fac[:-1]:
    i+=1
    k = (p-1) // q
    print('Step ',str(i),'/',str(t))
    x = discrete_log_rho(pow(b, k, p), pow(a, k, p), q)
    rs.append(int(x))
    ms.append(int(q))
    val, mod = CRT(ms, rs)
    
val, mod = CRT(ms, rs)
#print(rs)
#print(ms)
#print(val)
#print(mod)

key = val
print(key)
break
