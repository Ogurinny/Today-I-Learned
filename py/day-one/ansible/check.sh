lxc list | grep -E "cont-[1-5]" | awk '{print NR, $2}'
