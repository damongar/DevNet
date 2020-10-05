import pexpect

# -----------------------------------------------------------
# The following code connects to a device


def connect(dev_ip, username, password):

    print('--- attempting to: ssh '+username+'@'+dev_ip)

    session = pexpect.spawn('ssh '+username+'@'+dev_ip, timeout=20)
    result = session.expect(['password:', pexpect.TIMEOUT])

    # Check for failure
    if result != 0:
        print('--- Timout or unexpected reply from device')
        return 0

    print('--- attempting to: password: '+password)

    # Successfully got password prompt, logging in with password
    session.sendline(password)
    session.expect('#')

    return session  # return pexpect session object to caller

# -----------------------------------------------------------
