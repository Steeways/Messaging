# -*-coding:utf-8 -*

import socket as sk

HEADERSIZE = 10
new_msg = True

#def du socket
s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

#connection du socket au socket serveur
s.connect((sk.gethostname(), 1234))


full_msg = ''
while True :
    msg = s.recv(16)
    if new_msg :
        print(f'new message length : {msg[:HEADERSIZE]}')
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg.decode('utf-8')

    if len(full_msg) - HEADERSIZE == msglen :
        print('full msg received')
        print(full_msg[:HEADERSIZE])
        new_msg = True

print(full_msg)
