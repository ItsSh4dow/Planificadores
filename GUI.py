import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

class GUISJF:
    
    
    def __init__(self):
        # Variables
        self.nColumnas = 0
        self.nProcesos = 0
        self.rafagas = []
        self.tareas = []
        
        #tamaño de la ventana
        self.window = tk.Tk()
        self.window.title("Algoritmos de planificación")
        #  Obtenemos el largo y  ancho de la pantalla
        self.wtotal = self.window.winfo_screenwidth()
        self.htotal = self.window.winfo_screenheight()
        self.mitadX = round(self.wtotal/2-750/2)
        self.mitadY = round(self.htotal/2-500/2)
        self.window.geometry("750x500+%d+%d" % (self.mitadX, self.mitadY))
        self.titulo = tk.Label(self.window, text='Algoritmos de planificacion', font=("Century Gothic", 14))
        self.titulo.place(x=250,y=20)
        self.window.resizable(0,0)
        
        # Agrego los botones
        self.btnNuevoProceso = tk.Button(self.window, text='Agragar',font=("Century Gothic", 12), width=12, height=2, command=self.agregar)
        self.btnNuevoProceso.place(x=550,y=100)
        self.btnEliminarProceso = tk.Button(self.window, text='Eliminar',font=("Century Gothic", 12), width=12, height=2, command=self.eliminar)
        self.btnEliminarProceso.place(x=550,y=200)
        self.btnCalcular = tk.Button(self.window, text='Calcular',font=("Century Gothic", 12), width=12, height=2, command=self.calcular)
        self.btnCalcular.place(x=550,y=300)
        
        # Agrego la lista despleglable
        # con command= puedo agregar que se ejecute un metodo
        self.lista = ttk.Combobox(self.window, values=['SJF', 'Prioridades', 'Round-Robin'], state='readonly', width=13, height=15)
        self.lista.place(x=25, y=200)
        self.lista.set('SJF')
        
        # Agregamos todas las etiquetas        
        self.labelTiempoEspera = tk.Label(self.window, text='Tiempo total de espera: ', font=("Century Gothic", 10), width=21, height=2)
        self.labelTiempoEspera.place(x=50,y=380)
        self.labelTiempoEjecucion = tk.Label(self.window, text='Tiempo total de ejecucion: ', font=("Century Gothic", 10), width=22, height=2)
        self.labelTiempoEjecucion.place(x=50,y=420)
        
        # Resultados
        self.resultadoTiempoEspera = tk.Label(self.window, text='', font=("Century Gothic", 10), width=15, height=2)
        self.resultadoTiempoEspera.place(x=250,y=380)
        self.resultadoTiempoEjecucion = tk.Label(self.window, text='', font=("Century Gothic", 10), width=15, height=2)
        self.resultadoTiempoEjecucion.place(x=250,y=420)
        
        #Agregar tabla
        self.tabla = ttk.Treeview(self.window, selectmode='browse', columns=('rafaga', 'llegada'))
        # self.tabla['columns'] = ('ID', 'Tiempo Rafaga', 'Tiempo llegada')
        
        # Formatear las columnas
        # self.tabla.column('#0', width=0, stretch=tk.NO)
        self.tabla.column('#0', width=120)
        self.tabla.heading('#0', text="ID", anchor=tk.CENTER)
        self.tabla.column('rafaga', width=120)
        self.tabla.heading('rafaga', text="Tiempo Rafaga",anchor=tk.CENTER)
        self.tabla.column('llegada', width=120)
        self.tabla.heading('llegada', text="Tiempo llegada",anchor=tk.CENTER)
        self.tabla.place(x=150,y=130)  
    
        # Metodo para agregar un proceso
    def agregar(self):
        # Crear una ventana emergente
        self.mitadX = round(self.wtotal/2-750/2)
        self.mitadY = round(self.htotal/2-500/2)
        
        global ventana_emergente
        ventana_emergente = tk.Toplevel(self.window)
        posicion_x = int(ventana_emergente.winfo_screenwidth() / 2 - 200 / 2)
        posicion_y = int(ventana_emergente.winfo_screenheight() / 2 - 70 / 2)
        ventana_emergente.geometry(f"200x80+{posicion_x}+{posicion_y}")

        # Crear las etiquetas y cuadros de entrada para los datos
        etiquetaRafaga = tk.Label(ventana_emergente, text="Tiempo de rafaga")
        etiquetaRafaga.grid(row=0, column=0)
        global rafaga
        rafaga = tk.IntVar()
        rafaga_entry = tk.Entry(ventana_emergente, textvariable=rafaga)
        rafaga_entry.grid(row=0, column=1)
        
        etiquetaLlegada = tk.Label(ventana_emergente, text="Tiempo de llegada")
        etiquetaLlegada.grid(row=1, column=0)
        global llegada
        llegada = tk.IntVar()
        llegada_entry = tk.Entry(ventana_emergente, textvariable=llegada)
        llegada_entry.grid(row=1, column=1)
        
        # Crear un botón "Guardar"
        guardar_button = tk.Button(ventana_emergente, text="Guardar", command=self.guardar)
        guardar_button.grid(row=2, column=1)
        
    def eliminar(self):
        if (self.nProcesos > 0):    
            # Obtener el índice del último elemento agregado
            ultimo_indice = self.tabla.get_children()[-1]
            # Eliminar el elemento con el índice obtenido
            self.tabla.delete(ultimo_indice)
            self.procesos.pop(self.nProcesos-1)
            self.rafagas.pop(self.nProcesos-1)
            self.nProcesos -= 1
            
            
    def guardar(self):
        try:
            valorLlegada = llegada.get()
            valorRafaga = rafaga.get()
        
            self.rafagas.append(valorRafaga)
            
            self.tabla.insert("", "end", text=(self.nProcesos+1), values=(valorRafaga, valorLlegada))
            self.nProcesos +=1
            # Cerrar la ventana emergente
            ventana_emergente.destroy()
        except:
            messagebox.showerror("Error", "Se ha tratado de ingresar letras en vez de numeros")
                
    def calcular(self):
        if self.nProcesos > 0:
            # Agregamos todos los procesos a un array con su id
            i = 0
            while i < self.nProcesos:
                tarea = ('P'+str(self.nProcesos), self.rafagas[i])
                self.tareas.append(tarea)
                i +=1
            self.graficar()
            self.limpiarDatos()
            
    def limpiarDatos(self):
        self.tabla.delete(*self.tabla.get_children())
        
    def graficar(self):
        # Ordenar las tareas por duración
            self.tareas = sorted(self.tareas, key=lambda x: x[1])
            # Ejecutar cada tarea en orden, registrando el tiempo que tarda en completarse
            tiempo_total = 0
            tiempos = []
            tiempo_proceso = []
            aux = 0
            for x in self.tareas:
                nombre, duracion = x
                tiempo_total += duracion
                tiempos.append(tiempo_total)
                tiempo_proceso.append(tiempo_total - duracion)
                aux += tiempo_total - duracion
            # Ponemos el tiempo promedio de ejecucion en la label
            self.resultadoTiempoEjecucion.config(text=(str(tiempo_total/self.nProcesos)))
            self.resultadoTiempoEspera.config(text=str(aux/self.nProcesos))

            # Mostrar una gráfica con el tiempo que se ha llevado cada proceso
            plt.plot(range(1, len(tiempos)+1), tiempo_proceso, 'bo-')
            plt.xticks(range(1, len(tiempos)+1))
            plt.yticks(tiempos)
            plt.xlabel('Procesos')
            plt.ylabel('Tiempo')
            plt.title('Planificación Primero el trabajo más corto')

            for i, tarea in enumerate(self.tareas):
                nombre, duracion = tarea
                plt.text(i+1, tiempo_proceso[i], nombre, ha='center', va='bottom')
                
            plt.show()
            
            
if __name__ == '__main__':
    gui = GUISJF()
    gui.window.mainloop()