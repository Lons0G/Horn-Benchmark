import sys

def generar_benchamark_incremental(n, m, output):
    with open(output, 'w') as f:
        sys.stdout = f
        BF = []
        Q = 0
        sum = 2
        # Encabezado DIMACS
        print("p cnf {} {}".format(n, n * m)) 
        # Generar las cláusulas
        for i in range(1, n + 1):
            for j in range(2, m + 2):
                if j == 2:
                    BF.append(sum - 1)
                print('{} {} 0'.format(sum, -(sum - 1)))
                sum += 1
            sum += 1

        for element in BF:
            print(str(element) + ' 0')
        Q = (sum - 2)
        print(str(-Q) + ' 0')
    sys.stdout = sys.__stdout__

n = 5 
m = 5
generar_benchamark_incremental(n, m, 'benchmark_matrix.cnf')

