#!/bin/bash

input="user.dat"

while IFS=',' read -r username uid gid comment
do
	userdel -r "$username"
	rm -rf /home/$username
	echo "Delete $username"
done< $input

echo
tail -3 /etc/passwd
