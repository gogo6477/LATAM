import json
from collections import defaultdict
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Usar un diccionario para las menciones de usuarios
    user_mentions = defaultdict(int)

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Cargar el tweet
                tweet = json.loads(line)

                # Extraer el texto del tweet
                tweet_text = tweet.get('content', '')

                # Buscar menciones en el texto
                mentions = [word[1:] for word in tweet_text.split() if word.startswith('@')]

                # Contar las menciones
                for mention in mentions:
                    user_mentions[mention] += 1

            except json.JSONDecodeError:
                continue  # Ignorar tweets con errores de formato JSON

    # Convertir el diccionario a una lista de tuplas y ordenar
    top_users = sorted(user_mentions.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_users