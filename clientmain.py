# -*-coding:utf-8 -*

import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.connect((sk.gethostname(), 1234))
full_msg = ''
while True :

    msg = s.recv(8)
    
    if len(msg) <= 0 :
        break

    full_msg += msg.decode('utf-8')


print(full_msg)
