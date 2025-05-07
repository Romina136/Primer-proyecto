import datetime

def saludar():
    nombre = input("Ingrese su nombre: ")
    print("Hola,", nombre)

def mostrar_fecha():
    ahora = datetime.datetime.now()
    print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))

def mostrar_menu():
    print("\nMenú de opciones")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            saludar()
        elif opcion == "2":
            mostrar_fecha()
        elif opcion == "3":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    ejecutar_menu()
