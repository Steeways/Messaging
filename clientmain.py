# -*-coding:utf-8 -*

import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.connect((sk.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode('utf-8'))
