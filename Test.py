import matplotlib.pyplot as plt

# Definir la lista de tareas y su duración
tareas = [("P1", 18), ("P2", 16), ("P3", 10), ("P4", 5), ('P5', 9),('P6', 7),('P7', 8)]

# Ordenar las tareas por duración
tareas = sorted(tareas, key=lambda x: x[1])



# Ejecutar cada tarea en orden, registrando el tiempo que tarda en completarse
tiempo_total = 0
tiempos = []
tiempo_proceso = []

for tarea in tareas:
    nombre, duracion = tarea
    tiempo_total += duracion
    tiempos.append(tiempo_total)
    tiempo_proceso.append(tiempo_total - duracion)

# Mostrar una gráfica con el tiempo que se ha llevado cada proceso
plt.plot(range(1, len(tiempos)+1), tiempo_proceso, 'bo-')
plt.xticks(range(1, len(tiempos)+1))
plt.yticks(tiempos)
plt.xlabel('Tareas')
plt.ylabel('Tiempo')
plt.title('Planificación Primero el trabajo más corto')

for i, tarea in enumerate(tareas):
    nombre, duracion = tarea
    plt.text(i+1, tiempo_proceso[i], nombre, ha='center', va='bottom')
    
plt.show()
