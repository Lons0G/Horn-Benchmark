def generar_dimacs_grafo_completo(n, output):
    # Abrir el archivo de salida
    with open(output, 'w') as f:
        # Calcular el número de variables y reglas
        total_variable = n
        reglas = n * (n - 1)

        # Escribir el encabezado DIMACS
        f.write(f"p cnf {total_variable} {reglas}\n")

        # Generar las cláusulas
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    f.write(f"{i} -{j} 0\n")

        BF = 9
        f.write(f"{BF} 0\n")  # Imprimir BF con un 0 al final

        # Agregar "Query" (antes Constante Q)
        Q = total_variable
        f.write(f"{-Q} 0\n")  # Imprimir Q como negativo con un 0 al final

# Lista de valores para n
valores_n = [5, 75, 100, 250, 500, 750, 1000, 1500, 1750, 2000, 2500, 3000]

# Generar un archivo para cada valor de n
for n in valores_n:
    # Definir el nombre del archivo
    archivo = f'benchmark_completo_n{n}_Qvar.cnf'

    # Llamar a la función para generar el archivo
    generar_dimacs_grafo_completo(n, archivo)
    
    # Informar que el archivo fue creado
    print(f"Archivo generado: {archivo}")
