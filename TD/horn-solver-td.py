#def read_dimacs(file_path):
#    clauses = []
#    num_vars = 0
#    BF = []
#    Q = []
#    with open(file_path, 'r') as file:
#        for line in file:
#            line = line.strip()
#            if line.startswith('c'):
#                continue  # Ignorar comentarios
#            elif line.startswith('p'):
#                parts = line.split()
#                num_vars = int(parts[2])  # Número de variables
#            else:
#                clause = list(map(int, line.split()[:-1]))  # Ignorar el último 0
#                if clause:  # Asegurarse de que la cláusula no esté vacía
#                    if len(clause) == 1 and clause[0] > 0:
#                        BF.append(clause[-1])
#                    elif len(clause) == 1 and clause[0] < 0:
#                        Q = clause
#                    else:
#                        clauses.append(clause)
#
#
#   
#
#    for i in BF:
#        for j, c in enumerate(clauses):
#            if i == c[0]:
#                #print('Clausulas que se deducen de una: ', clauses[j])
#                clauses.remove(c)
#        
#
#    BR = {} 
#    for i, sublist in enumerate(clauses):
#        #print(sublist)
#        for element in sublist:
#            if element < 0:
#                clave = abs(element)
#                if clave not in BR:
#                    BR[clave] = [i]
#                else:
#                    BR[clave].append(i)
#
#
#    for i in BF:
#        if i not in BR:
#            #print(i)   
#            BR[i] = [] 
#
#    for i, sublist in enumerate(clauses):
#        if sublist[0] not in BR:
#            BR[sublist[0]] = []
#    return num_vars, clauses, BF, BR, Q

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
                    else:
                        clauses.append(clause)
    return BF

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
                        clauses.append(clause)
    
    # VERIFICAR
    BR = {} 
    for i, sublist in enumerate(clauses):
        for element in sublist:
            if element < 0:
                clave = abs(element)
                if clave not in BR:
                    BR[clave] = [i]
                else:
                    BR[clave].append(i)

    return clauses 

def read_dimacs(archivo):
    # Obtencion de las bases de literales
    B_literales = Base_literales(archivo) 
    
    # Obtencion de la base de hechos
    BF = Base_hechos(archivo)
    BR = Base_reglas(archivo)
    return BF, BR, B_literales

BF, BR, B_literales = read_dimacs('input4.dimacs')
print('Base de hechos: ',BF)
print('Base de reglas: ',BR)
print('Base de literales: ', B_literales)

