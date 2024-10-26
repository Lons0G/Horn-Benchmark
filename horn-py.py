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


def is_unit_clause(clause, assignments):
    return len(clause) == 1 and clause[0] not in assignments

def get_positive_literal(clause):
    for literal in clause:
        if literal > 0:
            return literal
    return None

def horn_solver(num_vars, clauses):
    assignments = {}
    queue = []

    # Inicializar la cola con cláusulas unitarias
    for clause in clauses:
        if is_unit_clause(clause, assignments):
            unit_literal = get_positive_literal(clause)
            if unit_literal is not None:
                assignments[unit_literal] = True
                queue.append(unit_literal)

    # Propagación
    while queue:
        literal = queue.pop()
        assignments[literal] = True

        # Revisar las cláusulas que contienen el literal
        for clause in clauses:
            if literal in clause:
                clause.remove(literal)  # Eliminar el literal de la cláusula

            # Si la cláusula se convierte en una cláusula unitaria
            if is_unit_clause(clause, assignments):
                unit_literal = get_positive_literal(clause)
                if unit_literal is not None and unit_literal not in assignments:
                    assignments[unit_literal] = True
                    queue.append(unit_literal)

    # Verificar si todas las cláusulas son satisfechas
    for clause in clauses:
        if not any((literal in assignments and assignments[literal]) or 
                   (literal < 0 and -literal in assignments and not assignments[-literal]) 
                   for literal in clause):
            return False  # Insatisfacible

    return True  # Satisfacible# Ejemplo de uso
if __name__ == "__main__":
    file_path = "input3.dimacs"  # Cambia esto al nombre de tu archivo DIMACS
    num_vars, clauses = read_dimacs(file_path)
    satisfiable = horn_solver(num_vars, clauses)
    
    print(num_vars)
    print(clauses)

    if satisfiable:
        print("El problema de Horn es satisfacible.")
    else:
        print("El problema de Horn es insatisfacible.")
