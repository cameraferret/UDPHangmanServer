import socket
UDP_IP = None
UDP_Port = 12313
guessWord = None

userGuesses = [None]

def getIP():
    IPs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IPs.connect(("8.8.8.8", 80))
    #print(IPs.getsockname()[0])
    return IPs.getsockname()[0]

def client():
    ClientUDP_IP = input("Please enter target IP: ") #try using whitePi @ 10.0.1.20
    ClientUDP_Port = 12313

    print("UDP target ip:", ClientUDP_IP)
    print("UDP target port:", ClientUDP_Port)


def sendMsg(_msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(_msg.encode()), (UDP_IP, UDP_Port)

def listen(): #here for the purposes of debugging my own code and only having to deploy one file to my raspis
    Listening_IP = getIP()
    UDP_port = 12313

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((Listening_IP, UDP_port))
    x = True
    while x:
        data, addr = sock.recvfrom(1024)
        UDP_IP = addr
        # print("Received message:", data)
        # print("Client IP address:", addr[0])
        if data is not None:
            guessWord = data
            x = False



def gameDebug():
    x = True

    while x:
        if x:
            Choice = input("Are you (1)hosting or (2)playing hangman?, enter (0) to quit: ")
            if Choice == '1': #server
                print("Welcome host")
                h = "Hamster"
                client()
                sendMsg(h)

            elif Choice == '2':
                listen()
                print("Word is ", guessWord[0], " letters long")
                print(guessWord[1:len(guessWord)])
                while str(guessWord).lower() != ('you win' and 'you lose'):
                    guess = input('Please guess a letter').lower()
                    sendMsg(guess[0])
                    listen()
                    userGuesses.append(guess[0].lower())
                    print("Your past guesses are ", userGuesses)

            elif Choice == '0':
                x = False


#client()
gameDebug()