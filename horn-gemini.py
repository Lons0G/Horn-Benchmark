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
    """
    Determina si una fórmula en formato DIMACS es satisfacible con Horn-SAT.

    Args:
        formula: Una lista de cláusulas, donde cada cláusula es una lista de literales.

    Returns:
        True si la fórmula es satisfacible, False en caso contrario.
    """

    G = nx.DiGraph()
    for clause in formula:
        positive_literals = [lit for lit in clause if lit > 0]
        negative_literals = [lit for lit in clause if lit < 0]
        if len(positive_literals) > 1:
            return False
        if positive_literals:
            G.add_edges_from([(abs(neg_lit), pos_lit) for neg_lit in negative_literals for pos_lit in positive_literals])

    try:
        nx.find_cycle(G)
        return False  # Si hay un ciclo, la fórmula no es satisfacible
    except nx.NetworkXNoCycle:
        return True

# Ejemplo de uso:
formula = [[1, -2], [-1, 3], [-2, -3], [-1, -2, -3]]
#formula = [[-1, 3], [-2, 3], [-3, 4], [-4]]
#formula = [[1, 2], [-1], [-2]]
file_path = "input3.dimacs"  # Cambia esto al nombre de tu archivo DIMACS
num_vars, clauses = read_dimacs(file_path)


if horn_sat(formula):
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
