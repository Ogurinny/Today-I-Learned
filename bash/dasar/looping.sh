#!/bin/bash
dirdef=/home/$USER/Documents

if [ $dirdef -eq 10 ]; then
    for i in {1..50}; do
        touch $dirdef/text$i.txt
    done
    else
        echo "dah ada 50"
    fi
