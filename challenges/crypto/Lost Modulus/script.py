#!/usr/bin/python3

from Crypto.Util.number import *
import binascii
import gmpy2

ct = "05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965"
ct = bytes_to_long(binascii.unhexlify(ct))

gmpy2.get_context().precision=200000
pt = gmpy2.root(ct,3) # e = 3
message = binascii.unhexlify(hex(int(pt))[2:])
print(message)
