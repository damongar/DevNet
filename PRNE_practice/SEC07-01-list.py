from pprint import pprint

device_info = []  # Create my device_info list

# Open the file and read in the single line o fdevice info
file = open('devices', 'r')
file_line = file.readline().strip()

print('read line: ', file_line)  # Print out the line just read

# Here is the main part: use the string 'split' function to convert
# the comma-separated string into a list of items
device_info = file_line.split(',')

pprint(device_info)  # Print out the list with mice formatting

file.close()  # Close the file after use
