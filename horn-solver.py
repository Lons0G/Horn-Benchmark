def read_dimacs(file_path):
    clauses = []
    num_vars = 0
    BF = []
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

file_path = "input4.dimacs"  
num_vars, clauses = read_dimacs(file_path)
print(clauses)

