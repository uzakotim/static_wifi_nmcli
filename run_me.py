import subprocess
import json

# BEFORE running this code
# configure parameters in config.json
# and add a line config.json in .gitignore

with open('config.json') as config_file:
    config = json.load(config_file)

# command = f'nmcli dev wifi connect {config["ssid"]} password {config["password"]}'
command = f'echo {config["ssid"]}'
commands = [
    f'sudo nmcli radio wifi on',
    f'sudo nmcli dev wifi connect {config["ssid"]} password {config["password"]}', 
    f'sudo nmcli con up {config["ssid"]}',
    f'sudo nmcli con mod {config["ssid"]} ipv4.addresses {config["ip"]}/24',
    f'sudo nmcli con mod {config["ssid"]} ipv4.gateway {config["gateway"]}',
    f'sudo nmcli con mod {config["ssid"]} ipv4.dns {config["dns"]}',
    f'sudo nmcli con mod {config["ssid"]} ipv4.method manual',
    f'sudo nmcli con up {config["ssid"]}',
    f'ip a'
]
for command in commands:
    subprocess.run(command, shell=True)