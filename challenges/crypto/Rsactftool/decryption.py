#!/usr/bin/python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.number import *
import primefac

def decryption():
	with open('pubkey.pem') as handle:
        	r = handle.read()

	ne = RSA.import_key(r)
	modulus = ne.n
	exponent = ne.e
	factor_n = primefac.factorint(modulus)
	primes = list(factor_n)
	primes = [int(i) for i in primes]
	p = primes[0]
	phi = (p ** 2) * (p - 1)
	d = inverse(exponent,phi)

	with open('key') as handle1:
		r1 = bytes.fromhex(handle1.read())

	aes_key  = pow(bytes_to_long(r1),d,modulus)
	ltb = long_to_bytes(aes_key)
	aes = AES.new(ltb,AES.MODE_ECB)

	with open("flag.txt.aes",'rb') as handle2:
        	flag = handle2.read().strip()

	print("Flag: ", aes.decrypt(flag))

if __name__ == '__main__':
	decryption()
