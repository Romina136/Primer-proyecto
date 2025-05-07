
def mostrar_menu():
    print("\nMENÚ DE OPCIONES")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1" or opcion == "2":
            print("Opción no implementada en esta rama.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()
