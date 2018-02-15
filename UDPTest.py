import socket

UDP_IP = "10.0.1.20"
UDP_Port = 5005
Message = "All your Base you wanker"

print("UDP target ip:", UDP_IP)
print("UDP target port:", UDP_Port)
print("Message:", Message)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(Message.encode(), (UDP_IP, UDP_Port))
