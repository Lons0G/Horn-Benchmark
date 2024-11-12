import sys

def generar_benchamark_incremental(n, output):
    with open(output, 'w') as f:
        sys.stdout = f
    
        # Encabezado DIMACS
        print("p cnf {} {}".format(n, n)) 
        sec = 2 
        prev = 0  
        # Generar las cláusulas
        for i in range(2, n+2):
            for j in range(-sec, -prev + 1, + 1):
                if j == -sec:
                    print(abs(j), end = ' ')
                else:
                    print(j, end = ' ') 
            if i != 2:
                print('0')
            else:
                print(' ')
            prev = sec 
            sec = sec + i

    sys.stdout = sys.__stdout__

n = 5 
generar_benchamark_incremental(n, 'benchmark_incremental.cnf')

#archivo = open("mi_archivo.cnf", "w")
#archivo.write(dimacs_string)
#archivo.close()

