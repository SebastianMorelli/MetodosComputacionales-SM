//Este código halla los números primos en un intervalo ingresado 

#include <iostream>
using namespace std;

//Declaración Variables 

int num1;
int num2;

//Declaración funciones

int primos(int,int);

int main()
{
  cout<<"Número incial del Intervalo:" ;
  cin >> num1;
  cout<<"Número final del Intervalo:" ;
  cin >> num2;
  
  cout<<primos(num1,num2)<<endl;
  
  return 0;
}

int primos (int Val1, int Val2){
  for(int i = Val1; i <= Val2; i++){
    int div = 0;
    if(i%2 != 0){
      for(int j=0; j <= i; j++){
        if(i%j == 0){
          div ++ ;
        }
      }
    }
    if(div == 2){
      return i;
    }
  }
}
