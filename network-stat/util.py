import os
import re
import logging as log
import urllib2

log.basicConfig(filename="log.txt",filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=log.DEBUG)

# A helper function to check if the host is connected to Internet or not.
# Returns True if connected, False otherwise.
def internetOn():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def pingUrl(url, count):
    pingCount = 1
    pingData = os.popen("ping -c %s -i 0.2 %s" % (count, url)).read()
    log.debug(pingData)
    #pat = re.compile("(Ch\.|CH\.|DD\.|Dd\.|PO\.|Po\.).*?:[0-9]+")
    pat = re.compile("/[0-9]+.*?/")

    avg = re.search("/[0-9]+.*?/", pingData).group()[1:-1]
    mdev = re.search("/[0-9]+[.][0-9]+ ", pingData).group()[1:-1]
    log.info(avg + " " + mdev)
    return avg, mdev

def linkQuality():
    pat = re.compile("[0-9]+/[0-9]+")
    temp = re.search(pat, os.popen("iwconfig").read())
    if temp:
        # Wifi interface was present
        log.info("Wifi Interface was present")
        quality = temp.group()[0:2]
        log.info(quality)
        return quality
    else:
        log.error("No wifi interface found")

def getFrequency():
    pat = re.compile("[25].*G")
    temp = re.search(pat, os.popen("iwconfig").read())

    if temp:
        # Wifi interface was present
        log.info("Wifi Interface was present")
        frequency = temp.group()[0]
        log.info(frequency)
        return frequency
    else:
        log.error("No wifi interface found")

def getDeviceMac():
    interfaceName = wifiInterfaceName()
    pat = re.compile(interfaceName+".*")
    temp = re.search(pat, os.popen("/sbin/ifconfig | grep " + interfaceName).read())

    if temp:
        log.info("Device Mac retrieved")
        mac = temp.group().split()[-1].strip()
        log.info(mac)
        return mac
    else:
        log.error("No wifi interface found")

# A helper function to get MAC address of the access point to which
# the client is connected
def getAccessPointMac():
    pat = re.compile("Point:.*")
    temp = re.search(pat, os.popen("iwconfig").read())

    if temp:
        # Wifi interface was present
        log.info("Wifi Interface was present")
        mac = temp.group().split()[1].strip() # To get the mac address
        log.info(mac)
        return mac
    else:
        log.error("No wifi interface found")

# A helper function to get wifi interface name
# We cannot assume wifi Interface name to be wlan0 all the time.
def wifiInterfaceName():
    temp = os.popen("iwconfig").read() # Runs and gets iwconfig command output
    result = re.search(".*802", temp)

    if result:
        interfaceName = result.group().split()[0]
        log.info("Wifi Interface Name is %s" % (interfaceName))
        return interfaceName
    else:
        log.error("No wifi interface found")

# A function to get IP address assigned to the Wifi Interface.
def getHostIP():
    interfaceName = wifiInterfaceName()
    pat = re.compile("inet addr:.*")
    temp = re.search(pat, os.popen("ifconfig " + interfaceName).read())

    if temp:
        log.info("Device IPv4 address obtained")
        ipv4 = temp.group().split(":")[1].split(" ")[0].strip()
        log.info(ipv4)
        return ipv4
    else:
        log.error("No wifi interface found")
    return 1

# A function to get Subnet mask assigned to the Wifi Interface
def getHostSubnetMask():
    interfaceName = wifiInterfaceName()
    pat = re.compile("Mask:.*")
    temp = re.search(pat, os.popen("ifconfig " + interfaceName).read())

    if temp:
        log.info("Device subnet mask obtained")
        subnet = temp.group().split(":")[1].strip()
        log.info(subnet)
        return subnet
    else:
        log.error("No wifi interface found")
    return 1
