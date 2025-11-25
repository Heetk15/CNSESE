# EXPERIMENT 10: Double Transposition Cipher (Double Rail Fence)

# --- Basic Rail Fence Functions ---
def rail_encrypt_single(text):
    text = text.replace(" ", "")
    rail1 = ""
    rail2 = ""
    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]
    return rail1 + rail2

def rail_decrypt_single(cipher):
    mid = (len(cipher) + 1) // 2
    rail1 = cipher[:mid]
    rail2 = cipher[mid:]
    result = ""
    i = j = 0
    while i < len(rail1) or j < len(rail2):
        if i < len(rail1):
            result += rail1[i]
            i += 1
        if j < len(rail2):
            result += rail2[j]
            j += 1
    return result

# --- Double Transposition Logic ---
def double_encrypt(text):
    # Pass 1
    step1 = rail_encrypt_single(text)
    # Pass 2
    step2 = rail_encrypt_single(step1)
    return step2

def double_decrypt(cipher):
    # Reverse Pass 2
    step1 = rail_decrypt_single(cipher)
    # Reverse Pass 1
    original = rail_decrypt_single(step1)
    return original

def main():
    while True:
        try:
            choice = int(input("\n--- Double Rail Fence Cipher ---\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice: "))
            if choice == 1:
                text = input("Enter text to encrypt: ")
                enc = double_encrypt(text)
                print(f"Double Encrypted: {enc}")
            elif choice == 2:
                text = input("Enter text to decrypt: ")
                dec = double_decrypt(text)
                print(f"Double Decrypted: {dec}")
            elif choice == 3:
                break
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    main()