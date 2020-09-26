current_version = 'Version 5.3.1'

# Print heading
print('')
print('Devices with bad software versions')
print('==================================')

#  Read all the lines of device information from file
file = open('devices', 'r')
for line in file:
    device_info_list = line.strip().split(',')  # Get device info into list

    # Put device info into a dictionary
    device_info = {}  # create an empty dictionary
    device_info['name'] = device_info_list[0]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]

    # compare version to 'current version'. print warning
    if device_info['version'] != current_version:
        print('Device: ', device_info['name'], '   Version: ', device_info['version'])

print('==================================')  # line break

file.close()  #put up the toys when finished playing
