//Este código soluciona una ecuación de difusión térmica de segundo orden en una placa de dos dimensiones.

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float lado = 1.0;
float cofdif = 1e-4;
float dx = 0.01;
float dt = 1.0;
float ladopeq = 0.20;
int numpunt = lado/dx;
float itera = 2500.0;
float T0 = 50.0;
float Tpeq = 100.0;

//Declaración funciones

float * yoAdivinoFuturos (float arrPast[], float arrPres[], float arrFut[]);
float * yoReemplazoPasados (float arrPasd[], float arrPresnt[],float arrFutu[]);

int main()
{
    //Declaración Arrays
    float x[numpunt][numpunt];
    float pastTxTy[numpunt];
    float presentTxTy[numpunt];
    float futureTxTy[numpunt];
    
    //Condiciones de Frontera 
   
    
    //Condición inicial

    for (int i = 1; i <= numpunt; i++){
        for(int j = 0; j<= numpunt; j++){
            
            float xlam = dx*i;
            float ylam = dx*j;
            if(xlam >= 0.20 && xlam <=0.40 && ylam >= 0.40 && ylam <= 0.60){
                
                pastTxTy[xlam][ylam] = Tpeq;
            }
            else{
                pastTxTy[xlam][ylam] = T0;
            }    
        }
        x[i][i] = {xlam},{xlam};
        cout<<x[i][i]<<" "<<pastTxTy[i]<<endl;
    }
    
//    //Segunda condición inicial pasado dt
//    for(int i = 1; i < numpunt; i++){
//    
//        presentWave[i] = (((pow(velc,2)*pow(dt,2))/(2*pow(dx,2))) * (pastWave[i+1] + pastWave[i-1] - 2*pastWave[i])) + pastWave[i];
//        cout<<x[i]<<" "<<presentWave[i]<<endl;
//    }
//    
//    //Output de las oiscilaciones futuras halladas
//    int contador = 0;
//    for (int i = 0; i < itera; i++){
//        
//        yoAdivinoFuturos (pastWave, presentWave, futureWave);
//        yoReemplazoPasados (pastWave, presentWave, futureWave);
//        
//        if(contador == 500){
//            for(int j = 0; j <= numpunt; j++){
//                cout<<x[j]<<" "<<presentWave[j]<<endl;
//                contador = 0;
//            }
//        }
//        
//        contador ++;
//    }    
}

//float * yoAdivinoFuturos (float arrPast[], float arrPres[], float arrFut[]){
//    
//    float * p0 = arrFut;
//    
//    for( int i = 1; i < numpunt; i++){
//        
//        arrFut[i] = ((pow(velc,2)*pow(dt,2)/pow(dx,2)) * (arrPres[i+1]+arrPres[i-1]-2*arrPres[i])) -arrPast[i] + (2*arrPres[i]);
//    }
//    
//    return p0;
//}
//
//float * yoReemplazoPasados (float arrPasd[], float arrPresnt[],float arrFutu[]){
//
//    float * p1 = arrPresnt;
//    
//    for( int i = 1; i < numpunt; i++){
//        
//        arrPasd[i] = arrPresnt[i];
//        arrPresnt[i] = arrFutu[i];
//    }
//    
//    return p1;   
//}
