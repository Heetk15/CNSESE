import numpy as np 

def double_encrypt(text):
    text=text.replace(" ","")
    rail1=""
    rail2="     "
    
    for i in range(0,len(text)):
        if i%2==0:
            rail1+=text[i]
        else:
            rail2+=text[i]

    return rail1+rail2

def double_decrypt(text):
    mid=(len(text)+1)//2
    rail1=text[:mid]
    rail2=text[mid:]
    result=''
    i=j=0
    while i <len(rail1) or j <len(rail2):
        if i<len(rail1):
            result+=rail1[i]
            i+=1
        if j<len(rail2):
            result+=rail2[j]
            j+=1
    return result

def main():
    
    text = "tanay"
    encrypted = double_encrypt(text)
    print(f"encrypted text = {encrypted}")
    decrypted = double_decrypt(encrypted)
    print(f"decrypted text = {decrypted}")
main()