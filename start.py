#!/usr/bin/python
from network_stat import *

if __name__ == '__main__':
    if internetOn():
        data = collectData()
        print data
        if uploadData(data):
            print "Data uploaded succesfully"
    else:
        print "Please turn on Internet and try running this script again."
