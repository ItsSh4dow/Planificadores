# Definir una lista de tuplas, donde cada tupla representa un proceso y su tiempo de ejecución
procesos = [("P1", 18), ("P2", 16), ("P3", 10), ("P4", 5), ('P5', 9),('P6', 7),('P7', 8)]

# Función para ordenar los procesos según su tiempo de ejecución (SJF)
def sjf(procesos):
    # Ordenar los procesos por su tiempo de ejecución
    procesos.sort(key=lambda x: x[1])
    
    # Calcular el tiempo de espera y de retorno para cada proceso
    tiempo_espera = 0
    tiempo_retorno = 0
    for i in range(len(procesos)):
        # Calcular el tiempo de espera para el proceso actual
        tiempo_espera += tiempo_retorno
        # Actualizar el tiempo de retorno para el proceso actual
        tiempo_retorno += procesos[i][1]
    
    # Calcular el tiempo de retorno promedio y el tiempo de espera promedio
    tiempo_retorno_promedio = tiempo_retorno / len(procesos)
    tiempo_espera_promedio = tiempo_espera / len(procesos)
    
    # Imprimir los resultados
    print("Proceso\tTiempo de ejecución")
    for proceso in procesos:
        print(proceso[0], "\t", proceso[1])
    print("Tiempo de retorno promedio:", tiempo_retorno_promedio)
    print("Tiempo de espera promedio:", tiempo_espera_promedio)

# Ejecutar la función
sjf(procesos)
