import numpy as np
import matplotlib.pyplot as plt

def graficar_multiples_lineas_archivos(archivos, labels):
    lineas_datos = []
    label_legends = []
    iter = 0
    for archivo in archivos:
        label_legends.append(labels[iter])
        with open(archivo, 'r') as f:
            datos = f.readlines()

        for linea in datos[:]:  
            valores = linea.strip().split(',')
            lineas_datos.append([float(valor) for valor in valores])

        datos_array = np.array(lineas_datos)
        print(datos_array)
        plt.plot(datos_array[:, 0], datos_array[:, 1], marker='o')
        lineas_datos= []
        iter += 1

    plt.xlabel('Tamaño N')
    plt.ylabel('Tiempo en segundos')
    plt.title('Top Down vs Bottom Up - Benchmark incremental')
    plt.legend(label_legends)  # Agregar leyenda si es necesario
    plt.grid(True)
    plt.show()

# Ejemplo de uso:
archivos_csv = ["TD/simulaciones/sim_incremental_TD.txt", "simulaciones/sim_incremental_n_lineal.txt"]
labels = ["Top Down", "Bottom Up"]
graficar_multiples_lineas_archivos(archivos_csv, labels)

#import matplotlib.pyplot as plt
#
## Datos de ejemplo (ajusta estos valores según tus datos reales)
#tiempo = [0, 2, 4, 6, 8, 10]
#gene1 = [0.3, 1.2, 1.3, 1.8, 1.6, 1.5]
#gene2 = [2.1, 2.4, 2.3, 2.1, 2.2, 2.8]
#gene3 = [0.3, 0.6, 1.1, 1.8, 2.2, 2.8]
#
## Crear la figura y los ejes
#plt.figure(figsize=(8, 6))
#
## Plot de las líneas
#plt.plot(tiempo, gene1, marker='o', color='red', label='gene 1')
#plt.plot(tiempo, gene2, marker='o', color='blue', label='gene 2')
#plt.plot(tiempo, gene3, marker='o', color='green', label='gene 3')
#
## Etiquetas de los ejes
#plt.xlabel('time [hour]')
#plt.ylabel('gene expression [log(TPM)]')
#
## Límites de los ejes
#plt.xlim(0, 10)
#plt.ylim(0, 3)
#
## Cuadrícula
#plt.grid(True)
#
## Leyenda
#plt.legend()
#
## Mostrar la gráfica
#plt.show()
