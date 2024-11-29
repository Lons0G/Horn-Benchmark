import time

def Base_literales(archivo):
    # Obtencion de las bases de literales
    literales = set()
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            if linea.startswith('p') or linea.startswith('c'):
                continue
            for literal in linea.split()[:-1]:
                literales.add(abs(int(literal)))
    return list(literales) 

def Base_hechos(archivo):
    clauses = []
    BF = []
    Q = 0
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea.startswith('p') or linea.startswith('c'):
                continue 
            else:
                # ignora el ultimo 0
                clause = list(map(int, linea.split()[:-1]))  # Ignorar el último 0
                # Si la clausula no esta vacia
                if clause: 
                    if len(clause) == 1 and clause[0] > 0:
                        BF.append(clause[-1])
                    elif len(clause) == 1 and clause[0] < 0:
                        Q = clause[0]
                    else:
                        clauses.append(clause)
    return BF, Q

def Base_reglas(archivo):
    base_reglas = {}
    clauses = []
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea.startswith('p') or linea.startswith('c'):
                continue 
            else:
                # Ignorar el último 0
                clause = list(map(int, linea.split()[:-1]))  
                # Si la cláusula no esta vacia
                if clause:
                    if len(clause) == 1 and clause[0] > 0:
                        continue
                    elif len(clause) == 1 and clause[0] < 0:
                        continue
                    else:
                        clauses.append(clause)
    
    return clauses 

def read_dimacs(archivo):
    # Obtencion de las bases de literales
    B_literales = Base_literales(archivo) 
    
    # Obtencion de la base de hechos
    BF, Q = Base_hechos(archivo)
    BR = Base_reglas(archivo)
    return BF, BR, Q, B_literales


def BTD(BF, BR, Q, BL):
    
    # Inicializando estructuras 
    for p in BL:
        state[str(p)] = 'UNEXPANDED'
        rules_with_head[str(p)] = []
    ##print("state")
    ##print(state)
    ##print("rules with head")
    ##print(rules_with_head)
   
    for p in BF:
        state[str(p)] = 'T' 
    ##print("state")
    ##print(state)
    
    for r, clause in enumerate(BR):
        rules_with_head[str(clause[0])].append(r)
        body[str(r)] = clause[1:]
    
    ##print("rules with head")
    ##print(rules_with_head)
    ##print("Body")
    ##print(body)
   

    if state[str(abs(Q))] == 'UNEXPANDED':
        OR(abs(Q))
    ##print('Q es: ', state[abs(Q)])
    ##print('estado de Q: ', state[str(abs(Q))])
    if state[str(abs(Q))] == 'T':
        #print('estado verdadero: ', state[str(str(Q))])
        return 1
    else:
        #print('estado falso: ', state[str(abs(Q))])
        return 0 

def OR(p):
    #print('Entro al OR') 
    state[str(p)] = 'EXPANDED'
    for r in rules_with_head[str(p)]:
        #print('este es r: ', r)
        state[str(p)] = AND(r)
        if state[str(p)] == 'T':
            #print('estado de p verdadero: ', abs(p))
            #print('estado de p verdadero = ', state[p])
            #print('estado de Q verdadero: ', abs(Q))
            #print('estado de Q verdadero = ', state[str(abs(Q))])           
            #if abs(Q) == p:
                #print('son iguales')
            return 
    return

def AND(r):
    for p in body[str(r)]:
        #print('estado de {}: {}'.format(abs(p), state[str(abs(p))]))
        if state[str(abs(p))] == 'UNEXPANDED':
            #print('p en el if unexpanded: ', p)
            #print('estado: ', body[str(r)])
            #print(str(abs(p)))
            OR(abs(p))
        if state[str(abs(p))] != 'T' and state[str(abs(p))] != 'EXPANDED':
            #print('retornara F: ', abs(p))
            return 'F'
    #print('retorno true') 
    return 'T'

##print('Base de hechos: ',BF)
##print('Base de reglas: ',BR)
##print('Query: ',Q)
##print('Base de literales: ', B_literales)
#if BTD(BF, BR, abs(Q), B_literales):
#    print('YES')
#else:
#    print('NO')
#


#benchmarks = [
#'Benchmarks/benchmark_matrix_75_50.cnf', 
#'Benchmarks/benchmark_matrix_100_50.cnf', 
#'Benchmarks/benchmark_matrix_250_50.cnf',
#'Benchmarks/benchmark_matrix_500_50.cnf',
#'Benchmarks/benchmark_matrix_750_50.cnf', 
#'Benchmarks/benchmark_matrix_1000_50.cnf', 
#'Benchmarks/benchmark_matrix_1500_50.cnf', 
#'Benchmarks/benchmark_matrix_1750_50.cnf', 
#'Benchmarks/benchmark_matrix_2000_50.cnf', 
#'Benchmarks/benchmark_matrix_2500_50.cnf' 
#]
benchmarks = [
    'Benchmarks/benchmark_matrix_75_75.cnf', 
    'Benchmarks/benchmark_matrix_100_100.cnf', 
    'Benchmarks/benchmark_matrix_250_250.cnf',
    'Benchmarks/benchmark_matrix_500_500.cnf',
    'Benchmarks/benchmark_matrix_750_750.cnf', 
    'Benchmarks/benchmark_matrix_1000_1000.cnf', 
    'Benchmarks/benchmark_matrix_1500_1500.cnf', 
    'Benchmarks/benchmark_matrix_1750_1750.cnf', 
    'Benchmarks/benchmark_matrix_2000_2000.cnf', 
    'Benchmarks/benchmark_matrix_2500_2500.cnf' 
]


    #benchmarks = [
    #    'Benchmarks/benchmark_inc_75.cnf', 
    #    'Benchmarks/benchmark_inc_100.cnf', 
    #    'Benchmarks/benchmark_inc_250.cnf',
    #    'Benchmarks/benchmark_inc_500.cnf',
    #    'Benchmarks/benchmark_inc_750.cnf', 
    #    'Benchmarks/benchmark_inc_1000.cnf', 
    #    'Benchmarks/benchmark_inc_1500.cnf', 
    #    'Benchmarks/benchmark_inc_1750.cnf', 
    #    'Benchmarks/benchmark_inc_2000.cnf', 
    #    'Benchmarks/benchmark_inc_2500.cnf' 
    #]
#benchmarks = [
#    'Benchmarks/benchmark_inc_75Q_.cnf', 
#    'Benchmarks/benchmark_inc_100Q_.cnf', 
#    'Benchmarks/benchmark_inc_250Q_.cnf',
#    'Benchmarks/benchmark_inc_500Q_.cnf',
#    'Benchmarks/benchmark_inc_750Q_.cnf', 
#    'Benchmarks/benchmark_inc_1000Q_.cnf', 
#    'Benchmarks/benchmark_inc_1500Q_.cnf', 
#    'Benchmarks/benchmark_inc_1750Q_.cnf', 
#    'Benchmarks/benchmark_inc_2000Q_.cnf', 
#    'Benchmarks/benchmark_inc_2500Q_.cnf' 
#]
        #

    #benchmarks = [
    #    'Benchmarks/benchmark_matrix_75_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_100_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_250_Q.cnf',
    #    'Benchmarks/benchmark_matrix_500_Q.cnf',
    #    'Benchmarks/benchmark_matrix_750_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_1000_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_1500_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_1750_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_2000_Q.cnf', 
    #    'Benchmarks/benchmark_matrix_2500_Q.cnf' 
    #]

    #benchmarks = [
    #    'Benchmarks/benchmark_completo_n75_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n100_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n250_Qvar.cnf',
    #    'Benchmarks/benchmark_completo_n500_Qvar.cnf',
    #    'Benchmarks/benchmark_completo_n750_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n1000_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n1500_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n1750_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n2000_Qvar.cnf', 
    #    'Benchmarks/benchmark_completo_n2500_Qvar.cnf' 
    #]
print('Benchmark matriz nxm')
iter = 0
test = [75, 100, 250, 500, 750, 1000, 1500, 1750, 2000, 2500]
for input in benchmarks:
    tiempos = []
    file_path = input  
    
    state = {} 
    rules_with_head = {}
    body = {}
    BF, BR, Q, B_literales = read_dimacs(input)
    i = 0 
    sat = 0
    while i < 100:
        start_time = time.perf_counter() #time.time()
        BTD(BF, BR, abs(Q), B_literales)
        end_time = time.perf_counter() #time.time()
        tiempos.append(end_time - start_time)
        i += 1
    tiempo = sum(tiempos) / len(tiempos)
    print(str(test[iter]) + ',' + str(tiempo))
    iter += 1

