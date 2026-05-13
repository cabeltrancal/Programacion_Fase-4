# Modificado por: Julian Cardenas
from utils.input_utils import obtener_opcion
from services.cliente_service import crear_cliente, obtener_clientes
from utils.logger import log_error, log_success
from utils.mensajes import mostrar_ok, mostrar_error, mostrar_info

def menu_cliente():
    """Menú principal para la gestión de clientes."""
    opciones = {
        "1": menu_crear_cliente,
        "2": menu_ver_clientes,
        "3": None # Salida
    }

    while True:
        print("\n" + "="*20)
        print("   MENÚ CLIENTE")
        print("="*20)
        print("1. Crear nuevo cliente")
        print("2. Ver listado de clientes")
        print("3. Volver al menú principal")

        opcion = obtener_opcion("Seleccione una acción", list(opciones.keys()))

        if opcion == "3":
            break
        
        # Ejecuta la función asociada a la opción
        accion = opciones.get(opcion)
        if accion:
            accion()

def menu_crear_cliente():
    """Interfaz para el registro de un nuevo cliente."""
    print("\n>>> REGISTRO DE NUEVO CLIENTE")
    
    try:
        nombre = input("Ingrese nombre completo: ").strip()
        email = input("Ingrese correo electrónico: ").strip()

        # Procesa la creación a través del service
        cliente = crear_cliente(nombre, email)

        mostrar_ok(f"Éxito: Cliente '{cliente.nombre}' registrado correctamente.")
        log_success(f"Registro exitoso: {cliente.email}", "UI_CLIENTE")

    except ValueError as ve:
        # Errores de validación (nombre corto, email inválido, etc.)
        mostrar_error(str(ve))
        log_error(f"Error de validación: {str(ve)}", "UI_CLIENTE")
    except Exception as e:
        # Errores inesperados de sistema
        log_error(f"Error crítico: {str(e)}", "UI_CLIENTE")
        mostrar_error("No se pudo completar el registro debido a un error interno.")

def menu_ver_clientes():
    """Interfaz para visualizar la base de datos de clientes."""
    print("\n" + "-"*30)
    print("      LISTA DE CLIENTES")
    print("-"*30)

    try:
        clientes = obtener_clientes()

        if not clientes:
            mostrar_info("La base de datos de clientes está vacía.")
            return

        # Encabezado de tabla simple
        print(f"{'ID':<4} | {'NOMBRE':<25} | {'EMAIL'}")
        print("-" * 60)

        for i, cliente in enumerate(clientes, 1):
            print(f"{i:<4} | {cliente['nombre']:<25} | {cliente['email']}")

    except Exception as e:
        log_error(f"Error al listar: {str(e)}", "UI_CLIENTE")
        mostrar_error("Ocurrió un problema al cargar la lista de clientes.")
