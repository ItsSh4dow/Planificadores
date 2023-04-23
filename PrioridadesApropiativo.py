class Proceso:
    def __init__(self, id, prioridad, tiempo_llegada, rafaga_cpu):
        self.id = id
        self.prioridad = prioridad
        self.tiempo_llegada = tiempo_llegada
        self.rafaga_cpu = rafaga_cpu
        self.tiempo_restante = rafaga_cpu

    def __repr__(self):
        return f"Proceso {self.id}"

def planificar(procesos):
    tiempo_transcurrido = 0
    procesos_restantes = procesos.copy()
    procesos_terminados = []

    while len(procesos_restantes) > 0:
        procesos_restantes.sort(key=lambda x: (x.prioridad, x.tiempo_restante))
        proceso_actual = procesos_restantes[0]

        if proceso_actual.tiempo_restante > 0:
            proceso_actual.tiempo_restante -= 1
            tiempo_transcurrido += 1

            for p in procesos_restantes:
                if p != proceso_actual and p.tiempo_llegada <= tiempo_transcurrido:
                    p.prioridad += 1

        else:
            proceso_actual.tiempo_finalizacion = tiempo_transcurrido
            procesos_terminados.append(proceso_actual)
            procesos_restantes.remove(proceso_actual)

    return procesos_terminados

# Ejemplo de uso
procesos = [
    Proceso("P1", 2, 0 ,  18),
    Proceso("P2", 1, 2 ,  16),
    Proceso("P3", 2, 5 ,  10),
    Proceso("P4", 3, 6 ,  5),
    Proceso("P5", 1, 7 ,  9),
    Proceso("P6", 2, 11 , 7),
    Proceso("P7", 1, 28 , 8)
]

procesos_terminados = planificar(procesos)

for p in procesos_terminados:
    print(f"{p}: tiempo de espera = {p.tiempo_finalizacion - p.tiempo_llegada - p.rafaga_cpu}")
