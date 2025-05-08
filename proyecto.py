def mostrar_menu():
    print ("MENU DE OPCIONES")
    print ("1.saludar")
def saludar():
    nombre = input ("como te llamas?")
    print ("holaa! , como estas?",nombre )
def ejecutar_opcion(opcion):
    if opcion == 1:
        saludar()
while True:
    mostrar_menu()
    try:
        opcion = int(input("seleccione una opcion:"))
        ejecutar_opcion(opcion)
    except ValueError:
        print("porfavor ingresa una opcion valida")