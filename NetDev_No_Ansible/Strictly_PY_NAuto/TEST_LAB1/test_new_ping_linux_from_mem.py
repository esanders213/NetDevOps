import csv
from fabric import Config, Connection

path = "/etc/ansible/NetDevOps/NetDev_No_Ansible/Strictly_PY_NAuto/linux_hosts.csv"

with open(path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        ip = row['ip']
        user = row['username']
        
        password = input("Please enter username for {} ".format(ip))
        new_config = Config({"sudo" : {"password" : password}})
        conn = Connection(ip, user, password, new_config)
        
        try:
            result = conn.run("ping -c 5 192.168.39.1")
            print(result)
            conn.close()
        
        except:
            print("Unable to connect to {} ".format(ip))
            
            