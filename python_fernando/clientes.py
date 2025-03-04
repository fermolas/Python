class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print("Email actualizado correctamente.")
    
    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print("Teléfono actualizado correctamente.")

# Ejemplo de uso
cliente1 = Cliente("Juan Pérez", "juan@example.com", "123456789")
print(cliente1.mostrar_info())

cliente1.actualizar_email("nuevojuan@example.com")
cliente1.actualizar_telefono("987654321")
print(cliente1.mostrar_info())
