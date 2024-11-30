#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
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

int main() {
  string archivo = "input4.dimacs";
  vector<int> literales = extraer_literales(archivo);

  cout << "Literales encontradas: ";
  for (int literal : literales) {
    cout << literal << " ";
  }
  cout << endl;

  return 0;
}
