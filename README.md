# linuxBrightnessControl
Screen brightness control for Linux, with desktop notification support

If your machine does not support native **keyboard brightness control**, this script enables it and offers **bindings** to **custom hotkeys**, complete with **desktop notifications**.

## Installation

Before usage, some configuration is needed. Run the commands bellow in the shell, from the directory containing the scripts.

```bash
sudo chmod u+x config.sh
./config.sh
```

The script will (optionally) also execute the ```set_hotkeys.py``` script, that will create keyboard shortcuts according to the ```keys.config``` file.

### Example: Default keybindings in keys.config

The format of a line in the file is
```name change key_comb``` where
* name: Name of the command
* change: Change to be applied to the current brightness level (ex. +0.1 or -0.1)
* key_comb: The hotkey combination to be used

The default bindings in the ```keys.config``` are
  
>brightnessDownSmall -0.05 F5  
>brightnessUpSmall +0.05 F6  
>brightnessDownMedium -0.1 <Control>F5  
>brightnessUpMedium +0.1 <Control>F6  
>brightnessDownBig -0.25 <Control><Shift>F5  
>brightnessUpBig +0.25 <Control><Shift>F6  

After running the script with the default ```keys.config```, the added hotkeys can be found in ```System Settings -> Keyboard -> Shortcuts -> Custom Shortcuts```

![example](example.png)

Note that you can change the contents of the ```keys.config``` file to the bindings of your choosing.

## Lone use of script

To decrease the brightness by x (0.1 in the bellow example) run

```bash
./brightness.sh -0.1
```

To increase the brightness by x (0.1 in the bellow example) run

```bash
./brightness.sh +0.1
```
