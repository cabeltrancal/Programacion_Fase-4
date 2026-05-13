# Modificado por: Julian Cardenas
from typing import List

def obtener_opcion(mensaje: str, opciones_validas: List[str]) -> str:
    """
    Solicita una opción al usuario de manera persistente hasta recibir una válida.
    
    :param mensaje: Texto descriptivo para el usuario.
    :param opciones_validas: Lista de strings con las opciones permitidas.
    :return: La opción seleccionada normalizada.
    """
    # Normalizamos las opciones válidas a minúsculas para una comparación flexible
    opciones_norm = [str(opt).strip().lower() for opt in opciones_validas]
    
    while True:
        entrada = input(f"{mensaje} ({'/'.join(opciones_validas)}): ").strip().lower()
        
        if entrada in opciones_norm:
            # Retornamos la opción original que corresponde a la entrada
            indice = opciones_norm.index(entrada)
            print() # Salto de línea estético
            return opciones_validas[indice]

        print(f"\n[ERROR] '{entrada}' no es válido. Intente con: {', '.join(opciones_validas)}\n")
