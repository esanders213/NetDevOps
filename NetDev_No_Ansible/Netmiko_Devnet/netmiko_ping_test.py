#Script to login to multiple hosts and ping 2.2.2.2
#Script idea came from AWS onsite interview

from netmiko import ConnectHandler
from device_info import EveNG_PC_BGP_E as devices

for device in devices:
    
    #int_ping = "ping 2.2.2.2"
    
    
    with ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"], 
                        ssh_strict = False) as ch:
    #with ConnectHandler(**device) as ch:
    
        try:
            send_ping = ch.send_command("ping 2.2.2.2")
            print(send_ping)
        
        except:
            print("Was not able to connect to host {}".format(device["address"]))
            
