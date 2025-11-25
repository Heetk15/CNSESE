import math

def get_key_order(key):
    # Create a sequence of numbers based on alphabetical order of key
    # Example: "ZEBRA" -> [4, 0, 1, 2, 3] (because A is index 1, B is 2, etc.)
    key_map = sorted([(char, i) for i, char in enumerate(key)])
    return [item[1] for item in key_map]

def encrypt_row_col(text, key):
    # Remove spaces
    text = text.replace(" ", "").lower()
    
    # Calculate dimensions
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    
    # Pad the text with 'x' to make it a perfect rectangle
    padding = (num_rows * num_cols) - len(text)
    text += 'x' * padding
    
    # Create the matrix (grid)
    matrix = []
    for i in range(num_rows):
        row = list(text[i * num_cols : (i + 1) * num_cols])
        matrix.append(row)
        
    # Read off columns based on key order
    key_order = get_key_order(key)
    ciphertext = ""
    
    for col_idx in key_order:
        for row in range(num_rows):
            ciphertext += matrix[row][col_idx]
            
    return ciphertext

def decrypt_row_col(cipher, key):
    # Calculate dimensions
    num_cols = len(key)
    num_rows = math.ceil(len(cipher) / num_cols)
    
    # Get the order to fill columns back in
    key_order = get_key_order(key)
    
    # Create an empty matrix
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the matrix column by column, following the key order
    current_char_idx = 0
    for col_idx in key_order:
        for row in range(num_rows):
            if current_char_idx < len(cipher):
                matrix[row][col_idx] = cipher[current_char_idx]
                current_char_idx += 1
    
    # Read the matrix row by row to get plaintext
    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext += matrix[row][col]
            
    return plaintext.rstrip('x') # Remove the padding we added

def main():
    while True:
        try:
            choice = int(input("\n--- Row Column Transposition ---\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice: "))
            if choice == 1:
                text = input("Enter text: ")
                key = input("Enter keyword (e.g., HACK): ")
                enc = encrypt_row_col(text, key)
                print(f"Encrypted: {enc}")
            elif choice == 2:
                text = input("Enter text: ")
                key = input("Enter keyword: ")
                dec = decrypt_row_col(text, key)
                print(f"Decrypted: {dec}")
            elif choice == 3:
                break
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()