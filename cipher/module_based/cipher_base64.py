import base64


def encryption64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encoded = base64_bytes.decode('ascii')
    print(encoded)
    return(encoded)


def decryption64(message):
    base64_bytes = message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decoded = message_bytes.decode('ascii')
    print(decoded)
    return(decoded)