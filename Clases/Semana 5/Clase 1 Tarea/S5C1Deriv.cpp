//Este código halla la derivada de coseno bajo un intervalo y un número de puntos dado.

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float inicio;
float finale;
int numpunt;
float *x;

//Declaración funciones

float * linspace(float ini, float fin, int div);

float * coseno(float arr1[], int div);

float * deriv(float arra[], float arrb[]);

int main()
{
    cout<<"Ingrese el inicio del intervalo: ";
    cin>>inicio;
    cout<<"Ingrese el final del intervalo: ";
    cin>>finale;
    cout<<"Ingrese el número de puntos del intervalo: ";
    cin>>numpunt;
    
    x = linspace(inicio,finale,numpunt);
    for(int i = 0; i<=numpunt;i++){
    cout<<coseno(x,numpunt)[i]<<", ";}
    
    cout<<"El arreglo con las derivdas numéricas es: ["<<endl;
    for(int i = 0; i<numpunt; i++){
        if(i<(numpunt//-1)){
            cout<<deriv(interval,cos)[i]<<", ";
        }
        else{
            cout<<deriv(interval,cos)[i]<<"]"<<endl;
        }

    return 0;
}


float * linspace (float ini, float fin, int div){
    float interval = (fin - ini)/div;
    float linspace[div];
    float *p = linspace;
    for(int i = 0; i <= div; i++){
        for(int j = ini; j <= fin; j += interval){
            linspace[i] = j;
        }
    return p;
    }
}

float * coseno(float arr1[], int div){
    float arraycos[div];
    float *p = arraycos;
    for (int i = 0; i<=div; i++){
        arraycos[i] = cos(arr1[i]);
    }
    return p;
}

float * deriv (float arra[], float arrb[]){
    
}
