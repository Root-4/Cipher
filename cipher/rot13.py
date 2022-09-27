

def rot13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])
    return(rt13(message))
