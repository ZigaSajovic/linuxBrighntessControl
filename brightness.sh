#!/bin/bash
#make sure ran by sudo
[ "$UID" -eq 0 ] || exec sudo "$0" "$@"

if [ $# -eq 0 ]
  then
    exit
fi
wrd=$1
lambda=${wrd/+/}
max_val=$(cat /sys/class/backlight/intel_backlight/max_brightness)
val=$(cat /sys/class/backlight/intel_backlight/brightness)
val_=$(echo "$val+($lambda)*$max_val"|bc -l)
new_val=${val_%.*}
if [ $new_val -lt 1 ]
  then
    new_val=1
elif [ $new_val -gt $max_val ]
  then
  new_val=$max_val
fi
proc=$(echo "100*$val_/$max_val"|bc -l)
proc=${proc%.*}
echo $new_val $proc

sudo su -c "echo $new_val >  /sys/class/backlight/intel_backlight/brightness" 2>> /dev/null
notify-send " " -i notification-display-brightness-low -h int:value:$proc -h string:x-canonical-private-synchronous:brightness &