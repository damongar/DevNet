
# Dont' forget to export your PYTHONPATH since main in now in a sub-directory 'lab'
# example: export PYTHONPATH=~/Desktop/PRNE/section14/14-3:$PYTHONPATH

from util.readdevs import read_device
from util.printdev import print_device_info

if __name__ == '__main__':
    devices_list = read_device('device.txt')
    print()
    for device in devices_list:
        device.connect()
        device.get_interfaces()
        print_device_info(device)
