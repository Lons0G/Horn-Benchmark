import time

def read_dimacs(file_path):
    clauses = []
    num_vars = 0
    BF = []
    Q = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c'):
                continue  # Ignorar comentarios
            elif line.startswith('p'):
                parts = line.split()
                num_vars = int(parts[2])  # Número de variables
            else:
                clause = list(map(int, line.split()[:-1]))  # Ignorar el último 0
                if clause:  # Asegurarse de que la cláusula no esté vacía
                    if len(clause) == 1 and clause[0] > 0:
                        BF.append(clause[-1])
                    elif len(clause) == 1 and clause[0] < 0:
                        Q = clause
                    else:
                        clauses.append(clause)


   

    for i in BF:
        for j, c in enumerate(clauses):
            if i == c[0]:
                #print('Clausulas que se deducen de una: ', clauses[j])
                clauses.remove(c)
        

    BR = {} 
    for i, sublist in enumerate(clauses):
        #print(sublist)
        for element in sublist:
            if element < 0:
                clave = abs(element)
                if clave not in BR:
                    BR[clave] = [i]
                else:
                    BR[clave].append(i)


    for i in BF:
        if i not in BR:
            #print(i)   
            BR[i] = [] 

    for i, sublist in enumerate(clauses):
        if sublist[0] not in BR:
            BR[sublist[0]] = []
    return num_vars, clauses, BF, BR, Q



def horn_sat(BF, BR, Q):
    #print('Ciclo BF != 0')
    while BF != []:
        #print('-------------------')
        p = BF.pop(0)
        #print('p = ', p)
        #print('Base de Hechos: ', BF)
        #print('Ciclo p e Body')
        for lp in BR[p]:
            #print('indice: ', lp)
            head = clauses[lp][0]
            body = clauses[lp][1:]
            #print('head: ', head)
            #print('body: ', body)
            #print('body antes: ', body)
            #print('regla antes: ', clauses[lp])
            clauses[lp].remove(-p)
            body.remove(-p)
            #print('body despues: ', body)
            #print('regla despues: ', clauses[lp])
            #print('body despues: ', body)
            if body == []:
                #print('Clausula vacia')
                #print('head: {} es Q: {}?'.format(head, abs(Q[0]))) 
                if head == abs(Q[0]):
                    return 1
                clauses[lp] = []
                BF.append(head)
            #print('BF actualizada: ', BF)
            

            #print('Clausulas: ', clauses)
            #print('Base de Reglas : ', BR)
            #print('-------------------')
            #print('-------------------')



#benchmarks = [
#'benchmark_matrix_75_50.cnf', 
#'benchmark_matrix_100_50.cnf', 
#'benchmark_matrix_250_50.cnf',
#'benchmark_matrix_500_50.cnf',
#'benchmark_matrix_750_50.cnf', 
#'benchmark_matrix_1000_50.cnf', 
#'benchmark_matrix_1500_50.cnf', 
#'benchmark_matrix_1750_50.cnf', 
#'benchmark_matrix_2000_50.cnf', 
#'benchmark_matrix_2500_50.cnf' 
#]
    #benchmarks = [
    #    'benchmark_matrix_75_75.cnf', 
    #    'benchmark_matrix_100_100.cnf', 
    #    'benchmark_matrix_250_250.cnf',
    #    'benchmark_matrix_500_500.cnf',
    #    'benchmark_matrix_750_750.cnf', 
    #    'benchmark_matrix_1000_1000.cnf', 
    #    'benchmark_matrix_1500_1500.cnf', 
    #    'benchmark_matrix_1750_1750.cnf', 
    #    'benchmark_matrix_2000_2000.cnf', 
    #    'benchmark_matrix_2500_2500.cnf' 
    #]


        #benchmarks = [
        #        'benchmark_inc_75.cnf', 
        #        'benchmark_inc_100.cnf', 
        #        'benchmark_inc_250.cnf',
        #        'benchmark_inc_500.cnf',
        #        'benchmark_inc_750.cnf', 
        #        'benchmark_inc_1000.cnf', 
        #        'benchmark_inc_1500.cnf', 
        #        'benchmark_inc_1750.cnf', 
        #        'benchmark_inc_2000.cnf', 
        #        'benchmark_inc_2500.cnf' 
        #    ]
        #benchmarks = [
        #        'benchmark_inc_75Q_.cnf', 
        #        'benchmark_inc_100Q_.cnf', 
        #        'benchmark_inc_250Q_.cnf',
        #        'benchmark_inc_500Q_.cnf',
        #        'benchmark_inc_750Q_.cnf', 
        #        'benchmark_inc_1000Q_.cnf', 
        #        'benchmark_inc_1500Q_.cnf', 
        #        'benchmark_inc_1750Q_.cnf', 
        #        'benchmark_inc_2000Q_.cnf', 
        #        'benchmark_inc_2500Q_.cnf' 
        #    ]
        #

benchmarks = [
    'benchmark_matrix_75_Q.cnf', 
    'benchmark_matrix_100_Q.cnf', 
    'benchmark_matrix_250_Q.cnf',
    'benchmark_matrix_500_Q.cnf',
    'benchmark_matrix_750_Q.cnf', 
    'benchmark_matrix_1000_Q.cnf', 
    'benchmark_matrix_1500_Q.cnf', 
    'benchmark_matrix_1750_Q.cnf', 
    'benchmark_matrix_2000_Q.cnf', 
    'benchmark_matrix_2500_Q.cnf' 
]


for input in benchmarks:
    tiempos = []
    file_path = input  
    num_vars, clauses, BF, BR, Q = read_dimacs(file_path)
    i = 0
    sat = 0
    while i < 100:
        start_time = time.time()
        horn_sat(BF, BR, Q)
        end_time = time.time()
        tiempos.append(end_time - start_time)
        i += 1
    tiempo = sum(tiempos) / len(tiempos)
    print(input + ' : ' + str(tiempo))


