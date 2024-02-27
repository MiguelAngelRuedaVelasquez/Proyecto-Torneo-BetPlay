import os
def menu_reportes():
    os.system('cls')
    while True:
        titulo = """
        ++++++++++++++++++++++++++++++
        + LIGA BETPLAY COLOMBIA 2024 +
        ++++++++++++++++++++++++++++++
        """
        print(titulo)
        print("1. Equipo con más goles anotados")
        print("2. Equipo con más puntos")
        print("3. Equipo con más partidos ganados")
        print("4. Total de goles anotados por todos los equipos")
        print("5. Promedio de goles anotados en el torneo")
        print("6. Ver estadísticas de todos los equipos")
        print("7. Volver al menú principal")

        choicer = int(input("Seleccione una opción: "))
        return choicer