
def mostrar_menu():
    print("\nMENÚ DE OPCIONES")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            saludar()  # Función de Noelia
        elif opcion == "2":
            mostrar_fecha()  # Función de Romina
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
