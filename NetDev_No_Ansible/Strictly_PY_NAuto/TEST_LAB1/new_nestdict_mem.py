# Test to see if I can write this by memory.
# Task:  Take a nested dictionary and print out information using pandas

import pandas as pd

my_data = {'device1' : {'eth0' : {'incoming packets' : 1500, 'outgoing packets' : 250}}, 
           'device2': {'eth1': {'incoming packets' : 950, 'outgoing packets' : 500}},
            'device3' : {'eth2' : {'incoming packets' : 700, 'outgoing packets' : 250}}
}

list_of_dicts = []
for devices, interfaces in my_data.items():
    print(devices)
    for eth, packets in interfaces.items():
        print(eth)
        nl = {'device': devices, 'interface': eth, **packets}
        list_of_dicts.append(nl)
        
df = pd.DataFrame(list_of_dicts, columns=['device', 'interface', 'incoming packets', 'outgoing packets'])
print(df)

# 1/30/2024 - was able to write this successfully without looking!
