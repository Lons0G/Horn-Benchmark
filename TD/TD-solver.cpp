#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

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
void BTD(const vector<int> &BF, const vector<vector<int>> &BR, int &Q,
         const vector<int> &BL) {

  cout << "Inicio de la funcion BTD" << endl;

  map<int, string> state;
  unordered_map<int, vector<int>> rules_with_head;

  // Inicialización
  for (int p : BL) {
    state[p] = "UNEXPANDED";
    rules_with_head[p] = {}; // Inicializar vector vacío
  }

  cout << "state" << endl;
  for (const auto &pair : state) {
    cout << pair.first << ": " << pair.second << endl;
  }
}

int main() {
  string archivo = "input4.dimacs";

  int Q = 0;
  vector<int> literales = extraer_literales(archivo);
  vector<int> BF = Base_Hechos_Q(archivo, Q);
  vector<vector<int>> BR = Base_reglas(archivo);

  cout << "Literales encontradas: ";
  for (int literal : literales) {
    cout << literal << " ";
  }
  cout << endl;

  cout << "Base de hechos : [";
  for (const auto &hecho : BF) {
    cout << " " << hecho;
  }
  cout << " ]" << endl;
  cout << "La query es: " << Q << endl;

  cout << "Base de reglas: [ ";
  for (vector<int> clausula : BR) {
    cout << "[ ";
    for (int literal : clausula) {
      cout << literal << " ";
    }
    cout << "] ";
  }
  cout << " ]" << endl;

  BTD(BF, BR, Q, literales);

  return 0;
}
