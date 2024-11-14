from typing import List, Tuple
import json
import re
from collections import defaultdict

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = defaultdict(int)

    # Leer el archivo línea por línea para manejar archivos grandes
    with open(file_path, 'r') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                # Buscar emojis usando una expresión regular
                emojis = re.findall(r'[^\w\s,]', tweet['content'])
                # Contar los emojis encontrados sin almacenar todos los resultados
                for emoji in emojis:
                    emoji_counter[emoji] += 1
            except json.JSONDecodeError:
                continue  # Ignorar líneas con errores en formato JSON

    # Obtener los 10 emojis más usados
    top_10_emojis = sorted(emoji_counter.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return top_10_emojis