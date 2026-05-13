# Modificado por: Julian Cardenas
import json
import os
from pathlib import Path
from typing import List, Dict, Any

# Uso de Path para mejor manejo de rutas en diferentes SO
RUTA_ASESORIAS = Path("data/asesorias.json")

def _asegurar_directorio():
    """Crea la carpeta de datos si no existe."""
    RUTA_ASESORIAS.parent.mkdir(parents=True, exist_ok=True)

def _leer_asesorias() -> List[Dict[str, Any]]:
    """Lee las asesorías almacenadas en el archivo JSON."""
    if not RUTA_ASESORIAS.exists():
        return []

    try:
        with open(RUTA_ASESORIAS, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def _guardar_asesorias(asesorias: List[Dict[str, Any]]):
    """Guarda la lista de asesorías en el archivo JSON."""
    _asegurar_directorio()
    with open(RUTA_ASESORIAS, "w", encoding="utf-8") as file:
        json.dump(asesorias, file, indent=4, ensure_ascii=False)

def crear_asesoria(nombre: str, especialista: str, precio_por_sesion: float) -> Dict[str, Any]:
    """Crea y guarda una nueva asesoría con validaciones técnicas."""
    
    if not nombre.strip() or not especialista.strip():
        raise ValueError("El nombre y el especialista son campos obligatorios.")

    if precio_por_sesion <= 0:
        raise ValueError("El precio por sesión debe ser un valor positivo.")

    asesorias = _leer_asesorias()

    # Validación de duplicados optimizada
    if any(a["nombre"].lower() == nombre.strip().lower() for a in asesorias):
        raise ValueError(f"La asesoría '{nombre}' ya se encuentra registrada.")

    nueva_asesoria = {
        "nombre": nombre.strip(),
        "especialista": especialista.strip(),
        "precio_por_sesion": float(precio_por_sesion)
    }

    asesorias.append(nueva_asesoria)
    _guardar_asesorias(asesorias)
    return nueva_asesoria

def obtener_asesorias() -> List[Dict[str, Any]]:
    """Retorna todas las asesorías registradas."""
    return _leer_asesorias()

def eliminar_asesoria(indice: int):
    """Elimina una asesoría según su posición en la lista."""
    asesorias = _leer_asesorias()

    if not (0 <= indice < len(asesorias)):
        raise IndexError("La asesoría seleccionada no existe en los registros.")

    asesorias.pop(indice)
    _guardar_asesorias(asesorias)

def agendar_asesoria(indice: int, sesiones: int) -> Dict[str, Any]:
    """Calcula el costo y genera el objeto de agendamiento."""
    asesorias = _leer_asesorias()

    if not (0 <= indice < len(asesorias)):
        raise IndexError("Índice de asesoría inválido.")

    if sesiones <= 0:
        raise ValueError("La cantidad de sesiones debe ser mayor a cero.")

    asesoria = asesorias[indice]
    total = sesiones * asesoria["precio_por_sesion"]

    return {
        "asesoria": asesoria["nombre"],
        "especialista": asesoria["especialista"],
        "sesiones": sesiones,
        "total": float(total)
    }
