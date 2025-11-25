import numpy as np

def gcd(a,b):
    if(a<b):
        r1=b
        r2=a
    else:
        r1=a
        r2=b
    while b!=0:
        a,b=b,a%b
    return a

def ext(a,b):
    if(a<b):
        r1=b
        r2=a
    else:
        r1=b
        r2=a%b
    t1=0;t2=1;s1=1;s2=0
    if(gcd(a,b)==1):
        print("MI exist")
        while r2!=0:
            q=r1//r2
            r=r1%r2
            t=t1-t2*q
            s=s1-s2*q
            r1=r2
            r2=r
            s1=s2
            s2=s
            t1=t2
            t2=t
    else:
        print("Mi DNEE")
        return
    mi=t1
    if(mi<0):
        mi+=b

    return mi

def main():
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))

    g=gcd(a,b)
    print(f"Gcd {a}, {b} : {g}")
    mi=ext(a,b)
    print(f"MI {a}, {b} : {mi}")


main()
    

    