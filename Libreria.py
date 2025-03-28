# Sistema de Gestión de Libros en una Biblioteca

# Conjuntos para almacenar los libros
coleccion_general = set()
libros_prestados = set()

def mostrar_menu():
    print("\nSistema de Gestión de Libros en una Biblioteca")
    print("1. Registrar libro en la Colección General")
    print("2. Registrar libro como Prestado")
    print("3. Consultar lista total de libros")
    print("4. Identificar libros en Colección General y Prestados")
    print("5. Libros solo en la Colección General")
    print("6. Libros solo en préstamo")
    print("7. Mostrar libros en ambos conjuntos (Colección General y Prestados)")
    print("8. Salir")

#Opcion 1
def registrar_libro_coleccion():
    libro = input("Introduce el nombre del libro para la Colección General: ")
    coleccion_general.add(libro)
    print(f"El libro '{libro}' ha sido registrado en la Colección General.")

#Opcion 2
def registrar_libro_prestado():
    libro = input("Introduce el nombre del libro para marcar como Prestado: ")
    libros_prestados.add(libro)
    print(f"El libro '{libro}' ha sido marcado como Prestado.")

#Opcion 3
def consultar_lista_libros():
    print("\nLista total de libros en la biblioteca:")
    print("Colección General:", coleccion_general)
    print("Libros Prestados:", libros_prestados)

#Opcion 4
def libros_en_ambos_conjuntos():
    # Intersección de la colección general y los libros prestados
    libros_comunes = coleccion_general & libros_prestados
    print("\nLibros en ambos conjuntos (Colección General y Prestados):", libros_comunes)

#Opcion 5
def libros_solo_coleccion():
    # Diferencia entre la colección general y los libros prestados
    libros_solo_coleccion = coleccion_general - libros_prestados
    print("\nLibros solo en la Colección General:", coleccion_general)

#Opcion 6
def libros_solo_prestados():
    # Diferencia entre los libros prestados y la colección general
    libros_solo_prestados = libros_prestados - coleccion_general
    print("\nLibros solo en préstamo:", libros_prestados)

#Opcion 7
def libros_diferencia_simetrica():
    # Diferencia simétrica entre los dos conjuntos (libros en uno de los dos pero no en ambos)
    libros_unicos = coleccion_general ^ libros_prestados
    print("\nLibros únicos en uno de los dos conjuntos (Colección General o Prestados, pero no ambos):", libros_unicos)

def ejecutar():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSelecciona una opción: "))
            if opcion == 1:
                registrar_libro_coleccion()
            elif opcion == 2:
                registrar_libro_prestado()
            elif opcion == 3:
                consultar_lista_libros()
            elif opcion == 4:
                libros_en_ambos_conjuntos()
            elif opcion == 5:
                libros_solo_coleccion()
            elif opcion == 6:
                libros_solo_prestados()
            elif opcion == 7:
                libros_diferencia_simetrica()
            elif opcion == 8:
                print("¡Gracias por usar el Sistema de Gestión de Libros!")
                break
            else:
                print("Opción no válida, por favor elige una opción correcta.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Iniciar el sistema
ejecutar()