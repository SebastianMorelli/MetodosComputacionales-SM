//Este código soluciona ecuaciones diferenciales de segundo orden

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float h = 0.01;
float mini = 0.0;
float maxi = 5.0;
int numpunt = (maxi - mini)/h;
int mass = 2;
int k = 300;

//Declaración funciones

float * rugen_Kutta2(float arr1, float arr2, float arr3);

int main()
{
    float t[numpunt];
    float x1[numpunt];
    float x2[numpunt];
    
    t[0] = mini;
    x1[0] = 0.1;
    x2[0] = 0;
    
    for(int i = 1; i <= numpunt; i++){
        t[i] = rugen_Kutta2(t[i-1], x1[i-1], x2[i-1])[0];
        x1[i] = rugen_Kutta2(t[i-1], x1[i-1], x2[i-1])[1];
        x2[i] = rugen_Kutta2(t[i-1], x1[i-1], x2[i-1])[2];
    }

    cout<<"Timepo(s): "<<"Posición "<<"Velocidad: "<<endl;
    for (int i = 1; i <= numpunt; i++){
        cout<<t[i]<<" "<<x1[i]<<" "<<x2[i]<<endl;
    }
}


float * rugen_Kutta2(float arr1, float arr2, float arr3){
    
    float arrayresult[3];
    float *p = arrayresult;
    
    float k1x1 = arr3;
    float k1x2 = -(k/mass)*arr2;
    
    float x1 = arr1 + (h/2.0);
    float y1x1 = arr2 + (h/2.0) * k1x1;
    float y2x1 = arr3 + (h/2.0) * k1x2;
    float k2x1 = y2x1;
    float k2x2 = -(k/mass)*y1x1;
    
    float x2 = arr1 + (h/2.0);
    float y1x2 = arr2 + (h/2.0) * k2x1;
    float y2x2 = arr3 + (h/2.0) * k2x2;
    float k3x1 = y2x2;
    float k3x2 = -(k/mass)*y1x2;
    
    float x3 = arr1 + (h/2.0);
    float y1x3 = arr2 + (h) * k3x1;
    float y2x3 = arr3 + (h) * k3x2;
    float k4x1 = y2x3;
    float k4x2 = -(k/mass)*y1x3;
    
    float prom_kx1 = (1.0/6.0)*(k1x1 + 2.0*k2x1 + 2.0*k3x1 + k4x1);
    float prom_kx2 = (1.0/6.0)*(k1x2 + 2.0*k2x2 + 2.0*k3x2 + k4x2);
    
    float x_new = arr1 + h;
    float y1_new = arr2 + h * prom_kx1;
    float y2_new = arr3 + h * prom_kx2;
    
    arrayresult[0] = x_new;
    arrayresult[1] = y1_new;
    arrayresult[2] = y2_new;
    
    return p;
}
