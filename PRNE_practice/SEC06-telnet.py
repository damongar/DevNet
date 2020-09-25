import pexpect

ip_address = '10.30.30.1'
username = 'cisco'
password = 'cisco'

print('\n-------------------------------------------------------')
print('--- Atempting connection via telnet to : ', ip_address)

# Create the pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout=20)
result = session.expect(['Uername: ', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print('--- Failure! creating session for: ', ip_address)
    exit()

# Session expecting username, enter it here
session.sendline(username)
result = session.expect(['Password: ', pexpect.TIMEOUT])

# Check for error, if then print error and exit
if result != 0:
    print('--- Failure! entering username: ', username)
    exit()

# Session expecting password, enter here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so print error and exit
if result != 0:
    print('Failure! entering password: ', password)
    exit()

print('--- Success! connecting to: ', ip_address)
print('---               Username: ', username)
print('---               Password: ', password)
print('------------------------------------------------\n')
