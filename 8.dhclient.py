# import numpy as np
# import random
# import socket 


# def main():
#     s=socket.socket()
#     s.connect(('localhost',8000))
#     p,g=map(int,s.recv(1024).decode().split(','))

#     b=random.randint(2,p-2)
#     print(f"B Proivate Key : {b}")

#     Xb=pow(g,b,p)
#     print(f"B Public key : {Xb}")

#     s.send(str(Xb).encode())
#     Xa=int(s.recv(1024).decode())
#     print(f"Public key A : {Xa}")
#     k=pow(Xa,b,p)
#     print(f"Common Key (B): {k}")

# main()


import socket
import random

def main():
    s=socket.socket()
    s.connect(('localhost',8000))
    p,g =map(int , s.recv(1024).decode().split(','))

    b=random.randint(2,p-2)
    print(f"B Private Key : {b}")

    Xb=pow(g,b,p)
    print(f"B public key : {Xb}")

    s.send(str(Xb).encode())
    Xa=int(s.recv(1024).decode())

    k=pow(Xa,b,p)
    print(f"Common key : {k}")


main()
