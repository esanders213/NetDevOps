from netmiko import ConnectHandler
import getpass
from fabric import Connection, Config

 # password = getpass.getpass("Enter your password: ")







import json
import pprint
import csv
path = "/etc/ansible/NetDevOps/NetDev_No_Ansible/Strictly_PY_NAuto/linux_hosts.csv"

ip_list = []
user_list = []

#file = open(path, 'r')
with open(path, newline='') as csvfile:
    #next(csvfile)
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        IPS = row["ip"]
        user = row["username"]
        ip_list.append(IPS)
        user_list.append(user)

#header = next(reader)
#print(header)
#print(reader)
#header = next(reader)

# for i in reader.keys():
#     ip_list.append(i)
    
# for key, values in reader.items():
#         print("This is the key" + str(key) + " this is the value" + str(values))
#         if reader[key] == "ip":
#             IPS = values
#             ip_list.append(values)
#         if reader[key] == "username":
#             USER = values
#             user_list.append(values)
        
print(ip_list)
print(user_list)

user = 0
    
for ip in ip_list:
    
    password = input("Enter password for {} ".format(ip))
    config = Config(overrides={'sudo': {'password': password}})
    conn = Connection(ip, user=user_list[user], config=config, look_for_keys=False)
    
    # Executes the command on the connected device.
    result = conn.run("ping -c 5 192.168.39.1") 
    print(result)
    # device = ConnectHandler(device_type='linux', 
    #                         ip=ip, 
    #                         username=user_list[user], 
    #                         password= input("Please type Password"  ))
    
    # output = device.send_command("sh run | i hostname")
    # print (output)
    # print("################################")
    # output = device.send_command("sh ver")
    # pprint (output)
    # print("################################")
    # print("################################")
    print("################################")
    # output = device.send_command("ping -c 5 192.168.39.1")
    # print (output)
    conn.close()
    user = user + 1
    
    
    # Code from https://youtu.be/Xi52tx6phRU
    
    