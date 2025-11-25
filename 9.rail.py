# EXPERIMENT 9: Rail Fence Transposition Cipher (Single Depth)

def rail_encrypt(text):
    # Remove spaces for standard rail fence
    text = text.replace(" ", "")
    rail1 = ""
    rail2 = ""  # FIX: Originally you had "     " here, which corrupted the data.
    
    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2

def rail_decrypt(cipher):
    # Calculate split point
    mid = (len(cipher) + 1) // 2
    
    rail1 = cipher[:mid]
    rail2 = cipher[mid:]
    
    result = ''
    i = 0
    j = 0
    
    # Zig-zag merge
    while i < len(rail1) or j < len(rail2):
        if i < len(rail1):
            result += rail1[i]
            i += 1
        if j < len(rail2):
            result += rail2[j]
            j += 1
            
    return result

def main():
    while True:
        try:
            choice = int(input("\n--- Rail Fence Cipher ---\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice: "))
            if choice == 1:
                text = input("Enter text to encrypt: ")
                enc = rail_encrypt(text)
                print(f"Encrypted: {enc}")
            elif choice == 2:
                text = input("Enter text to decrypt: ")
                dec = rail_decrypt(text)
                print(f"Decrypted: {dec}")
            elif choice == 3:
                break
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    main()