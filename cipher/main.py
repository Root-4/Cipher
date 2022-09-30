import sys
from rot13 import rot13
from fernet import encryption, decryption

print("Hello Encrypted is :", encryption("Hello"))
print("Encrypted text in ROT-13 cipher is ", rot13("HellO"))
