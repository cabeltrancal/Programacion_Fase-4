# Modificado por: Julian Cardenas
import json
from pathlib import Path
from typing import List, Dict, Any

# Uso de Path para mayor seguridad en el manejo de archivos
RUTA_EQUIPOS = Path("data/equipos.json")

def _asegurar_directorio():
    """Garantiza la existencia de la carpeta de datos."""
    RUTA_EQUIPOS.parent.mkdir(parents=True, exist_ok=True)

def _leer_equipos() -> List[Dict[str, Any]]:
    """Lee y parsea el archivo de equipos JSON."""
    if not RUTA_EQUIPOS.exists():
        return []

    try:
        with open(RUTA_EQUIPOS, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def _guardar_equipos(equipos: List[Dict[str, Any]]):
    """Persiste la lista de equipos en el disco."""
    _asegurar_directorio()
    with open(RUTA_EQUIPOS, "w", encoding="utf-8") as file:
        json.dump(equipos, file, indent=4, ensure_ascii=False)

def crear_equipo(nombre: str, tipo: str, precio_por_dia: float) -> Dict[str, Any]:
    """Crea un nuevo equipo con validaciones de integridad."""
    
    if not nombre.strip() or not tipo.strip():
        raise ValueError("Nombre y tipo son campos requeridos.")

    if precio_por_dia <= 0:
        raise ValueError("El precio por día debe ser un valor positivo.")

    equipos = _leer_equipos()

    # Validación eficiente de duplicados
    nombre_limpio = nombre.strip()
    if any(e["nombre"].lower() == nombre_limpio.lower() for e in equipos):
        raise ValueError(f"El equipo '{nombre_limpio}' ya existe en el inventario.")

    nuevo_equipo = {
        "nombre": nombre_limpio,
        "tipo": tipo.strip(),
        "precio_por_dia": float(precio_por_dia)
    }

    equipos.append(nuevo_equipo)
    _guardar_equipos(equipos)
    return nuevo_equipo

def obtener_equipos() -> List[Dict[str, Any]]:
    """Obtiene la lista completa de equipos."""
    return _leer_equipos()

def eliminar_equipo(indice: int):
    """Elimina un equipo según su índice en la lista."""
    equipos = _leer_equipos()

    if not (0 <= indice < len(equipos)):
        raise IndexError("Índice fuera de rango: El equipo no existe.")

    equipos.pop(indice)
    _guardar_equipos(equipos)

def alquilar_equipo(indice: int, dias: int) -> Dict[str, Any]:
    """Procesa la lógica de alquiler y cálculo de costos."""
    equipos = _leer_equipos()

    if not (0 <= indice < len(equipos)):
        raise IndexError("Referencia de equipo inválida.")

    if dias <= 0:
        raise ValueError("La duración del alquiler debe ser de al menos 1 día.")

    equipo = equipos[indice]
    total = dias * equipo["precio_por_dia"]

    return {
        "equipo": equipo["nombre"],
        "tipo": equipo["tipo"],
        "dias": dias,
        "total": float(total)
    }
