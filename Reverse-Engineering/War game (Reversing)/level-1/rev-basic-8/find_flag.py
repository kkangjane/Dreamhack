a = [0xAC, 0xF3, 0x0C, 0x25, 0xA3, 0x10, 0xB7, 0x25, 0x16, 0xC6, 0xB7, 0xBC, 0x07, 0x25, 0x02, 0xD5, 0xC6, 0x11, 0x07, 0xC5, 0x00, 0x00]

for i in range(0x15) :
    for flag in range(0, 128) :
        if flag * 0xFB & 0xFF == a[i] :
            print(chr(flag), end='')

print()