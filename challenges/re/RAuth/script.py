#!/usr/bin/python3

from Crypto.Cipher import Salsa20
import base64

nonce = b'd4c270a3' # rax register
key = b'ef39f4f20e76e33bd25f4db338e81b10'
ct = base64.b64decode('BQVfsaMpqNVY2fVWpssx8yRDKjHJnexy4z62b2KtG/k=') # it was in hex but i've converted that to base64 for simplicity

cipher = Salsa20.new(key=key, nonce=nonce)
pt = cipher.decrypt(ct)

print(pt)
