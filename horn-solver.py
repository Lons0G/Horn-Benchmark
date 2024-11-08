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

    return num_vars, clauses, BF, Q



print('Inicializacion')

file_path = "input4.dimacs"  
num_vars, clauses, BF, Q = read_dimacs(file_path)
yes = 0
print('clausulas: ', clauses)
print('Base de Hechos: ', BF)
print('Query: ', Q)

print('Ciclo BF != 0')
while BF != [] and yes != 1:
    print('-------------------')
    p = BF.pop(0)
    print('p = ', p)

    if p < 0:
        p = abs(p)

    print('Ciclo p e Body')
    for i, c in enumerate(clauses):
        head = clauses[i][0]
        body = clauses[i][1:]
        print('head: ', head)
        print('body: ', body)
        print('body antes: ', body)
        if p in body:
            body.remove(p)
            clauses[i].remove(p)
        elif -p in body:
            body.remove(-p)
            clauses[i].remove(-p)
        print('body despues: ', body)
        if body == []:
            print('Clausula vacia')
            print('{} =? {}'.format(head, Q)) 
            if head == abs(Q[0]):
                yes = 1
            BF.append(head)
        print('-------------------')
        print(clauses)
if yes == 0:
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
