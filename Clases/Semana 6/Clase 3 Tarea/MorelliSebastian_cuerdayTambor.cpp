//Este código soluciona una ecuación de onda de primer orden.

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
float * yoReemplazoPasados (float arrPasd[], float arrFutu[]);

int main()
{
    float x[numpunt];
    float PastWave[numpunt];
    float presentWave[numpunt];
    float futureWave[numpunt];
 
    float j = 0;
    float k = A0;
    for (int i = 0; i <= numpunt; i++){
        float xRope = dx*i;
        if(xRope <= longi/2){
            j+=2*A0/numpunt;
            PastWave[i] = j;
        }
        else{
            k-=2*A0/numpunt;
            PastWave[i] = k;
        }
        x[i] = xRope;
        cout<<x[i]<<" "<<PastWave[i]<<" "<<endl;    
    }
        
    
    for (int i = 0; i < itera/100; i++){
        for(int j = 0; j <= numpunt; j++){
        
            yoAdivinoFuturos (inicialWave, futureWave);
            yoReemplazoPasados (inicialWave, futureWave);
        
            cout<<inicialWave[j]<<" ";
        }
    }    
}

float * yoAdivinoFuturos (float arrPast[], float arrPres[], float arrFut[]){
    
    float * p0 = arrFut;
    
    for( int i = 1; i < numpunt; i++){
        
        arrFut[i] = (pow(velc,2)*pow(dt,2)/pow(dx,2)) * (arrPres[i]+arrPres[i]-2*arrPres[i-1]) -arrPast[i] + 2*arrPres[i];
    }
    
    return p0;
}

float * yoReemplazoPasados (float arrPasd[], float arrPresnt[],float arrFutu[]){

    float * p1 = arrPasd;
    
    for( int i = 1; i < numpunt; i++){
        
        arrPasd[i] = arrPresnt[i];
        arrPres[i] = arrFutu[i];
    }
    
    return p1;   
}
