from pwn import *

def Person(object):
    self



p = remote('host3.dreamhack.games', 14856)

p.recvuntil(b'Prime: ')
prime = int(p.recvline()[:-1], 16)


p.interactive()