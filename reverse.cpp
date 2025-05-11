// Questao 5
// Desenvolvido no Ubuntu 22.04 e compilado com g++ 11.4.0
// Compilar: g++ -std=c++20 reverse.cpp -o reverse
// Executar: ./reverse
#include <iostream>
#include <string>

using namespace std;

string reverseString(string str) {
  string aux = "";

  for (auto it = str.rbegin(); it != str.rend(); ++it) {
    aux += *it;
  }

  return aux;
}

int main() {
  cout << reverseString("Teste da Target Sistemas") << endl;

  return 0;
}