import socket as sk
import select
import errno
import sys

HEADER_LENGTH = 10
IP = sk.gethostbyname(sk.gethostname())
PORT = 1234
my_username = input('username : ')
client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)


client_socket.connect((IP,PORT))
client_socket.setblocking(False)

#encoding and sending the username
username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)





while True :
    message = input(f"{my_username} >")

    #Si on a un message à envoyer :
    if message :
        message = message.encode("utf-8")
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)


#trying to receive :
    try :
        while True :

            username_header = client_socket.recv(HEADER_LENGTH)

            if not len(username_header) :
                print("connection closed by the server")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

    except IOError as e :
        #erreurs si il n'y a plus de messages à recevoir :
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK :
            print('Reading error',str(e))
            sys.exit()
        continue

    except Exception as e:
        print("general error", str(e))
        sys.exit()
        pass






































# -*-coding:utf-8 -*
#
# import socket as sk
#
# HEADERSIZE = 10
# new_msg = True
#
# #def du socket
# s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
#
# #connection du socket au socket serveur
# s.connect((sk.gethostname(), 1234))
#
#
# full_msg = ''
# while True :
#     msg = s.recv(16)
#     if new_msg :
#         print(f'new message length : {msg[:HEADERSIZE]}')
#         msglen = int(msg[:HEADERSIZE])
#         new_msg = False
#
#     full_msg += msg.decode('utf-8')
#
#     if len(full_msg) - HEADERSIZE == msglen :
#         print('full msg received')
#         print(full_msg[:HEADERSIZE])
#         new_msg = True
#
# print(full_msg)
