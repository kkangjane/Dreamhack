from pwn import *

p = remote('host3.dreamhack.games', 8276)
e = ELF('./validator_server')

