def encrypt(plain_text: str, key: int) -> str:
    return "".join(
        chr((ord(char) + key - 65) % 26 + 65) if char.isalpha() else char
        for char in plain_text
    )


def decrypt(encrypted_text: str, key: int) -> str:
    return "".join(
        chr((ord(char) - key - 65) % 26 + 65) if char.isalpha() else char
        for char in encrypted_text
    )


def main():
    key = int(input("Enter the key : "))
    plain_text = input("Enter the text to be encrypted : ").upper()
    encrypted_text = encrypt(plain_text, key)
    print("Encrypted text: ", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text: ", decrypted_text)


if __name__ == "__main__":
    main()
