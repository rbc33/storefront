from cryptography.fernet import Fernet

# Genera una clave de cifrado (guárdala de forma segura)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(data):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt(encrypted_data):
    return cipher_suite.decrypt(encrypted_data.encode()).decode()
