# This script will create a "ip ssh pubkey-chain" on a cisco IOS device
# by pushing the "windows_user" public key-hash for the public key to all 
# devices in what ever section of device_info.py you decide to import.  
# See device_info.py to edit device info or call a different device. 
# NOTE: Similar to pushing key-strings but found I only need to send the 
# RSA hash which is much smaller.  Less steps.

from netmiko import ConnectHandler

from device_info import EveNG_PC_BGP_E as devices # noqa

# Below can be used for 1 device but we're using "device_info" above.  Testing only!
# device = {
#     'device_type': 'cisco_ios',
#     'ip': '10.51.100.2',
#     'port': '22',
#     'username': 'neteng',
#     'password': 'neteng',
#}

#New windows_user SSH public key details
SSHpub = {"username": "netauto",   # This can be any username.  Locally significant on the Cisco device.
            "key-hash": "key-hash ssh-rsa F6413E6C465490E36482F93409D78F0A",
            "exit": "exit"
            }

#Create a CLI configuration.  These are the commands pushed to the network device.
SSHpub_config = [
    "ip ssh pubkey-chain",
    "username {}".format(SSHpub["username"]),
    "{}".format(SSHpub["key-hash"]),
    "exit",
]

# The below for loop will push a the windows_user public ssh-rsa key-hash for ssh
#auth key authentication. Make sure you edit correctly. 

for device in devices:
    # Below was just testing the printing of key and value pairs.
    #for key, value in device.items():
    #    print(key, value)
    
    # Creates the info for connecting to the device.  Stores as a variable "connection".
    # This will loop through the devices array for every device dict you've called from your
    # imported call to device_info.py!
    with ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"]) as connection:
    
    # Send configuration to device stored in the "connection" var.
        output = connection.send_config_set(SSHpub_config)

    # Print the raw command output to the screen.  
        print("The following configuration was sent: ")
        print(output)

