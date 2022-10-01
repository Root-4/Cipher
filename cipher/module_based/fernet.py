from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


def encryption_fernet(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage


def decryption_fernet(message):
    decMessage = fernet.decrypt(message).decode()
    return decMessage
