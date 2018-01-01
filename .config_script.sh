#!/bin/bash
#make sure ran by sudo
[ "$UID" -eq 0 ] || exec sudo "$0" "$(whoami)" "$@"

echo "$(who | awk '{print $1}') ALL=(root) NOPASSWD: $(pwd)/brightness.sh" >>/etc/sudoers
chown root:root brightness.sh
chmod u+rwx brightness.sh
chmod go-w+rx brightness.sh