import numpy as np
import matplotlib.pyplot as plt

def graficar_multiples_lineas_archivos(archivos):
    lineas_datos = []
    label_legends = []
    for archivo in archivos:
        label_legends.append(archivo)
        with open(archivo, 'r') as f:
            datos = f.readlines()

        for linea in datos[:]:  
            valores = linea.strip().split(',')
            lineas_datos.append([float(valor) for valor in valores])

        datos_array = np.array(lineas_datos)
        print(datos_array)
        plt.plot(datos_array[:, 0], datos_array[:, 1])
        lineas_datos= []

    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfica de múltiples líneas')
    plt.legend(label_legends)  # Agregar leyenda si es necesario

    plt.show()

# Ejemplo de uso:
archivos_csv = ["datos1.csv", "datos2.csv", "datos3.csv"]
graficar_multiples_lineas_archivos(archivos_csv)
