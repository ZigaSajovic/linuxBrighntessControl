#!/bin/bash
#make sure ran by sudo
[ "$UID" -eq 0 ] || exec sudo "$0" "$(whoami)" "$@"

echo "Setting script privileges"
toAppend="$SUDO_USER ALL=(root) NOPASSWD: $(pwd)/brightness.sh"
if [ -z "$(cat /etc/sudoers |grep $toAppend)" ]; then
  echo $toAppend >> /etc/sudoers
  . ~/.zshrc
fi
echo "Script now owned by root"
chown root:root brightness.sh
echo "Script only writable by root"
chmod u+rwx brightness.sh
echo "All users can execute the script"
chmod go-w+rx brightness.sh

