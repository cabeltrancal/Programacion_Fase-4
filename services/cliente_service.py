# Modificado por: Julian Cardenas
import json
import re
from pathlib import Path
from typing import List, Dict, Any
from models.cliente import Cliente

# Uso de Path para compatibilidad entre sistemas operativos
RUTA_CLIENTES = Path("data/clientes.json")

def _asegurar_directorio():
    """Crea la carpeta data si no existe para evitar errores de escritura."""
    RUTA_CLIENTES.parent.mkdir(parents=True, exist_ok=True)

def _leer_clientes() -> List[Dict[str, Any]]:
    """Lee y retorna la lista de clientes desde el JSON."""
    if not RUTA_CLIENTES.exists():
        return []

    try:
        with open(RUTA_CLIENTES, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def _guardar_clientes(clientes: List[Dict[str, Any]]):
    """Guarda la lista de clientes con formato legible."""
    _asegurar_directorio()
    with open(RUTA_CLIENTES, "w", encoding="utf-8") as file:
        json.dump(clientes, file, indent=4, ensure_ascii=False)

def crear_cliente(nombre: str, email: str) -> Cliente:
    """Crea un cliente con validaciones estrictas y lo persiste."""
    
    # Validación y limpieza de nombre
    nombre_limpio = nombre.strip()
    if not (3 <= len(nombre_limpio) <= 50):
        raise ValueError("El nombre debe tener entre 3 y 50 caracteres.")
    
    if not all(c.isalpha() or c.isspace() for c in nombre_limpio):
        raise ValueError("El nombre solo permite letras y espacios.")

    # Validación y limpieza de email
    email_limpio = email.strip().lower()
    # Expresión regular mejorada para estándares modernos
    patron_email = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    
    if not re.match(patron_email, email_limpio):
        raise ValueError("El formato del email no es válido.")

    clientes = _leer_clientes()

    # Validación de duplicados
    if any(c["email"] == email_limpio for c in clientes):
        raise ValueError(f"El email '{email_limpio}' ya está registrado.")

    # Instancia y persistencia
    nuevo_cliente = Cliente(nombre_limpio, email_limpio)
    
    cliente_dict = {
        "nombre": nuevo_cliente.nombre,
        "email": nuevo_cliente.email
    }

    clientes.append(cliente_dict)
    _guardar_clientes(clientes)
    
    return nuevo_cliente

def obtener_clientes() -> List[Dict[str, Any]]:
    """Retorna todos los registros de clientes."""
    return _leer_clientes()
