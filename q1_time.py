from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter


"""
    Retorna las 10 fechas con el mayor número de tweets.
    
    Args:
        file_path (str): Ruta al archivo JSON con los datos de tweets.
        
    Returns:
        List[Tuple[datetime.date, int]]: Lista de tuplas, donde cada tupla contiene una fecha 
                                         y la cantidad de tweets de esa fecha, ordenada 
                                         por el número de tweets en orden descendente.
    """
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para almacenar la fecha y un contador de tweets por usuario
    tweet_dates = {}
    
    # Abrir el archivo JSON y leer línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Cargar el tweet
                tweet = json.loads(line)
                # Obtener la fecha del tweet desde el campo 'date' en la raíz
                date_str = tweet['date']
                # Obtener el nombre de usuario
                username = tweet['user']['displayname']
                # Convertir la fecha al formato datetime, ajustando para la hora y zona horaria
                tweet_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').date()

                # Si la fecha no está en el diccionario, la agregamos con un contador vacío
                if tweet_date not in tweet_dates:
                    tweet_dates[tweet_date] = Counter()
                
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
        top_user = user_counts.most_common(1)[0][0]
        # Agregar el resultado (fecha, usuario más activo)
        result.append((date, top_user))
    
    # Devolver la lista con las top 10 fechas y el usuario más activo en cada una
    return result