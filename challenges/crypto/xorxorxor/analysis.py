#!/usr/bin/python3

cipher = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"
cipher = bytes.fromhex(cipher)

flag_start = b"HTB{"
key = [o1 ^ o2 for (o1, o2) in zip(cipher, flag_start)]
print(key)

flag = []
key_len = len(key)
for i in range(len(cipher)):
    flag.append(cipher[i] ^ key[i % key_len])

flag = "".join(chr(o) for o in flag)

print("Flag:",flag)
