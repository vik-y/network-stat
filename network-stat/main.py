from util import *


'''
Guidelines:

Don't leave unnecessary print statements lying around in your code.
Use:

log.info(msg) # To log random information
log.warning(msg) # To log warning messages
log.error(msg) # To log error messages

'''

# Test util functions
DNS_SERVER = "172.16.50.10"
average, mdev = pingUrl(DNS_SERVER, 1)
print wifiInterfaceName()
print linkQuality()
print getFrequency()
print internetOn()
print getAccessPointMac()
