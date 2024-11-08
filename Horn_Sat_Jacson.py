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
                tokens = line.split()
                clause = [int(tok) for tok in tokens[:-1]]  # Ignorar el último 0
                if clause:  # Asegurarse de que la cláusula no esté vacía
                    clauses.append(clause)
                    BF.append(clause[0])


    # Crear la lista de p con 6 sublistas vacías
    lista_de_p = [[] for _ in range(num_vars)]

    # Llenar la lista de p con las cláusulas correspondientes
    for clause in clauses:
        for var in range(1, num_vars+1):
            if var in clause or -var in clause:
                lista_de_p[var - 1].append(clause)

    print('clauses: ', clauses)
    print('num_vars: ', num_vars)
    print('BF: ', BF)
    print('lista_de_p: ', lista_de_p)

    return num_vars, clauses, BF



# Leer el archivo DIMACS y resolver el SAT
file_path = 'input4.dimacs'  # Cambia este path al archivo correcto
variables, clauses, BF = read_dimacs(file_path)

