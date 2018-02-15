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
    print("Message:", Message)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(Message.encode(), (UDP_IP, UDP_Port))


def host(): #here for the purposes of debugging my own code and only having to deploy one file to my raspis
    UDP_IP = getIP()
    UDP_port = 12313

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_port))
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message:", data)
        print("Client IP address:", addr[0])

#client()
getIP()