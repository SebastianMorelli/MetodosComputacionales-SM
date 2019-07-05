//Este código implemente el rpducto de variables

#include <iostream>
using namespace std;

//Declaracion Variables

int a = 2;
float b = 3.0;

//Declaracion funciones

float product (int,float);

int main()
{
  cout<< "el producto de a por b es:" << product(a,b)<< endl;
  return 0;
}

float product (int val1, float val2)
{
  float val3 = val1*val2;
  return val3;
}
