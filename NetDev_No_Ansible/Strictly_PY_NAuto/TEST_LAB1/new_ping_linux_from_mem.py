# Write a ping script from scratch that logs into a linux box and pings gateways
# Attempt to do this using a csv file but you could define these separately
import csv
from fabric import Connection, Config

path = "/etc/ansible/NetDevOps/NetDev_No_Ansible/Strictly_PY_NAuto/linux_hosts.csv"

with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        print(row)
        ip = row["ip"]
        user = row["username"]
        password = input('Please enter password for {} '.format(ip))
        new_config = Config(overrides={'sudo': {'password' : password}})
        conn = Connection(ip, user, config=new_config)
        
        try:
            result = conn.run("ping -c 5 192.168.39.1")
            print(result)
            conn.close()
        
        except:
            print("Unable to connect to {} ".format(ip))
        
    
    
    
    
            
        
