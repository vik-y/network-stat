import os
import re
import logging as log
import urllib2

log.basicConfig(filename="log.txt",filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=log.DEBUG)

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
def pingDNS(dns):

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
    # Returns mac address of the wifi interface of computer.
    # Note: Cant assume that Device mac will be same as
    return 1

def getAccessPointMac():
    # If connected to a wifi interface then this should return
    # the mac address of the wifi interface
    # If not connected to a wifi interface then this should return 0
    return 1
