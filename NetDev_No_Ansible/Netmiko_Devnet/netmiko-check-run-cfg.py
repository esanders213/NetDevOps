# Simple script that connects ssh to a cisco IOS device and runs 'show running-config | b ip ssh'.
# then prints the output.

from netmiko import ConnectHandler

from device_info import IOS_E as device

# device = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.39.51',
#     'username': 'netauto',
#     'use_keys': True,
#     'key_file': 'C:\\Users\\Erik\\.ssh\\windows_user.pem'
#     #'password': 'netauto',
# }



for device in devices

connection = ConnectHandler(**device)
output = connection.send_command('show running-config | b ip ssh')
print(output)