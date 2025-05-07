import datetime

# Función de Noelia
def saludar():
    nombre = input("¿Cómo te llamas? ")
    print("¡Hola! ¿Cómo estás,", nombre + "?")

# Función de Romina
def mostrar_fecha():
    hoy = datetime.datetime.now()
    print("Fecha y hora actual:", hoy.strftime("%Y-%m-%d %H:%M:%S"))

# Función de Araceli (tú)
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
            saludar()
        elif opcion == "2":
            mostrar_fecha()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Por favor, ingresa una opción válida.")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_menu()
