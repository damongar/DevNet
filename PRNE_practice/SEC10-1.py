devices_list = []  # Create empty list

# Read in the devices file
file = open('devices', 'r')
for line in file:
    devices_info_list = line.strip().split(',')
    devices_list.append(devices_info_list)

file.close()

print('')
print('Name      OS-type   IP-address          Software      ')
print('------   ---------  -------------       --------------')

# iterate the list of devices, print out the values in ni format
for device in devices_list:
    print('{0:8} {1:8} {2:20} {3:20}'.format(device[0], device[1], device[2], device[3]))

print('')
