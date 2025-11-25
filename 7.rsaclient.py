# import socket

# s=socket.socket()

# s.connect(("localhost",8000))

# e,n=map(int,s.recv(1024).decode().split(','))
# m=int(input("Enterr Message : "))
# ct=pow(m,e,n)
# s.send(str(ct).encode())
# print(f"Encrypted : {ct}")


import socket

s=socket.socket()

s.connect(('localhost',8000))

e,n=map(int, s.recv(1024).decode().split(','))
m=int(input("Enter Message"))
ct=pow(m,e,n)
s.send(str(ct).encode())
print(f"Encrypted text : {ct}")
