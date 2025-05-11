// Questao 2
// Desenvolvido no Ubuntu 22.04 e compilado com g++ 11.4.0
// Compilar: g++ -std=c++20 fibonacci.cpp -o fibonacci
// Executar: ./fibonacci
#include <iostream>
#include <string>

using namespace std;

string isFibonacci(int number) {
  int fib1 = 0, fib2 = 1;

  while (fib2 < number) {
    int aux = fib1 + fib2;
    fib1 = fib2;
    fib2 = aux;
  }

  return fib2 > number ? "Não pertence a sequência de Fibonacci" : "Pertence a sequência de Fibonacci";
}

int main() {
  int number;

  cout << "Insira o número: ";
  cin >> number;

  cout << isFibonacci(number) << endl;
  
  return 0;
}