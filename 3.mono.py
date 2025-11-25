import numpy as np


# mono_list=list('qwertyuiopasdfghjklzxcvbnm')
# def mono_encrypt(text):
#     result=""
#     for ch in text.lower():
#         if 'a'<= ch <= 'z':
#             result+=(mono_list[(ord(ch)-97)])
#         else:
#             result+=ch
    
#     return result


# def mono_decrypt(text):
#     result=""
#     for ch in text.lower():
#         if 'a'<= ch <= 'z':
#             idx=mono_list.index(ch)
#             result+=chr(idx+97)
#         else:
#             result+=ch
    
#     return result
    

mono_key=list('qwertyuiopasdfghjklzxcvbnm')
def mono_encrypt(text):
    result=""
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            result+=(mono_key[(ord(ch)-97)])
        else:
            result+=ch
    
    return result


def mono_decrypt(text):
    result=""
    for ch in text.lower():
        if 'a' <= ch <='z':
            idx=mono_key.index(ch)
            result+=chr(idx+97)
        else:
            result+=ch
    return result


def main():
    while True:
        choice=int(input("Enter choice: 1/Encrypt - 2/decrypt 3/exit"))
        if choice==1:
            text=input("Enter text:")
            enc = mono_encrypt(text)
            print("Encrypted:", enc)
        elif choice==2:
            text=input("Enter text:")
            dec = mono_decrypt(text)
            print("Decrypted:", dec)
        elif choice==3:
            break
           
main()