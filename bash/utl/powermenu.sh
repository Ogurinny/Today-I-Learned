#!/bin/bash

options="Shutdown
Reboot
Logout"
selected=$(echo -e "$options" | wofi -dmenu -p "Power Menu")

case "$selected" in
    "Shutdown")
        systemctl poweroff
        ;;
    "Reboot")
        systemctl reboot
        ;;
    "Logout")
        # This command depends on the user's desktop environment/window manager.
        # pkill -u $USER is a generic way to log out.
        pkill -u $USER
        ;;
esac