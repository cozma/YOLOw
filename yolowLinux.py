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
        
    currBatt = open('/sys/class/power_supply/BAT0/energy_now','r')
    for current in currBatt:
        curr = float(current)
         
    battPercent = ("%.1f" % ((curr/full)*100))
     
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
    setLimit = input("Battery % to get warnings at (1-100) ")
    
    compare = str(setLimit) + ".0%"
    print "You have set your battery warning percent to " + compare
    
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
                output = batteryPercent()
                print output
                if output == compare:
                    print "dying!"
                    yo("32e37dc1-3b51-13c1-13ab-e64da3a8dade",person)
                    ##sys.exit()
                    break
                        
            batt.close()
        charge.close()
        
batteryPercent()
getBattery()



