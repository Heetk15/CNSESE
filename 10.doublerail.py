def rail_encrypt(text):
    text = text.replace(" ", "")
    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2


def rail_decrypt(cipher):
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


# ---------------- DOUBLE RAIL FENCE ---------------- #

def double_encrypt(text):
    step1 = rail_encrypt(text)     # First rail fence
    final = rail_encrypt(step1)    # Second rail fence
    return final


def double_decrypt(cipher):
    step1 = rail_decrypt(cipher)    # Undo second rail fence
    final = rail_decrypt(step1)     # Undo first rail fence
    return final


# ---------------- TEST ---------------- #

def main():
    text = "tanay"

    enc = double_encrypt(text)
    print("Double Encrypted:", enc)

    dec = double_decrypt(enc)
    print("Double Decrypted:", dec)

main()
