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
current_keys=list(map(lambda x:eval(call(["/bin/bash","-c","gsettings get "+subkey1+item_s+x.split("/")[-2]+"/ binding"])),keys))
current_commands=list(map(lambda x:eval(call(["/bin/bash","-c","gsettings get "+subkey1+item_s+x.split("/")[-2]+"/ command"])),keys))
current_names=list(map(lambda x:eval(call(["/bin/bash","-c","gsettings get "+subkey1+item_s+x.split("/")[-2]+"/ name"])),keys))
key_map={key:command for key,command in zip(current_keys,current_commands)}
command_map={command:key for key,command in zip(current_keys,current_commands)}
name_map={name:key for name,key in zip(current_names,current_keys)}

try:
  with open(keys_list,"r") as f:
    commands=[]
    for line in f:
      if line[0]=="#":
        continue
      try:
        name, command, key=line.strip().split(" ")
      except:
        continue
      if any(map(lambda x: key in x,current_keys)):
        print("HOTKEY ERROR: The hotkey-combination '%s' is already binded to command '%s'. Replace it in the config file '%s'"%(key,key_map[key],keys_list))
        continue
      if any(map(lambda x: get_command(command) in x,current_commands)):
        print("COMMAND ERROR: The command '%s' is already binded to key '%s'. Replace it in the config file '%s'"%(get_command(command),command_map[get_command(command)],keys_list))
        continue
      if any(map(lambda x: name in x,current_names)):
        print("NAME ERROR: The name '%s' is already binded to key '%s'. Replace it in the config file '%s'"%(name,name_map[name], keys_list))
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
