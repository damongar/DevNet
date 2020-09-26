from pprint import pprint

# Heading
print('')
print('Counts of different OS-typs for all devices')
print('===========================================')

os_types = { 'Cisco IOS':      {'count': 0, 'devs':[] },
             'Cisco Nexus':    {'count': 0, 'devs':[] },
             'Cisco IOS-XR':   {'count': 0, 'devs':[] },
             'Cisco IOS-XE':   {'count': 0, 'devs':[] } }

# Read all lines of device information from file
file = open('devices', 'r')
for line in file:
    device_info_list = line.strip().split(',')  # Get info into list

    #put information into dictionary for this device
    device_info = {}  # create empty dict
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]

    name = device_info['name']   # get device name
    os = device_info['os-type']  # get the OS-type for compare

    # Based on the OS-type, increment the count and add the mane to list
    if os == 'ios':
        os_types['Cisco IOS']['count'] += 1
        os_types['Cisco IOS']['devs'].append(name)

    elif os == 'nx-os':
        os_types['Cisco Nexus']['count'] += 1
        os_types['Cisco Nexus']['devs'].append(name)

    elif os == 'ios-xr':
        os_types['Cisco IOS-XR']['count'] += 1
        os_types['Cisco IOS-XR']['devs'].append(name)

    elif os == 'ios-xe':
        os_types['Cisco IOS-XE']['count'] += 1
        os_types['Cisco IOS-XE']['devs'].append(name)

    else:
        print('   Warning: unknown device type:', os)

pprint(os_types)  # Print os types with formatting
print('')  # print blank line
print('===========================================')

file.close()  # put up the devices file
