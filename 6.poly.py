import numpy as np

# poly_key="tanay"


# def poly_encrypt(text):
#     out=""
#     j=0
#     for ch in text.lower():
#         if 'a' <= ch <= 'z':
#             p=ord(ch)-97
#             k=ord(poly_key[j%len(poly_key)])-97
#             out+=chr((p+k)%26+97)
#             j+=1
#         else:
#             out+=ch
#     return out


# def poly_decrypt(text):
#     out=""
#     j=0
#     for ch in text.lower():
#         if 'a' <= ch <= 'z':
#             c=ord(ch)-97
#             k=ord(poly_key[j%len(poly_key)])-97
#             out+=chr((c-k+26)%26+97)
#             j+=1
#         else:
#             out+=ch
#     return out


poly_keys='tanay'

def poly_encrypt(text):
    out='' 
    j=0
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            p=ord(ch)-97
            k=ord(poly_keys[j%len(poly_keys)])-97
            out+=chr((p+k)%26+97)
            j+=1
        else:
            out+=ch
    
    return out
def poly_decrypt(text):
    out='' 
    j=0
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            p=ord(ch)-97
            k=ord(poly_keys[j%len(poly_keys)])-97
            out+=chr((p-k+26)%26+97)
            j+=1
        else:
            out+=ch
    
    return out
        


def main():
    while True:
        choice=int(input("Enter choice: 1/Encrypt - 2/decrypt 3/exit"))
        if choice==1:
            text=input("Enter text:")
            enc = poly_encrypt(text)
            print("Encrypted:", enc)
        elif choice==2:
            text=input("Enter text:")
            dec = poly_decrypt(text)
            print("Decrypted:", dec)
        elif choice==3:
            break
              
main()