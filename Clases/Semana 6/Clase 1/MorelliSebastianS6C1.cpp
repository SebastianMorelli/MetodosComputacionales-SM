//Este código soluciona ecuaciones diferenciales de segundo orden

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

int ini = 0;
int fini = 2;
int numpunt = 80;
float vel = 1.0;
float dx = (fini - ini)/numpunt;
float dt = (dx/vel)*0.25;

//Declaración funciones

float * yoAdivinoFuturo (float arrPast, float arrFut);

int main()
{
    float inicialWave[numpunt];
    float futureWave[numpunt];
 
    for (int i = 0; i <= numpunt; i++){
        xWave = dx*i
        
        if(xWave < 0.75 || xWave > 1.25){
            inicialWave[i] = 1.0; 
        }
        
        else{
            inicialWave[i]=2.0;
        }
    }
    
}


float * yoAdivinoFuturo (float arrPast, flaot arrFut){
    for( int i = 1; i <= numpunt; i++){
    arrFut[i] = (vel*dt)/dx * (arrPast[i]-arrPast[i-1]) + arrPast[i];
    }
}
