//Este código soluciona ecuaciones diferenciales de primer orden

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float h = 0.01;
float mini = 0.0;
float maxi = 4.0;
int numpunt = (maxi - mini)/h;


//Declaración funciones

float * euler(float arr1[], float arr2[], int div);

int main()
{
    float x[numpunt];
    float y[numpunt];
    cout<<"La solución a la ecuación diferencial por el método de euler es: [";
    for (int i = 0; i < numpunt; i++){
        if(i < numpunt-1){
            cout<<euler(x,y,numpunt)[i]<<", ";
        }
        
        else{
            cout<<euler(x,y,numpunt)[i]<<"]";
        }
    }
}

float * euler(float arr1[], float arr2[], int div){
    arr1[0] = mini;
    arr2[0] = 1.0;
    float *p0 = arr1;
    float *p1 = arr2;
    for(int i = 1; i <= div; i++){
        arr1[i] = arr1[i-1] + h;
        arr2[i] = arr2[i-1] + h * (-arr2[i-1]);
    }
    return p1;
}
