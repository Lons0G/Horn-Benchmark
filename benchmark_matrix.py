import sys

def generar_benchamark_incremental(n, m, output):
    with open(output, 'w') as f:
        sys.stdout = f
        

        sum = 2
        # Encabezado DIMACS
        print("p cnf {} {}".format(n, n * m)) 
        # Generar las cláusulas
        for i in range(1, n + 1):
            for j in range(2, m + 2):
                print('{} {}'.format(sum, -(sum - 1)))
                sum += 1 
    sys.stdout = sys.__stdout__

n = 5
m = 5
generar_benchamark_incremental(n, m, 'benchmark_matrix.cnf')

#archivo = open("mi_archivo.cnf", "w")
#archivo.write(dimacs_string)
#archivo.close()

