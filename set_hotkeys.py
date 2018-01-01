import subprocess as sp
import os
script_name="brightness.sh"
keys_list="keys.config"
keys_="org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
subkey1 = keys_.replace(" ", ".")[:-1]+":"
item_s = "/"+keys_.replace(" ", "/").replace(".", "/")+"/"
call=lambda cmd:sp.check_output(cmd).decode()

tmp_keys=call(["gsettings", "get"]+keys_.split(" "))
keys=eval(tmp_keys)if tmp_keys[0]=="[" else []
get_command=lambda x:"./"+os.path.join("/".join(os.getcwd().split("/")[3:]),script_name)+(" %s"%x)
try:
  with open(keys_list,"r") as f:
    commands=[]
    for line in f:
      if line[0]=="#":
        continue
      name, command, key=line.strip().split(" ")
      if any(map(lambda x: key in x,keys)):
        print("The hotkey-combination %s already in use."%key)
        continue
      n=next((a for a,b in enumerate(map(lambda x:x.split("/")[-2],keys)) if "custom"+str(a)!=b),len(keys))
      new_hotkey=item_s+"custom"+str(n)+"/"
      keys.append(new_hotkey)
      commands.append('gsettings set '+subkey1+new_hotkey+" name '"+name+"'")
      commands.append('gsettings set '+subkey1+new_hotkey+" command '"+get_command(command)+"'")
      commands.append('gsettings set '+subkey1+new_hotkey+" binding '"+key+"'")
    sp.call(["/bin/bash","-c", 'gsettings set '+keys_+' "'+str(keys)+'"'])
    for command in commands:
      sp.call(["/bin/bash","-c", command])
except FileNotFoundError:
  print("The file named \"%s\" does not exist."%keys_list)
