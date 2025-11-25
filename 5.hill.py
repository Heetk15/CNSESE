import numpy as np
from sympy import Matrix

# hill_key=np.array([
#     [6, 24, 1],
#     [13, 16, 10],
#     [20, 17, 15]
# ])

# inv_hill=np.array(Matrix(hill_key).inv_mod(26))

# def hill_encrypt(text):
#     text=text.lower()
#     if len(text)%3 !=0:
#         print("Invalid String")
#         return 
    
#     result=""
#     for i in range (0,len(text),3):
#         block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
#         encrypted=(hill_key.dot(block))%26
#         for x in encrypted:
#             result+=chr(x[0]+97)
        
#     return result

# def hill_decrypt(text):
#     text=text.lower()
#     if len(text)%3 !=0:
#         print("Invalid String")
#         return 
    
#     result=""
#     for i in range (0,len(text),3):
#         block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
#         encrypted=(inv_hill.dot(block))%26
#         for x in encrypted:
#             result+=chr(x[0]+97)
        
#     return result


hill_key=np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

hill_inv=np.array(Matrix(hill_key).inv_mod(26))

def hill_encrypt(text):
    if len(text)%3 !=0:
        print("String INvalid")
        return
    
    result=""
    for i in range(0,len(text),3):
        block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
        encrypted=(hill_key.dot(block))%26
        
        for x in encrypted:
            result+=chr(x[0]+97)
        
    return result
def hill_decrypt(text):
    if len(text)%3 !=0:
        print("String INvalid")
        return
    
    result=""
    for i in range(0,len(text),3):
        block=np.array([[ord(text[i])-97],[ord(text[i+1])-97],[ord(text[i+2])-97]])
        encrypted=(hill_inv.dot(block))%26
        
        for x in encrypted:
            result+=chr(x[0]+97)
        
    return result

def main():
    while True:
        choice=int(input("Enter choice: 1/Encrypt - 2/decrypt 3/exit"))
        if choice==1:
            text=input("Enter text:")
            enc = hill_encrypt(text)
            print("Encrypted:", enc)
        elif choice==2:
            text=input("Enter text:")
            dec = hill_decrypt(text)
            print("Decrypted:", dec)
        elif choice==3:
            break
        


        
main()


