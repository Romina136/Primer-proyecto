def menu():
    while True  :
        print("\nMenú de opciones:")
        print("1. Saludar")
        print("2. Mostrar fecha")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "3":
            print("salir del programa")
        else:
            print("Opción no implementada en esta rama.")


if __name__ == "__main__":
    menu()
