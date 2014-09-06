import ctypes
import commands
import requests
import sys
import time
from threading import Timer
from datetime import datetime
from ctypes import wintypes


token = "32e37dc1-3b51-13c1-13ab-e64da3a8dade"
username = raw_input("Username: ")


class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ExternalPower', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
    ]

SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)
GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
GetSystemPowerStatus.restype = wintypes.BOOL

#status = SYSTEM_POWER_STATUS()


def yo_all(api_token):
    return requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})

def yo(api_token, username):
    return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': username})

def chargingStatusLoop():
    while True:
        status = SYSTEM_POWER_STATUS()
        if not GetSystemPowerStatus(ctypes.pointer(status)):
            raise ctypes.WinError()
        time.sleep(1)
        if status.BatteryLifePercent < 55 and not status.ExternalPower:
            yo(token, username)
        elif status.ExternalPower == False:
            sys.stdout.write("Discharging.")
            time.sleep(1)
            sys.stdout.write(".")
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.write(str(status.BatteryLifePercent))
            sys.stdout.write("%")
            print ' '
        elif status.ExternalPower == True:
            sys.stdout.write("Charging.")
            time.sleep(1)
            sys.stdout.write(".")
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.write(str(status.BatteryLifePercent))
            sys.stdout.write("%")
            print ' '

chargingStatusLoop()
        
        
