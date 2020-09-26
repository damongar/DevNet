from collections import namedtuple
from pprint import pprint

# define namedtuple and parameters
Dev_info = namedtuple('Dev_info' , ['name', 'os_type', 'ip', 'user', 'password'])

devices = {}  # Create empty dict to hold info

# Open devices file and read
file = open('devices', 'r')
for line in file:

    device_info = Dev_info(*(line.strip().split(',')))
    print('Device Information: ', device_info)
    devices[device_info.name] = device_info


pprint(devices)  # print result with nice formatting

file.close()  # clean up after yourself
