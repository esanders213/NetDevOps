#!/user/bin/env python
# This is the same as jinja_template1 but I'm using the ex3_svi_template.j2 & ex3_vlan _template.j2 for the templates.  
# This allows me to edit theh j2 templates directly and keep the code the same.  
# Instead of deleting the old code I commented it out below for reference.

from jinja2 import Template

vlan_var = 101
svi_ip = '192.168.1.1'
svi_mask = '255.255.255.0'

# vlan_template = Template('vlan {{id}} \n'
#                          ' name VLAN_{{id}}')

# Code commented out above is replaced with below to use ex3_vlan_template.j2
with open("ex3_vlan_template.j2") as f:
    vlan_in_temp = Template(f.read())

# svi_template = Template('interface vlan {{id}} \n'
#                         ' description This is the SVI for VLAN {{id}} \n'
#                         ' ip address {{address}} {{mask}}')

# Code commented out above is replaced with below to use ex3_SVI_template.j2
with open("ex3_svi_template.j2") as f:
    svi_in_temp = Template(f.read())
    
# code commented out below is changed to the next lines below. 
# vlan_output = vlan_template.render(id=vlan_var)
# svi_output = svi_template.render(id=vlan_var, address=svi_ip, mask=svi_mask)

vlan_output = vlan_in_temp.render(id=vlan_var)
svi_output = svi_in_temp.render(id=vlan_var, ip=svi_ip, mask=svi_mask)

# Below code is the same as the first template1.
print()
print('!Output from vlan_template')
print(vlan_output)
print()
print('!Output from SVI'
      ' template')

print(svi_output)
print()


