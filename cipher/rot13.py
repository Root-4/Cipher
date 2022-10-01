def encryption13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])
    return rt13(message.lower())


def decryption13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])
    return rt13(message.lower())
