#!/usr/bin/python3

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * ord(char) + 18) % 256)
    return bytes(ct)

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}!@#$%^&*()_-+=[]\\|;:'\"/.,*<>?"
f = []

for i in a:
	ct = encryption(i)
	f.append(ct.hex())

l = ['aa', '6e', 'c8', '2b', 'f6', '22', '22', '7b', 'b7', '0e', '7f', 'b7', '35', '22', '49', 'b7', 'd8', '93', 'c4', '93', 'd8', '53', '9d', 'ec', '8f', 'b7', '93', '5d', '49', '0e', '7f', '9d', '22', 'ec', '89', 'b7', 'a3', '22', 'ec', '8f', 'd8', '0e', '7f', '89', '21']
n = []

for j in l:
	if j in f:
		m = f.index(j)
		n.append(a[m])

flag = ''.join(n)
print(flag)
