# Modificado por: Julian Cardenas
from models.base_model import BaseModel

class Cliente(BaseModel):
    """
    Representa un cliente del sistema.
    Hereda el ID automático desde BaseModel.
    """

    def __init__(self, nombre: str, email: str):
        super().__init__()
        
        # Validación básica de datos
        if not nombre or not email:
            raise ValueError("El nombre y el email no pueden estar vacíos.")
            
        self.nombre = nombre
        self.email = email

    def __str__(self) -> str:
        """Retorna una representación en texto del cliente."""
        return f"Cliente {self.id}: {self.nombre} ({self.email})"

    def __repr__(self) -> str:
        """Representación técnica para depuración."""
        return f"Cliente(id={self.id}, nombre='{self.nombre}')"
