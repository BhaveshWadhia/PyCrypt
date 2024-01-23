import rsa
from cryptography.fernet import Fernet
from encryptor_module import encrypt_func, shift_key
from decryptor_module import decrypt_func
""""
Module Name: cryptography_module
Functions:   ceaser_cipher(message) - Function contains operations to perform ceaser cipher encryption
Classes:     symmetric_key - Class contains different functions to perform symmetric key encryption
             asymmetric_key - Class contains different functions to perform asymmetric key encryption
Description: PyCrypt different encryption algorithms module
"""


def ceaser_cipher(message, func):
    if func == "encrypt":
        try:
            cipher_txt = encrypt_func(message)
        except Exception:
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return cipher_txt, shift_key
    elif func == "decrypt":
        try:
            decrypt_txt = decrypt_func(message)
        except Exception:
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return decrypt_txt, shift_key


class symmetric_key:
    key = None
    fernet = None

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message):
        try:
            self.cipher_txt = self.fernet.encrypt(message.encode())
            self.cipher_txt = self.cipher_txt.decode()
        except Exception as exp:
            print(exp)
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return str(self.cipher_txt), str(self.key.decode())

    def decrypt(self, message):
        message = message.encode()
        try:
            self.decrypt_txt = self.fernet.decrypt(message).decode()
        except Exception as exp:
            print(exp)
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return str(self.decrypt_txt), str(self.key.decode())


class asymmetric_key:
    publicKey = None
    privateKey = None
    encMessage = None

    def generate_key(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)

    def encrypt(self, message):
        try:
            self.cipher_txt = rsa.encrypt(message.encode(), self.publicKey)
            self.encMessage = self.cipher_txt
        except Exception as exp:
            print(exp)
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return str(self.encMessage), str(self.publicKey), str(self.privateKey)

    def decrypt(self):
        try:
            decrpyt_txt = rsa.decrypt(self.encMessage, self.privateKey).decode()
        except Exception as exp:
            print(exp)
            print("Exception Occurred!!")
            return "Exception Occured!!", "Failed!!"
        return decrpyt_txt, str(self.publicKey), str(self.privateKey)
