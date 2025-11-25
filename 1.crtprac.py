import numpy as np

def eucledian(a,b):
    if(a>b):
        r1=a
        r2=b
    else:
        r1=b
        r2=a
    while(r2!=0):
        q=r1//r2
        r=r1%r2
        r1=r2
        r2=r

    return r1

def MI(a,b):
    if(a<=b):
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    t1=0
    t2=1
    if(eucledian(r1,r2)==1):
        print("Mi Exists")
        while(r2!=0):
            q=r1//r2
            r=r1%r2
            t=t1-t2*q
            t1=t2
            t2=t
            r1=r2
            r2=r
    else:
        print("MI does not exist")
        return
    
    mi=t1
    if (mi<0):
        mi+=b

    return mi

def crt (c,m,k):
    M=1
    for i in range (0,k):
        M=M*m[i]
    
    M_vals=[]
    for i in range (0,k):
        M_vals.append(M//m[i])

    Minv=[]
    for i in range (0,k):
        Minv.append(MI(M_vals[i],m[i]))
    
    cvals=0
    for i in range(0,k):
        cvals+=(c[i]*M_vals[i]*Minv[i])%M

    return cvals%M


def main():
    n1=int(input("Enter Number 1 : "))
    n2=int(input("Enter Number 2 : "))

    m=[]
    k=int(input("Enter number of moduli :"))

    for i in range (0,k):
        m.append(int(input("Enter m[i]")))


    a=[]
    b=[]
    for i in range (0,k):
        a.append(n1%m[i])
        b.append(n2%m[i])

    choice=int(input("Choose Operation 1-Addition / 2-Subtraction / 3-Multiplication / 4-Division"))
    c=[]
    if(choice==1):
        for i in range (0,k):
            c.append((a[i]+b[i])%m[i])
    elif(choice==2):
        for i in range (0,k):
            c.append((a[i]-b[i])%m[i])
    elif(choice==3):
        for i in range (0,k):
            c.append((a[i]*b[i])%m[i])
    elif(choice==4):
        for i in range (0,k):
            c.append((a[i]*MI(b[i],m[i]))%m[i])
    
    print(crt(c,m,k))
main()