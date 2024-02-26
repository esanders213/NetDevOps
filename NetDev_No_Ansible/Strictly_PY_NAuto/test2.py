#Built-in Methods in python.  No additional modules

IP = "172.16.10.1"

# This will show you all the options you can apply with IP variable.
#print (dir(IP))

New_IP = IP.replace("172", "192").replace("16", "168")
print(New_IP)

#LISTS

Old_IP = "172.16.90.1"
Old_IP = Old_IP.replace()
#Prints a list of all octets in IP.  Splits at the "."
New_IP = IP.split(".")
print(New_IP)
#Prints first octet / first item in list
print(New_IP[0])
#Prints both first octet and 3rd octet / item 0 and 2 in list
print(New_IP[0:2])

#Sorts the list of octets in order from least to greatest number
New_IP.sort()
print(New_IP)


#DICTIONARIES
# Defines the ROUTERS dictionary and prints the type
ROUTERS = {"R1":"IOS", "R2":"IOS-XR", "R3":"NX-OS"}
print(type(ROUTERS))

#Prints the dictionary item referenced by key
print(ROUTERS["R3"])

#Working with Files

import os  # Required to use "os"
#Tells you the working directory in linux you are working with.
print(os.getcwd())

#os.mkdir("TEST_LAB1")
os.chdir("//etc/ansible/NetDevOps/NetDev_No_Ansible/Strictly_PY_NAuto/TEST_LAB1")
print(os.getcwd())

#Prints the list of files in a directory. (Like running ls in linux)
print(os.listdir())

#Runs the command on terminal.  This will print the info in Cisco1.txt file.
print(os.system("cat Cisco1.txt"))


#FUNCTIONS / DEFINITIONS

# Example function that calls with variables and prints the config.
def ospf_process(process_id, network, mask, area):
    print(f" router ospf {process_id} \n network {network} {mask} area {area}")
    
ospf_process ("10", "10.1.1.0", "0.0.0.255" , "50")


# Conditionals & Loops

devices = {"R1":"IOS", "R2":"XR", "R3":"NX-OS"}

# Allows user to enter input.  You can enter a key to the devices dict.
node = input('Type in your node:  ')

# Conditional if / else.  If input/node matches in devices, it will trigger "if"
# If node != key in dict, it will trigger "else"
if node in devices:
    print (f"I can configure {devices[node]}")
else:
    print('I dont know much about these devices')

# Loop that will print all keys in dict
for items in devices:
    print(items)

# Loop through only the values in the devices dict. Uses D.items() method
for key,value in devices.items():
    print (value)

# Loop through both keys and values in the devices dict
for key,value in devices.items():
    print (key,value)
    

    