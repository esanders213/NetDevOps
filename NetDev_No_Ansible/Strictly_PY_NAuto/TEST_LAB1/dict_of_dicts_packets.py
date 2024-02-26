# Robinhood interview question:
# Done on codesignal.  Asked to print out the nexted dictionary.
# I wrote several examples below.  Some tuples of dicts, lists of dicts and dicts of dicts.
# The last few below are using pandas for table printing.

import pandas as pd
from pprint import pprint

list_Of_Nest_Dict_data = [{'device1': {'eth0' : {'incoming packets' : 1545, 'outgoing packets' : 1000}}}, 
{'device2': {'eth0' : {'incoming packets' : 760, 'outgoing packets' : 325}}}, 
{'device3': {'eth0' : {'incoming packets' : 2510, 'outgoing packets' : 950}}}]

pprint(type(list_Of_Nest_Dict_data))
pprint(list_Of_Nest_Dict_data)

for device in list_Of_Nest_Dict_data:
      # Print device name. 
    for device_name, interface in device.items():
        print(device_name)
        for incoming, outgoing in interface.items():
            print(incoming, outgoing)
            
print("#################################################")
print("#################################################")
print("Now lets print the same my_data list of nested dictionaries but just the data!")
print("")            

list_Of_Nest_Dict_data_2 = [{'device1': {'eth0' : {'incoming packets' : 1545, 'outgoing packets' : 1000}}}, 
{'device2': {'eth0' : {'incoming packets' : 760, 'outgoing packets' : 325}}}, 
{'device3': {'eth0' : {'incoming packets' : 2510, 'outgoing packets' : 950}}}]

for device in list_Of_Nest_Dict_data_2:
    #print("Device name: ", device)
    #print("interface: ", eth_num)
    for device_name, int_2 in device.items():
        print(device_name)
        print(int_2)
    for incoming, outgoing in int_2.items():
        print("Incoming: ", incoming)
        print("outgoing: ", outgoing)


print("#################################################")
print("#################################################")
print("Now lets print the same my_data dictionary that's spaced as a tuple!")
print("")

#  This was confusing but makes sense now.  Below is a tuple nested dictionary.  It is a tuple because
# it is surrounded by ().  Inside is a nested dictionary.  You have to handle tuples different
# Below is a for loop to handle it.

tuple_Of_Nest_Dict_data = ({'device1': {'eth0' : {'incoming packets' : 1545, 
                                'outgoing packets' : 1000}}}, 
{'device2': {'eth1' : {'incoming packets' : 760, 
                                  'outgoing packets' : 325}}}, 
{'device3': {'eth2' : {'incoming packets' : 2510, 
                                  'outgoing packets' : 950}}})

# Loop through the tuple of dictionaries
for i in range(len(tuple_Of_Nest_Dict_data)):
  # Get the dictionary at index i
  d = tuple_Of_Nest_Dict_data[i]
  # Loop through the keys and values of the dictionary
  for name, info in d.items():
    # Print the device name
    print(name)
    # Print the eth0 information
    print(info)

print("#################################################")
print("#################################################")
print("Now lets print just the data from my_data dictionary that's spaced as a tuple!")
print("")

tuple_Of_Nest_Dict_data_2 = ({'device1': {'eth0' : {'incoming packets' : 1545, 
                                'outgoing packets' : 1000}}}, 
{'device2': {'eth1' : {'incoming packets' : 760, 
                                  'outgoing packets' : 325}}}, 
{'device3': {'eth2' : {'incoming packets' : 2510, 
                                  'outgoing packets' : 950}}})

# Loop through the tuple of dictionaries
#for i in range(len(tuple_Of_Nest_Dict_data_2)):
  # Get the dictionary at index i
#  d = tuple_Of_Nest_Dict_data_2[i]
# Loop through the keys and values of the dictionary

# Loop through original tuple for each device dictionary.
for device_dict in tuple_Of_Nest_Dict_data_2:
  # Loop through device_dict for keys and values (device, interface)
  for device, eth_dict in device_dict.items():
    # Get device key name and print it.
    print(device)
    # Loop through eth_dict for packet_dict
    for eth_name, packet_dict in eth_dict.items():
        print(eth_name)
        # Loop through packet_dict to pull it's key, value pair and print them.
        for packet_type, count in packet_dict.items():
            print(packet_type, ": ",count)
        
# Using pandas with tuple:
""" 
print("#################################################")
print("#################################################")
print("Now, let's use pandas with our tuple to print it with a dataframe!")
print("")



# Define the tuple of nested dictionaries
tuple_of_nest_dict_data_2 = ({'device1': {'eth0' : {'incoming packets' : 1545, 
                                'outgoing packets' : 1000}}}, 
{'device2': {'eth1' : {'incoming packets' : 760, 
                                  'outgoing packets' : 325}}}, 
{'device3': {'eth2' : {'incoming packets' : 2510, 
                                  'outgoing packets' : 950}}})
 """
# Convert the tuple into a list of dictionaries
""" list_of_dicts = []
for device_dict in tuple_of_nest_dict_data_2:
    for device, eth_dict in device_dict.items():
        for eth_name, packet_dict in eth_dict.items():
            # Create a dictionary with the device, eth, and packet information
            d = {"device": device, "eth": eth_name, **packet_dict}
            # Append the dictionary to the list
            list_of_dicts.append(d)

# Create a data frame from the list of dictionaries
df = pd.DataFrame(list_of_dicts, columns=["device", "interface", "incoming packets", "outgoing packets"])

# Print the data frame
print(df) """

print("#################################################")
print("#################################################")
print("Now, let's use pandas on a standard list of dictionaries to print it with a dataframe!")
print("")

dict_of_dicts = {'device1': {'eth0' : {'incoming packets' : 1545, 'outgoing packets' : 1000}}, 
                'device2': {'eth1' : {'incoming packets' : 760, 'outgoing packets' : 325}}, 
                'device3': {'eth2' : {'incoming packets' : 2510, 'outgoing packets' : 950}}
                }

# Create a list of dictionaries from the dictionary of nested dictionaries
list_of_dicts2 = []

# First define device name variables and nested interface dicts
for this_device, eth_val in dict_of_dicts.items():
    #Test printing this_device key.
    print(this_device)
    #Test printing eth_val value string.
    
    # Next, define interface variables and nested packet dicts
    for new_eth_key, packets2 in eth_val.items():
        print(new_eth_key)
        print(packets2['incoming packets'])
        print(packets2['outgoing packets'])
        nd = {'device': this_device, 'interface': new_eth_key, **packets2}
        list_of_dicts2.append(nd)
        print(list_of_dicts2)
        
df = pd.DataFrame(list_of_dicts2, columns=["device", "interface", "incoming packets", "outgoing packets"])
print(df)

        
# list_of_dicts = []
# in_count = []
# for k, v in dict_of_dicts.items():
#     list_of_dicts.append(k)
#     print(k)
#     for eth in v.items():
#         in_count.append(eth)
#         out_count.append()

# Use json_normalize to flatten the nested dictionaries
# df = pd.json_normalize(list_of_dicts)

# # Rename the columns
# df.columns = ['device', 'eth', 'incoming packets', 'outgoing packets']

# # Print the data frame
# print(df)


# OLD CODE BELOW for PRACTICE
# Convert the tuple into a list of dictionaries
#list_of_dicts = []
# for device_dict in list_of_nest_dict_data_3:
#     for device, eth_dict in device_dict.items():
#         for eth_name, packet_dict in eth_dict.items():
#             # Create a dictionary with the device, eth, and packet information
#             d = {"device": device, "eth": eth_name, **packet_dict}
#             # Append the dictionary to the list
#             list_of_dicts.append(d)

# Create a data frame from the list of dictionaries
# for i in len(dict_of_dicts):
#     df = pd.json_normalize(dict_of_dicts[i], sep='_')

# df.columns = ["device", "interface", "incoming_Packets", "Outgoing_Packets" ]
# print(df)

#df = pd.DataFrame(dict_of_dicts, columns=["device", "eth", "incoming packets", "outgoing packets"])

# Print the data frame
#print(df)





##################### Advanced pandas with nested dicts.  Not printing correctly######################
################### Should come back and figure this out.  the .json.normalize fuction is powerful####

""" 
tuple_of_nest_dict_data_2 = [{'device1': {'eth0' : {'incoming packets' : 1545, 
                                'outgoing packets' : 1000}}}, 
{'device2': {'eth1' : {'incoming packets' : 760, 
                                  'outgoing packets' : 325}}}, 
{'device3': {'eth2' : {'incoming packets' : 2510, 
                                  'outgoing packets' : 950}}}]

# Create a list of dictionaries from the tuple of nested dictionaries
list_of_dicts = [d for device_dict in tuple_of_nest_dict_data_2 for d in device_dict.values()]

print(list_of_dicts)
print(device_dict)
print(d)
print(device_dict.values())
# Use json_normalize to flatten the nested dictionaries
df = pd.json_normalize(list_of_dicts, sep='_')
print(df) """

# df = pd.json_normalize(device_dict, sep='_')
# print(df)

# Rename the columns
# df.columns = ['device', 'eth', 'incoming packets', 'outgoing packets', 'extra_col_1', 'extra_col_2']

# # Drop the extra columns
# df = df.drop(columns=['extra_col_1', 'extra_col_2'])

# # Print the data frame
# print(df)