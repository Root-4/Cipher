import sys
from rot13 import encryption13, decryption13
from module_based.fernet import encryption_fernet, decryption_fernet
from module_based.cipher_rsa import encryption_rsa, decryption_rsa


def main():
    choice = int(input("Press 1 for Encryption, 2 for Decryption"))
    message = input("Enter the message :")

    if choice == 1:
        print("Encrypted Fernet Text: ", encryption_fernet(message))
        print("Encrypted text in ROT-13 cipher: ", encryption13(message))
        print("Encrypted text in rsa cipher: ", encryption_rsa(message))
    elif choice == 2:
        print("Decrypted Fernet Text: ", decryption_fernet(message))
        print("Decrypted text in ROT-13: ", decryption_13(message))
        print("Decrypted rsa Text: ", decryption_rsa(message))
    else:
        print("Bad Choice")


if __name__ == "__main__":
    main()
