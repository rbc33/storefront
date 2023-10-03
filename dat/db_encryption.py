from cryptography.fernet import Fernet
import dj_database_url

# Genera una clave de cifrado (guárdala de forma segura)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(data):
    return cipher_suite.encrypt(data.encode()).decode()


db_username = "ricdeb"
db_password = "0055005544650227"

encrypted_username = encrypt(db_username)
encrypted_password = encrypt(db_password)


db_url = f"mysql:///{encrypted_username}:{encrypted_password}@db4free.net:3306/storefront3"

print("URL de conexión a la base de datos encriptada:")
print(db_url)


