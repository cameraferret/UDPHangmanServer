import socket

def getIP():
    IPs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IPs.connect(("8.8.8.8", 80))
    print(IPs.getsockname()[0])
    return IPs.getsockname()[0]

def client():
    UDP_IP = input("Please enter target IP: ") #try using whitePi @ 10.0.1.20
    UDP_Port = 5005
    Message = "All your Base you wanker"

    print("UDP target ip:", UDP_IP)
    print("UDP target port:", UDP_Port)
    print("Message:", Message)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto(Message.encode(), (UDP_IP, UDP_Port))

def host():
    pass

#client()
getIP()