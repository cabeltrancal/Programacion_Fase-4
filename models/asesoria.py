# Modificado por: Julian Cardenas
from models.servicio import Servicio

class ServicioAsesoria(Servicio):
    """Representa una asesoría especializada basada en sesiones."""

    def __init__(self, sesiones: int, precio_por_sesion: float, **kwargs):
        # Asegura la herencia y compatibilidad con futuros atributos de Servicio
        super().__init__(**kwargs) 
        
        if sesiones <= 0 or precio_por_sesion < 0:
            raise ValueError("Error contable: Las sesiones y el precio deben ser valores positivos.")
            
        self.sesiones = sesiones
        self.precio_por_sesion = precio_por_sesion

    def calcular_costo(self) -> float:
        """Calcula el costo total (Base gravable para factura electrónica)."""
        return float(self.sesiones * self.precio_por_sesion)

    def descripcion(self) -> str:
        return f"Asesoría Técnica: {self.sesiones} sesiones registradas."
