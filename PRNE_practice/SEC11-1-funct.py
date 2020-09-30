#---- Function to read device into from file ---
def read_device_info():

    #read in the devices from the file
    file = open('devices', 'r')
    for line in file:
        device_info_list = line.split(',')  #get info into list
        devices_list.append(device_info_list)

    file.close()  # close file after use

#--- Fuction to go through devices printing them to a table ----
def print_device_info():

    print('')
    print('Name    OS-type    IP address           Software            ')
    print('------  --------   ----------------     --------------------')

    # Go through list of devices, print out values in nice format
    for device in devices_list:

        print('{0:8} {1:10} {2:20} {3:20}'.format(device[0],device[1], device[2],device[3])),

    print('')

#---- Main: redevice info then print ----------------------

devices_list = []  # Create blank devices_list

read_device_info()
print_device_info()
