#Socket = endpoint that receives data
#(with a socket, you send and receive data, it sits at an ip and a port.)

#-*-coding:utf-8 -*

import socket as sk
import select


HEADER_LENGTH = 10
IP = sk.gethostbyname(sk.gethostname())
PORT = 1234
server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)


server_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
server_socket.bind((IP,PORT))
server_socket.listen()


sockets_list = [server_socket]
clients = {}



def receive_msg(client_socket) :
    try :
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header) :
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header" : message_header, "data" : client_socket.recv(message_length)}


    except :
        return False



while True :
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets :
        if notified_socket == server_socket :
            client_socket, client_adress = server_socket.accept()

            user = receive_msg(client_socket)
            if user is False :
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user
            username = user["data"].decode("utf-8")

            #juste un print super relou qui veut rien dire
            print(f"accepted new connection from {client_adress[0]}:{client_adress[1]} username:{username}")

        else :
            message = receive_msg(notified_socket)

            if message is False :
                print(f"closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"reveived message from {user['data'].decode('utf-8')} : {message['data'].decode('utf-8')}")

            for client_socket in clients :
                if client_socket != notified_socket :
                    client_socket.send(user["header"] + user["data"] + message["header"] + message["data"])


    for notified_socket in exception_sockets :
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
