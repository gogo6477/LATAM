from typing import List, Tuple
import json
import re
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    # Leer el archivo línea por línea para manejar archivos grandes
    with open(file_path, 'r') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                # Buscar emojis usando una expresión regular
                emojis = re.findall(r'[^\w\s,]', tweet['content'])
                # Contar los emojis encontrados
                emoji_counter.update(emojis)
            except json.JSONDecodeError:
                continue  # Ignorar líneas con errores en formato JSON

    # Obtener los 10 emojis más usados
    top_10_emojis = emoji_counter.most_common(10)
    
    return top_10_emojis
