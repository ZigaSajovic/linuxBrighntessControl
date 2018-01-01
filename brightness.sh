#!/bin/bash
#make sure ran by sudo
[ "$UID" -eq 0 ] || exec sudo "$0" "$@"

if [ $# -eq 0 ]
  then
    exit
fi
lambda=$1
val=$(cat /sys/class/backlight/intel_backlight/brightness)
val_=$(echo $lambda*$val|bc -l)
new_val=${val_%.*}
if [ $new_val -lt 1 ]
  then
    new_val=1
fi

sudo su -c "echo $new_val >  /sys/class/backlight/intel_backlight/brightness" 2>> /dev/null
