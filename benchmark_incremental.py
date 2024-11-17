import sys

def generar_benchamark_incremental(n, output):
    with open(output, 'w') as f:
        sys.stdout = f
        Q = 0
        # Encabezado DIMACS
        print("p cnf {} {}".format(n, n)) 
        # Generar las cláusulas
        for i in range(2, n+2):
            print(i, end = ' ')
            for j in range(i - 1, 0, - 1):
                print(-j, end = ' ')
            print('0')
            Q = i
        print('1 0')
        print(str(-Q) + ' 0')
    sys.stdout = sys.__stdout__


n = 75
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 100
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 250
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 500
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 750
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 1000
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 1500
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 1750
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 2000
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')

n = 2500 
input = 'benchmark_inc_' + str(n) + '.cnf'
generar_benchamark_incremental(n, input)
print(input + ' : Terminado')





