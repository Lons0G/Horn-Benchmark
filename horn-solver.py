import networkx as nx

def read_dimacs(file_path):
    clauses = []
    num_vars = 0

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
                    clauses.append(clause)

    return num_vars, clauses

def horn_sat(formula):
    G = nx.DiGraph()
    for clause in formula:
        positive_literals = [lit for lit in clause if lit > 0]
        negative_literals = [lit for lit in clause if lit < 0]
        if len(positive_literals) > 1:
            return False, {}  # No es una cláusula de Horn
        if positive_literals:
            G.add_edges_from([(abs(neg_lit), pos_lit) for neg_lit in negative_literals for pos_lit in positive_literals])

    try:
        nx.find_cycle(G)
        return False, {}  
    except nx.NetworkXNoCycle:
        # Si no hay ciclo, se puede construir una asignación satisfactoria
        assignment = {}
        for clause in formula:
            positive_literals = [lit for lit in clause if lit > 0]
            negative_literals = [lit for lit in clause if lit < 0]
            if positive_literals:
                pos_lit = positive_literals[0]
                assignment[pos_lit] = 1  
                for neg_lit in negative_literals:
                    assignment[abs(neg_lit)] = 0  

        # Asegurarse de que todos los literales no asignados tengan un valor
        for clause in formula:
            for lit in clause:
                if abs(lit) not in assignment:
                    assignment[abs(lit)] = 1 if lit > 0 else 0  

        return True, assignment

file_path = "input3.dimacs"
num_vars, clauses = read_dimacs(file_path)

satisfacible, asignacion = horn_sat(clauses)

if satisfacible:
    print("La fórmula es satisfacible.")
    print("Asignación de literales:", asignacion)
else:
    print("La fórmula no es satisfacible.")
