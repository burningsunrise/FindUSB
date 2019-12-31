#!/usr/bin/python3
import pyudev
import subprocess
import time
import os

def usbPolling():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    usb_list = []

    try:
        for device in iter(monitor.poll, None):
            if device.action == 'add':
                print(f"{device} connected")
                usb_list.append(device)
    except KeyboardInterrupt:
        print('\n')
        print(usb_list)

usbPolling()