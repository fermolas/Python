import bcrypt
import json
import os

# Archivo donde se almacenarán los usuarios
USERS_FILE = "usuarios.json"

# Cargar usuarios desde el archivo JSON
def cargar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    return {}

# Guardar usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

# Registrar un nuevo usuario
def registrar_usuario():
    usuarios = cargar_usuarios()
    
    3
    
    contraseña = input("Ingrese una contraseña: ")
    contraseña_hash = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())

    usuarios[usuario] = contraseña_hash.decode()
    guardar_usuarios(usuarios)
    print("✅ Usuario registrado exitosamente.")

# Verificar credenciales de inicio de sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario not in usuarios:
        print("❌ Usuario no encontrado.")
        return

    contraseña = input("Ingrese su contraseña: ")
    contraseña_hash = usuarios[usuario].encode()
    
    if bcrypt.checkpw(contraseña.encode(), contraseña_hash):
        print("✅ Inicio de sesión exitoso.")
    else:
        print("❌ Contraseña incorrecta.")

# Menú principal
def menu():
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
