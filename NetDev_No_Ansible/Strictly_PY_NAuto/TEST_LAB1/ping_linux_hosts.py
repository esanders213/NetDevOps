
#################### PING multiple Linux Hosts from csv ###############################

import csv
from fabric import Connection, Config

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
        
print(ip_list)
print(user_list)

user = 0
for ip in ip_list:
    
    password = input("Enter password for {} ".format(ip))
    config = Config(overrides={'sudo': {'password': password}})
    conn = Connection(ip, user=user_list[user], config=config) #look_for_keys=False)
    
    # Executes the command on the connected device.
    try: 
        result = conn.run("ping -c 5 192.168.39.1") 
        print(result.stdout.strip())

        print("################################")
    # output = device.send_command("ping -c 5 192.168.39.1")
    # print (output)
        conn.close()
        user = user + 1
    except:
        print("Was unable to connect to {}.".format(ip))
        
        