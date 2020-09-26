from pprint import pprint

devices = []  # create empty outer list for all devices

# Open the file and read single line of device informaiton
file = open('devices', 'r')
for line in file:
    device_info = tuple(line.strip().split(' , '))  # get device info into tuple

    # Print out what we have so far
    print('device_info: ', device_info)

    # Append the new devices read form file
    devices.append(device_info)

# Done reading all the lines from the file

pprint(devices)  # print out the tuple with nice formating

file.close()  # close the file after use.
