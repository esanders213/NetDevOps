# DevNet Always-On NETCONF/YANG & RESTCONF Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "ios-xe-mgmt.cisco.com",
             "netconf_port": 10000,
             "restconf_port": 9443,
             "ssh_port": 8181,
             "username": "root",
             "password": "D_Vay!_10&",
             "device_type": "cisco_ios"
          }
# DevNet Always-On NETCONF/YANG & RESTCONF Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology
# try this one if you can't access the previous one
ios_xe_latest = {
             "address": "sandbox-iosxe-latest-1.cisco.com",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "admin",
             "password": "C1sco12345",
             "device_type": "cisco_ios"
          }
# DevNet Always-On Sandbox NX-OS
#
nxos1 = {
             "address": "sbx-nxos-mgmt.cisco.com",
             "netconf_port": 10000,
             "restconf_port": 443,
             "ssh_port": 818122,
             "username": "admin",
             "password": "Admin_1234!",
             "device_type": "cisco_nxos"
          }

# DevNet Lab Sandbox Manual entry

Dev_E = {
            "address": "10.10.20.48",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "developer",
             "password": "C1sco12345",
             "device_type": "cisco_ios"
    
          }

# Erik's local Cisco IOS C3560CX Switch

IOS_E = {
             "address": "192.168.39.50",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
}

# Array of Dicts for Eve-NG Devices configured 
EveNG_PC_BGP_E = [
            {
             #"hostname": "R5-INET",
             "address": "192.168.39.51",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            {
             #"hostname": "R6",
             "address": "10.0.113.6",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            {
             #"hostname": "R4",
             "address": "10.0.113.1",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            {
             #"hostname": "R3",
             "address": "10.1.1.1",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            {
             #"hostname": "R2",
             "address": "10.1.1.2",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            {
             #"hostname": "R1",
             "address": "172.16.1.1",
             "netconf_port": 830,
             "restconf_port": 443,
             "ssh_port": 22,
             "username": "neteng",
             "password": "neteng",
             "device_type": "cisco_ios"
},
            
            ]
   


# Sample GitHub Editor Comment.  