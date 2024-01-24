from netmiko import ConnectHandler
import re
from device_info import EveNG_PC_BGP_E as devices
from netmiko_get_interface import Int_Check 

# First check if network device has the interface created.


last_octet = 200
str_octet = str(last_octet)

for device in devices:
    
    loopback = {
            "int_name": "loopback103",
            "description": "loopback created with netmiko loop py",
            "IP_addr": "192.16.0.{}".format(str_octet),
            "netmask": "255.255.255.255"}

    int_config = [
            "interface {}".format(loopback["int_name"]),
            "description {}".format(loopback["description"]),
            "ip address {} {}".format(loopback["IP_addr"], loopback["netmask"]),
            "no shut"
        ]
    
    with ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"]) as ch:

        
        if Int_Check(loopback, ch) == False:
            # Sends commands to device
            output = ch.send_config_set(int_config)

            # Print the raw command output to the screen
            print("The following configuration was sent: ")
            print(output)
            last_octet = last_octet + 1
            str_octet = str(last_octet)
        else:
            print("Int_Check returned True meaning the interfaces already exists")
            
    