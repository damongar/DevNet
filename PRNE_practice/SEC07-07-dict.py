from pprint import pprint

device_info = {}  # Create my device_info dictionary

# Open the file and read in the single line o fdevice info
file = open('devices', 'r')
file_line = file.readline().strip()

print('read line: ', file_line)  # Print out the line just read

# Here is the main part: use the string 'split' function to convert
# the comma-separated string into a list of items
device_info_list = file_line.split(',')

# Now put the items fromt the list into the dictionary
device_info['name'] = device_info_list[0]
device_info['os_type'] = device_info_list[1]
device_info['ip'] = device_info_list[2]
device_info['username'] = device_info_list[3]
device_info['password'] = device_info_list[4]

pprint(device_info)  # Print out the list with mice formatting

file.close()  # Close the file after use
