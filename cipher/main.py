import sys
from rot13 import rot13
from fernet import encryption, decryption

def main():
    choice=int(input("Press 1 for Encryption, 2 for Decryption"))
    message=input("Enter the message :")

    if(choice==1):
        print("Encrypted Fernet Text: ", encryption(message))
        print("Encrypted text in ROT-13 cipher: ", rot13(message))
    elif(choice==2):
        print("Decrpted Fernet Text: ", decryption(message))
    else
        print("Bad Choice")

if __name__=="__main__":
    main()
