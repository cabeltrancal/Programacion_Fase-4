# Modificado por: Julian Cardenas
from models.servicio import Servicio

class ServicioEquipo(Servicio):
    """Representa un servicio de alquiler de equipos."""

    def __init__(self, dias: int, precio_por_dia: float, **kwargs):
        # Inicializa la clase padre para asegurar la integridad del modelo
        super().__init__(**kwargs) 
        
        if dias <= 0 or precio_por_dia < 0:
            raise ValueError("Los días deben ser mayores a cero y el precio no puede ser negativo.")
            
        self.dias = dias
        self.precio_por_dia = precio_por_dia

    def calcular_costo(self) -> float:
        """Calcula el costo total del alquiler."""
        return float(self.dias * self.precio_por_dia)

    def descripcion(self) -> str:
        """Retorna una descripción detallada."""
        return f"Alquiler de equipo: {self.dias} días."
