import re
import json
import os
import time

json_path = r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\Parcial\pp_lab1_aquino_mariano_nicolas\dream_team.json"

def imprimir_menu():
    """
    The function "imprimir_menu()" prints a menu with various options for a basketball statistics
    program.
    """
    menu_dream_team =\
    """
    ⠀⣶⣶⣶⣶⣶⣶⣶⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⡆⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣄⠀⠀⠀⠀⠀⢠⣶⣶⣶⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣾⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⠁⠀⠀⢿⣿⣿⣿⣿⣿⣿⡇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀
    ⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
    ⢠⣭⣭⣭⣭⣭⣭⣥⠀⠀⠀⢠⣭⣭⣭⣭⣭⣭⡄⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣥⡄⣬⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⡄⠀⠀⠀⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⣀⣀⣀⣀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣄⣀⣀⣼⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣧⣤⣾⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⠁⠈⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⡆⠀⠀
    ⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⠀⠀
    ⠀⠀⠈⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠋⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣡⣤⣴⠄⠀⢸⣿⣿⣿⣿⣿⣿⣇⠀
    ⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣠⡀⠀⠀⠠⠁⠘⣿⣿⠀⢠⣾⣿⡄⠀⠀⣀⣀⣁⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣶⣤⣤⡾⠻⣶⡾⠛⠛⢧⣤⣾⣿⣿⣿⠀
    ⢸⣿⠉⣭⢹⣿⠉⢿⡏⢩⣹⡏⠟⣩⡏⣩⣭⣯⠉⣭⡏⣭⠙⣿⠉⢻⡏⣿⣿⠉⣿⣿⣿⣿⠟⢿⡿⠃⠀⣿⣿⣄⡀⢿⣿⣿⣿⣿⣿⠀
    ⢸⣿⠀⣤⠘⡇⠐⠸⡷⣤⠘⡇⣄⢹⡇⣤⣴⣿⠀⣿⡇⣤⠘⡏⠘⠘⡇⣿⣿⠀⣿⣿⣿⡟⠀⠀⠁⠂⣠⣟⠛⠉⠀⠀⢿⣿⣿⣿⣿⠀
    ⢸⣿⣦⣤⣾⣶⣿⣷⣷⣤⣾⣷⣿⣦⣧⣤⣤⣿⣶⣿⣧⣤⣶⣷⣿⣶⣷⣤⣼⣦⣤⣼⣿⠁⠀⢀⣴⣾⣿⣿⣷⣤⡀⠀⠘⣿⣿⣿⣿⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⢹⣿⣿⣿

    Bienvenido al PARCIAL DE MAYO 2023. A continuacion, el menu de opciones:
    1. Mostrar la lista de todos los jugadores del Dream Team.
    2. Seleccionar un jugador por su índice y mostrar sus estadísticas completas.
    3. Guardar las estadísticas del jugador seleccionado en el punto 2 en un archivo ".csv".
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
    Obtener el archivo ".csv" correspondiente.
    22. (EXTRA) Ingresar un valor y obtener los jugadores que hayan jugado igual o mas cantidad de partidos All-Star que ese valor.
    23. (EXTRA) Obtener el jugador con mayor cantidad de partidos All-Star jugados
    24. (EXTRA) Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking:
    ● Porcentaje de tiros de campo
    ● Porcentaje de tiros libres
    ● Porcentaje de tiros triples
    Obtener el archivo ".csv" correspondiente.
    25. (EXTRA) Obtener la cantidad de jugadores cuya posicion es Ala-Pivot
    26. (EXTRA) Obtener nombres de aquellos jugadores cuya posicion sea Ala-Pivot
    27. (EXTRA) Obtener nombres de aquellos jugadores cuya posicion sea Base
    28. (JUEGO EXTRA): Se le hará una pregunta sobre las estadisticas obtenidas a lo largo del menu 
    y usted deberá contestarla, para luego comprobar si su respuesta es correcta o incorrecta.
    29. (EXTRA) Si ha respondido 2 o mas preguntas correctamente en el juego de la opción 28, podrá acceder a un certificado ".txt".
    30. SALIR
    _________________________________________________________________________________________________________________
    """
    print(menu_dream_team)

def menu_principal():
    """
    The function "menu_principal" takes user input and returns an integer if it matches a specific
    pattern, otherwise it returns -1.
    :return: The function `menu_principal()` returns an integer value representing the user's selected
    option from the menu. If the user's input is not a valid option, the function returns -1.
    """
    imprimir_menu()
    user_input_str = input("Ingrese su opcion: ")
    result = re.search("^([1-9]|0[1-9]|[1-2][0-9]|30)$", user_input_str)
    if result:
        return int(user_input_str)
    else:
        return -1

def leer_archivo(file_adress):
    """
    The function reads a JSON file and returns a list of players from the file.
    
    :param file_adress: The file path or address of the JSON file that needs to be read
    :return: a list of players from a JSON file located at the file address specified in the function
    argument.
    """
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

#--------------------------------------------EXERCISES------------------------------------------------------

# 1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def show_all_players(dream_team_list):
    """
    The function takes a list of dictionaries representing players in a dream team and returns a list of
    strings containing each player's name and position.
    
    :param dream_team_list: A list of dictionaries containing information about each player in a dream
    team. Each dictionary should have the following keys: 'nombre' (player name), 'posicion' (player
    position)
    :return: a list of strings, where each string contains the name and position of a player in the
    input `dream_team_list`.
    """
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
    """
    The function returns the statistics dictionary of a player from a dream team list based on the index
    choice.
    
    :param dream_team_list: a list of dictionaries representing a dream team, where each dictionary
    contains information about a player, including their name, position, and statistics
    :param index_choice: The index of the player in the dream_team_list whose statistics we want to
    retrieve
    :return: the statistics dictionary of a player from the dream team list based on the index choice
    provided.
    """
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
    """
    This function saves the statistics of a selected player from a dream team list into a CSV file.
    
    :param dream_team_list: A list of dictionaries containing information about basketball players,
    including their name, position, and statistics
    :param selected_index: The index of the player in the dream_team_list whose statistics are to be
    saved in the CSV file
    """
    with open("parcial_punto_3.csv", "w") as file:
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
    """
    The function takes a list of dictionaries representing players and returns a list of their names.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains information such as the player's name, position, and statistics
    :return: a list of player names from the input list of dictionaries `dream_team_list`.
    """
    players_list_names = []
    for player in dream_team_list:
        players_list_names.append(player["nombre"])
    return players_list_names

def validate_input_and_return_player_index(dream_team_list):
    """
    This function validates user input for a player's name and returns the index of the player in a
    dream team list.
    
    :param dream_team_list: a list of dictionaries representing a Dream Team, where each dictionary
    contains information about a player such as their name, position, and stats
    :return: the index of the player selected by the user if the input is valid and the player is in the
    dream team list. If the input is invalid or the player is not in the dream team list, the function
    returns -80.
    """
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
    """
    The function takes a list of players and a selected player, and returns a string containing the
    achievements of the selected player.
    
    :param dream_team_list: A list of dictionaries containing information about each player in a dream
    team, such as their name, position, and achievements
    :param selected_player: The index of the player in the dream_team_list whose achievements we want to
    display
    :return: The function `show_achievements` returns a string message that displays the achievements of
    a selected player from a dream team list. The message includes the player's name and a list of their
    achievements.
    """
    achievements_txt = "\n".join(dream_team_list[selected_player]["logros"])
    achievements_message = f"Logros de {dream_team_list[selected_player]['nombre']}: \n{achievements_txt}"
    return achievements_message

# 5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
# Team, ordenado por nombre de manera ascendente.

def calculate_and_show_avg_score_by_game(dream_team_list):
    """
    This function calculates and returns the average score per game for a given list of players.
    
    :param dream_team_list: a list of dictionaries representing the players in a dream team, where each
    dictionary contains information about the player's statistics and performance. Specifically, each
    dictionary has a key "estadisticas" which contains another dictionary with the key
    "promedio_puntos_por_partido" representing the player's average score
    :return: a string that includes the average score per game of a given dream team list.
    """
    accumulator = 0
    for player in dream_team_list:
        accumulator = accumulator + player["estadisticas"]["promedio_puntos_por_partido"]
    score_by_game_avg = accumulator / len(dream_team_list)

    return f"El promedio de puntos por partido de todo el equipo junto es de {score_by_game_avg} puntos."

def order_players_by_avg_score_by_game_asc(dream_team_list):
    """
    This function orders a list of players by their average score per game in ascending order and
    returns a string with their names and rankings.
    
    :param dream_team_list: A list of dictionaries, where each dictionary represents a player in a dream
    team and contains information about the player's name and statistics. The statistics are stored in a
    nested dictionary under the key "estadisticas", and include the player's average score per game
    :return: a string with the names of the players in the input list "dream_team_list", sorted in
    ascending order by their average score per game. The string includes the position of each player in
    the sorted list.
    """
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
    """
    This function checks if a selected basketball player belongs to the Basketball Hall of Fame based on
    their achievements.
    
    :param dream_team_list: a dictionary containing information about basketball players, where the keys
    are the player's name and the values are another dictionary with the player's achievements and other
    information
    :param selected_player: The name of the player that we want to check if they belong to the
    Basketball Hall of Fame
    :return: a string indicating whether the selected player belongs to the Basketball Hall of Fame or
    not. The string includes the player's name and either "pertenece al Basketball Hall of Fame"
    (belongs to the Basketball Hall of Fame) or "no pertenece al Basketball Hall of Fame" (does not
    belong to the Basketball Hall of Fame).
    """
    achievements_string = " ".join(dream_team_list[selected_player]["logros"])
    result_hall_of_fame = re.search("Fama", achievements_string)
       
    if result_hall_of_fame:
        return f"{dream_team_list[selected_player]['nombre']} pertenece al Basketball Hall of Fame"
    else:
        return f"{dream_team_list[selected_player]['nombre']} no pertenece al Basketball Hall of Fame"

# 7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales

def show_top_rebound_player(dream_team_list):
    """
    This function takes a list of basketball players and returns the name of the player with the highest
    total rebounds.
    
    :param dream_team_list: a list of dictionaries representing basketball players and their statistics.
    Each dictionary contains the keys "nombre" (name) and "estadisticas" (statistics), where the value
    of "estadisticas" is another dictionary containing the keys "rebotes_totales" (total rebounds) and
    other
    :return: a string that states the name of the player with the highest total rebounds in the input
    list of players.
    """
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
    """
    This function takes a list of basketball players and returns the name of the player with the highest
    field goal percentage.
    
    :param dream_team_list: a list of dictionaries representing basketball players and their statistics.
    Each dictionary contains the keys "nombre" (name) and "estadisticas" (statistics), where the value
    of "estadisticas" is another dictionary containing the key "porcentaje_tiros_de_campo" (field goal
    :return: a string that includes the name of the player with the highest field goal percentage in the
    input list of players.
    """
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
    """
    This function takes a list of players and returns the name of the player with the highest number of
    total assists.
    
    :param dream_team_list: A list of dictionaries representing the players in a dream team, where each
    dictionary contains the player's name and statistics. The statistics are stored in a nested
    dictionary under the key "estadisticas", which includes the total number of assists under the key
    "asistencias_totales"
    :return: a string that states the name of the player with the highest number of total assists in the
    input list of players.
    """
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
    """
    This function takes a list of players and a user input, and returns a string of the names of players
    whose average score per game is above the user input.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains their name and statistics
    :param user_input: The user_input parameter is a float representing the minimum average score that a
    player must have in order to be included in the above_avg_players_list
    :return: a string that lists the names of the players in the input dream_team_list who have an
    average score per game greater than the user_input. If there are no players who meet this criteria,
    the function returns a string indicating that there are no such players.
    """
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
    """
    This function takes a list of basketball players and a user input for average rebounds per game, and
    returns a string of the names of players who have an average rebounds per game above the user input.
    
    :param dream_team_list: A list of dictionaries, where each dictionary represents a basketball player
    and contains their name and statistics
    :param user_input: The user_input parameter is a float representing the minimum average rebounds per
    game that a player must have in order to be included in the above_avg_players_list
    :return: a string that lists the names of the players in the input dream_team_list who have an
    average rebounds per game statistic greater than the user_input. If there are no players who meet
    this criteria, the function returns a string indicating that there are no such players.
    """
    above_avg_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["promedio_rebotes_por_partido"] > user_input:
            above_avg_players_list.append(player["nombre"])
    if len(above_avg_players_list) > 0:
        above_avg_players_string = "\n".join(above_avg_players_list)
    else:
        above_avg_players_string = "No hay jugadores que hayan superado dicho promedio"
    return above_avg_players_string

# 12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
# más asistencias por partido que ese valor.

def show_above_assist_by_game_avg_players(dream_team_list, user_input):
    """
    This function takes a list of players and a user input for average assists per game, and returns a
    string of the names of players who have an average assists per game higher than the user input.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains their name and statistics (including average assists per game)
    :param user_input: The user_input parameter is a float representing the minimum average number of
    assists per game that a player must have in order to be included in the above_avg_players_list
    :return: a string that lists the names of the players in the input dream_team_list whose average
    assists per game is greater than the user_input. If there are no players who meet this criteria, the
    function returns a string that says "No hay jugadores que hayan superado dicho promedio".
    """
    above_avg_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["promedio_asistencias_por_partido"] > user_input:
            above_avg_players_list.append(player["nombre"])
    if len(above_avg_players_list) > 0:
        above_avg_players_string = "\n".join(above_avg_players_list)
    else:
        above_avg_players_string = "No hay jugadores que hayan superado dicho promedio"
    return above_avg_players_string

# 13) Calcular y mostrar el jugador con la mayor cantidad de robos totales.

def show_top_steal_player(dream_team_list):
    """
    This function takes a list of basketball players and returns the name of the player with the highest
    number of total steals.
    
    :param dream_team_list: a list of dictionaries representing the players in a basketball team, where
    each dictionary contains the player's name and statistics. The statistics are stored in a nested
    dictionary under the key "estadisticas", which includes the total number of steals under the key
    "robos_totales". The function returns a
    :return: a string that includes the name of the player with the highest total steals in the input
    list of players.
    """
    flag_top_steal_player = False
    for player in dream_team_list:
        if flag_top_steal_player == False:
            max_steal_player_name = player["nombre"]
            max_steal = player["estadisticas"]["robos_totales"]
            flag_top_steal_player = True
        elif player["estadisticas"]["robos_totales"] > max_steal:
            max_steal_player_name = player["nombre"]
            max_steal = player["estadisticas"]["robos_totales"]
    return f"El jugador con mayor cantidad de robos totales es: {max_steal_player_name}"

# 14) Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.

def show_top_block_player(dream_team_list):
    """
    This function takes a list of players and returns the name of the player with the highest number of
    total blocks.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains the player's name and statistics
    :return: a string that states the name of the player with the highest number of total blocks in the
    input list of players.
    """
    flag_top_block_player = False
    for player in dream_team_list:
        if flag_top_block_player == False:
            max_block_player_name = player["nombre"]
            max_block = player["estadisticas"]["bloqueos_totales"]
            flag_top_block_player = True
        elif player["estadisticas"]["bloqueos_totales"] > max_block:
            max_block_player_name = player["nombre"]
            max_block = player["estadisticas"]["bloqueos_totales"]
    return f"El jugador con mayor cantidad de bloqueos totales es: {max_block_player_name}"

# 15) Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
# porcentaje de tiros libres superior a ese valor.

def show_above_free_throws_percentage_players(dream_team_list, user_input):
    """
    This function takes a list of basketball players and a user input for a free throw percentage, and
    returns a string of the names of players whose free throw percentage is above the user input.
    
    :param dream_team_list: A list of dictionaries representing basketball players and their statistics
    :param user_input: The minimum free throw percentage that a player must have to be included in the
    list of above percentage players
    :return: a string that contains the names of the players from the input list "dream_team_list" whose
    free throw percentage is above the user input value "user_input". If there are no players with a
    free throw percentage above the user input value, the function returns a string that says "No hay
    jugadores que hayan superado dicho porcentaje".
    """
    above_percentage_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["porcentaje_tiros_libres"] > user_input:
            above_percentage_players_list.append(player["nombre"])
    if len(above_percentage_players_list) > 0:
        above_percentage_players_string = "\n".join(above_percentage_players_list)
    else:
        above_percentage_players_string = "No hay jugadores que hayan superado dicho porcentaje"
    return above_percentage_players_string

# 16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
# jugador con la menor cantidad de puntos por partido.

def calculate_and_show_score_by_game_avg_excluding_the_lowest(dream_team_list):
    """
    This function calculates and returns the average score per game for a dream team list, excluding the
    lowest scoring player.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains the following keys:
    :return: the average score per game of the dream team, excluding the lowest scoring player.
    """
    flag_lowest_scoring_player = False
    for player in dream_team_list:
        if flag_lowest_scoring_player == False:
            min_scoring_player_name = player["nombre"]
            min_score = player["estadisticas"]["promedio_puntos_por_partido"]
            flag_lowest_scoring_player = True
        elif player["estadisticas"]["promedio_puntos_por_partido"] < min_score:
            min_scoring_player_name = player["nombre"]
            min_score = player["estadisticas"]["promedio_puntos_por_partido"]
    
    accumulator = 0
    for player in dream_team_list:
        if player["nombre"] != min_scoring_player_name:
            accumulator = accumulator + player["estadisticas"]["promedio_puntos_por_partido"]
    score_by_game_avg = accumulator / (len(dream_team_list)-1)
    return score_by_game_avg

# 17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos

def calculate_and_show_top_achievement_player(dream_team_list):
    """
    This function takes a list of players and returns the name of the player with the most achievements.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player in a dream
    team and contains the keys "nombre" (player name) and "logros" (a list of achievements for that
    player)
    :return: a string that states the name of the player with the highest number of achievements in the
    input list of players.
    """
    flag_top_achievement_player = False
    for player in dream_team_list:
        if flag_top_achievement_player == False:
            max_achievement_player_name = player["nombre"]
            max_achievement = len(player["logros"])
            flag_top_achievement_player = True
        elif len(player["logros"]) > max_achievement:
            max_achievement_player_name = player["nombre"]
            max_achievement = len(player["logros"])

    return f"El jugador con mayor cantidad de logros obtenidos es: {max_achievement_player_name}"

# 18) Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
# porcentaje de tiros triples superior a ese valor.

def show_above_triples_percentage_players(dream_team_list, user_input):
    """
    This function takes a list of basketball players and a user input percentage, and returns a string
    of the names of players who have a three-point shooting percentage above the user input.
    
    :param dream_team_list: A list of dictionaries, where each dictionary represents a basketball player
    and their statistics
    :param user_input: The user_input parameter is a float representing the minimum percentage of
    three-point shots made by a player that the function will consider as "above average"
    :return: a string that lists the names of the players in the input dream_team_list whose
    "porcentaje_tiros_triples" statistic is greater than the user_input. If there are no players that
    meet this criteria, the function returns a string that says "No hay jugadores que hayan superado
    dicho porcentaje".
    """
    above_percentage_players_list = []

    for player in dream_team_list:
        if player["estadisticas"]["porcentaje_tiros_triples"] > user_input:
            above_percentage_players_list.append(player["nombre"])
    if len(above_percentage_players_list) > 0:
        above_percentage_players_string = "\n".join(above_percentage_players_list)
    else:
        above_percentage_players_string = "No hay jugadores que hayan superado dicho porcentaje"
    return above_percentage_players_string

# 19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas

def calculate_and_show_player_with_highest_amount_of_seasons(dream_team_list):
    """
    This function calculates and shows the player with the highest amount of seasons in a given dream
    team list.
    
    :param dream_team_list: a list of dictionaries representing the players in a dream team, where each
    dictionary contains the player's name and statistics such as the number of seasons played
    :return: a string that includes the name of the player with the highest amount of seasons played in
    a given list of players.
    """
    flag_player_with_highest_amount_of_seasons = False
    for player in dream_team_list:
        if flag_player_with_highest_amount_of_seasons == False:
            max_seasons_player_name = player["nombre"]
            max_seasons = player["estadisticas"]["temporadas"]
            flag_player_with_highest_amount_of_seasons = True
        elif player["estadisticas"]["temporadas"] > max_seasons:
            max_seasons_player_name = player["nombre"]
            max_seasons = player["estadisticas"]["temporadas"]

    return f"El jugador con mayor cantidad de temporadas jugadas es: {max_seasons_player_name}"

# 20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
# posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
# ese valor.

def calculate_and_show_sorted_players_above_user_input_field_goal_percentage(dream_team_list, user_input):
    """
    This function takes a list of basketball players and a user input for field goal percentage, sorts
    the players by position, and returns a string of the names and positions of players who have a
    higher field goal percentage than the user input.
    
    :param dream_team_list: a list of dictionaries representing a basketball team, where each dictionary
    contains information about a player, including their name, position, and statistics such as their
    field goal percentage
    :param user_input: The user_input parameter is a float representing the minimum field goal
    percentage that a player must have in order to be included in the list of sorted players
    :return: a string that contains the names and positions of the players from the input list whose
    field goal percentage is above the user input, sorted by their position. If there are no players
    with a field goal percentage above the user input, the function returns a string indicating that
    there are no such players.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for index_A in range(len(dream_team_list) - 1):
                if dream_team_list[index_A]["posicion"] > dream_team_list[index_A+1]["posicion"]:
                    dream_team_list[index_A],dream_team_list[index_A+1] = dream_team_list[index_A+1],dream_team_list[index_A]
                    flag_swap = True

    above_input_sorted_players = []
    for player in dream_team_list:
        if player["estadisticas"]["porcentaje_tiros_triples"] > user_input:
            above_input_sorted_players.append(f"{player['nombre']} - {player['posicion']}")

    if len(above_input_sorted_players) > 0:
        above_percentage_players_string = "\n".join(above_input_sorted_players)
        return above_percentage_players_string
    else:
        above_percentage_players_string = "No hay jugadores que hayan superado dicho porcentaje"
        return above_percentage_players_string

#--------------------------------------------BONUS EXERCISES------------------------------------------------------


# 21) Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
# ● Puntos
# ● Rebotes
# ● Asistencias
# ● Robos
# Exportar a csv.
# Ejemplo:
#     Jugador    Puntos Rebotes  Asistencias Robos
# Michael Jordan    1      1          1        2
# Magic             2      3          4        4

def rank_players(dream_team_list):
    """
    The function sorts a list of basketball players by their total points, rebounds, assists, and
    steals, and writes the rankings to a CSV file.
    
    :param dream_team_list: A list of dictionaries representing the players in a basketball team, where
    each dictionary contains the player's name and their statistics for points, rebounds, assists, and
    steals
    """
    sorted_by_total_score = dream_team_list[:]
    flag_swap_total_score = True
    while flag_swap_total_score:
        flag_swap_total_score = False

        for index_A in range(len(sorted_by_total_score) - 1):
                if sorted_by_total_score[index_A]["estadisticas"]["puntos_totales"] < sorted_by_total_score[index_A+1]["estadisticas"]["puntos_totales"]:
                    sorted_by_total_score[index_A],sorted_by_total_score[index_A+1] = sorted_by_total_score[index_A+1],sorted_by_total_score[index_A]
                    flag_swap_total_score = True

    sorted_by_total_rebounds = dream_team_list[:]
    flag_swap_total_rebounds = True
    while flag_swap_total_rebounds:
        flag_swap_total_rebounds = False

        for index_A in range(len(sorted_by_total_rebounds) - 1):
                if sorted_by_total_rebounds[index_A]["estadisticas"]["rebotes_totales"] < sorted_by_total_rebounds[index_A+1]["estadisticas"]["rebotes_totales"]:
                    sorted_by_total_rebounds[index_A],sorted_by_total_rebounds[index_A+1] = sorted_by_total_rebounds[index_A+1],sorted_by_total_rebounds[index_A]
                    flag_swap_total_rebounds = True

    sorted_by_total_assists = dream_team_list[:]
    flag_swap_total_assists = True
    while flag_swap_total_assists:
        flag_swap_total_assists = False

        for index_A in range(len(sorted_by_total_assists) - 1):
                if sorted_by_total_assists[index_A]["estadisticas"]["asistencias_totales"] < sorted_by_total_assists[index_A+1]["estadisticas"]["asistencias_totales"]:
                    sorted_by_total_assists[index_A],sorted_by_total_assists[index_A+1] = sorted_by_total_assists[index_A+1],sorted_by_total_assists[index_A]
                    flag_swap_total_assists = True

    sorted_by_total_steals = dream_team_list[:]
    flag_swap_total_steals = True
    while flag_swap_total_steals:
        flag_swap_total_steals = False

        for index_A in range(len(sorted_by_total_steals) - 1):
                if sorted_by_total_steals[index_A]["estadisticas"]["robos_totales"] < sorted_by_total_steals[index_A+1]["estadisticas"]["robos_totales"]:
                    sorted_by_total_steals[index_A],sorted_by_total_steals[index_A+1] = sorted_by_total_steals[index_A+1],sorted_by_total_steals[index_A]
                    flag_swap_total_steals = True

    with open("parcial_punto_21.csv", "w") as file:
        file.write("Jugador,Puntos,Rebotes,Asistencias,Robos")
        file.write("\n")
        for player_original in dream_team_list:
            for index in range(len(sorted_by_total_score)):
                if player_original["nombre"] == sorted_by_total_score[index]["nombre"]:
                    total_score_rank = index
            for index in range(len(sorted_by_total_rebounds)):
                if player_original["nombre"] == sorted_by_total_rebounds[index]["nombre"]:
                    total_rebounds_rank = index
            for index in range(len(sorted_by_total_assists)):
                if player_original["nombre"] == sorted_by_total_assists[index]["nombre"]:
                    total_assists_rank = index
            for index in range(len(sorted_by_total_steals)):
                if player_original["nombre"] == sorted_by_total_steals[index]["nombre"]:
                    total_steals_rank = index
            file.write(f"{player_original['nombre']},{total_score_rank+1},{total_rebounds_rank+1},{total_assists_rank+1},{total_steals_rank+1}\n")

# 22) BONUS- Encontrar y mostrar aquellos jugadores que hayan jugado igual mas cantidad de partidos All-Star 
# que el numero ingresado por el usuario

def calculate_and_show_above_input_value_all_star_players(dream_team_list, user_input):
    """
    This function takes a list of basketball players and a user input value, and returns a string of the
    names of players who have played an equal or greater number of All-Star games than the user input
    value.
    
    :param dream_team_list: It is a list of dictionaries containing information about players in a dream
    team, including their name and achievements
    :param user_input: The number of All-Star games played that the user is searching for in the
    dream_team_list
    :return: a string that lists the names of all players in the input dream_team_list who have played
    an equal or greater number of All-Star games than the user_input value. If there are no such
    players, the function returns a string indicating that there are no players who meet the criteria.
    """
    all_star_players = []

    for player in dream_team_list:
        for achievement in player["logros"]:
            result_all_star = re.search("All-Star", achievement)
            if result_all_star:
                amount_of_all_star_played = re.search("^[0-9]+", achievement)
                all_star_players.append({player["nombre"]:int(amount_of_all_star_played.group())})
    
    above_user_input_all_star_players_list = []
    
    for item in all_star_players:
        for key, value in item.items():
            if value >= user_input:
                above_user_input_all_star_players_list.append(key)
    
    if len(above_user_input_all_star_players_list) > 0:
        above_input_all_star_players_string = "\n".join(above_user_input_all_star_players_list)
        return above_input_all_star_players_string
    else:
        above_input_all_star_players_string = "No hay jugadores que hayan jugado igual o mayor cantidad de partidos All-Star que el valor ingresado"
        return above_input_all_star_players_string

# 23) BONUS- Encontrar y mostrar al jugador con mayor cantidad de partidos All-Star jugados

def find_and_show_player_with_highest_amount_of_all_star_games(dream_team_list):
    """
    This function finds and returns the name of the player with the highest amount of All-Star games
    played from a given list of players.
    
    :param dream_team_list: a list of dictionaries, where each dictionary represents a player and
    contains their name and a list of their achievements (logros). The function searches through the
    achievements to find the number of All-Star games played by each player and returns the name of the
    player with the highest number of All-Star games
    :return: the name of the player with the highest amount of All-Star games played, based on the input
    list of players' information.
    """
    all_star_players = []

    for player in dream_team_list:
        for achievement in player["logros"]:
            result_all_star = re.search("All-Star", achievement)
            if result_all_star:
                amount_of_all_star_played = re.search("^[0-9]+", achievement)
                all_star_players.append({player["nombre"]:int(amount_of_all_star_played.group())})
    
    flag_top_all_star_player = True
    for item in all_star_players:
        for key, value in item.items():
            if flag_top_all_star_player == True:
                top_all_star_player_name = key
                max_all_star_games = value
                flag_top_all_star_player = False
            elif value > max_all_star_games:
                top_all_star_player_name = key
                max_all_star_games = value
    return top_all_star_player_name

# 24) BONUS- Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
# ● Porcentaje de tiros de campo
# ● Porcentaje de tiros libres
# ● Porcentaje de tiros triples
# Exportar a csv.
# Ejemplo:
#     Jugador    Porcentaje_tiros_de_campo Porcentaje_de_tiros_libres Porcentaje_de_tiros_triples
# Michael Jordan    1                                   1                            1       
# Magic             2                                   3                            4        

def rank_players_by_field_goals_free_throw_triples_percentages(dream_team_list):
    """
    This function ranks basketball players in a dream team list based on their field goal, free throw,
    and triple percentages and writes the results to a CSV file.
    
    :param dream_team_list: A list of dictionaries, where each dictionary represents a basketball player
    and their statistics. The dictionary should have the following keys: "nombre" (string),
    "estadisticas" (dictionary). The "estadisticas" dictionary should have the following keys:
    "porcentaje_tiros_de_c
    """
    sorted_by_field_goals = dream_team_list[:]
    flag_swap_field_goals = True
    while flag_swap_field_goals:
        flag_swap_field_goals = False

        for index_A in range(len(sorted_by_field_goals) - 1):
                if sorted_by_field_goals[index_A]["estadisticas"]["porcentaje_tiros_de_campo"] < sorted_by_field_goals[index_A+1]["estadisticas"]["porcentaje_tiros_de_campo"]:
                    sorted_by_field_goals[index_A],sorted_by_field_goals[index_A+1] = sorted_by_field_goals[index_A+1],sorted_by_field_goals[index_A]
                    flag_swap_field_goals = True

    sorted_by_free_throws = dream_team_list[:]
    flag_swap_free_throws = True
    while flag_swap_free_throws:
        flag_swap_free_throws = False

        for index_A in range(len(sorted_by_free_throws) - 1):
                if sorted_by_free_throws[index_A]["estadisticas"]["porcentaje_tiros_libres"] < sorted_by_free_throws[index_A+1]["estadisticas"]["porcentaje_tiros_libres"]:
                    sorted_by_free_throws[index_A],sorted_by_free_throws[index_A+1] = sorted_by_free_throws[index_A+1],sorted_by_free_throws[index_A]
                    flag_swap_free_throws = True

    sorted_by_triples = dream_team_list[:]
    flag_swap_triples = True
    while flag_swap_triples:
        flag_swap_triples = False

        for index_A in range(len(sorted_by_triples) - 1):
                if sorted_by_triples[index_A]["estadisticas"]["porcentaje_tiros_triples"] < sorted_by_triples[index_A+1]["estadisticas"]["porcentaje_tiros_triples"]:
                    sorted_by_triples[index_A],sorted_by_triples[index_A+1] = sorted_by_triples[index_A+1],sorted_by_triples[index_A]
                    flag_swap_triples = True

    with open("parcial_punto_24.csv", "w") as file:
        file.write("Jugador,Porcentaje_tiros_de_campo,Porcentaje_de_tiros_libres,Porcentaje_de_tiros_triples")
        file.write("\n")
        for player_original in dream_team_list:
            for index in range(len(sorted_by_field_goals)):
                if player_original["nombre"] == sorted_by_field_goals[index]["nombre"]:
                    total_field_goals_rank = index
            for index in range(len(sorted_by_free_throws)):
                if player_original["nombre"] == sorted_by_free_throws[index]["nombre"]:
                    total_free_throws_rank = index
            for index in range(len(sorted_by_triples)):
                if player_original["nombre"] == sorted_by_triples[index]["nombre"]:
                    total_triples_rank = index
            file.write(f"{player_original['nombre']},{total_field_goals_rank+1},{total_free_throws_rank+1},{total_triples_rank+1}\n")

# 25) BONUS- Hallar y mostar la cantidad de jugadores cuya posicion sea "Ala-Pivot"

def find_and_show_amount_of_wing_pivot_players(dream_team_list):
    """
    This function counts the number of players in a given list who have the position "Ala-Pivot" and
    returns a string with the count.
    
    :param dream_team_list: a list of dictionaries representing the players in a basketball dream team.
    Each dictionary contains information about a player, including their name, position, and other
    attributes. The function is designed to iterate through this list and count the number of players
    who are listed as "Ala-Pivot" (wing pivot)
    :return: a string that states the number of players in the input list with the position "Ala-Pivot".
    The string includes the number of players found and the phrase "En el dream team hay" (which means
    "In the dream team there are" in Spanish).
    """
    counter = 0
    for player in dream_team_list:
        if player["posicion"] == "Ala-Pivot":
            counter = counter + 1
    return f"En el dream team hay {counter} jugadores Ala-Pivot"

# 26) BONUS- Hallar y mostrar todos aquellos jugadores cuya posicion sea "Ala-Pivot"

def find_and_show_every_wing_pivot_player(dream_team_list):
    """
    The function finds and returns the names of all players in a given list who play the position of
    "Ala-Pivot".
    
    :param dream_team_list: A list of dictionaries representing the players in a basketball team. Each
    dictionary contains information about a player, including their name and position
    :return: a string that contains the names of all the players in the input list who have the position
    "Ala-Pivot".
    """
    wing_pivot_players_list = []
    for player in dream_team_list:
        if player["posicion"] == "Ala-Pivot":
            wing_pivot_players_list.append(player["nombre"])
    wing_pivot_players_string = "\n".join(wing_pivot_players_list)
    return wing_pivot_players_string

# 27) BONUS- Hallar y mostrar todos aquellos jugadores cuya posicion sea "Base"

def find_and_show_every_base_player(dream_team_list):
    """
    This function takes a list of players and returns a string of the names of all the players who play
    the position of "Base".
    
    :param dream_team_list: A list of dictionaries, where each dictionary represents a player in a dream
    team. Each dictionary has the following keys: "nombre" (player name), "posicion" (player position),
    and other keys representing player statistics
    :return: a string that contains the names of all the players in the input list whose position is
    "Base". The names are separated by newlines.
    """
    base_players_list = []
    for player in dream_team_list:
        if player["posicion"] == "Base":
            base_players_list.append(player["nombre"])
    base_players_string = "\n".join(base_players_list)
    return base_players_string

# 28) JUEGO BONUS: Se le hará una pregunta sobre las estadisticas obtenidas a lo largo del menu 
# y usted deberá contestarla, para luego comprobar si su respuesta es correcta o incorrecta.

def show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, to_call_function):
    """
    This function validates user input for a player's name, checks if it is correct, and returns a
    status message.
    
    :param dream_team_list: A list containing the players in a dream team
    :param to_call_function: The name of the function that is being called and whose output is being
    used to validate the user input
    :return: a string indicating whether the user input was correct ("Bien"), incorrect ("Mal"), or
    invalid ("Error").
    """
    players_names_txt = "\n".join(show_every_player(dream_team_list))
    print(f"Se presentan a continuacion los nombres de los jugadores: \n\n{players_names_txt}\n")

    user_choice_player_name = input("Ingrese el nombre del jugador: ")
    result_alphabetic = re.search("^[a-zA-Z ]+$",user_choice_player_name)
    if result_alphabetic:
        fixed_user_choice_player_name = user_choice_player_name.strip().title()
        if fixed_user_choice_player_name in show_every_player(dream_team_list):
            result_player_name = re.search("es: ([a-zA-Z ]+)$", to_call_function)
            if fixed_user_choice_player_name == result_player_name.group(1): #Para obtener la expresion capturada
                print("Excelente! Respuesta correcta")
                return "Bien"
            else:
                print(f"Respuesta incorrecta. La respuesta correcta es {result_player_name.group(1)}")
                return "Mal"
        else:
            print("El jugador ingresado no pertenece al Dream Team")
            return "Error"
    else:
        print("Solo ingresar caracteres alfabeticos")
        return "Error"

def play_basketball_stadistics_game(dream_team_list):
    """
    This function plays a basketball statistics game by asking the user questions about players and
    their statistics, and returns the number of correct answers.
    
    :param dream_team_list: The dream_team_list parameter is a list of dictionaries containing
    information about basketball players, such as their name, team, position, and statistics like
    rebounds, assists, steals, blocks, and field goal percentage
    """
    os.system('cls')
    counter = 0
    flag_exit = False
    list_of_questions_numbers = [7, 8, 9, 13, 14, 17, 19]
    for question_number in list_of_questions_numbers:
        match (question_number):
            case 7:
                while True:
                    print("Cual es el jugador con mayor cantidad de rebotes totales?")
                    rebound_answer_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, show_top_rebound_player(dream_team_list))
                    if rebound_answer_output != "Error":
                        if rebound_answer_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 8:
                while True:
                    print("Cual es el jugador con el mayor porcentaje de tiros de campo?")
                    field_goal_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, show_top_field_goal_player(dream_team_list))
                    if field_goal_output != "Error":
                        if field_goal_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 9:
                while True:
                    print("Cual es el jugador con la mayor cantidad de asistencias totales?")
                    assists_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, show_top_assist_player(dream_team_list))
                    if assists_output != "Error":
                        if assists_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 13:
                while True:
                    print("Cual es el jugador con la mayor cantidad de robos totales?")
                    steals_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, show_top_steal_player(dream_team_list))
                    if steals_output != "Error":
                        if steals_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 14:
                while True:
                    print("Cual es el jugador con la mayor cantidad de bloqueos totales?")
                    blocks_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, show_top_block_player(dream_team_list))
                    if blocks_output == "Error":
                        if blocks_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 17:
                while True:
                    print("Cual es el jugador con la mayor cantidad de logros obtenidos?")
                    achievements_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, calculate_and_show_top_achievement_player(dream_team_list))
                    if achievements_output != "Error":
                        if achievements_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
            case 19:
                while True:
                    print("Cual es el jugador con la mayor cantidad de temporadas jugadas?")
                    seasons_output = show_players_offer_input_validate_input_and_check_if_input_if_correct_or_not(dream_team_list, calculate_and_show_player_with_highest_amount_of_seasons(dream_team_list))
                    if seasons_output != "Error":
                        if seasons_output == "Bien":
                            counter = counter + 1
                        break
                    else:
                        clear_console()
        print(f"\nCantidad de respuestas correctas hasta el momento: {counter}\n  ")
        
        while True:
            user_choice_play_game = input("Si desea seguir jugando escriba 'SI', de lo contrario escriba 'NO': ") 
            if user_choice_play_game == "NO":
                flag_exit = True
                break
            if user_choice_play_game == "SI":
                break
            else:
                print("Debe escribir SI o NO. Respete mayusculas")

        if flag_exit == True:
            break
        os.system('cls')
    return counter

# 29) EXTRA- Si ha respondido bien al menos dos de las preguntas del juego, podra acceder a esta opcion para generar un certificado de respuesta correcta

def check_amount_of_right_answers(amount_of_correct_answers):
    """
    This function checks if the amount of correct answers is greater than or equal to 2 and if so,
    creates a certificate file with the amount of correct answers, otherwise it prints a message to keep
    trying.
    
    :param amount_of_correct_answers: an integer representing the number of correct answers a player has
    achieved in a game
    """
    if amount_of_correct_answers >= 2:
        with open("NBA_certificate.txt", "w") as file:
            file.write(f"Felicitaciones. Ha obtenido el certificado de NBA debido a su cantidad de respuestas correctas \nCantidad de respuestas correctas: {amount_of_correct_answers} \n\nGracias por participar del juego \n-NBA")
    else:
        print("No ha obtenido la cantidad necesaria de respuestas correctas para obtener el certificado. Por favor siga intentandolo")

#------------------------------------------------APP---------------------------------------------------------------

def dream_team_app(dream_team_list):
    """
    This is a function that runs a menu-driven application for managing a dream team list and provides
    various options for displaying and analyzing player statistics.
    
    :param dream_team_list: It is a list containing information about basketball players, such as their
    name, position, and statistics. This list is used as input for various functions in the program
    """
    dream_team_list_duplicate = dream_team_list[:]
    flag_enable_csv = False
    flag_enable_certificate = False
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
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    if user_choice_player_int < 12:
                        for item, value in show_player_stadistics(dream_team_list_duplicate, user_choice_player_int).items():
                            print(f"{item}: {value}")
                        flag_enable_csv = True
                    else:
                        print("Ha ingresado un indice invalido (Superior a la cantidad de los jugadores disponibles)")    
                else:
                    print("Ha ingresado un indice invalido (Ingresar solo numeros)")
            case 3:
                if flag_enable_csv == True:
                    save_stadistics_in_csv(dream_team_list_duplicate, user_choice_player_int)
                else:
                    print("Primero debe seleccionar la opcion 2")
            case 4:
                players_names_txt = "\n".join(show_every_player(dream_team_list_duplicate))
                print(f"Se presentan a continuacion los nombres de los jugadores: \n{players_names_txt}")

                input_validation = validate_input_and_return_player_index(dream_team_list_duplicate)
                if input_validation >= 0:
                    print(show_achievements(dream_team_list_duplicate, input_validation))
            case 5:
                print(calculate_and_show_avg_score_by_game(dream_team_list_duplicate))
                print(f"A continuacion, los jugadores ordenados de acuerdo a su promedio de puntos por partido en forma ascendente: \n{order_players_by_avg_score_by_game_asc(dream_team_list_duplicate)}")
            case 6:
                players_names_txt = "\n".join(show_every_player(dream_team_list_duplicate))
                print(f"Se presentan a continuacion los nombres de los jugadores: \n{players_names_txt}")

                input_validation = validate_input_and_return_player_index(dream_team_list_duplicate)
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
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_score_by_game_avg_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 11:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_rebounds_by_game_avg_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 12:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_assist_by_game_avg_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 13:
                print(show_top_steal_player(dream_team_list_duplicate))  
            case 14:
                print(show_top_block_player(dream_team_list_duplicate)) 
            case 15:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_free_throws_percentage_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 16:
                print(calculate_and_show_score_by_game_avg_excluding_the_lowest(dream_team_list_duplicate))
            case 17:
                print(calculate_and_show_top_achievement_player(dream_team_list_duplicate))
            case 18:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(show_above_triples_percentage_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 19:
                print(calculate_and_show_player_with_highest_amount_of_seasons(dream_team_list_duplicate))
            case 20:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(calculate_and_show_sorted_players_above_user_input_field_goal_percentage(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 21:
                rank_players(dream_team_list_duplicate)
            case 22:
                user_choice_player_txt = input("Ingrese un valor numerico: ")
                user_choice_player_txt_stripped = user_choice_player_txt.strip()
                result = re.match("[0-9]+$", user_choice_player_txt_stripped)
                if result: 
                    user_choice_player_int = int(user_choice_player_txt)
                    print(calculate_and_show_above_input_value_all_star_players(dream_team_list_duplicate, user_choice_player_int))
                else:
                    print("Ha ingresado un valor invalido (Ingresar solo numeros)")
            case 23:
                print(find_and_show_player_with_highest_amount_of_all_star_games(dream_team_list_duplicate))
            case 24:
                rank_players_by_field_goals_free_throw_triples_percentages(dream_team_list_duplicate)
            case 25:
                print(find_and_show_amount_of_wing_pivot_players(dream_team_list_duplicate))
            case 26:
                print(find_and_show_every_wing_pivot_player(dream_team_list_duplicate))
            case 27:
                print(find_and_show_every_base_player(dream_team_list_duplicate))
            case 28:
                amount_of_correct_answers = play_basketball_stadistics_game(dream_team_list_duplicate)
                flag_enable_certificate = True
            case 29:
                if flag_enable_certificate == True:
                    print("Creando certificado. (10%)", end="")
                    time.sleep(0.4)
                    print("\rCreando certificado.. (30%)", end="") #Muevo el cursor al inicio de la linea actual
                    # Por defecto, el valor de end es "\n" entonces se usa end="" 
                    #para evitar que se imprima un salto de línea al final de cada print.
                    time.sleep(0.4)
                    print("\rCreando certificado.. (50%)", end="") 
                    time.sleep(0.4)
                    print("\rCreando certificado... (70%)", end="")
                    time.sleep(0.4)
                    print("\rCreando certificado.... (90%)", end="")
                    time.sleep(0.4)
                    print("\rCreando certificado..... (100%)", end="")
                    time.sleep(0.4)
                    check_amount_of_right_answers(amount_of_correct_answers)
                    print("\nSe ha creado el certificado!")
                else:
                    print("Para obtener el certificado primero debe elegir la opcion 28 y responder 2 o mas preguntas correctamente")
            case 30:
                os.system('cls')
                break
            case _:
                print("Ha ingresado una opcion incorrecta")
        clear_console()

dream_team_app(leer_archivo(json_path))