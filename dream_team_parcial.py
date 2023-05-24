import re
import json
import os

json_path = r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\Parcial\pp_lab1_aquino_mariano_nicolas\dream_team.json"

def imprimir_dato(given_string):
    #Takes a string as input
    #Prints the string
    print(given_string)

def imprimir_menu():
    # Prints the menu
    menu_dream_team =\
    """
    Bienvenido al PARCIAL DE MAYO. A continuacion, el menu de opciones:
    1. Mostrar la lista de todos los jugadores del Dream Team.
    2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas.
    3. Guardar las estadísticas del jugador seleccionado en el punto 2 en un archivo CSV.
    4. Buscar un jugador por su nombre y mostrar sus logros.
    5. Obtener promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
    6. Averiguar si el jugador pertenece al Salon de la fama del Baloncesto.
    7. Obtener el jugador con la mayor cantidad de rebotes totales.
    8. Obtener el jugador con el mayor porcentaje de tiros de campo.
    9. Obtener el jugador con la mayor cantidad de asistencias totales.
    10. Ingresar un valor y obtener los jugadores que han promediado más puntos por partido que ese valor.
    11. Ingresar un valor y obtener los jugadores que han promediado más rebotes por partido que ese valor.
    12. Ingresar un valor y obtener los jugadores que han promediado más asistencias por partido que ese valor.
    13. Obtener el jugador con la mayor cantidad de robos totales.
    14. Obtener el jugador con la mayor cantidad de bloqueos totales.
    15. Ingresar un valor y obtener los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
    16. Obtener el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
    17. Obtener el jugador con la mayor cantidad de logros obtenidos.
    18. Ingresar un valor y obtener los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
    19. Obtener el jugador con la mayor cantidad de temporadas jugadas.
    20. Ingresar un valor y obtener los jugadores , ordenados por posición en la cancha, que hayan tenido un 
    porcentaje de tiros de campo superior a ese valor.
    21. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking:
    ● Puntos 
    ● Rebotes 
    ● Asistencias 
    ● Robos
    Obtener el csv correspondiente.
    _________________________________________________________________________________________________________________
    """
    imprimir_dato(menu_dream_team)

def menu_principal():
    imprimir_menu()
    user_input_str = input("Ingrese su opcion: ")
    result = re.match("^([0-9])|([0-1][0-9])|(2[0-1])$", user_input_str)
    if result:
        return int(user_input_str)
    else:
        return -1

def leer_archivo(file_adress):
    with open(file_adress,"r") as lovely_file:
        data = json.load(lovely_file)
        dream_team_list = data["jugadores"]
    return dream_team_list

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

# EJERCICIO 1: Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def show_all_players(dream_team_list):
    players_list = []
    for player in dream_team_list:
        message = f"{player['nombre']} - {player['posicion']}"
        players_list.append(message)
    return players_list

# 2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
# completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
# partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
# promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
# tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

def show_player_stadistics(dream_team_list, index_choice):
    players_stadistics_dictionary = dream_team_list[index_choice]["estadisticas"]
    return players_stadistics_dictionary

# 3) Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
# permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El
# archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
# puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes
# por partido, asistencias totales, promedio de asistencias por partido, robos totales,
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
# porcentaje de tiros triples.

def save_stadistics_in_csv(dream_team_list, selected_index):
    with open("parcial_punto_2.csv", "w") as file:
                file.write("nombre,posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples")
                file.write("\n")

                player_stadistics_exercise_2_dict = show_player_stadistics(dream_team_list, selected_index)
                player_stadistics_list = []
                for item in player_stadistics_exercise_2_dict.values():
                    item_txt = str(item)
                    player_stadistics_list.append(item_txt)
                player_stadistics_numbers_string = ",".join(player_stadistics_list)
                
                file.write(f"{dream_team_list[selected_index]['nombre']},{dream_team_list[selected_index]['posicion']},{player_stadistics_numbers_string}")

def dream_team_app(dream_team_list):
    dream_team_list_duplicate = dream_team_list[:]
    flag_enable_csv = False
    while True:
        user_choice = menu_principal()
        match(user_choice):
            case 1:
                for item in show_all_players(dream_team_list_duplicate):
                    print(item)
            case 2:
                for i in range(len(dream_team_list_duplicate)):
                    print (f"Indice: {i} - {show_all_players(dream_team_list_duplicate)[i]}")
                user_choice_player_txt = input("Ingrese el indice deseado: ")
                user_choice_player_int = int(user_choice_player_txt)
                if user_choice_player_int < 12:
                    for item, value in show_player_stadistics(dream_team_list_duplicate, user_choice_player_int).items():
                        print(f"{item}: {value}")
                    flag_enable_csv = True
                else:
                    print("Ha ingresado un indice invalido")
            case 3:
                if flag_enable_csv == True:
                    save_stadistics_in_csv(dream_team_list_duplicate, user_choice_player_int)
                else:
                    print("Primero debe seleccionar la opcion 2")
        clear_console()

dream_team_app(leer_archivo(json_path))