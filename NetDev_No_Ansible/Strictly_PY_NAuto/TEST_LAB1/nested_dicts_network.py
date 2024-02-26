import pandas as pd

dict_of_dicts = {'device1': {'eth0' : {'incoming packets' : 1545, 'outgoing packets' : 1000}}, 
                'device2': {'eth1' : {'incoming packets' : 760, 'outgoing packets' : 325}}, 
                'device3': {'eth2' : {'incoming packets' : 2510, 'outgoing packets' : 950}}
                }

# Create a list of dictionaries from the dictionary of nested dictionaries
list_of_dicts = []

# First define device name variables and nested interface dicts
for device, interface in dict_of_dicts.items():
    #Test printing this_device key.
    print(device)
    #Test printing eth_val value string.
    
    # Next, define interface variables and nested packet dicts
    for new_int_key, packets in interface.items():
        #Test prints below:
        #print(new_int_key)
        #print(packets['incoming packets'])
        #print(packets['outgoing packets'])
        
        #Create a new dictionary with the correct key values for pandas to use:
        nd = {'device': device, 'interface': new_int_key, **packets}
        
        # Add new nd dict to a list_of_dicts variable.
        list_of_dicts.append(nd)
        #print(list_of_dicts)

# Creates the pandas dataframe and matches dict keys to the columns.  Names have to match!!!!
df = pd.DataFrame(list_of_dicts, columns=["device", "interface", "incoming packets", "outgoing packets"])
print(df)