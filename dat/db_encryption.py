# En un script separado, por ejemplo, config_database.py
from db import encrypt

# Datos de conexión a la base de datos
db_username = "ricdeb"
db_password = "0055005544650227"

encrypted_username = encrypt(db_username)
encrypted_password = encrypt(db_password)

# Crea la URL de conexión a la base de datos con los datos encriptados
import dj_database_url

db_url = f"mysql:///{encrypted_username}:{encrypted_password}@db4free.net:3306/storefront3"

print("URL de conexión a la base de datos encriptada:")
print(db_url)

# Usa dj-database-url para cargar la configuración de la base de datos
# db_config = dj_database_url.parse(db_url)