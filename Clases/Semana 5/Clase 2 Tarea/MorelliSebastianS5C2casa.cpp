//Este código soluciona ecuaciones diferenciales de primer orden

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float h = 0.01;
float mini = 0.0;
float maxi = 2.0;
int numpunt = (maxi - mini)/h;


//Declaración funciones

float * euler(float arr1[], float arr2[], int div);
float * rugen_Kutta(float arra[], float arrb[], int divi);

int main()
{
    float x[numpunt];
    float y[numpunt];

    cout<<"La solución a la ecuación diferencial por el método de euler es: "<<endl;
    for (int i = 0; i < numpunt; i++){
        cout<<euler(x,y,numpunt)[i]<<", ";
    }
    
    cout<<"La solución a la ecuación diferencial por el método de Rugen-Kutta es: "<<endl;
    for (int i = 0; i < numpunt; i++){
            cout<<rugen_Kutta(x, y, numpunt)[i]<<", ";
    }
}

float * euler(float arr1[], float arr2[], int div){
    arr1[0] = mini;
    arr2[0] = 1.0;
    float *p0 = arr2;
    for(int i = 1; i <= div; i++){
        arr1[i] = arr1[i-1] + h;
        arr2[i] = arr2[i-1] + h * (-arr2[i-1]);
    }
    return p0;
}

float * rugen_Kutta(float arra[], float arrb[], int divi){
    arra[0] = mini;
    arrb[0] = 1.0;
    float *p1 = arrb;
    for(int i = 1; i <= divi; i++){
        float k1 =h * -(arrb[i-1]);
        float k2 =h * -(arrb[i-1] + 0.5 * k1);
        float k3 =h * -(arrb[i-1] + 0.5 * k2);
        float k4 =h * -(arrb[i-1] + k3);
        
        float prom = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);
    
        arra[i] = arra[i-1] + h;
        arrb[i] = arrb[i-1] + prom;
    }
    return p1;
}