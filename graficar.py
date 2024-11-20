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
        plt.plot(datos_array[:, 0], datos_array[:, 1])
        lineas_datos= []
        iter += 1

    plt.xlabel('Tamaño N (Cuando Q es la misma)')
    plt.ylabel('Tiempo en segundos')
    plt.title('Gráfica de múltiples líneas')
    plt.legend(label_legends)  # Agregar leyenda si es necesario

    plt.show()

# Ejemplo de uso:
archivos_csv = ["simulaciones/sim_incremental_Q.txt", "simulaciones/sim_incremental_Q_lineal.txt"]
labels = ["Algoritmo Cuadratico", "Algoritmo Lineal"]
graficar_multiples_lineas_archivos(archivos_csv, labels)
