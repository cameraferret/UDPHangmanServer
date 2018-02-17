#Randolph Wilson /Avery Snyder
#Python 3.6, UDP Hangman Client
import socket
UDP_port = 12313
userGuess = []

win = str('You win!').lower()
lose = str('You lost! Better luck next time!').lower()

def getIP():  #Multi-interface systems sometimes the unwanted IP when using the build in python socket tools for getting hostname
    IPs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IPs.connect(("8.8.8.8", 80))
    #print(IPs.getsockname()[0])
    return IPs.getsockname()[0]

myIP = getIP()

def listen():
    #here for the purposes of debugging my own code and only having to deploy one file to my raspis
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((myIP, UDP_port))
    print('waiting')
    x = True
    while x:
        data, addr = sock.recvfrom(1024)
        UDP_IP = addr
        # print("Received message:", data)
        # print("Client IP address:", addr[0])
        if data is not None:
            x = False
            sock.close()
            #print("Debug listening: ", data) #needed to see what packets looked like from java
            return str(data)
def checkGameState(_msg):
   if(_msg.lower() == win):
       print(_msg)
       quit()
   if(_msg.lower() == lose):
       print(_msg)
       quit()

def play():	
    UDP_IP = input("Please enter server IP: ") #try using whitePi @ 10.0.1.20

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str('a').encode(), (UDP_IP, UDP_port)) #the server needs one packet to start
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    unknownWord = listen()
    unknownWord = unknownWord[2:len(unknownWord)-1]

    print("Guesses left ", int(unknownWord[0]))
    print(unknownWord[1:])

    while str(unknownWord).lower() != ('You win!' and 'You lost! Better luck next time!'):
        

        userTry = input('Please guess a letter: ').lower()
        if userTry in userGuess:
            print("Whoops you guessed that already")
        else:
            sock.sendto(userTry[0].encode(), (UDP_IP, UDP_port))
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            unknownWord = listen() #Listening for reply to the guess 
            unknownWord = unknownWord[2:len(unknownWord)-1]
            checkGameState(unknownWord)
            print("Guesses left: ", unknownWord[0],"",unknownWord[1:])
            userGuess.append(userTry[0].lower())
            print("Your past guesses are ", userGuess)

play()
