from datetime import datetime

def log_error(mensaje):
    """Registra un mensaje de error con fecha y hora en el archivo de logs."""
    with open("data/logs.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ERROR: {mensaje}\n")