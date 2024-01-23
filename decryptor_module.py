from encryptor_module import encrypted_key, shift_key, arr

"""
Module Name: decryptor_module
Functions:   decrypt_func(message) - To perform ceaser cipher decryption 
Description: PyCrypt decryptor for ceaser cipher module
"""


def decrypt_func(msg):
    result = ""
    shift_pattern = arr.array('i', [])
    # Decrypt the key
    for j in range(len(encrypted_key)):
        shift_pattern.append((encrypted_key[j] - shift_key) % 12)
    # Transverse the plain txt
    for i in range(len(msg)):
        char = msg[i]
        result += chr(ord(char) - shift_pattern[i] % 12)
    return result
