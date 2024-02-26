# This will push an OSPF config to multiple devices
# Built for the EVE_NG BGP lab to push OSPF as the IGP underlay

from netmiko import ConnectHandler
from device_info import EveNG_PC_BGP_E as devices

ospf_cfg = ["router ospf 1",
            "network {} mask {} area 0".format()
        
    
]