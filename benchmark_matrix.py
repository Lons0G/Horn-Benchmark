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


n = 75
m = 75
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)

n = 100 
m = 100
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')
n = 250
m = 250
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 500
m = 500
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 750
m = 750
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 1000
m = 1000
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 1500
m = 1500
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 1750
m = 1750
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 2000
m = 2000
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')

n = 2500
m = 2500
input = 'benchmark_matrix_' + str(n) + '_' + str(m) + '.cnf'
generar_benchamark_incremental(n, m, input)
print(input + ' : Terminado')








