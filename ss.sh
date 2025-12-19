#!/bin/bash
DIR=~/Pictures/Screenshots
mkdir -p "${DIR}"

TIME=$(date +"%Y-%m-%d_%H-%M-%S")
FILENAME="${DIR}/${TIME}.png"

grim "$FILENAME"
