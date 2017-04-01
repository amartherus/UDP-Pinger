#####################################################################
# UDP Client
# 
# Author: Andrew Martherus
#
# Summary: Send 10 messages over UDP (a ping) and find the round trip 
# time before you get a reply from the server (the pong)
####################################################################

from socket import *
import time

def main():
    # Set variables to establish connection
    serverAddr = 'localhost'
    port = 12000
    numPings = 0 # We will send 10 pings to the server

    data = raw_input("Enter data: ")

    while numPings < 10:
        mainSocket = socket(AF_INET,SOCK_DGRAM)  # create the socket
        numPings += 1

        try:
            # assignment says wait up to 1 second
            mainSocket.settimeout(1.0) 
            startTime = time.time() #check current time

            mainSocket.sendto(data,(serverAddr, port)) # send the message
            modifiedMessage, serverAddress = mainSocket.recvfrom(1024) 
            RTT = time.time() - startTime

        except timeout:  # timeout message
            print 'PING' + str(numPings) + ': Packet Dropped!'
            mainSocket.close()
        else: # ping message
            print 'PING' + str(numPings) + ' Returned: ' + modifiedMessage + ' in ' + str(RTT) + ' seconds!'

    mainSocket.close()
    pass

if __name__ == '__main__':
    main()



