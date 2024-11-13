import sys

def generar_benchamark_incremental(n, output):
    with open(output, 'w') as f:
        sys.stdout = f
    
        # Encabezado DIMACS
        print("p cnf {} {}".format(n, n)) 
        # Generar las cláusulas
        for i in range(2, n+2):
            print(i, end = ' ')
            for j in range(i - 1, 0, - 1):
                print(-j, end = ' ')
            print('0')

    sys.stdout = sys.__stdout__

n = 5 
generar_benchamark_incremental(n, 'benchmark_incremental.cnf')

#archivo = open("mi_archivo.cnf", "w")
#archivo.write(dimacs_string)
#archivo.close()

