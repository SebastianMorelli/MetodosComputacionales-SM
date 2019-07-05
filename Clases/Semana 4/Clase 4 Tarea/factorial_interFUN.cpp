//Este código halla el factorial de un número 

#include <iostream>
using namespace std;

//Declaración Variables 

int num;

//Declaración funciones

int fact(int);

int main()
{
  cout<<"Número:" ;
  cin >> num;
  cout<<fact(num)<<endl;
  
  return 0;
}

int fact (int Val)
{
  int cont = 1;
  for(int i = 1; i <= Val; i ++)
  {
    cont = cont*i;
  }
  return cont;
}
