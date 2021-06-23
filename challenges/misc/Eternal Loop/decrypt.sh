#!/bin/bash

zip2john 6969.zip > crack
john --wordlist=/usr/share/wordlists/rockyou.txt crack
john crack --show | cut -d ":" -f2
