import socket

def getIP():
    IPs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IPs.connect(("8.8.8.8", 80))
    #print(IPs.getsockname()[0])
    return IPs.getsockname()[0]

def client():
    UDP_IP = input("Please enter target IP: ") #try using whitePi @ 10.0.1.20
    UDP_Port = 12313
    Message = "All your Base you wanker"

    print("UDP target ip:", UDP_IP)
    print("UDP target port:", UDP_Port)
    #print("Message:", Message)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(Message.encode(), (UDP_IP, UDP_Port))
    return Message


def host(): #here for the purposes of debugging my own code and only having to deploy one file to my raspis
    UDP_IP = getIP()
    UDP_port = 12313

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_port))
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message:", data)
        print("Client IP address:", addr[0])

def gameDebug():
    x = True

    while x:
        Choice = input("Are you (1)hosting or (2)playing hangman?, enter (0) to quit")
        if Choice == 1: #server
            pass
        if Choice == 2:
            msg = client()
            while str(msg).lower() != ('you win' and 'you lose'):
                print("Word is ", msg[0], " characters long")
                print(msg[1:len(msg)])
                guess = input('Please guess a letter').lower()

        if Choice == 0:
            break


#client()
getIP()