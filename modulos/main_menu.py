import os
def main_menu():
    os.system('cls')
    while True:
        titulo = """
        ++++++++++++++++++++++++++++++
        + LIGA BETPLAY COLOMBIA 2024 +
        ++++++++++++++++++++++++++++++
        """
        print(titulo)
        print("1. Registrar equipo")
        print("2. Registrar partido")
        print("3. Reportes")
        print("4. Salir")

        choice = int(input("Seleccione una opción: "))
        return choice 
