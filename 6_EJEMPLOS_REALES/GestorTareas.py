# tareas.py
tareas = []  # Variable global para guardar tareas

def agregar_tarea(descripcion, prioridad="normal"):
    """Agrega una tarea a la lista."""
    tarea = {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(tarea)
    return f"Tarea '{descripcion}' agregada"

def listar_tareas():
    """Retorna todas las tareas."""
    return tareas

def completar_tarea(indice):
    """Marca una tarea como completada."""
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        return f"Tarea completada"
    return "Índice inválido"

def tareas_pendientes():
    """Retorna solo tareas no completadas."""
    return [t for t in tareas if not t["completada"]]

# Filtrar por prioridad con lambda
def por_prioridad(prioridad):
    return list(filter(lambda t: t["prioridad"] == prioridad, tareas))