import numpy as np

pf_keys = [
    list('playf'),
    list('irbcd'),
    list('eghkm'),
    list('noqst'),
    list('uvwxz')
]

def pf_find(pfkeys, a, b):
    pos = [0] * 4
    for i in range(0, 5):
        for j in range(0, 5):
            if pfkeys[i][j] == a:
                pos[0] = i
                pos[1] = j
            if pfkeys[i][j] == b:
                pos[2] = i
                pos[3] = j
    return pos

def pf_prepare(text):
    text = text.lower().replace('j', 'i')
    cleaned = ""
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            cleaned += ch
            
    result = ''
    i = 0
    while i < len(cleaned):
        a = cleaned[i]
        if (i + 1) < len(cleaned):
            b = cleaned[i + 1]
            if a == b:
                result += a + 'x'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'x'
            i += 1
    return result

def pf_encrypt(text):
    text = pf_prepare(text)
    op = ""
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        r1, c1, r2, c2 = pf_find(pf_keys, a, b)
        if r1 == r2:
            op += pf_keys[r1][(c1 + 1) % 5]
            op += pf_keys[r2][(c2 + 1) % 5]
        elif c1 == c2:
            op += pf_keys[(r1 + 1) % 5][c1]
            op += pf_keys[(r2 + 1) % 5][c2]
        else:
            op += pf_keys[r1][c2]
            op += pf_keys[r2][c1]
    return op

def pf_decrypt(text):
    text = pf_prepare(text) 
    op = ""
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        r1, c1, r2, c2 = pf_find(pf_keys, a, b)
        if r1 == r2:
            op += pf_keys[r1][(c1 - 1) % 5]
            op += pf_keys[r2][(c2 - 1) % 5]
        elif c1 == c2:
            op += pf_keys[(r1 - 1) % 5][c1]
            op += pf_keys[(r2 - 1) % 5][c2]
        else:
            op += pf_keys[r1][c2]
            op += pf_keys[r2][c1]
    return op

def main():
    while True:
        try:
            choice = int(input("Enter choice: 1/Encrypt - 2/Decrypt - 3/Exit: "))
            if choice == 1:
                text = input("Enter text: ")
                enc = pf_encrypt(text)
                print("Encrypted:", enc)
            elif choice == 2:
                text = input("Enter text: ")
                dec = pf_decrypt(text)
                print("Decrypted:", dec)
            elif choice == 3:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()