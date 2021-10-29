import socket, struct

#TODO This isn't working, maybe redo it.
#TODO Make this OO

class Waker():
    def makeMagicPacket(self, macAddress):
        # Take the entered MAC address and format it to be sent via socket
        splitMac = str.split(macAddress,':')
    
        # Pack together the sections of the MAC address as binary hex
        hexMac = struct.pack('BBBBBB', int(splitMac[0], 16),
                             int(splitMac[1], 16),
                             int(splitMac[2], 16),
                             int(splitMac[3], 16),
                             int(splitMac[4], 16),
                             int(splitMac[5], 16))
    
        self.packet = '\xff'.encode() * 6 + hexMac * 16 #create the magic packet from MAC address

    def sendPacket(self, packet, destIP, destPort = 7):
        # Create the socket connection and send the packet
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(packet,(destIP,destPort))
        s.close()
        
    def wake(self, macAddress, destIP, destPort=7):
        self.makeMagicPacket(macAddress)
        self.sendPacket(self.packet, destIP, destPort)
        print('Packet successfully sent to', macAddress)

def wakeup():
    #This is all the information that needs to be changed to make this work for you
    mac = ''
    ip = '' #The IP address where the packet should be sent
    port = 7 #The port the packet will be sent on
    
    wol = Waker()
    wol.makeMagicPacket(mac)
    wol.sendPacket(wol.packet, ip, port)
    print('Packet successfully sent to', mac)