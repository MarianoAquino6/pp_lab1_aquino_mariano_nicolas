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
    with open(file_adress,"r", encoding="utf-8") as lovely_file:
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

# 1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
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

# 4) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
# campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
# Fama del Baloncesto, etc.

def show_every_player(dream_team_list):
    players_list_names = []
    for player in dream_team_list:
        players_list_names.append(player["nombre"])
    return players_list_names

def validate_input_and_return_fixed_input(dream_team_list):
    user_choice_player_name = input("Ingrese el nombre del jugador: ")
    result_alphabetic = re.search("^[a-zA-Z ]+$",user_choice_player_name)
    if result_alphabetic:
        fixed_user_choice_player_name = user_choice_player_name.strip().title()
        if fixed_user_choice_player_name in show_every_player(dream_team_list):
            for index in range(len(dream_team_list)):
                if fixed_user_choice_player_name == dream_team_list[index]["nombre"]:
                    selected_player_index = index
                    return selected_player_index
        else:
            print("El jugador ingresado no pertenece al Dream Team")
            return -80
    else:
        print("Solo ingresar caracteres alfabeticos")
        return -80

def show_achievements(dream_team_list, selected_player):
    achievements_txt = "\n".join(dream_team_list[selected_player]["logros"])
    achievements_message = f"Logros de {dream_team_list[selected_player]['nombre']}: \n{achievements_txt}"
    return achievements_message

# 5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
# Team, ordenado por nombre de manera ascendente.

def calculate_and_show_avg_score_by_game(dream_team_list):
    accumulator = 0
    for player in dream_team_list:
        accumulator = accumulator + player["estadisticas"]["promedio_puntos_por_partido"]
    score_by_game_avg = accumulator / len(dream_team_list)

    return f"El promedio de puntos por partido de todo el equipo junto es de {score_by_game_avg} puntos."

def order_players_by_avg_score_by_game_asc(dream_team_list):
    dream_team_list_sorted = dream_team_list[:]
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for index_A in range(len(dream_team_list_sorted) - 1):
                if dream_team_list_sorted[index_A]["estadisticas"]["promedio_puntos_por_partido"] > dream_team_list_sorted[index_A+1]["estadisticas"]["promedio_puntos_por_partido"]:
                    dream_team_list_sorted[index_A],dream_team_list_sorted[index_A+1] = dream_team_list_sorted[index_A+1],dream_team_list_sorted[index_A]
                    flag_swap = True
    
    sorted_players_names_list = []
    for index in range(len(dream_team_list_sorted)):
        to_save_string = f"{index+1}°. {dream_team_list_sorted[index]['nombre']}"
        sorted_players_names_list.append(to_save_string)
    sorted_players_names_txt = "\n".join(sorted_players_names_list)

    return sorted_players_names_txt

# 6) Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
# miembro del Salón de la Fama del Baloncesto.

def show_if_player_belongs_to_basketball_hall_of_fame(dream_team_list, selected_player):
    achievements_string = " ".join(dream_team_list[selected_player]["logros"])
    result_hall_of_fame = re.search("Fama", achievements_string)
       
    if result_hall_of_fame:
        return f"{dream_team_list[selected_player]['nombre']} pertenece al Basketball Hall of Fame"
    else:
        return f"{dream_team_list[selected_player]['nombre']} no pertenece al Basketball Hall of Fame"

# 7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales

def show_top_rebound_player(dream_team_list):
    flag_top_rebound_player = False
    for player in dream_team_list:
        if flag_top_rebound_player == False:
            max_rebounds_player_name = player["nombre"]
            max_rebounds = player["estadisticas"]["rebotes_totales"]
            flag_top_rebound_player = True
        elif player["estadisticas"]["rebotes_totales"] > max_rebounds:
            max_rebounds_player_name = player["nombre"]
            max_rebounds = player["estadisticas"]["rebotes_totales"]
    return f"El jugador con mayor cantidad de rebotes totales es: {max_rebounds_player_name}"

# 8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.

def show_top_field_goal_player(dream_team_list):
    flag_top_field_goal_player = False
    for player in dream_team_list:
        if flag_top_field_goal_player == False:
            max_field_goal_player_name = player["nombre"]
            max_field_goal = player["estadisticas"]["porcentaje_tiros_de_campo"]
            flag_top_field_goal_player = True
        elif player["estadisticas"]["porcentaje_tiros_de_campo"] > max_field_goal:
            max_field_goal_player_name = player["nombre"]
            max_field_goal = player["estadisticas"]["porcentaje_tiros_de_campo"]
    return f"El jugador con mayor porcentaje de tiros de campo es: {max_field_goal_player_name}"

# 9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.

def show_top_assist_player(dream_team_list):
    flag_top_assist_player = False
    for player in dream_team_list:
        if flag_top_assist_player == False:
            max_assist_player_name = player["nombre"]
            max_assist = player["estadisticas"]["asistencias_totales"]
            flag_top_assist_player = True
        elif player["estadisticas"]["asistencias_totales"] > max_assist:
            max_assist_player_name = player["nombre"]
            max_assist = player["estadisticas"]["asistencias_totales"]
    return f"El jugador con mayor cantidad de asistencias es: {max_assist_player_name}"

# 10) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
# más puntos por partido que ese valor.

def show_above_score_by_game_avg_players(dream_team_list, user_input):
    above_avg_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["promedio_puntos_por_partido"] > user_input:
            above_avg_players_list.append(player["nombre"])
    if len(above_avg_players_list) > 0:
        above_avg_players_string = "\n".join(above_avg_players_list)
    else:
        above_avg_players_string = "No hay jugadores que hayan superado dicho promedio"
    return above_avg_players_string

# 11) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
# más rebotes por partido que ese valor.

def show_above_rebounds_by_game_avg_players(dream_team_list, user_input):
    above_avg_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["promedio_rebotes_por_partido"] > user_input:
            above_avg_players_list.append(player["nombre"])
    if len(above_avg_players_list) > 0:
        above_avg_players_string = "\n".join(above_avg_players_list)
    else:
        above_avg_players_string = "No hay jugadores que hayan superado dicho promedio"
    return above_avg_players_string

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
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                else:
                    print("Ha ingresado un indice invalido (Ingresar solo numeros)")

                if user_choice_player_int < 12:
                    for item, value in show_player_stadistics(dream_team_list_duplicate, user_choice_player_int).items():
                        print(f"{item}: {value}")
                    flag_enable_csv = True
                else:
                    print("Ha ingresado un indice invalido (Superior a la cantidad de los jugadores disponibles)")
            case 3:
                if flag_enable_csv == True:
                    save_stadistics_in_csv(dream_team_list_duplicate, user_choice_player_int)
                else:
                    print("Primero debe seleccionar la opcion 2")
            case 4:
                players_names_txt = "\n".join(show_every_player(dream_team_list_duplicate))
                print(f"Se presentan a continuacion los nombres de los jugadores: \n{players_names_txt}")

                input_validation = validate_input_and_return_fixed_input(dream_team_list_duplicate)
                if input_validation >= 0:
                    print(show_achievements(dream_team_list_duplicate, input_validation))
            case 5:
                print(calculate_and_show_avg_score_by_game(dream_team_list_duplicate))
                print(f"A continuacion, los jugadores ordenados de acuerdo a su promedio de puntos por partido: \n{order_players_by_avg_score_by_game_asc(dream_team_list_duplicate)}")
            case 6:
                players_names_txt = "\n".join(show_every_player(dream_team_list_duplicate))
                print(f"Se presentan a continuacion los nombres de los jugadores: \n{players_names_txt}")

                input_validation = validate_input_and_return_fixed_input(dream_team_list_duplicate)
                if input_validation >= 0:
                    print(show_if_player_belongs_to_basketball_hall_of_fame(dream_team_list_duplicate, input_validation))
            case 7:
                print(show_top_rebound_player(dream_team_list_duplicate))    
            case 8:
                print(show_top_field_goal_player(dream_team_list_duplicate)) 
            case 9:
                print(show_top_assist_player(dream_team_list_duplicate)) 
            case 10:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_score_by_game_avg_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 11:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_rebounds_by_game_avg_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case _:
                print("Ha ingresado una opcion incorrecta")
        clear_console()

dream_team_app(leer_archivo(json_path))