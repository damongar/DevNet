devices_list = []  # Create empty list

# Read in the devices file
file = open('devices', 'r')
line = file.readline()
while line:
    device_info_list = line.strip().split(',')  # Get device info into a list

    # Put device info into a dictionary
    device_info = {}
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]

    # append device and info into the devices list
    devices_list.append(device_info)

    line = file.readline()

file.close()

# Use while loop to print the results
print('')
print('Name     OS-type  IP address           Software         ')
print('------   -------  ------------------   -----------------')

index = 0
while index < len(devices_list):

    device = devices_list[index]

    print('{0:8} {1:8} {2:20} {3:20}'.format(device['name'],
                                             device['os-type'],
                                             device['ip'],
                                             device['version']))

    index += 1

print('')
