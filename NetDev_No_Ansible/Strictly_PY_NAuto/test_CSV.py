import csv
from datetime import datetime

path = "/etc/ansible/NetDevOps/NetDev_No_Ansible/Strictly_PY_NAuto/linux_hosts.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
data = [row for row in reader] #Read the remaining data

print(header)

# data = []
# for row in reader:
#     # row = [device name, IP, username]
#     device = str(row[0])
#     IP = str(row[1])
#     user = str(row[2])

#     data.append([device, IP, user])
    
print(data[0])
print(data[1])

    
    