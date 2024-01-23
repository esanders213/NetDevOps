# This script will create a "ip ssh pubkey-chain" on a cisco IOS device
# by pushing the "windows_user" public key-strings for the public key to all 
# devices in what ever section of device_info.py you decide to import.  
# See device_info.py to edit device info or call a different device. 

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
            "key-string1": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCMbfnn4jRR/g26fouozuVWiYIt6bCuVL29",
            "key-string2": "Kj0vrvNVt6BUxe2JpK+DbWCV39tFRc94TG1FxHkR6OljcGcXxdp3wXr1t28eWbJI",
            "key-string3": "XEjhO/KRhuivZpJzAl+caHcAjMkkWAyW/iHTtU70mCMfGPSlTDZ4N6esd6mWvrVG",
            "key-string4": "RQQGBysymDGii9UZgy3qLIJvnoITHKpB3etmvgMWR7PfaYXhb4WPf5XCnd+m1AqE",
            "key-string5": "f3hLGHFBnebHLarg/DgtRFH/dBpvLSL53lLwTwtGcqkTRk0ji4fhNxry2gAJmlhx",
            "key-string6": "9oOE/xrzge2y3WuNoCACu6cCzzobGSjaedYDpZ+wwz0ZxjJaJHXT",
            "exit": "exit"
            }

#Create a CLI configuration.  These are the commands pushed to the network device.
SSHpub_config = [
    "ip ssh pubkey-chain",
    "username {}".format(SSHpub["username"]),
    "key-string",
    "{}".format(SSHpub["key-string1"]),
    "{}".format(SSHpub["key-string2"]),
    "{}".format(SSHpub["key-string3"]),
    "{}".format(SSHpub["key-string4"]),
    "{}".format(SSHpub["key-string5"]),
    "{}".format(SSHpub["key-string6"]),
    "exit",
]


# The below for loop will push a the windows_user public key-strings for ssh
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


# Below is from chatGPT and did not work.  Would get hung up on specfic commands using .send_command.

# connection = ConnectHandler(**device)
# #connection.send_command('configure terminal')
# connection.send_command('username netauto privilege 15')
# #connection.send_command('crypto key generate rsa modulus 2048')
# connection.send_command('ip ssh pubkey-chain')
# connection.send_command('username netauto')
# connection.send_command('key-string')
# connection.send_command('AAAAB3NzaC1yc2EAAAADAQABAAABAQCMbfnn4jRR/g26fouozuVWiYIt6bCuVL29')
# connection.send_command('Kj0vrvNVt6BUxe2JpK+DbWCV39tFRc94TG1FxHkR6OljcGcXxdp3wXr1t28eWbJI')
# connection.send_command('XEjhO/KRhuivZpJzAl+caHcAjMkkWAyW/iHTtU70mCMfGPSlTDZ4N6esd6mWvrVG')
# connection.send_command('RQQGBysymDGii9UZgy3qLIJvnoITHKpB3etmvgMWR7PfaYXhb4WPf5XCnd+m1AqE')
# connection.send_command('f3hLGHFBnebHLarg/DgtRFH/dBpvLSL53lLwTwtGcqkTRk0ji4fhNxry2gAJmlhx')
# connection.send_command('9oOE/xrzge2y3WuNoCACu6cCzzobGSjaedYDpZ+wwz0ZxjJaJHXT')
# connection.send_command('end')
# connection.send_command('write mem')
# connection.disconnect()        