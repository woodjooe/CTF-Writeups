import time

current_time_seconds = int(time.time())

from ctypes import CDLL


libc = CDLL("libc.so.6")
libc.srand(current_time_seconds)


for i in range(0xd - 1):
    var1 = (libc.rand() & 0xfff)
    print(var1)


#just run ghidra and checkout the functions till you find the main function that generates the password
#run this script at the same time you contact the server at.