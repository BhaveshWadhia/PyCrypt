import array as arr

"""
Module Name: encryptor_module
Functions:   encrypt_func(message) - To perform ceaser cipher encryption
             generate_key(message) - To generate key for ceaser cipher encryption
Description: PyCrypt encryptor for ceaser cipher module
"""

set_of_keys = "abcdefghijklmnopqrstuvwxyzZ1234567890!@#$%^&-+/*="
shift_key = 2603
encrypted_key = arr.array('i', [])


def encrypt_func(msg):
    result = ""
    global encrypted_key
    # Generate a private key to encrypt the plain text message
    shift_pattern = generate_key(msg)
    for i in range(len(msg)):
        char = msg[i]
        result += chr(ord(char) + shift_pattern[i] % 12)
    # Encrypt the private key values using public
    for i in range(len(shift_pattern)):
        encrypted_key.append((shift_pattern[i] + shift_key) % 12)
    return result


def generate_key(msg):
    keys = arr.array('i', [])
    # Traverse the plain txt & generate a key for every character
    for i in range(len(msg)):
        keys.append(set_of_keys.find(msg[i]))
    return keys
