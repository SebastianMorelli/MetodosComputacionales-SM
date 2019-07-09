//Este código soluciona una ecuación de onda de primer orden.

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float longi = 1.0;
float velc = 300.0;
float dx = 0.005;
float dt = (dx/velc)*0.25;
int numpunt = longi/dx;
float itera = 0.1/dt;

//Declaración funciones

float * yoAdivinoFuturos (float arrPast[], float arrFut[]);
float * yoReemplazoPasados (float arrPasd[], float arrFutu[]);

int main()
{
    float inicialWave[numpunt];
    float futureWave[numpunt];
 
    for (int i = 0; i <= numpunt; i++){
        
        float xWave = dx*i;
        
        if(xWave < 0.75 || xWave > 1.25){
            inicialWave[i] = 1.0; 
        }
        
        else{
            inicialWave[i]=2.0;
        }
        cout<<inicialWave[i]<<" ";
    }
    
    for (int i = 0; i < itera/100; i++){
        for(int j = 0; j <= numpunt; j++){
        
            yoAdivinoFuturos (inicialWave, futureWave);
            yoReemplazoPasados (inicialWave, futureWave);
        
            cout<<inicialWave[j]<<" ";
        }
    }    
}

float * yoAdivinoFuturo (float arrPast[], float arrFut[]){
    
    float * p0 = arrFut;
    
    for( int i = 1; i < numpunt; i++){
        
        arrFut[i] = (velc*dt)/dx * (arrPast[i]-arrPast[i-1]) + arrPast[i];
    }
    
    return p0;
}

float * yoReemplazoPasados (float arrPasd[], float arrFutu[]){

    float * p1 = arrPasd;
    
    for( int i = 1; i < numpunt; i++){
        
        arrPasd[i] = arrFutu[i];
    }
    
    return p1;   
}
