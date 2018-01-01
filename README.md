# linuxBrightnessControl
Script to control screen brightness for Linux

If your machine does not support native keyboard brightness control, this script can be binded as a custom hotkey.

## Configure

To use the script, some configuration is needed. Run the commands bellow in the shell, from the directry containing the scripts.

```bash
sudo chmod u+x config.sh
./config.sh
```

## Use

To decrease the brightness by a factor of 0.9 run

```bash
./brightness.sh 0.9
```

To increase the brightness by a factor of 1.1 run

```bash
./brightness.sh 1.1
```
