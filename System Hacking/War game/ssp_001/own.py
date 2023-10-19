from pwn import *

# index = [ebp-0x94]
# name_len = [ebp - 0x90]
# select = [ebp-0x8a]
# box = [ebp - 0x88]
# name - [ebp-0x48]
# canary = [ebp-0x8]

p = remote('host3.dreamhack.games', 20563)

# read canary
