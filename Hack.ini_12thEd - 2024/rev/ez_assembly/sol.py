'''

The program reads this data from the data section:

------------------------------------------------------
section .data
    output dq 0xfffffffffffffe34, 0xfffffffffffffe60, 0xfffffffffffffe6c, 0xfffffffffffffe50, 0xfffffffffffffe50, 0xfffffffffffffe4c, 0xfffffffffffffe7c, 0xfffffffffffffe30, 0xfffffffffffffe6c, 0xfffffffffffffe34, 0xfffffffffffffe14, 0xfffffffffffffe24, 0xfffffffffffffe60, 0xffffffffffffff40, 0xfffffffffffffe84, 0xfffffffffffffe34, 0xffffffffffffff30, 0xffffffffffffff3c, 0xfffffffffffffef0, 0xfffffffffffffe84, 0xffffffffffffff30, 0xffffffffffffff2c, 0xffffffffffffff2c, 0xfffffffffffffe4c, 0xfffffffffffffe78, 0xfffffffffffffed0, 0xfffffffffffffe1c, 0xfffffffffffffe84, 0xffffffffffffff3c, 0xffffffffffffff2c, 0xfffffffffffffe84, 0xfffffffffffffe60, 0xffffffffffffff30, 0xfffffffffffffeb8, 0xfffffffffffffef0, 0xffffffffffffff04, 0xfffffffffffffe0c
    input resb 38
------------------------------------------------------

and compares it with the input in the check function

------------------------------------------------------
check:
    cmp byte [input + rcx], 10
    je  end

    movzx rax, byte [input + rcx]
    neg rax
    shl rax, 2
    mov rbx, [output + rcx]
    cmp rax, rbx
    jne  not_equal

    inc rcx
    jmp check
------------------------------------------------------

as u can see:
    neg rax
    shl rax, 2

this is our issue:
    neg rax: This instruction negates (flips the sign of) the value in the rax register. This is equivalent to multiplying the value in rax by -1.

    shl rax, 2: This instruction performs a left shift on the value in the rax register.
    

run the script to rectify it. Here we reverse the operation performed on our input and run it on the data in the data section
'''

l=[0xfffffffffffffe34, 0xfffffffffffffe60, 0xfffffffffffffe6c, 0xfffffffffffffe50, 0xfffffffffffffe50, 0xfffffffffffffe4c, 0xfffffffffffffe7c, 0xfffffffffffffe30, 0xfffffffffffffe6c, 0xfffffffffffffe34, 0xfffffffffffffe14, 0xfffffffffffffe24, 0xfffffffffffffe60, 0xffffffffffffff40, 0xfffffffffffffe84, 0xfffffffffffffe34, 0xffffffffffffff30, 0xffffffffffffff3c, 0xfffffffffffffef0, 0xfffffffffffffe84, 0xffffffffffffff30, 0xffffffffffffff2c, 0xffffffffffffff2c, 0xfffffffffffffe4c, 0xfffffffffffffe78, 0xfffffffffffffed0, 0xfffffffffffffe1c, 0xfffffffffffffe84, 0xffffffffffffff3c, 0xffffffffffffff2c, 0xfffffffffffffe84, 0xfffffffffffffe60, 0xffffffffffffff30, 0xfffffffffffffeb8, 0xfffffffffffffef0, 0xffffffffffffff04, 0xfffffffffffffe0c]

s=''

for i in l:
    c = (-i%0xffffffffffffffff) + 1
    c = chr(c//4)
    s += c

print(s)