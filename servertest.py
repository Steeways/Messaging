#Socket = endpoint that receives data
#(with a socket, you send and receive data, it sits at an ip and a port.)

#-*-coding:utf-8 -*

import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.bind((sk.gethostname(), 1234))
s.listen(5)


while True:
    clientsocket, adress = s.accept()
    print(f"connection from {adress} has been established!")

    clientsocket.send(bytes('Welcome to the server', 'utf-8'))
    
