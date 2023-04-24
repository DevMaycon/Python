import socket 
import base64
from time import sleep

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 9090))
    s.sendall(b"Hello, Frank")
    msg = (s.recv(1024).decode())
    a = -1
    while True:
        a += 1
        print("decrypted -->", a)
        print(msg[:10])
        before_msg = msg
        try:
            last_msg = base64.b64decode(before_msg)
        except:
            print("BASE64 Key FOUND [+]:", msg.decode())
            break
        msg = last_msg
        sleep(0.1)
print(msg.decode())
