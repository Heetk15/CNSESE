# import socket 

# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a

# def mi(a,b):
#     r1=b
#     r2=a
#     t1=0
#     t2=1
#     while r2!=0:
#         q=r1//r2
#         r=r1%r2
#         r1=r2
#         r2=r
#         t=t1-t2*q
#         t1=t2
#         t2=t
#     if t1<0:
#         t1+=b
    
#     return t1

# p=int(input('Enter P'))
# q=int(input('Enter Q'))
# n=p*q
# phi=(p-1)*(q-1)
# e=int(input('Enter e '))
# d=mi(e,phi)

# s=socket.socket()
# s.bind(('localhost',8000))
# s.listen(1)
# conn,_=s.accept()

# conn.send(f'{e},{n}'.encode())


# ct=int(conn.recv(1024).decode())
# pt=pow(ct,d,n)

# print(f"Decrypted {pt}")


import socket

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def mi(a,b):
    r1=b
    r2=a
    t1=0
    t2=1
    while r2!=0:
        q=r1//r2
        r=r1%r2
        t=t1-t2*q
        r1=r2
        r2=r
        t1=t2
        t2=t

    mi=t1
    if mi<0:
        mi+=b
    return mi

p=int(input("Enter P"))
q=int(input("Enter q"))
n=p*q
phi=(p-1)*(q-1)

e=int(input("Enter e"))
d=mi(e,phi)

s=socket.socket()
s.bind(('localhost',8000))
s.listen(1)
conn,_=s.accept()

conn.send(f"{e},{n}".encode())

ct=int(conn.recv(1024).decode())
decrypt=pow(ct,d,n)

print(f"Decrypted Text : {decrypt}")
