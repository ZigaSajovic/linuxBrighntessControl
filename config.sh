#!/bin/bash
sudo chmod u+x .config_script.sh
./.config_script.sh
while true; do
    read -p "Do you wish to bind the default hotkeys from the keys.config file? <y/n> " yn
    case $yn in
        [Yy]* )  python set_hotkeys.py; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done