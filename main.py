import modulos.main_menu as mm
import modulos.menu_reportes as menu_reportes
import modulos.registros as r
if __name__ == '__main__' :
    
    AppisRunning = True
    while AppisRunning:
        choice= mm.main_menu()
        if (choice == 1):
            Registrar = True
            while Registrar:
             mm.os.system('cls')
             r.registrar_equipo()
             Registrar = bool(input('Desea agregar otro equipo S(Si) o Enter(No)'))
        elif (choice ==2):
            r.registrar_partido()
        elif (choice == 3): 
            Report= True
            while Report:
                choicer= menu_reportes.menu_reportes()
                if (choicer== 1):
                    r.reporte_max_goles()
                elif (choicer == 2):
                    r.reporte_max_puntos()
                elif (choicer == 3):
                    r.reporte_max_partidos_ganados()
                elif (choicer == 4):
                    r.total_goles_anotados()
                elif (choicer == 5):
                    r.promedio_goles_anotados()
                elif (choicer == 6):
                    r.mostrar_estadisticas_equipos()
                elif (choicer == 7):
                    Report = False
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        elif (choice == 4):
            AppisRunning = False
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            mm.main_menu()
        
    