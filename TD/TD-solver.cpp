#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

// Funciones
void OR(int p, map<int, string> &state,
        unordered_map<int, vector<int>> &rules_with_head);

string AND(int r, map<int, string> &state,
           unordered_map<int, vector<int>> &rules_with_head);

vector<int> extraer_literales(const string &archivo) {
  set<int> literales;
  ifstream input(archivo);

  string linea;
  while (getline(input, linea)) {
    if (linea.substr(0, 2) == "c " || linea.substr(0, 2) == "p ")
      continue;

    istringstream iss(linea);
    int literal;
    while (iss >> literal) {
      literales.insert(abs(literal));
    }
  }

  return vector<int>(literales.begin(), literales.end());
}

vector<vector<int>> extraer_clausulas(const string &archivo) {
  vector<vector<int>> clausulas;

  ifstream input(archivo);
  string linea;

  while (getline(input, linea)) {
    if (linea.substr(0, 2) == "c " || linea.substr(0, 2) == "p ") {
      continue;
    }

    vector<int> clausula;
    istringstream iss(linea);
    int literal;
    while (iss >> literal) {
      if (literal == 0) {
        break; // Final de la cláusula
      }
      clausula.push_back(literal);
    }
    clausulas.push_back(clausula);
  }
  input.close();
  return clausulas;
}

vector<int> Base_Hechos_Q(const string &archivo, int &Q) {
  vector<int> BF;

  vector<vector<int>> clausulas = extraer_clausulas(archivo);
  // Imprimir las cláusulas (ejemplo)
  // for (const auto &clausula : clausulas) {
  //  for (int literal : clausula) {
  //    cout << literal << " ";
  //  }
  //  cout << endl;
  //}

  // Imprimiendo el size de las clausulas
  int i_cls = 0;
  for (const auto &clausula : clausulas) {
    // cout << "el size de la clausula: " << i_cls << " es " << clausula.size()
    //      << endl;
    if (clausula.size() == 1 && clausulas[i_cls][0] > 0) {
      BF.push_back(clausulas[i_cls][0]);
    } else if (clausula.size() == 1 && clausulas[i_cls][0] < 0) {
      Q = clausulas[i_cls][0] * -1;
    }
    i_cls++;
  }

  return BF;
}

vector<vector<int>> Base_reglas(const string &archivo) {
  vector<vector<int>> clauses;
  ifstream inputFile(archivo);
  string line;

  while (getline(inputFile, line)) {
    istringstream iss(line);
    string token;
    vector<int> clause;

    // Ignorar comentarios y encabezado
    if (line.empty() || line[0] == 'c' || line[0] == 'p') {
      continue;
    }

    // Convertir la línea a una lista de enteros
    while (iss >> token) {
      clause.push_back(stoi(token));
    }
    clause.pop_back(); // Eliminar el último 0

    // Verificar la cláusula y agregarla si es válida
    if (!clause.empty() && clause.size() > 1) {
      clauses.push_back(clause);
    }
  }

  inputFile.close();
  return clauses;
}

// TOP DOWN BASIC
int BTD(const vector<int> &BF, const vector<vector<int>> &BR, int &Q,
        const vector<int> &BL) {

  cout << "Inicio de la funcion BTD" << endl;

  map<int, string> state;
  unordered_map<int, vector<int>> rules_with_head;

  // Inicialización
  for (int p : BL) {
    state[p] = "UNEXPANDED";
    rules_with_head[p] = {}; // Inicializar vector vacío
  }

  // cout << "state" << endl;
  // for (const auto &pair : state) {
  //   cout << pair.first << ": " << pair.second << endl;
  // }

  for (size_t r = 0; r < BR.size(); r++) {
    const vector<int> &clause = BR[r];
    rules_with_head[clause[0]].push_back(r);
    // body[to_string(r)] = vector<int>(clause.begin() + 1, clause.end());
  }

  // cout << "Rules with head" << endl;
  // for (const auto &pair : rules_with_head) {
  //   cout << "Head: " << pair.first << ", Rules: ";
  //   for (int rule : pair.second) {
  //     cout << rule << " ";
  //   }
  //   cout << endl;
  // }

  if (state[Q] == "UNEXPANDED") {
    // cout << "OR" << endl;
    OR(Q, state, rules_with_head);
  }
  // cout << "Q es: " << state[abs(Q)] << endl;
  // cout << "estado de Q: " << state[to_string(abs(Q))] << endl;
  if (state[Q] == "T") {
    // cout << "estado verdadero: " << state[to_string(to_string(Q))] <<
    cout << "Yes" << endl;
    // end_time = time.perf_counter(); // time.time()
    // tiempo = (end_time - start_time)
    return 1;
  } else {
    // cout << "estado falso: " << state[to_string(abs(Q))] << endl;
    cout << "No" << endl;
    // end_time = time.perf_counter(); // time.time()
    // tiempo = (end_time - start_time)
    return 0;
  }
}

// OR
void OR(int p, map<int, string> &state,
        unordered_map<int, vector<int>> &rules_with_head) {
  // cout << "Entro al OR" << endl;
  state[p] = "EXPANDED";
  for (int r : rules_with_head[p]) {
    // cout << "este es r: " << r << endl;
    state[p] = AND(r, state, rules_with_head);
    if (state[p] == "T") {
      // cout << "estado de p verdadero: " << abs(p) << endl;
      // cout << "estado de p verdadero = " << state[p] << endl;
      // cout << "estado de Q verdadero: " << abs(Q) << endl;
      // cout << "estado de Q verdadero = " << state[abs(Q)] << endl;
      // if (abs(Q) == p) {
      //     cout << "son iguales" << endl;
      // }
      return;
    }
  }
  return;
}

// AND
string AND(int r, map<int, string> &state,
           unordered_map<int, vector<int>> &rules_with_head) {
  for (int p : rules_with_head[r]) {
    // cout << "estado de " << p << ": " << state[p] << endl;
    if (state[p] == "UNEXPANDED") {
      // cout << "p en el if unexpanded: " << p << endl;
      // cout << "estado: " << rules_with_head[r] << endl;
      // cout << p << endl;
      OR(p, state, rules_with_head);
    }
    if (state[p] != "T" && state[p] != "EXPANDED") {
      // cout << "retornara F: " << p << endl;
      return "F";
    }
  }
  // cout << "retorno true" << endl;
  return "T";
}

int main() {
  string archivo = "benchmark_matrix_75_75.cnf";

  int Q = 0;
  vector<int> literales = extraer_literales(archivo);
  vector<int> BF = Base_Hechos_Q(archivo, Q);
  vector<vector<int>> BR = Base_reglas(archivo);

  // cout << "Literales encontradas: ";
  // for (int literal : literales) {
  //   cout << literal << " ";
  // }
  // cout << endl;

  // cout << "Base de hechos : [";
  // for (const auto &hecho : BF) {
  //   cout << " " << hecho;
  // }
  // cout << " ]" << endl;
  // cout << "La query es: " << Q << endl;

  // cout << "Base de reglas: [ ";
  // for (vector<int> clausula : BR) {
  //   cout << "[ ";
  //   for (int literal : clausula) {
  //     cout << literal << " ";
  //   }
  //   cout << "] ";
  // }
  // cout << " ]" << endl;

  BTD(BF, BR, Q, literales);

  return 0;
}
