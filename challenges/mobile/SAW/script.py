#!/usr/bin/python3

# I've found this values in libdefault.so in lib and reverse engineered this using ida freeware
# After which, I've used adb to backup this app and found the flag

l = [0x6C, 0x67, 0x28, 0x6E, 0x2A, 0x58, 0x62, 0x68]
m = [0x0A, 0x0B, 0x18, 0x0F, 0x5E, 0x31, 0x0C, 0x0F]
result = []

for i in range(len(l)):
	result.append(chr(l[i] ^ m[i]))

print(''.join(result))
