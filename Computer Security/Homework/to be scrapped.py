import base64

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) %BLOCK_SIZE).encode()
unpad = lambda s: s[0:-ord(s[len(s)-1:])]

class AESCipher:
    def __init__(self, key):
        self.key = "{: <16}".format(key)
        self.iv = Random.new().read(AES.block_size)
        self.crypto = AES.new(self.key, AES.MODE_CBC, IV=self.iv)
    
    def encrypt(self ,plaintext, toString=True):

        if(isinstance(plaintext,bytes)):
            plaintext = pad(plaintext)
        else:
            plaintext = pad(plaintext.encode('utf-8'))
        
        print(plaintext)
        print(len(plaintext))

        ciphertext = self.crypto.encrypt(plaintext)

        return base64.b64encode(ciphertext).decode('utf-8') if toString else ciphertext

    def decrypt(self, ciphertext):

        if(isinstance(ciphertext,bytes)):
            ciphertext = self.crypto.decrypt(ciphertext)
        else:
            ciphertext = self.crypto.decrypt(ciphertext.encode('utf-8'))

        return unpad(ciphertext)

if __name__ == "__main__":
    key = "abcdefghijklmnop"
    plaintext=""
    cipher = AESCipher(key)

    filepath = r'Computer Security\과제\04 plaintext.txt'
    with open(filepath,'r',encoding='utf-8') as file:

        for line in file:
            plaintext += line

    encryption = cipher.encrypt(plaintext)

    decryption = cipher.decrypt(encryption)

    print("key : ",key)
    print("encryption : ",encryption)
    print("decryption : ",decryption)
