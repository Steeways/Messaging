#Socket = endpoint that receives data
#(with a socket, you send and receive data, it sits at an ip and a port.)

#-*-coding:utf-8 -*

import socket as sk
HEADERSIZE = 10
s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.bind((sk.gethostname(), 1234))
s.listen(5)


while True:
    clientsocket, adress = s.accept()
    print(f"connection from {adress} has been established!")
    msg = "welcome to the server"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg, 'utf-8'))
