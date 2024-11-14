from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

"""
    Retorna las 10 fechas con el mayor número de tweets y el usuario más activo en cada una de esas fechas.
    
    Args:
        file_path (str): Ruta al archivo JSON con los datos de tweets.
        
    Returns:
        List[Tuple[datetime.date, str]]: Lista de tuplas, donde cada tupla contiene una fecha 
                                         y el nombre de usuario que más tweets hizo en esa fecha.
    """
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para almacenar la fecha y un contador de tweets por usuario
    tweet_dates = defaultdict(lambda: defaultdict(int))
    
    # Procesar el archivo línea por línea para optimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Cargar el tweet
                tweet = json.loads(line)
                # Obtener la fecha del tweet desde el campo 'date' en la raíz
                date_str = tweet['date']
                # Obtener el nombre de usuario
                username = tweet['user']['displayname']
                # Convertir la fecha al formato datetime
                tweet_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').date()

                # Incrementar el contador de tweets para ese usuario en esa fecha
                tweet_dates[tweet_date][username] += 1

            except json.JSONDecodeError:
                continue  # Ignorar líneas con errores en el formato JSON

    # Ordenar las fechas de acuerdo con el total de tweets, seleccionando las 10 fechas con más tweets
    top_dates = sorted(tweet_dates.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Para cada fecha, encontrar el usuario con más tweets
    result = []
    for date, user_counts in top_dates:
        # Encontrar el usuario que más tweets tiene
        top_user = max(user_counts, key=user_counts.get)
        # Agregar el resultado (fecha, usuario más activo)
        result.append((date, top_user))
    
    # Devolver la lista con las top 10 fechas y el usuario más activo en cada una
    return result
