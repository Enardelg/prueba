# Decorador para asignar prioridad según la descripción
def asignar_prioridad(func):
    def wrapper(*args, **kwargs):
        descripcion = kwargs.get('descripcion', '').lower()

        if 'urgente' in descripcion or 'caído' in descripcion:
            kwargs['prioridad'] = 'Alta'
        elif 'lento' in descripcion or 'error' in descripcion:
            kwargs['prioridad'] = 'Media'
        else:
            kwargs['prioridad'] = 'Baja'

        return func(*args, **kwargs)
    return wrapper

# Generador de tickets con ID autoincremental
def generador_tickets():
    ticket_id = 1
    while True:
        descripcion = input("\n📝 Describe el problema (o escribe 'salir' para terminar): ")
        if descripcion.lower() == 'salir':
            break
        yield {'id': ticket_id, 'descripcion': descripcion}
        ticket_id += 1

# Función que procesa y muestra el ticket, decorada con asignar_prioridad
@asignar_prioridad
def procesar_ticket(**kwargs):
    print(f"\n📨 Ticket recibido:")
    print(f"ID: {kwargs.get('id')}")
    print(f"Descripción: {kwargs.get('descripcion')}")
    print(f"🔥 Prioridad asignada: {kwargs.get('prioridad')}")
    print("-" * 40)

# Programa principal
if __name__ == "__main__":
    for ticket in generador_tickets():
        procesar_ticket(**ticket)
