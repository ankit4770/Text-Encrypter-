def encrypt(text, shift):
    """
    Encrypts the given text using the Caesar Cipher algorithm.

    Args:
        text (str): The text you want to encrypted
        shift (int): The number of positions to shift the letters

    Returns:
        str: The encrypted text
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar Cipher algorithm.

    Args:
        text (str): The text to be decrypted
        shift (int): The number of positions to shift the letters

    Returns:
        str: The decrypted text
    """
    return encrypt(text, -shift)

def main():
    text = input("Enter the text you want to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = encrypt(text, shift)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()