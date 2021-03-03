from pprint import pprint
import os

# Open the file and read single line of device informaiton
file = open('devices', 'r')
file_line = file.readline().strip()

print('read line: ', file_line)  # print the line just read

# split() will provide us with a list that we convert to a tuple
device_info = tuple(file_line.split(' , '))

pprint(device_info)  # print out the tuple with nice formating

file.close()  # close the file after use.
