from pprint import pprint
import re

#  create regular expression to match gigabit interfaces
gig_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

# create empty dict to hold route number / interface
routes = {}

# open file and read lines
file = open('ip_routes', 'r')
for line in file:
    match = gig_pattern.search( line )  # Match for GigabitEthernet

    # check to see if match the Gig Ethernet string
    if match:
        intf = match.group(2)  # grab the interface from match
        routes[intf] = routes[intf] + 1 if intf in routes else 1
    else:
        continue

print('')
print('Number of routes per interface')
print('------------------------------')
pprint(routes)
print('')
file.close()
