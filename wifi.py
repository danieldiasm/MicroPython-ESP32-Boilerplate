import network
from time import sleep

# TODO Make this object oriented

def connect(wifi_led, colour1, colour2):
    colour_off(0,0,0)
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    pass_file = open('essid-passwd.txt', 'r')
    essid_file = open('essid-name.txt', 'r')

    ESSID = essid_file.read()
    PASSWD = pass_file.read()
    
    essid_file.close()
    pass_file.close()

    wlan.connect(ESSID,PASSWD)

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