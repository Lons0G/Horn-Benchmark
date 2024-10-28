#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/graphviz.hpp>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace boost;

// Definimos el tipo de grafo usando la lista de adyacencia
typedef adjacency_list<vecS, vecS, directedS> Graph;

std::pair<bool, std::unordered_map<int, int>>
horn_sat(const std::vector<std::vector<int>> &formula) {
  Graph g;

  // Construir el grafo
  for (const auto &clause : formula) {
    std::vector<int> positive_literals;
    std::vector<int> negative_literals;

    for (int lit : clause) {
      if (lit > 0) {
        positive_literals.push_back(lit);
      } else {
        negative_literals.push_back(-lit);
      }
    }

    // Verificar si hay más de un literal positivo
    if (positive_literals.size() > 1) {
      return {false, {}}; // No es una cláusula de Horn
    }

    // Agregar aristas al grafo
    if (!positive_literals.empty()) {
      int pos_lit = positive_literals[0];
      for (int neg_lit : negative_literals) {
        add_edge(neg_lit, pos_lit, g);
      }
    }
  }

  // Verificar si hay ciclos en el grafo
  std::unordered_set<int> visited;
  std::unordered_set<int> rec_stack;

  std::function<bool(int)> dfs = [&](int v) {
    if (rec_stack.count(v))
      return false; // Ciclo detectado
    if (visited.count(v))
      return true; // Ya visitado

    visited.insert(v);
    rec_stack.insert(v);

    for (auto neighbor : boost::make_iterator_range(adjacent_vertices(v, g))) {
      if (!dfs(neighbor)) {
        return false;
      }
    }

    rec_stack.erase(v);
    return true;
  };

  for (auto v : boost::make_iterator_range(vertices(g))) {
    if (!visited.count(v)) {
      if (!dfs(v)) {
        return {false, {}}; // Ciclo encontrado
      }
    }
  }

  // Si no hay ciclos, construir la asignación
  std::unordered_map<int, int> assignment;
  for (const auto &clause : formula) {
    std::vector<int> positive_literals;
    std::vector<int> negative_literals;

    for (int lit : clause) {
      if (lit > 0) {
        positive_literals.push_back(lit);
      } else {
        negative_literals.push_back(-lit);
      }
    }

    if (!positive_literals.empty()) {
      int pos_lit = positive_literals[0];
      assignment[pos_lit] = 1; // Asignar el literal positivo a 1
      for (int neg_lit : negative_literals) {
        assignment[neg_lit] = 0; // Asignar los literales negativos a 0
      }
    }
  }

  // Asegurarse de que todos los literales no asignados tengan un valor
  for (const auto &clause : formula) {
    for (int lit : clause) {
      if (assignment.find(abs(lit)) == assignment.end()) {
        assignment[abs(lit)] =
            (lit > 0) ? 1 : 0; // Asignar a 1 o 0 según el signo
      }
    }
  }

  return {true, assignment};
}

int main() {
  // Ejemplo de uso
  std::vector<std::vector<int>> formula = {
      {1, -2}, {-1, 3}, {-2, -3}, {-1, -2, -3}};
  auto [satisfacible, asignacion] = horn_sat(formula);

  if (satisfacible) {
    std::cout << "La fórmula es satisfacible." << std::endl;
    std::cout << "Asignación de literales:" << std::endl;
    for (const auto &[literal, value] : asignacion) {
      std::cout << "Literal " << literal << ": " << value << std::endl;
    }
  } else {
    std::cout << "La fórmula no es satisfacible." << std::endl;
  }

  return 0;
}
