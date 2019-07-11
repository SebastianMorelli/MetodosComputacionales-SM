//Este código soluciona una ecuación de onda de segundo orden con extremos fijos.

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float longi = 1.0;
float velc = 300.0;
float dx = 0.005;
float dt = (dx/velc)*0.25;
float A0 = 0.1;
int numpunt = longi/dx;
float itera = 0.1/dt;

//Declaración funciones

float * yoAdivinoFuturos (float arrPast[], float arrPres[], float arrFut[]);
float * yoReemplazoPasados (float arrPasd[], float arrPresnt[],float arrFutu[]);

int main()
{
    //Declaración Arrays
    float x[numpunt];
    float pastWave[numpunt];
    float presentWave[numpunt];
    float futureWave[numpunt];
    
    //Condiciones de Frontera 
    x[0] = 0;
    x[numpunt] = 0;
    pastWave[0] = 0;
    pastWave[numpunt] = 0;
    presentWave[0] = 0;
    presentWave[numpunt] = 0;
    futureWave[0] = 0;
    futureWave[numpunt] = 0;
    
    //Condición inicial
    float j = 0;
    float k = A0;
    for (int i = 1; i < numpunt; i++){
        float xRope = dx*i;
        if(xRope <= longi/2){
            j+=2*A0/numpunt;
            pastWave[i] = j;
        }
        else{
            k-=2*A0/numpunt;
            pastWave[i] = k;
        }
        x[i] = xRope;
        cout<<x[i]<<" "<<pastWave[i]<<endl;    
    }
    
    //Segunda condición inicial pasado dt
    for(int i = 1; i < numpunt; i++){
    
        presentWave[i] = (((pow(velc,2)*pow(dt,2))/(2*pow(dx,2))) * (pastWave[i+1] + pastWave[i-1] - 2*pastWave[i])) + pastWave[i];
        cout<<x[i]<<" "<<presentWave[i]<<endl;
    }
    
    //Output de las oiscilaciones futuras halladas
    int contador = 0;
    for (int i = 0; i < itera; i++){
        
        yoAdivinoFuturos (pastWave, presentWave, futureWave);
        yoReemplazoPasados (pastWave, presentWave, futureWave);
        
        if(contador == 500){
            for(int j = 0; j <= numpunt; j++){
                cout<<x[j]<<" "<<presentWave[j]<<endl;
                contador = 0;
            }
        }
        
        contador ++;
    }    
}

float * yoAdivinoFuturos (float arrPast[], float arrPres[], float arrFut[]){
    
    float * p0 = arrFut;
    
    for( int i = 1; i < numpunt; i++){
        
        arrFut[i] = ((pow(velc,2)*pow(dt,2)/pow(dx,2)) * (arrPres[i+1]+arrPres[i-1]-2*arrPres[i])) -arrPast[i] + (2*arrPres[i]);
    }
    
    return p0;
}

float * yoReemplazoPasados (float arrPasd[], float arrPresnt[],float arrFutu[]){

    float * p1 = arrPresnt;
    
    for( int i = 1; i < numpunt; i++){
        
        arrPasd[i] = arrPresnt[i];
        arrPresnt[i] = arrFutu[i];
    }
    
    return p1;   
}

