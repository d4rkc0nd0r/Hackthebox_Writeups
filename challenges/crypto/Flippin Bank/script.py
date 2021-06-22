#!/usr/bin/python3

def decrypt():
	# AES CBC bit flipping
	# logged_username=bdmin&password=g0ld3n_b0y$$$$$$$
	# Refer app.py

	# send this creds as username and password fields

	user = "bdmin" # this is kept purposely
	passwd = "g0ld3n_b0y"
	padding = "$" * 7 # this isn't exactly how the padding looks like

	msg = "logged_username=" + user + "&password=" + passwd + padding

	encrypted_msg = "15e26dec37eb258c35ecaed4760bae4251eb351c27a99cb6bad19f7c2faca0e986e3197def7d57e07fe316628ada2e33" # encrypt_data()
	l = encrypted_msg[0:2]
	b = encrypted_msg[32:34]

	# 0x15 ^ decrypt_data(0x51) = 0x62 [b]
	# decrypt_data(0x51) = 0x15 ^ 0x62 [b]
	# decrypt_data(0x51) = 0x77 

	a = hex(0x77 ^ 0x61)[2:] # 0x61 [a] 

	# flipping l so that it becomes logged_username=admin&password=g0ld3n_b0y which is the goal of the challenge

	nc = str(a) + "e26dec37eb258c35ecaed4760bae4251eb351c27a99cb6bad19f7c2faca0e986e3197def7d57e07fe316628ada2e33"

	print(f"message: {nc} ") # send this output to enter ciphertext field

if __name__ == "__main__":
	decrypt()
