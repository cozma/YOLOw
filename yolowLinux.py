#!/usr/bin/env python
import ctypes
import commands
import requests
import sys
import time

def yo(api_token, username):
    return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': username})

def batteryPercent():
    fullBatt = 0
    currBatt = 0
    battPercent = 0
    
    fullBatt = open('/sys/class/power_supply/BAT0/energy_full','r')
    for keep in fullBatt:
        full = float(keep)
       ## print full
    currBatt = open('/sys/class/power_supply/BAT0/energy_now','r')
    for current in currBatt:
        curr = float(current)
        ##print curr
    battPercent = ("%.1f" % ((curr/full)*100))
    ##print battPercent
    stringPercent = str(battPercent)
    finalPercent = (stringPercent + "%")
    return finalPercent
        
       
    

def getBattery():
    person = raw_input("Enter your username: ")
    print person
    battlvl = 31978000
    choose = True
    status = None
    output = None
    compare = "45.0%"
    print compare
    
    while True:
        time.sleep(3)
        charge = open('/sys/class/power_supply/BAT0/status','r')
        
        for search in charge:
            status = search
            print status
            choose = (status[:-1] == 'Charging')
            break
        if not choose:
            batt = open('/sys/class/power_supply/BAT0/energy_now','r') ##opens the directory containing pi serial
            for line in batt:      ##in the file
                num = int(line)
                ##print num
                print batteryPercent()
                print len(batteryPercent())
                output = batteryPercent()
                print output
                if output == compare:
                    print "dying!"
                    yo("c5a366e9-9a91-e7ba-1c1f-815bb67c8c74",person)
                    ##sys.exit()
                    break
                        
            batt.close()
        charge.close()
        
batteryPercent()
getBattery()



