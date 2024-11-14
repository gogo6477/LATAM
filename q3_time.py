import json
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Contador para las menciones de usuarios
    user_mentions = Counter()

    # Leer el archivo línea por línea para no cargar todo en memoria
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Cargar el tweet
                tweet = json.loads(line)

                # Extraer el texto del tweet
                tweet_text = tweet.get('content', '')

                # Buscar menciones en el texto (palabras que comienzan con '@')
                mentions = [word[1:] for word in tweet_text.split() if word.startswith('@')]

                # Contar las menciones
                user_mentions.update(mentions)

            except json.JSONDecodeError:
                continue  # Ignorar tweets con errores de formato JSON

    # Obtener los 10 usuarios más mencionados
    top_users = user_mentions.most_common(10)

    return top_users