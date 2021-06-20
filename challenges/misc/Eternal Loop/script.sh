#!/bin/bash
# This script breaks at 6969.zip

filename="$1"
count=0

while [ $count -eq 0 ]
do
	password=$(strings $filename | tail | grep "zipPK" | tr -d ".zipPK")
	7z x $filename -p$password
	count=$?
	zip=".zip"
	newfilename=$password$zip
	filename=$newfilename
done
