Contactos = {}

def crear_contacto():
    nombre = input("Ingrese el nombre: ")
    if nombre in Contactos:
        print("El contacto ya existe.")
    else:
        telefono = input("Ingrese el número de teléfono: ")
        email = input("Ingrese el email: ")
        nuevos = {"telefono": telefono, "email": email}
        Contactos[nombre] = nuevos
        print("Ha sido agregado con éxito.")

def leer_contactos():
    if not Contactos:
        print("No hay contactos registrados.")
    else:
        for nombre, nuevos in Contactos.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {nuevos['telefono']}")
            print(f"Email: {nuevos['email']}")
            print("------------------------")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in Contactos:
        nuevos = Contactos[nombre]
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {nuevos['telefono']}")
        print(f"Email: {nuevos['email']}")
    else:
        print("Contacto no encontrado")

def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in Contactos:
        print("1. Actualizar teléfono")
        print("2. Actualizar email")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            telefono = input("Ingrese el nuevo número de teléfono: ")
            Contactos[nombre]["telefono"] = telefono
        elif opcion == "2":
            email = input("Ingrese el nuevo email: ")
            Contactos[nombre]["email"] = email
        else:
            print("Opción inválida.")
        print("Contacto actualizado con éxito.")
    else:
        print("Contacto no encontrado")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in Contactos:
        del Contactos[nombre]
        print("Contacto eliminado con éxito.")
    else:
        print("Contacto no encontrado")

while True:
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            crear_contacto()
        elif opcion == "2":
            leer_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            actualizar_contacto()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

