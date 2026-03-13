#!/bin/bash

jumlah_lxc=10

lxccc=$(lxc list -c n --format csv | wc -l)

for i in {1..10}; do
  if [ $lxccc -lt 10 ]; then
    lxc launch images:alpine/edge cont-$i
    lxccc=$(lxc list -c n --format csv | wc -1)
  else
    echo "container dah mencukupiiii uyyy"
    break
  fi
done

echo "Sekarang container kamu berjumlah $lxccc"
