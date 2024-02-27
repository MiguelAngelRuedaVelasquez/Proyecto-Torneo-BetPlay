equipos = []  #Esto es para registrar los equipos
def registrar_equipo(equipos : list): #agrego parametro que equipos es lista
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    nuevo_equipo = {
        'nombre': nombre_equipo,
        'PJ': 0,'PG': 0,'PP': 0,'PE': 0, 'GF': 0,'GC': 0, 'TP': 0
    }
    equipos.append(nuevo_equipo)

def actualizar_estadisticas(equipo, goles_a_favor, goles_en_contra, resultado): #actualizar las estadisticas
    equipo['PJ'] += 1
    equipo['GF'] += goles_a_favor
    equipo['GC'] += goles_en_contra

    if resultado == "Ganado":
        equipo['PG'] += 1
        equipo['TP'] += 3
    elif resultado == "Empatado":
        equipo['PE'] += 1
        equipo['TP'] += 1
    else:
        equipo['PP'] += 1

def registrar_partido(): #registrar los partidos
    local = input("Ingrese el nombre del equipo local: ")
    visitante = input("Ingrese el nombre del equipo visitante: ")
    goles_local = int(input("Ingrese la cantidad de goles del equipo local: "))
    goles_visitante = int(input("Ingrese la cantidad de goles del equipo visitante: "))

    equipo_local = next((equipo for equipo in equipos if equipo['nombre'] == local))
    equipo_visitante = next((equipo for equipo in equipos if equipo['nombre'] == visitante))

    if goles_local > goles_visitante:
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Ganado")
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Perdido")
    elif goles_local < goles_visitante:
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Ganado")
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Perdido")
    else:
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Empatado")
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Empatado")

def get_goles_anotados(equipo):
    return equipo['GF']

def get_puntos(equipo):
    return equipo['TP']

def get_partidos_ganados(equipo):
    return equipo['PG']

def reporte_max_goles():
    equipo_mas_goles = max(equipos, key=get_goles_anotados)
    print("El equipo que más goles anotó es:", equipo_mas_goles['nombre'])

def reporte_max_puntos():
    equipo_mas_puntos = max(equipos, key=get_puntos)
    print("El equipo que más puntos tiene es:", equipo_mas_puntos['nombre'])

def reporte_max_partidos_ganados():
    equipo_mas_ganados = max(equipos, key=get_partidos_ganados)
    print("El equipo que más partidos ganó es:", equipo_mas_ganados['nombre'])

def total_goles_anotados():
    total_goles = sum(equipo['GF'] for equipo in equipos)
    print("El total de goles anotados por todos los equipos es:", total_goles)

def promedio_goles_anotados():
    total_partidos = sum(equipo['PJ'] for equipo in equipos)
    total_goles = sum(equipo['GF'] for equipo in equipos)
    promedio = total_goles / total_partidos if total_partidos > 0 else 0
    print("El promedio de goles anotados en el torneo es:", promedio)



def mostrar_estadisticas_equipos(): #opcion 6, muestra las estadisticas guardadas en la lista equipos
    print("Estadísticas de todos los equipos:")
    for equipo in equipos:
        print(f"Equipo: {equipo['nombre']}")
        print(f"PJ: {equipo['PJ']}")
        print(f"PG: {equipo['PG']}")
        print(f"PP: {equipo['PP']}")
        print(f"PE: {equipo['PE']}")
        print(f"GF: {equipo['GF']}")
        print(f"GC: {equipo['GC']}")
        print(f"TP: {equipo['TP']}")

