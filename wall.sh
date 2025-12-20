#!/bin/bash

WALLPAPER_DIR="$HOME/Pictures/wallpapers"  # ganti kalau folder kamu beda

# List file yang support (image/video)3
selected=$(ls "$WALLPAPER_DIR" | grep -iE '\.(jpg|jpeg|png|gif|mp4|webm|webp)$' | wofi --dmenu -p "Pilih Wallpaper:" --lines 15 --width 600 --height 800)

if [ -n "$selected" ]; then
    fullpath="$WALLPAPER_DIR/$selected"
    # Set wallpaper dengan transisi fade
    awww img "$fullpath" --transition-type any --transition-duration 1 --transition-fps 60
fi