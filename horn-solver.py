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


    BR = {} 
    for i, sublist in enumerate(clauses):
        for element in sublist:
            if element < 0:
                clave = abs(element)
                if clave not in BR:
                    BR[clave] = [i]
                else:
                    BR[clave].append(i)
    

    for i in BF:
        if i not in BR:
            print(i)
            BR[i] = []
    return num_vars, clauses, BF, BR, Q



def horn_sat(BF, BR, Q):
    print('Ciclo BF != 0')
    while BF != []:
        print('-------------------')
        p = BF.pop(0)
        print('p = ', p)
        print('Base de Hechos: ', BF)
        print('Ciclo p e Body')

        #while p not in BR:
        #    print('La literal no aplica: ', p)
        #    p = BF.pop(0)
        #    print('Nueva p: ', p)

        for lp in BR[p]:
            print('indice: ', lp)
            head = clauses[lp][0]
            body = clauses[lp][1:]
            print('head: ', head)
            print('body: ', body)
            print('body antes: ', body)
            print('regla antes: ', clauses[lp])
            clauses[lp].remove(-p)
            body.remove(-p)
            print('body despues: ', body)
            print('regla despues: ', clauses[lp])
            print('body despues: ', body)
            if body == []:
                print('Clausula vacia')
                print('head: {} es Q: {}?'.format(head, abs(Q[0]))) 
                if head == abs(Q[0]):
                    return 1
                clauses[lp] = []
                BF.append(head)
                print('BF actualizada: ', BF)
            

            print('Clausulas: ', clauses)
            print('Base de Reglas : ', BR)
            print('-------------------')
            print('-------------------')



print('Inicializacion')

file_path = "input4.dimacs"  
num_vars, clauses, BF, BR, Q = read_dimacs(file_path)
yes = 0
print('clausulas: ', clauses)
print('Base de Hechos: ', BF)
print('Base de Reglas: ', BR)
print('Query: ', Q)
if horn_sat(BF, BR, Q):
    print("La fórmula no essatisfacible.")
else:
    print("La fórmula es satisfacible.")
