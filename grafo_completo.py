def generar_dimacs_grafo_completo(n):
  # Encabezado DIMACS
  dimacs = f"p cnf {n} {n*(n-1)}\n"

  # Generar las cláusulas
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i != j:
        dimacs += f"{i} -{j} 0\n"

  return dimacs

n = 5 
dimacs_string = generar_dimacs_grafo_completo(n)

archivo = open("mi_archivo.cnf", "w")
archivo.write(dimacs_string)
archivo.close()

print(dimacs_string)
