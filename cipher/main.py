import sys
from rot13 import encryption13, decryption13
from module_based.fernet import encryption_fernet, decryption_fernet
from module_based.cipher_rsa import encryption_rsa, decryption_rsa
from module_based.cipher_base64 import encryption64, decryption64

def main():
    choice = int(input("Press 1 for Encryption, 2 for Decryption\n"))
    message = input("Enter the message :\n")

    if choice == 1:
        eType=int(input("Enter\n1 for Fernet\n2 for ROT-13\n3 for rsa\n"))
        if eType == 1:
            print("Encrypted Fernet Text: ", encryption_fernet(message))
        
        elif eType == 2:
            print("Encrypted text in ROT-13 cipher: ", encryption13(message))
        elif eType == 3:
            print("Encrypted text in rsa cipher: ", encryption_rsa(message))
        else:
            print("Bad Choice")
    elif choice == 2:
        dtype=int(input("Enter\n1 for Fernet\n2 for ROT-13\n3 for rsa\n"))
        if dtype == 1:
            print("Decrypted Fernet Text: ", decryption_fernet(message))
        elif dtype == 2:
            print("Decrypted text in ROT-13: ", decryption_13(message))
        elif dtype == 3:
            print("Decrypted rsa Text: ", decryption_rsa(message))
        else:
            print("Bad Choice")
    else:
        print("Bad Choice")


if __name__ == "__main__":
    main()
