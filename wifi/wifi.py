import network
from time import sleep

# TODO Make this object oriented
# A Watcher to keep the connection alive would be helpful

def connect(wifi_led, colour1=None, colour2=None):
    colour_off = (0,0,0)
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    with open('essid-name.txt', 'r') as essid_file:
        ESSID = essid_file.read()
    
    with open('essid-passwd.txt', 'r') as pass_file:
        PASSWD = pass_file.read()

    wlan.connect(ESSID,PASSWD)

    if colour1 is None and colour2 is None:
        while (not wlan.isconnected()):
            wifi_led.colour(colour2)
            sleep(0.1)
            wifi_led.colour(colour1)
            sleep(0.1)
        
        wlan.config(dhcp_hostname='OUTLET-001')
        
        for i in range(4):
            wifi_led.colour(colour1)
            sleep(0.1)
            wifi_led.colour(colour_off)
            sleep(0.1)
            
    else: 
        while (not wlan.isconnected()):
            sleep(0.5)