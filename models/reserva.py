# Modificado por: Julian Cardenas
from models.cliente import Cliente
from models.servicio import Servicio

class Reserva:
    """Gestiona la asociación entre un cliente y un servicio prestado."""

    def __init__(self, cliente: Cliente, servicio: Servicio):
        # Validación para asegurar que los objetos sean de las clases correctas
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise TypeError("Se requiere una instancia válida de Cliente y Servicio.")
            
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    def confirmar(self):
        """Cambia el estado de la reserva a confirmada."""
        self.estado = "confirmada"

    def cancelar(self):
        """Cambia el estado de la reserva a cancelada."""
        self.estado = "cancelada"

    def __str__(self) -> str:
        """Retorna el resumen de la reserva."""
        return f"Reserva [{self.estado.upper()}]: {self.cliente.nombre} - {self.servicio.descripcion()}"
