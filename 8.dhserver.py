# import numpy as np
# import random
# import socket 

# def main():
#     p=int(input('Enter P(p>5 prime nnumber) : '))
#     g=int(input('Enter Primitive Root :'))

#     s=socket.socket()
#     s.bind(('localhost',8000))
#     s.listen(1)
#     conn,_=s.accept()

#     conn.send(str(f"{p},{g}").encode())
#     a=random.randint(2,p-2)
#     print(f"A private key : {a}")

#     Xa=pow(g,a,p)
#     print(f"A Public Key :{Xa}")

#     conn.send(str(Xa).encode())
#     Xb=int(conn.recv(1024).decode())

#     k=pow(Xb,a,p)
#     print(f"Common key (A) :{k}")

# main()


import numpy as np
import random 
import socket 

def main():
    p=int(input("Enter P (Prime number >5)"))
    g=int(input("Enter G: "))
    s=socket.socket()
    s.bind(('localhost',8000))
    s.listen(1)
    conn,_=s.accept()

    conn.send(f'{p},{g}'.encode())

    a=random.randint(2,p-2)
    print(f"A Private key : {a}")
    Xa=pow(g,a,p)
    print(f"A public Key : {Xa}")

    Xb=int(conn.recv(1024).decode())
    conn.send(str(Xa).encode())

    k=pow(Xb,a,p)
    print(f"Common key : {k}")


main()