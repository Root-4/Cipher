import rsa


publicKey, privateKey = rsa.newkeys(512)


def encryption_rsa(message):
    encoded = rsa.encrypt(message.encode(), publicKey)
    return encoded


def decryption_rsa(message):
    decoded = rsa.decrypt(message, privateKey).decode()
    return decoded
