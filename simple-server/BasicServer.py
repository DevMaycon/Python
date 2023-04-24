
#Made by Dev.M
"""
ServerFunctions.py

Server/Function

    - intercept bytes/messages --> OK
        \_ encrypt all messages --> OK
    
"""

import base64

class server:
    def intercept_messages(msg: bytes):
        for i in range(10):
            b_e = msg
            message_encrypted = base64.b64encode(b_e)
            msg = message_encrypted
        return message_encrypted


"""
StartServer.py

Server/socket - made by cou.

    - start server; -- > OK
    - intercept bytes of the client; --> OK 
    
"""

import socket

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 9090))
        s.listen()
        client, client_addr = s.accept()
        with client:
            while True:
                data = server.intercept_messages(client.recv(1024))
                if not data:
                    break
                client.sendall(data)
